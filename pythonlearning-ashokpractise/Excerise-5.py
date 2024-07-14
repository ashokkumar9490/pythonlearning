portfolio = [
{"symbol": "AAPL", "shares": 100, "price": 150.00},
{"symbol": "GOOG", "shares": 50, "price": 2000.00},
{"symbol": "TSLA", "shares": 25, "price": 700.00},
]
holdings_breakdown={}
 
def analyze_portfolio(portfolio):
    total_shares=0
    total_value=0
    total=0
   
    for stock in portfolio:
        total_value=stock["shares"]*stock["price"]  
        print("Total Value: ",total_value)
        total_shares += stock["shares"]  
        print("Total Shares: ",total_shares)
        total += total_value
        print("Total",total)
        total_portfolio_percentage=(total_value/total)*100
        holdings_breakdown[stock["symbol"]]={'num_shares':stock['shares'],
                                       'total_value':total_value,
                                       'percentage_of_portfolio':  total_portfolio_percentage}
        average_price_per_share=total/total_shares
        print("Average Price per Share",average_price_per_share)
        print()
    return {"total_shares": total_shares,
              "total_value": total,
              "average_price_per_share": average_price_per_share,
              "holdings_breakdown": holdings_breakdown}
 
portfolio_analysis = analyze_portfolio(portfolio)
print(portfolio_analysis)
 