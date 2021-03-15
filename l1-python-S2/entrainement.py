import tkinter as tk

##################
# Constantes

LARGEUR = 600
HAUTEUR = 400
demarrer = 1
###################
# Fonctions


def creer_balle():
    """Dessine un rond bleu et retourne son identifiant
     et les valeurs de déplacements dans une liste"""
    x, y = LARGEUR // 2, HAUTEUR // 2
    rayon = 20
    dx, dy = 3, 5
    cercle = canvas.create_oval((x-rayon, y-rayon),
                                (x+rayon, y+rayon),
                                fill="blue")
    return [cercle, dx, dy]


def mouvement(balle):
    """Déplace la balle et ré-appelle la fonction avec un compte-à-rebours"""
    global id_after
    rebond()
    canvas.move(balle[0], balle[1], balle[2])
    id_after = canvas.after(20, lambda: mouvement(balle))


def rebond():
    """Fait rebondir la balle sur les bords du canevas"""
    global balle
    x0, y0, x1, y1 = canvas.coords(balle[0])
    if x0 <= 0 or x1 >= 600:
        balle[1] = -balle[1]
    if y0 <= 0 or y1 >= 400:
        balle[2] = -balle[2]


def start(balle):
    global demarrer
    if demarrer:
        mouvement(balle)
        bouton.config(text="Arrêter")
    else:
        canvas.after_cancel(id_after)
        bouton.config(text="Démarrer")
    demarrer = 1 - demarrer

######################
# programme principal

racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=600, height=400)
canvas.grid()
balle = creer_balle()
bouton = tk.Button(racine, text = "Demarrer", command = lambda : start(balle))
bouton.grid()
racine.mainloop()