while True:
    try:
        n1 = int(input("Enter the first integer : "))
        n2 = int(input("Enter the second integer : "))
        break
    except ValueError:
        print("\nPlease enter valid integers.")

smallest = n1 if n1 < n2 else n2

print(f"\nThe smallest number is : {smallest}")
