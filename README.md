# Benjamin Graham Stock Screener

This project is a simple web application that screens stocks based on the value investing principles of Benjamin Graham. It provides a user-friendly interface to run the analysis and view the results.

## Features

-   **Value Investing Criteria**: Screens stocks based on 6 of Benjamin Graham's key quantitative criteria:
    -   Price-to-Earnings (P/E) Ratio <= 9.0
    -   Price-to-Book (P/B) Ratio <= 1.2
    -   Debt-to-Asset Ratio <= 1.1
    -   Current Ratio >= 1.5
    -   Positive earnings growth over the last 5 years.
    -   Consistent dividend payments.
-   **Web Interface**: A simple, clean web UI built with Flask allows for easy interaction.
-   **Dynamic Results**: Run the screener with a single button click and view the results displayed dynamically on the page.
-   **Filtered Views**: The results are presented in two tables: one for all stocks that pass the criteria, and another for those that are also priced under $50.

## Setup and Installation

To get the project up and running on your local machine, follow these steps:

1.  **Clone the repository** (if you haven't already):
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Install dependencies**:
    This project uses a `requirements.txt` file to manage its dependencies. Install them using pip:
    ```bash
    pip install -r requirements.txt
    ```

## How to Run the Application

Once the dependencies are installed, you can start the web application by running the `app.py` file:

```bash
python app.py
```

The application will start a local development server, and you will see output in your terminal indicating that the server is running. By default, it runs on port 8080.

## Usage

1.  **Open your web browser** and navigate to the following URL:
    [http://localhost:8080](http://localhost:8080)

2.  You will see the main page of the stock screener. Click the **"Run Screener"** button to start the analysis.

3.  Please be patient, as the script needs to fetch data for multiple stocks, which can take a moment.

4.  Once the analysis is complete, the results will be displayed on the page in two tables.
