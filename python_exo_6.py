try:
    note = float(input("Enter the exam grade (0 to 20) : "))

    print(
        "Invalid grade !" if note < 0 or note > 20 else
        "Refusé" if note < 10 else
        "Passable" if note < 12 else
        "Assez bien" if note < 14 else
        "Bien" if note < 16 else
        "Très bien" if note < 18 else
        "Félicitations du jury"
    )

except ValueError:
    print("\nPlease enter a valid decimal number.")
