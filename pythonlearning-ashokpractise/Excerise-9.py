import numpy as np
 
def analyze_stock_prices(prices):
    closing_prices = prices[:, -1].astype(float)
    highest_close_index = np.argmax(closing_prices)
    lowest_close_index = np.argmin(closing_prices)
    highest_close_day = prices[highest_close_index, 0]
    lowest_close_day = prices[lowest_close_index, 0]
    daily_changes = np.diff(closing_prices)
    average_daily_change = np.mean(daily_changes)
    std_dev_of_daily_changes = np.std(daily_changes)
 
    analysis_results = {
        "Highest closing price day": highest_close_day,
        "Lowest closing price day": lowest_close_day,
        "Average daily change": round(average_daily_change, 2),
        "Standard deviation of daily changes": round(std_dev_of_daily_changes, 2)
    }
    return analysis_results

prices = np.array([
    ['2023-12-01', 100, 105, 98, 102],
    ['2023-12-02', 103, 108, 99, 105],
    ['2023-12-04', 101, 107, 97, 100]
])