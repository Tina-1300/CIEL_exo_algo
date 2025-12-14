prices = {"adult": 7,"child": 3}
adults, children = int(input("Enter the number of adults : ")), int(input("Enter the number of children : "))

total_price = adults * prices["adult"] + children * prices["child"]

print(f"\nTotal price : {total_price} €")
