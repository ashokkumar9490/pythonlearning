class Driver:
    def __init__ (self,name):
        self.name = name
        self.rides = []
    def add_ride(self,fare):
        self.rides.append(fare)
    def display_rides(self):
        total_fare = sum(self.rides)
        total_rides = len(self.rides)
        print(f"Driver: {self.name}")
        print(f"Total Fare:${total_fare}")
        print(f"Total Rides:{total_rides}")
        for i, fare in enumerate(self.rides, 1):
            print(f"Ride {i}: ${fare}")
drivers =  {
            "Ashok": Driver("Ashok"),
            "Kumar": Driver("kumar"), 
            "Surya": Driver("surya")
}
    
drivers["Ashok"].add_ride(20)
drivers["Kumar"].add_ride(30)
drivers["Kumar"].add_ride(40)
drivers["Surya"].add_ride(30)
for driver_name,driver in drivers.item():
        driver.diplay.rides()
        print()      

        

