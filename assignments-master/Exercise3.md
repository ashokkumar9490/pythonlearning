### Python - Exercise-3  

## Create A python program to practice Inputs and Formatting. This exercise involves creating a function called generate_invoice that takes user input and formats it into a professional-looking invoice.  

Function: generate_invoice(customer_name, items, tax_rate)  

Parameters:  

customer_name: A string representing the customer's name.  
items: A list of tuples where each tuple represents an item on the invoice (item_name, price, quantity).  
tax_rate: A float representing the sales tax rate (e.g., 0.07 for 7%).  
Returns:  

None (The function prints the formatted invoice to the console)  
Sample Input:  
customer_name = "John Doe"  
items = [("Computer", 1000.00, 1), ("Mouse", 20.00, 2)]  
tax_rate = 0.07  

generate_invoice(customer_name, items, tax_rate)  

Sample Output:   

====================================  
**Invoice**  
====================================  
Customer Name: John Doe  

**Items**  
| Item Name | Price | Quantity | Subtotal |  
|---|---|---|---|  
| Computer | $1,000.00 | 1 | $1,000.00 |  
| Mouse | $20.00 | 2 | $40.00 |  

**Subtotal:** $1,040.00  
**Tax (7%):** $72.80  
**Total:** $1,112.80  

====================================  
Thank you for your business!  
====================================  


Challenge:  

Extend the function to allow optional parameters for additional invoice details like invoice number, date,  and company information.  
Implement error handling for invalid user input (e.g., non-numeric values for price or quantity).  
