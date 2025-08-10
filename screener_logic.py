import yfinance as yf
import pandas as pd
from datetime import datetime

def screen_stock(ticker):
    """
    Screens a stock based on Benjamin Graham's investment criteria.
    """
    try:
        stock = yf.Ticker(ticker)
        info = stock.info

        # Some stocks might not have all the info available.
        # We'll use .get() to avoid errors and return None if a key is missing.
        pe_ratio = info.get('trailingPE')
        pb_ratio = info.get('priceToBook')
        price = info.get('regularMarketPrice')

        # If essential data is missing, we can't analyze the stock.
        if any(v is None for v in [pe_ratio, pb_ratio, price]):
            return None

        # --- Benjamin Graham Criteria ---

        # 1. P/E Ratio <= 9.0
        if pe_ratio > 9.0:
            return None

        # 2. P/B Ratio <= 1.2
        if pb_ratio > 1.2:
            return None

        # --- Ratios from Balance Sheet ---
        bs = stock.balance_sheet
        if bs.empty:
            return None

        # Get the most recent year's data
        latest_bs = bs.iloc[:, 0]

        total_assets = latest_bs.get('Total Assets')
        total_liabilities = latest_bs.get('Total Liab')
        current_assets = latest_bs.get('Total Current Assets')
        current_liabilities = latest_bs.get('Total Current Liabilities')

        if any(v is None for v in [total_assets, total_liabilities, current_assets, current_liabilities]):
            return None

        # 3. Debt-to-Asset Ratio <= 1.1
        if total_assets == 0: return None
        debt_to_asset_ratio = total_liabilities / total_assets
        if debt_to_asset_ratio > 1.1:
            return None

        # 4. Current Ratio >= 1.5
        if current_liabilities == 0: return None
        current_ratio = current_assets / current_liabilities
        if current_ratio < 1.5:
            return None

        # --- Earnings Growth ---
        financials = stock.financials
        if financials.empty or 'Basic EPS' not in financials.index:
            return None

        eps = financials.loc['Basic EPS']
        if len(eps) < 5:
            return None

        # 5. Earnings growth > 33% over last 5 years (using EPS)
        # We need to handle cases where the base year EPS is zero or negative
        if eps.iloc[4] <= 0:
            return None
        if eps.iloc[0] <= eps.iloc[4] * 1.33:
            return None

        # --- Dividend Payments ---
        dividends = stock.dividends
        # 6. Must pay dividends
        if dividends.empty:
            return None

        # If all criteria are met, return the stock's data
        return {
            "ticker": ticker,
            "price": price,
            "pe_ratio": round(pe_ratio, 2),
            "pb_ratio": round(pb_ratio, 2),
            "current_ratio": round(current_ratio, 2),
            "debt_to_asset_ratio": round(debt_to_asset_ratio, 2),
        }

    except Exception:
        # This will catch any other errors during the analysis of a single stock
        # and allow the script to continue with the next one.
        return None

def run_screener(tickers):
    """
    Runs the stock screener for a list of tickers.
    Returns two lists: all passed stocks, and stocks under $50.
    """
    passed_stocks = []
    for ticker in tickers:
        # Adding a print statement to show progress in the server logs
        print(f"Analyzing {ticker}...")
        result = screen_stock(ticker)
        if result:
            passed_stocks.append(result)

    filtered_stocks = [stock for stock in passed_stocks if stock['price'] < 50]

    return passed_stocks, filtered_stocks
