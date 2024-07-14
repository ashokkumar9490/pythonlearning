def convert_units(value, from_unit, to_unit):
    # Define conversion factor variable
    conversion_factor = None


    if from_unit == "km" and to_unit == "mi":
        conversion_factor = 1000  # 1 kilometer = 0.621371 mile

    
    elif from_unit == "mi" and to_unit == "km":
        conversion_factor = 1 / 1000 # 1 mile = 1.60934 kilometers

    
    elif from_unit == "lb" and to_unit == "g":
        conversion_factor = 453.592  # 1 pound = 453.592 grams

    
    elif from_unit == "g" and to_unit == "lb":
        conversion_factor = 0.00220462  # 1 gram = 0.00220462 pounds

    if conversion_factor is not None:
        converted_value = value * conversion_factor
        return converted_value
    else:
        print("Conversion not supported for the given units.")
        return None

# Sample Input: Convert 10 kilometers to miles
converted_distance = convert_units(10, "km", "mi")
print(converted_distance)

# Sample Input: Convert 20 pounds to grams
converted_weight = convert_units(20, "lb", "g")
print(converted_weight)

