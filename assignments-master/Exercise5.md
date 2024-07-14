### Python - Exercise-5  

## Create A python program to practice Data Structures Manipulation Exercise: Stock Portfolio Analyzer. This exercise involves creating a function called analyze_portfolio that analyzes a portfolio of stocks and calculates various metrics.  

Function: analyze_portfolio(portfolio)  

Parameter:  

portfolio: A list of dictionaries. Each dictionary represents a stock in the portfolio and contains the following keys:  
symbol: A string representing the stock symbol (e.g., "AAPL", "GOOG").  
shares: An integer representing the number of shares owned.  
price: A float representing the current price per share.  
Returns:  

A dictionary containing the following information about the portfolio:  
total_shares: The total number of shares across all stocks in the portfolio.  
total_value: The total value of the portfolio (calculated by multiplying share count by price for each stock and summing them up).  
average_price_per_share: The average price per share across all stocks in the portfolio (weighted by share count).  
holdings_breakdown: A dictionary where keys are stock symbols and values are dictionaries containing:  
num_shares: The number of shares owned for that specific stock.  
total_value: The total value of that specific stock holding (shares * price).  
percentage_of_portfolio: The percentage of the total portfolio value represented by that specific stock holding.  
Sample Input:  

Python  
portfolio = [  
    {"symbol": "AAPL", "shares": 100, "price": 150.00},  
    {"symbol": "GOOG", "shares": 50, "price": 2000.00},  
    {"symbol": "TSLA", "shares": 25, "price": 700.00},  
]  

portfolio_analysis = analyze_portfolio(portfolio)  
print(portfolio_analysis)  

Sample Output:  

{  
  'total_shares': 175,  
  'total_value': 227500.0,  
  'average_price_per_share': 1300.0,  
  'holdings_breakdown': {  
    'AAPL': {  
      'num_shares': 100,  
      'total_value': 15000.0,  
      'percentage_of_portfolio': 6.62%  
    },  
    'GOOG': {  
      'num_shares': 50,  
      'total_value': 100000.0,  
      'percentage_of_portfolio': 44.00%  
    },  
    'TSLA': {  
      'num_shares': 25,  
      'total_value': 17500.0,  
      'percentage_of_portfolio': 7.70%  
    }  
  }  
}  
Explanation: 

The analyze_portfolio function should iterate through the provided portfolio list of dictionaries.

Initialize variables to store the total number of shares (total_shares), total portfolio value (total_value), and a dictionary to store holdings breakdown (holdings_breakdown).

Inside the loop, for each stock in the portfolio:

Calculate the total value of that specific holding (shares * price).
Update the total_shares and total_value variables.
Create a dictionary entry for the holdings_breakdown with details like number of shares, total value, and percentage of the portfolio represented by that stock (calculated based on total value).
After iterating through all stocks, calculate the average price per share by dividing the total portfolio value by the total number of shares.

Return a dictionary containing the calculated total_shares, total_value, average_price_per_share, and the holdings_breakdown dictionary.

Challenge:  

Extend the function to handle additional information in the portfolio dictionary (e.g., purchase price per share). You can modify the calculations and breakdown accordingly.  
Allow the function to accept an optional parameter to sort the holdings_breakdown by different criteria (e.g., number of shares, total value).  