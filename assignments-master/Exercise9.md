### Python - Exercise-9  

## Create A python program to practice Python  NumPy: Stock Price Analysis with Time Series Data. This exercise involves creating a function called analyze_stock_prices that utilizes NumPy arrays to analyze historical stock price data.

Function: analyze_stock_prices(prices)

Parameter:

prices (NumPy array): A 2D NumPy array where each row represents a day's data. The first column represents the date (string or datetime format), and subsequent columns represent different price metrics (e.g., Open, High, Low, Close).  
Analysis performed:  

Calculate the daily price change (Close - Previous Close) for each day.  
Find the day with the highest closing price.  
Find the day with the lowest closing price.  
Calculate the average daily price change (excluding the first day as it doesn't have a previous close).  
Calculate the standard deviation of the daily price changes.  


# Sample usage (assuming prices is a NumPy array loaded from your data source)
analysis_results = analyze_stock_prices(prices)  
print(analysis_results)  

Sample Input (Example NumPy array - replace with actual data):

array([['2023-12-01', 100, 105, 98, 102],  
       ['2023-12-02', 103, 108, 99, 105],  
       ['2023-12-04', 101, 107, 97, 100]])  

Sample Output:  

{  
  "Highest closing price day": "2023-12-02",  
  "Lowest closing price day": "2023-12-04",  
  "Average daily change": 1.0,  
  "Standard deviation of daily changes": 1.4142135623730951  
}  

Explanation:  

The analyze_stock_prices function takes a 2D NumPy array (prices) containing historical stock price data.  
It extracts the closing prices using slicing and calculates daily price changes using np.diff.  
The function finds the days with the highest and lowest closing prices using np.argmax and np.  argmin.  
It calculates the average and standard deviation of the daily price changes using np.mean and np.std, excluding the first day.  
Finally, a dictionary containing the analysis results is returned.  

Challenge:

Extend the function to handle different price metrics (e.g., Open, High, Low) and calculate additional statistics (e.g., percentage change).  
Allow the function to take an optional argument specifying which column represents the closing price.  