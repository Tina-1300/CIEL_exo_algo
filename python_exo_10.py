ep = 0.1  #  mm
hauteur_tour_eiffel = 324  # m
pliage = 0 

while ep/1000 <= hauteur_tour_eiffel:  
    ep *= 2
    pliage += 1

print(f"il faux plier la feuille {pliage} fois pour dépasser la hauteur de la tour eiffel : {hauteur_tour_eiffel} m\népésseur de la feuile aprè {pliage} : {ep/1000} m")
