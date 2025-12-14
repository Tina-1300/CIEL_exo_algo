total_bille = 1000
billes_utiliser = 0

for etage in range(1, total_bille + 1):
    if billes_utiliser + etage**2 > total_bille:
        etage -= 1  
        break
    billes_utiliser += etage**2

print(f"Inès peux avoire {etage} étage pour sa piramide de billes")
