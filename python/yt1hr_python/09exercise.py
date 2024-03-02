weight=(float(input("Weight:")))
unit=input("(k)g or (G)ram:").upper()
if unit=='K':
    weight_in_grams=int(weight*1000)
    print(f"Weight in Grams:{weight_in_grams}")
elif unit=='G':
    weight_in_kg=(weight/1000)
    print(f"Weight in kilograms:{weight_in_kg}")
else:
    print("Invalid unit. Please enter 'K' or 'G'.")