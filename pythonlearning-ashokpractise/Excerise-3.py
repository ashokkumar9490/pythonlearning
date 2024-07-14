def generate_invoice(customer_name, items, tax_rate):
    print("=" * 50)
    print("Invoice")
    print("\nCustomer Name:", customer_name)

    print("\nItems\n")
    print("{:<15} {:<10} {:<10} {:<10}".format("Item Name", "Price", "Quantity", "Subtotal"))
    print("-" * 50)
    
    subtotal = 0
    for item in items:
        item_name, price, quantity = item
        item_total = price * quantity
        subtotal += item_total
        print("{:<15} ${:<10.2f} {:<10} ${:<10.2f}".format(item_name, price, quantity, item_total))
    
    
    tax_amount = subtotal * tax_rate
    total = subtotal + tax_amount
    
     
    print("\nSubtotal: ${:.2f}".format(subtotal))
    print("Tax ({}%): ${:.2f}".format(tax_rate * 100, tax_amount))
    print("Total: ${:.2f}".format(total))
    print("=" * 50)
    print("Thanks for business")


customer_name = input("Enter customer name: ")


items = []
while True:
    item_name = input("Enter item name (or type 'done' to finish): ")
    if item_name.lower() == 'done':
        break
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    items.append((item_name, price, quantity))

 
tax_rate = float(input("Enter tax rate (e.g., 0.07 for 7%): "))

generate_invoice(customer_name, items, tax_rate)