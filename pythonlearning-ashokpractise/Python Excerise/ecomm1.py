class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
 
    def get_price(self):
        return self.price
 
class ElectronicDevice(Product):
    def __init__(self, name, brand, price):
        super().__init__(name, price)
        self.brand = brand
 
class Order:
    def __init__(self, items):
        self.items = items
        self.total_price = self.calculate_total_price()
 
    def calculate_total_price(self):
        total = 0
        for item in self.items:
            total += item.get_price()
        return total
 
def write_order_to_file(Order, filename):
    with open(filename, 'w') as file:
         file.write("Order Items:\n")
         for item in Order.items:
          file.write(f"{item.name} ({item.brand}) - ${item.price:.2f}\n")
          file.write(f"Total Price: ${Order.total_price:.2f}\n")

# Sample usage
device1 = ElectronicDevice("Laptop", "Dell", 799.99)
device2 = ElectronicDevice("Phone", "Apple", 1099.99)
 
order_items = [device1, device2]
my_order = Order(order_items)
 
write_order_to_file(my_order, "outfile.txt")
