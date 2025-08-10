from flask import Flask, render_template, jsonify
from screener_logic import run_screener

app = Flask(__name__)

# A predefined list of tickers to screen.
TICKERS = [
    "AAPL", "MSFT", "GOOGL", "JNJ", "PG", "XOM", "PFE", "INTC",
    "CSCO", "KO", "T", "F", "GE", "BAC", "WFC", "VZ", "CVX", "IBM"
]

@app.route('/')
def index():
    """
    Renders the main page.
    """
    return render_template('index.html')

@app.route('/run_screener', methods=['POST'])
def run_screener_route():
    """
    Runs the screener and returns the results as JSON.
    """
    passed_stocks, filtered_stocks = run_screener(TICKERS)
    return jsonify({
        'passed_stocks': passed_stocks,
        'filtered_stocks': filtered_stocks
    })

# The app is now run from the run_and_verify.py script
