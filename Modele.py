import sqlite3
class Modele():
    def __init__(self,parent):
        self.largeur=700
        self.hauteur=400
        self.parent=parent
        self.conn = sqlite3.connect('donnees4.db')
        self.c = self.conn.cursor()
        self.c.execute("CREATE TABLE IF NOT EXISTS Projets (id INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL  UNIQUE,projet text , debut date, fin date )")
        self.c.execute("CREATE TABLE IF NOT EXISTS Etapes (id INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL  UNIQUE,projetId int,  nom text, duree int,priorite int ,FOREIGN KEY (projetId) REFERENCES Projets(id) ON DELETE CASCADE) ")
        self.c.execute("CREATE TABLE IF NOT EXISTS Membres (id INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL  UNIQUE,nom text,projetId int,FOREIGN KEY (projetId) REFERENCES Projets(id) ON DELETE CASCADE)")
        self.c.execute("CREATE TABLE IF NOT EXISTS Taches (id INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL  UNIQUE,etapeId int,nom text, duree reel,sprintId int,responsableId int,completion int, priorite int,FOREIGN KEY (sprintId) REFERENCES Sprints(id) ON DELETE CASCADE, FOREIGN KEY (responsableId) REFERENCES Membres(id) ON DELETE CASCADE) ")
        self.c.execute("CREATE TABLE IF NOT EXISTS Sprints (id INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL  UNIQUE,projetId int,nom text,FOREIGN KEY (projetId) REFERENCES Projets(id) ON DELETE CASCADE) ")
        self.c.execute("CREATE TABLE IF NOT EXISTS TachesPrerequis (tacheId int, prerequisId int,FOREIGN KEY (tacheId) REFERENCES Taches(id) ON DELETE CASCADE,FOREIGN KEY (prerequisId) REFERENCES Taches(id) ON DELETE CASCADE)")
        
    def sauvegardeNouveau(self,projet):
        datedebut="2015"+"-"+str(projet["debut Projet"][0])+"-"+str(projet["debut Projet"][1])
        datefin="2015"+"-"+str(projet["fin Projet"][0])+"-"+str(projet["fin Projet"][1])
        commande="INSERT INTO Projets(id,projet,debut,fin) VALUES(NULL,"+"'"+projet["nom"]+"'"+","+"'"+datedebut+"'"+","+"'"+datefin+"')"
        print(commande)
        self.c.execute(commande)
        self.c.execute("SELECT last_insert_rowid() FROM Projets")
        id=self.c.fetchone()
        print(id)
        if(projet["membres"]):
            for membre in projet["membres"]:
                commande="INSERT INTO Membres(id,nom,projetId) VALUES(NULL,"+"'"+str(membre)+"'"+","+str(id[0])+")"
                self.c.execute(commande)
                print(commande)
        return id
    def getListeMembres(self,id):
        self.c.execute("SELECT nom FROM Membres WHERE projetId="+str(id[0]))
        return self.c.fetchall()
        
    def updateProjet(self,projet):
        if(projet["id"]):
            id=projet["id"]
        else:
            self.c.execute("SELECT last_insert_rowid() FROM Projets")
            id=self.c.fetchone()
            id=id[0]
        if(projet["etapes"]):
            self.c.execute("DELETE FROM Etapes WHERE projetId=" + str(id[0]))
            for i in projet["etapes"]:
                self.c.execute("INSERT INTO Etapes(id,projetId,nom,duree,priorite) VALUES(NULL,"+str(id[0])+",'" + i[0]+","+ i[1]+","+i[2]+")")
                self.c.execute("SELECT last_insert_rowid() FROM Etapes")
                idEtape=self.c.fetchone()
                idEtape=idEtape[0]
                if(i[3]):
                    self.c.execute("DELETE FROM Taches WHERE etapeId=" + id)
                    for j in projet["etapes"]:
                        for i in j["taches"]:
                            self.c.execute("INSERT INTO Taches(id,etapeId,nom,duree,sprintId,responsableId,completion,priorite) VALUES(NULL,"+idEtape+",'" + i[0]+","+ i[1]+","+i[2]+")")
                        
         
        
        self.conn.commit()
    def listeProjet(self):
        self.c.execute("SELECT projet, id FROM Projets")
        return (self.c.fetchall())

    
    def effacerProjet(self, delProjet):
        self.c.execute("DELETE FROM Projets WHERE id=" + delProjet)
        self.conn.commit()
        
    def afficherProjet(self):
        self.c.execute("SELECT * FROM Projets")
        return (self.c.fetchall())
    def afficherMembres(self):
        self.c.execute("SELECT * FROM Membres WHERE projetId = 1")
        return (self.c.fetchall())
    def afficherEtapes(self):
        self.c.execute("SELECT * FROM Etapes WHERE projetId = 1")
        return (self.c.fetchall())
    def afficherSprints(self):
        self.c.execute("SELECT * FROM Sprints WHERE projetId = 1")
        return (self.c.fetchall()) 
    def afficherTaches(self):
        self.c.execute("SELECT * FROM Taches WHERE sprintId = 1")
        return (self.c.fetchall())
