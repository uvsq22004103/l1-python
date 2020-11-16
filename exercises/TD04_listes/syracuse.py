def syracuse(n):
    """ Retourne la liste des valeurs de la suite en partant de n jusqu'à 1 """
    n = int(input("choisir un nombre entier"))
    l = []
    while n != 1:
        l.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
    l.append(1)
    return(l)
print(syracuse(3))