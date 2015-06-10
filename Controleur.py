import sqlite3
from Modele import *
from Vue import *
class Controleur():
    def __init__(self):
        
        #c.execute("INSERT INTO Projets (projet, id) VALUES('Sennin', 2)")
        #conn.commit()

        
        self.modele=Modele(self)
        self.vue=Vue(self,self.modele.largeur,
                     self.modele.hauteur)
        self.menu()

    def menu(self):
        self.vue.menu()
    
if __name__ == '__main__':
    c=Controleur()