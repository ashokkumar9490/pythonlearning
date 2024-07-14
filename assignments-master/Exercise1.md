### Python - Exercise-1  

## Create A python program to practice Data Conversion. This exercise involves creating a function called convert_units that converts values between different measurement units.  

Function: convert_units(value, from_unit, to_unit)  

Parameters:  

value: A numeric value (float) representing the quantity to be converted.  
from_unit: A string representing the starting unit of measurement (e.g., "cm", "in", "kg", "lb").  
to_unit: A string representing the target unit of measurement (e.g., "m", "ft", "g", "oz").  
Returns:  

A float representing the converted value in the target unit.  
Sample Input:  

# Convert 5 kilometers to miles  
converted_distance = convert_units(5, "km", "mi")  
print(converted_distance)  

# Convert 2 pounds to grams  
converted_weight = convert_units(2, "lb", "g")  
print(converted_weight)  

Sample Output:  

3.11  # 5 kilometers in miles (rounded)  
907.18  # 2 pounds in grams (rounded)  

Challenge:  

Extend the function to handle additional unit types (e.g., temperature, volume).  
Implement error handling for invalid unit inputs. You can raise exceptions or return appropriate error messages.  
