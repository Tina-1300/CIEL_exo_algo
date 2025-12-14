MAJOR_AGE = 18
MAX_AGE = 130

try:
    age = int(input("Enter your age : "))

    print("\nInvalid age !" if not 0 <= age <= MAX_AGE else "\nMajeur !" if age >= MAJOR_AGE else "\nMineur !")

except ValueError:
    print("\nPlease enter a valid number.")
