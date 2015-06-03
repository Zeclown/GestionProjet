import sqlite3
from Modele import *
from Vue import *
class Controleur():
    def __init__(self):
        conn = sqlite3.connect('donnees.db')
        c = conn.cursor()
        
        c.execute("CREATE TABLE IF NOT EXISTS Projets (projet text, id int, debut date, fin date ,PRIMARY KEY (id))")
        c.execute("CREATE TABLE IF NOT EXISTS Etapes (projetId int, id int, nom text, duree date,priorite int ,PRIMARY KEY (id),FOREIGN KEY (projetId) REFERENCES Projets(id)) ")
        c.execute("CREATE TABLE IF NOT EXISTS Membres (projetId int, nom text, id int ,PRIMARY KEY (id),FOREIGN KEY (projetId) REFERENCES Projets(id))")
        c.execute("CREATE TABLE IF NOT EXISTS Taches (EtapeId int,id int,nom text, duree reel,sprintId int,responsableId int,completion int, priorite int,PRIMARY KEY (id),FOREIGN KEY (sprintId) REFERENCES Sprints(id),FOREIGN KEY (responsableId) REFERENCES Membres(id) ) ")
        c.execute("CREATE TABLE IF NOT EXISTS Sprints (projetId int, id int, nom text,PRIMARY KEY (id),FOREIGN KEY (projetId) REFERENCES Projets(id)) ")
        c.execute("CREATE TABLE IF NOT EXISTS TachesPrerequis (tacheId int, prerequisId int,FOREIGN KEY (tacheId) REFERENCES Taches(id),FOREIGN KEY (prerequisId) REFERENCES Taches(id))")
        
        self.modele=Modele(self)
        self.vue=Vue(self,self.modele.largeur,
                     self.modele.hauteur)
        self.menu()

    def menu(self):
        self.vue.menu()
    
if __name__ == '__main__':
    c=Controleur()
    