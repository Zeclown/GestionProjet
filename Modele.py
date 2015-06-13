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
        tableau=[]
        tableau=self.c.fetchall()
        for i in tableau:
            i=i[0]
        return tableau
    def getIdMembre(self,projetid,nom):
        nom = nom[:-2]
        nom=nom[1:]
        print("SELECT id FROM Membres WHERE projetId="+str(projetid[0]) +" AND nom =" +nom)
        self.c.execute("SELECT id FROM Membres WHERE projetId="+str(projetid[0]) +" AND nom =" +nom)
        return self.c.fetchone()
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
                duree=0
                for j in i["taches"]:
                    duree+=int(j["duree"])
                print("INSERT INTO Etapes(id,projetId,nom,duree,priorite) VALUES(NULL,"+str(id[0])+",'" + i["nom"]+"',"+ str(duree)+","+i["priorite"]+")")
                self.c.execute("INSERT INTO Etapes(id,projetId,nom,duree,priorite) VALUES(NULL,"+str(id[0])+",'" + i["nom"]+"',"+ str(duree)+","+i["priorite"]+")")
                self.c.execute("SELECT last_insert_rowid() FROM Etapes")
                idEtape=self.c.fetchone()
                idEtape=idEtape[0]
                if(i["taches"]):
                    self.c.execute("DELETE FROM Taches WHERE etapeId=" + str(idEtape))
                    for s in i["taches"]:
                        print("INSERT INTO Taches(id,etapeId,nom,duree,sprintId,responsableId,completion,priorite) VALUES(NULL,"+str(idEtape)+",'" + s["nom"]+"',"+ str(s["duree"])+","+str(s["proprietaire"][0])+","+str(s["sprint"])+","+str(s["completion"])+","+str(s["priorite"])+")")
                        self.c.execute("INSERT INTO Taches(id,etapeId,nom,duree,sprintId,responsableId,completion,priorite) VALUES(NULL,"+str(idEtape)+",'" + s["nom"]+"',"+ str(s["duree"])+","+str(s["proprietaire"][0])+","+str(s["sprint"])+","+str(s["completion"])+","+str(s["priorite"])+")")
                    
     
        
        self.conn.commit()
    def listeProjet(self):
        self.c.execute("SELECT projet, id FROM Projets")
        return (self.c.fetchall())

    
    def effacerProjet(self, delProjet):
        self.c.execute("DELETE FROM Projets WHERE id=" + delProjet)
        self.conn.commit()
        
    def afficherProjet(self, projetID):
        self.c.execute("SELECT * FROM Projets WHERE id=" + projetID)
        return (self.c.fetchall())
    def afficherMembres(self, projetID):
        self.c.execute("SELECT nom FROM Membres WHERE projetId=" + projetID)
        return (self.c.fetchall())
    def afficherEtapes(self, projetID):
        self.c.execute("SELECT nom FROM Etapes WHERE projetId=" + projetID)
        return (self.c.fetchall())
    def afficherSprints(self, projetID):
        self.c.execute("SELECT nom FROM Sprints WHERE projetId=" + projetID)
        return (self.c.fetchall()) 
    def afficherTaches(self, projetID):
        self.c.execute("SELECT nom FROM Taches WHERE sprintId=(SELECT id FROM Sprints WHERE projetId=" + projetID + ")")
        return (self.c.fetchall())
