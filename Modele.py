import sqlite3
class Modele():
    def __init__(self,parent):
        self.largeur=700
        self.hauteur=400
        self.parent=parent
        self.conn = sqlite3.connect('donnees4.db')
        self.c = self.conn.cursor()
        self.c.execute("CREATE TABLE IF NOT EXISTS Projets (id INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL  UNIQUE,projet text , debut date, fin date )")
        self.c.execute("CREATE TABLE IF NOT EXISTS Etapes (projetId int, id int AUTO_INCREMENT, nom text, duree date,priorite int ,PRIMARY KEY (id),FOREIGN KEY (projetId) REFERENCES Projets(id) ON DELETE CASCADE) ")
        self.c.execute("CREATE TABLE IF NOT EXISTS Membres (projetId int, nom text, id int AUTO_INCREMENT ,PRIMARY KEY (id),FOREIGN KEY (projetId) REFERENCES Projets(id) ON DELETE CASCADE)")
        self.c.execute("CREATE TABLE IF NOT EXISTS Taches (EtapeId int,id int AUTO_INCREMENT,nom text, duree reel,sprintId int,responsableId int,completion int, priorite int,PRIMARY KEY (id),FOREIGN KEY (sprintId) REFERENCES Sprints(id) ON DELETE CASCADE, FOREIGN KEY (responsableId) REFERENCES Membres(id) ON DELETE CASCADE) ")
        self.c.execute("CREATE TABLE IF NOT EXISTS Sprints (projetId int, id int AUTO_INCREMENT, nom text,PRIMARY KEY (id),FOREIGN KEY (projetId) REFERENCES Projets(id) ON DELETE CASCADE) ")
        self.c.execute("CREATE TABLE IF NOT EXISTS TachesPrerequis (tacheId int, prerequisId int,FOREIGN KEY (tacheId) REFERENCES Taches(id) ON DELETE CASCADE,FOREIGN KEY (prerequisId) REFERENCES Taches(id) ON DELETE CASCADE)")
        
    def sauvegardeNouveau(self,projet):
        datedebut="2015"+"-"+str(projet["Debut Projet"][0])+"-"+str(projet["Debut Projet"][1])
        datefin="2015"+"-"+str(projet["Fin Projet"][0])+"-"+str(projet["Fin Projet"][1])
        commande="INSERT INTO Projets(id,projet,debut,fin) VALUES(NULL,"+"'"+projet["nom"]+"'"+","+"'"+datedebut+"'"+","+"'"+datefin+"')"
        print(commande)
        self.c.execute(commande)
        
        self.conn.commit()
    def listeProjet(self):
        self.c.execute("SELECT projet, id FROM Projets")
        return (self.c.fetchall())

