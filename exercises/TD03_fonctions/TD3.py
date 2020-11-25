def AffichePluriel(val,mot):
    if val != 0 or val != 1:
        print(mot, end="")
    else:
        print(mot, end="s")

def afficheTemps(temps):
    temps[0] = jour
    temps[1] = heure
    temps[2] = minute
    temps[3] = seconde
    return(jour, heure, minute, seconde)
afficheTemps((1,0,14,23))


