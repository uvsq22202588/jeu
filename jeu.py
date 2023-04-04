import tkinter as tk

# --------------------------#
#                           #
#            JEU            #
#                           #
# --------------------------#
class Game():
    def __init__(self):
        """
        Une fonction qui initialise les variable self.
        """
        self.fenetre = tk.Tk()
        self.fenetre.geometry("1000x1000")
        self.fond = tk.Canvas(self.fenetre, width=1000, height=1000, bg="blue")
        self.nb_vie = 3
        self.perso = tk.Canvas(self.fenetre, width=100, height=100, bg="white")
        self.perso.create_line()
        self.texte_vie = tk.Label(self.fenetre, text="Il vous reste "+str(self.nb_vie)+" vies")
        self.x = 1
        self.y = 1
        self.x_min=0
        self.x_max=1000
        self.y_max=1000
        self.y_min=0
        self.liste_floor=[90]

    def gravite(self):
        while self.x > self.liste_floor[0]:
            self.x+=1
        


    def deplacement_haut(self):
        if self.x > self.x_min and self.x < self.x_max:
            self.x -= 1
            self.perso.grid(row = self.x, column = self.y)
        else: self.x +=1

    def deplacement_bas(self):
        if self.x >= self.x_min and self.x < self.x_max:
            self.x += 1
            self.perso.grid(row = self.x, column = self.y)
        else: self.x -=1

    def deplacement_gauche(self):
        if self.y >= self.y_min and self.y < self.y_max:
            self.y += 1
            self.perso.grid(row = self.x, column = self.y)
        else: self.y -=1

    def deplacement_droite(self):
        if self.x >= self.y_min and self.x < self.y_max:
            self.y -= 1
            self.perso.grid(row = self.x, column = self.y)
        else: self.y +=1

    def clic(event):
        X = event.x
        Y = event.y
        print(X,Y)

    def mouvement(self):
        self.fenetre.bind('z', lambda event : self.deplacement_haut())
        self.fenetre.bind('s', lambda event : self.deplacement_bas())
        self.fenetre.bind('q', lambda event : self.deplacement_droite())
        self.fenetre.bind('d', lambda event : self.deplacement_gauche())
        self.fenetre.bind('<Button-1>', lambda event : self.clic())
    
    def initialisation(self):  
        """
        Une fonction qui affiche tous les Canvas, Label, Button.
        """
        for i in range(1000):
            self.fenetre.grid_columnconfigure(i,weight=1)
            self.fenetre.grid_rowconfigure(i,weight=1)
        self.fond.grid(row = 0, column = 0, rowspan=500, columnspan=500)
        self.perso.grid(row = self.x , column = self.y)

    def lancement(self):
        
        self.initialisation()
        self.mouvement()
        self.gravite()
        self.fenetre.mainloop()

game = Game()
game.lancement()