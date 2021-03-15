import tkinter as tk
import random as rd


demarrer = 1

#fonctions
def Démarrer(balle):
    global demarrer
    if demarrer:
        mouvement(balle)
        bouton.config(text="Arrêter")
    else:
        canvas.after_cancel(id_after)
        bouton.config(text="Démarrer")
    demarrer = 1 - demarrer
        


def creer_balle():
    x, y = 300, 200
    r = 20
    cercle = canvas.create_oval((x-r, y-r), (x+r, y+r), fill="blue")
    nb1 = rd.randint(1, 7)
    nb2 = rd.randint(1, 7)
    return [cercle, nb1, nb2]

def mouvement (balle):
    global id_after
    balle = rebond1(balle)
    canvas.move(balle[0], balle[1], balle[2])
    id_after = canvas.after(20, lambda : mouvement(balle))

def rebond1(balle):
    if balle <=0 or balle >= 600:
        balle[1] = -balle[1]
    if balle <= 0 or balle >= 400:
        balle[2] = -balle[2]
    return balle





#programme principal
racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width = 600, height = 400)
canvas.grid()
balle = creer_balle()
bouton = tk.Button(racine, text="Démarrer", command = lambda : Démarrer(balle))
bouton.grid()

racine.mainloop()