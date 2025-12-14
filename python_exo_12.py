import random
import sys
import time

def write_effect(text, delay=0.07):
    for char in text:sys.stdout.write(char),sys.stdout.flush(),time.sleep(delay)
    print()

secret_number = random.randint(0, 1000)
tentatives = 0
max_tentatives = 10

write_effect("Devine le nombre entre 0 et 1000 ! Tu as 10 tentatives\n")

while tentatives < max_tentatives:
    try:
        proposition = int(input(f"Tentative {tentatives + 1} : "))
    except ValueError:
        write_effect("Merci de saisir un nombre enthier entre 0 et 1000.")
        continue

    tentatives += 1
    message = (
        "\nBravo tu as gagnier !" if proposition == secret_number
        else "Trop petit !" if proposition < secret_number
        else "Trop grand !"
    )
    write_effect(message)

    if proposition == secret_number:
        break
else:
    write_effect(f"\nDommage !")
