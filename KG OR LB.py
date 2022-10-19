weight = int(input("Weight:"))
unit = input('(K) kg or (L)lb:')

if unit.upper() == "K":
    converted = weight / 0.45
    print("Weight in kg:" + str(converted))
else:
    converted = weight * 0.45
    print("Weight in lb:" + str(converted))
