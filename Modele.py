import sqlite3
class Modele():
    def __init__(self,parent):
        self.largeur=700
        self.hauteur=400
        self.parent=parent
        self.conn = sqlite3.connect('donnees.db')
        self.c = self.conn.cursor()
        
    def listeProjet(self):
        self.c.execute("SELECT projet, id FROM Projets")
        return (self.c.fetchall())