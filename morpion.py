from tkinter import *

# Création de la classe Morpion
class Morpion:
    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.fenetre.title("Jeu de tic tac toe")
        self.fenetre.geometry("450x450")
        self.fenetre.config(background="black")
        self.joueur = 1
        self.cases = []
        self.partie_en_cours = True
        self.menu()
        self.grille()

    #Mise en place du menu
    def menu(self):
        self.menu = Menu(self.fenetre)
        self.fenetre.config(menu=self.menu)
        self.menu_jeu = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Nouvelle partie", command=self.nouvelle_partie)
        self.menu.add_cascade(label="Quitter", command=self.fenetre.quit)

    #Mise en place de la grille
    def grille(self):
        for i in range(3):
            ligne = []
            for j in range(3):
                case = Button(self.fenetre, width=20, height=10, command=lambda x=i, y=j: self.jouer(x, y))
                case.grid(row=i, column=j)
                ligne.append(case)
            self.cases.append(ligne)

    #Mise en place de la fonction de jeu
    def jouer(self, x, y):
        if self.cases[x][y]["text"] == "" and self.joueur == 1 and self.partie_en_cours:
            self.cases[x][y]["text"] = "X"
            self.joueur = 2
        elif self.cases[x][y]["text"] == "" and self.joueur == 2 and self.partie_en_cours:
            self.cases[x][y]["text"] = "O"
            self.joueur = 1
        self.verifier()

    #Mise en place de la fonction de vérification pour savoir s'il y a un gagnant ou bien match nul
    def verifier(self):
        gagnant = False
        for i in range(3):
            if self.cases[i][0]["text"] == self.cases[i][1]["text"] == self.cases[i][2]["text"] != "":
                self.cases[i][0].config(bg="green")
                self.cases[i][1].config(bg="green")
                self.cases[i][2].config(bg="green")
                self.fin(self.cases[i][0]["text"])
                gagnant = True
        for i in range(3):
            if self.cases[0][i]["text"] == self.cases[1][i]["text"] == self.cases[2][i]["text"] != "":
                self.cases[0][i].config(bg="green")
                self.cases[1][i].config(bg="green")
                self.cases[2][i].config(bg="green")
                self.fin(self.cases[0][i]["text"])
                gagnant = True

        if self.cases[0][0]["text"] == self.cases[1][1]["text"] == self.cases[2][2]["text"] != "":
            self.cases[0][0].config(bg="green")
            self.cases[1][1].config(bg="green")
            self.cases[2][2].config(bg="green")
            self.fin(self.cases[0][0]["text"])
            gagnant = True

        if self.cases[0][2]["text"] == self.cases[1][1]["text"] == self.cases[2][0]["text"] != "":
            self.cases[0][2].config(bg="green")
            self.cases[1][1].config(bg="green")
            self.cases[2][0].config(bg="green")
            self.fin(self.cases[0][2]["text"])
            gagnant = True

        if all(self.cases[i][j]["text"] != "" for i in range(3) for j in range(3)) and not gagnant and self.partie_en_cours:
            self.fin_match_nul()

    #Mise en place de la fonction de fin de partie en cas de victoire d'un des joueur
    def fin(self, vainqueur):
        self.partie_en_cours = False
        self.fenetre.title("Morpion - Le joueur {} a gagné !".format(vainqueur))
        for i in range(3):
            for j in range(3):
                self.cases[i][j]["state"] = "disabled"

    #Mise en place de la fonction de fin de partie en cas de match nul
    def fin_match_nul(self):
        self.partie_en_cours = False
        self.fenetre.title("Morpion - Match nul !")
        for ligne in self.cases:
            for case in ligne:
                case["state"] = "disabled"
                case.config(bg="red")

    #Mise en place de la fonction de nouvelle partie (quand on clique sur le menu)
    def nouvelle_partie(self):
        for ligne in self.cases:
            for case in ligne:
                case.destroy()
        self.cases = []
        self.partie_en_cours = True
        self.joueur = 1
        self.grille()
        self.fenetre.title("Jeu de tic tac toe")

#Lancement du jeu à partir de la classe Morpion
if __name__ == "__main__":
    fenetre = Tk()
    morpion = Morpion(fenetre)
    fenetre.mainloop()