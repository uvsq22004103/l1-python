import tkinter as tk

cpt = 0
stop = False

def start():
    """Recommencer du début"""
    global cpt, stop
    Canvas.itemconfigure(rectangle, fill="red")
    cpt = 0
    stop = False

def est_dans_rectangle(x, y):
    """Retourne True si le point de coordonées (x,y) est dans le rectangle,
    et False sinon"""
    return 100 < x < 400 and 100 < y < 400 



def change_colors(event):
    """Change la couleur du rectangle"""
    global cpt, stop
    liste_couleur = ["red", "blue"]
    if est_dans_rectangle(event.x, event.y) and not stop:
        Canvas.itemconfigure(rectangle, fill=liste_couleur[cpt])
        cpt = (cpt + 1) % 2
        #alternative cpt = 1 - cpt
    else:
        #quand on clique en dehors du rectangle
        stop = True



racine = tk.Tk()
racine.title("Exercice 1 tkinter")
Canvas = tk.Canvas(racine, width=500, height=500, bg="black")
Canvas.grid(row=0, column=0)
rectangle = Canvas.create_rectangle(100, 100, 400, 400, fill="red")
Canvas.bind("<Button-1>", change_colors)


bouton = tk.Button(racine, text="Recommencer", command=start)
bouton.grid(row=1)


racine.mainloop()
