#########################################################
#                                                       #
#  Le bouton pour editer les projets est a la ligne 88  #
#                                                       #
#########################################################
from tkinter import *
import tkinter as tk
class Vue():
    def __init__(self,parent,longueur,hauteur):
        self.parent=parent
        self.longueur=longueur
        self.hauteur=hauteur
        self.listeMembres=[]
        self.listeEtape=[]
        self.listeTache=[]
        self.id=None
        self.root=Tk()
        self.root.resizable(0,0)
        self.root.title("Project Manager 1337")
        self.canevas=Canvas(self.root, bd=-2,width=self.longueur,height=self.hauteur,bg="black")
        self.canevas.pack()
        self.canevas.pack_propagate(False)
        self.frameMenu=FrameMenu(self.canevas,self,bg="#AC30D6",height=200,width=200,bd=9,relief=GROOVE)
        self.frameMenu.pack_propagate(False)
        self.frameProjet=FrameProjet(self.canevas,self,bg="#AC30D6",height=self.hauteur-18,width=self.longueur-18,bd=9,relief=GROOVE)
        self.frameProjetSuivant=FrameProjetSuivant(self.canevas,self,bg="#AC30D6",height=self.hauteur-18,width=self.longueur-18,bd=9,relief=GROOVE)
        self.frameEtape=FrameEtape(self.canevas,self,bg="#AC30D6",height=self.hauteur-18,width=self.longueur-18,bd=9,relief=GROOVE)
        self.creerFrameOuvrirProjet()
        self.creerFrameLoadProjet()
        
        self.frameAffiche=None
    def menu(self):
        for i in range(self.longueur):
            self.canevas.create_line(self.longueur,0,i*10,self.hauteur,fill="#AC30D6")
        for i in range(self.hauteur):
            self.canevas.create_line(0,self.hauteur,self.longueur,i*20,fill="#AC30D6") 
        self.swapper(self.frameMenu)
        self.root.mainloop()
    
    def nouveauProjet(self):
        self.swapper(self.frameProjet)
    def swapper(self,frame):
        if(self.frameAffiche!=None):
            self.frameAffiche.pack_forget()
        self.frameAffiche=frame
        self.frameAffiche.pack()
        
    def creerFrameOuvrirProjet(self):
           self.frameOuvrirProjet = Frame(self.canevas,width=200, height=200, bg="red")
           self.labelNom=Label(self.frameOuvrirProjet, text="Projets", bg="#AC30D6")
           self.labelNom.pack()
           self.listeProjet=Listbox(self.frameOuvrirProjet)
           self.listeProjet.pack()
           self.buttonLoad = Button(self.frameOuvrirProjet, text = "LOAD", bg="pink", command=self.frameLoadProjet)
           self.buttonLoad.pack(side=LEFT,padx=20)
           self.buttonDelete = Button(self.frameOuvrirProjet, text = "DELETE", command=self.deleteProjet)
           self.buttonDelete.pack(side=LEFT,padx=20)
    def frameOuvrirProjet(self):
        nomDeProjets = self.parent.modele.listeProjet()
        for nom in nomDeProjets:
            self.listeProjet.insert(END, nom)
        #print(nomDeProjets)
        self.swapper(self.frameOuvrirProjet)
    
    def deleteProjet(self):
        delProjet = self.listeProjet.get(self.listeProjet.index(ACTIVE))
        print(delProjet)
        delProjetProjet = str(delProjet[1])
        self.parent.modele.effacerProjet(delProjetProjet) #####ICI!!!!!!!!!!!!!!!!!!!!!
        self.listeProjet.delete(self.listeProjet.index(ACTIVE))
        print(delProjet)
        print("Project successfully deleted")
    
    def creerFrameLoadProjet(self):
        self.frameLoadProjet = Frame(self.canevas,width=200, height=200)
        self.labelLoad=Label(self.frameLoadProjet, text="Projets")
        self.labelLoad.grid(sticky=W, column=0, row=0)
        self.lNomProjet = Label(self.frameLoadProjet, text="Nom du projet: ")
        self.lNomProjet.grid(sticky=W, column=0, row=1)
        self.lMembres = Label(self.frameLoadProjet, text="Membres: ")
        self.lMembres.grid(sticky=W, column=0, row=2)
        self.lEtapes = Label(self.frameLoadProjet, text="Etapes: ")
        self.lEtapes.grid(sticky=W, column=0, row=3)
        self.lSprints = Label(self.frameLoadProjet, text="Sprints: ")
        self.lSprints.grid(sticky=W, column=0, row=4)
        self.lTaches = Label(self.frameLoadProjet, text="Taches: ")
        self.lTaches.grid(sticky=W, column=0, row=5)
        self.lDebut = Label(self.frameLoadProjet, text="Debut: ")
        self.lDebut.grid(sticky=W, column=0, row=6)
        self.lFin = Label(self.frameLoadProjet, text="Fin: ")
        self.lFin.grid(sticky=W, column=1, row=6)
        self.bEdit = Button(self.frameLoadProjet, text="Edit")
        self.bEdit.grid(sticky=W+E, column=0, row=8)
        #print("ICI", self.parent.modele.listeProjet())
        #self.ListeEtape=Listbox(self.frameLoadProjet)
        #self.ListeEtape.pack()
        
    def frameLoadProjet(self):
        projetSelecter = self.listeProjet.get(self.listeProjet.index(ACTIVE))
        #print("Rici", projetSelecter[1])
        #self.labelLoad=(frameLoad)
        Projet = self.parent.modele.afficherProjet(str(projetSelecter[1]))
        print(Projet[0][1])
        Membres = self.parent.modele.afficherMembres(str(projetSelecter[1]))
        print(Membres)
        Etapes = self.parent.modele.afficherEtapes(str(projetSelecter[1]))
        print(Etapes)
        Sprints = self.parent.modele.afficherSprints(str(projetSelecter[1]))
        print(Sprints)
        Taches = self.parent.modele.afficherTaches(str(projetSelecter[1]))
        print(Taches)
        
        self.swapper(self.frameLoadProjet)
        
        
    def ouvrirEtape(self,etape):
        self.frameEtape.labelNom.config(text=self.listeEtape[etape]["nom"])
        taches=self.listeEtape[etape]["taches"]
        self.frameEtape.etape=etape
        for tache in taches:
            self.frameEtape.listboxTaches.insert(END,tache["nom"])
        for membre in self.parent.modele.getListeMembres(self.id):
            self.frameEtape.optionMenuMembres['menu'].add_command(label=membre, command=tk._setit(self.frameEtape.membres, membre))
        self.swapper(self.frameEtape)
        
         
        
        

    def creerFrameAfficherProjet(self):#####
        pass
    
    def frameAfficherProjet(self):#####
        pass

    
class FrameMenu(Frame):
    def __init__(self,master,vue,**kw):
        self.vue=vue
        Frame.__init__(self,master,**kw) #init de la classe dont j'herite
        self.bouttonCreer=Button(self,relief=RIDGE,overrelief=GROOVE,text="Nouveau Projet",bg="#AC30D6",command=self.vue.nouveauProjet)
        self.bouttonCreer.pack(pady=20)
        self.bouttonOuvrir=Button(self,relief=RIDGE,overrelief=GROOVE,text="Projet Existant",bg="#AC30D6",command=self.vue.frameOuvrirProjet)
        self.bouttonOuvrir.pack()
class FrameProjetSuivant(Frame):
    def __init__(self,master,vue,**kw):
        Frame.__init__(self,master,**kw) #init de la classe dont j'herite
        self.master=master
        self.vue=vue
        self.labelEtape=Label(self,text="Etape a ajouter ",bg="#AC30D6")
        self.labelEtape.grid(column=0,row=1)
        self.entryEtape=Entry(self)
        self.entryEtape.grid(column=1,row=1)
        self.buttonAjouterEtape=Button(self,text="Ajouter",command=self.ajouterEtape)
        self.buttonAjouterEtape.grid(column=2,row=1,padx=10)
        self.frameEtape=Frame(self,width=150,height=100,bg="#AC30D6",relief=GROOVE,bd=5)
        self.frameEtape.grid_propagate(True)
        self.labelEtapeTitre=Label(self.frameEtape,width=15,text="Etapes",bd=4,bg="#AC30D6",relief=RIDGE)
        self.labelEtapeTitre.grid(column=0,row=0,padx=10)
        self.frameEtape.grid(column=0,row=0)
        self.scrollbar = Scrollbar(self, orient=VERTICAL)
        self.scrollbar.grid(column=1,row=0)
        self.listboxEtape=Listbox(self.frameEtape,bg="#AC30D6",yscrollcommand=self.scrollbar.set)
        self.listboxEtape.grid(column=0,row=1)
        self.scrollbar.config(command=self.listboxEtape.yview)
        self.buttonEnleverEtape=Button(self,text="Enlever",command=self.enleverEtape)
        self.buttonEnleverEtape.grid(column=2,row=2)
        self.buttonModifierEtape=Button(self,text="Ouvrir",command=self.ouvrirEtape)
        self.buttonModifierEtape.grid(column=3,row=2)
        self.buttonSauvegardeQuitter=Button(self,text="Savegarder et quitter",command=self.updateProjet)
        self.buttonSauvegardeQuitter.grid(column=3,row=1)
        self.labelEtapeChoisie=Label(self,text="")
        self.spinBoxPriorite=Spinbox(self,from_=0, to=10)
        self.labelPriorite=Label(self,text="Priorite")
        
    def updateProjet(self):
        self.projet={"id":self.vue.id,"etapes":""}
        self.projet["etapes"]=self.vue.listeEtape
        self.vue.parent.modele.updateProjet(self.projet)   
    def ajouterEtape(self):
        if(self.entryEtape.get()!=""):
            self.listboxEtape.insert(END,self.entryEtape.get())
            self.vue.listeEtape.append({"nom":self.entryEtape.get(),"taches":[]})
        self.listboxEtape.activate(self.listboxEtape.index(ACTIVE))    
        self.ouvrirEtape()
    def enleverEtape(self):
        if(self.listboxEtape.index(ACTIVE)):
            self.vue.listeEtape.pop(self.listboxEtape.index(ACTIVE))
            self.listboxEtape.delete(self.listboxEtape.index(ACTIVE))
    def ouvrirEtape(self):
        self.etapeChoisie=self.listboxEtape.index(ACTIVE)
        self.vue.ouvrirEtape(self.etapeChoisie)
        
        
class FrameEtape(Frame):
    def __init__(self,master,vue,**kw):
         Frame.__init__(self,master,**kw) #init de la classe dont j'herite
         self.vue=vue
         self.prerequis=[]
         self.etape=None
         self.labelNom=Label(self,text="",bg="#AC30D6")
         self.labelNom.grid(row=0,column=0)
         self.labelTache=Label(self,text="Tache a ajouter ",bg="#AC30D6")
         self.labelTache.grid(column=0,row=1)
         self.entryTache=Entry(self)
         self.entryTache.grid(column=1,row=1)
         self.buttonAjouterTache=Button(self,text="Ajouter",command=self.ajouterTache)
         self.buttonAjouterTache.grid(column=2,row=1,padx=10)
         self.frameTaches=Frame(self,width=300,height=160,bg="#AC30D6",relief=GROOVE,bd=5)
         
         self.labelTachesTitre=Label(self.frameTaches,width=15,text="Taches",bd=4,bg="#AC30D6",relief=RIDGE)
         self.labelTachesTitre.grid(column=0,row=0,padx=10)
         self.labelPriorite=Label(self,text="Priorite",bg="#AC30D6")
         self.spinBoxPriorite=Spinbox(self,from_=1 ,to=10)
         self.spinBoxPriorite.grid(column=3,row=2)
         self.labelProprietaire=Label(self,text="Membre Proprietaire",bg="#AC30D6")
         self.labelProprietaire.grid(column=3,row=0)
         self.membres = StringVar(self)
         self.membres.set("") # initial value
         self.optionMenuMembres = OptionMenu(self, self.membres, "",)
         self.optionMenuMembres.grid(column=3,row=1)
         self.labelPriorite.grid(column=3,row=2,sticky=N)
         self.buttonAjouterPrerequis=Button(self,text="Ajouter",command=self.ajouterPrerequis)
         self.buttonEnleverPrerequis=Button(self,text="Enlever",command=self.enleverPrerequis)
         self.buttonEnleverPrerequis.grid(column=1,row=2)
         self.buttonAjouterPrerequis.grid(column=2,row=2)
         self.framePrerequis=Frame(self,width=150,height=50,bg="#AC30D6",relief=GROOVE,bd=5)
         self.labelTachePrerequis=Label(self.framePrerequis,text="Prerequis",bg="#AC30D6")
         self.listboxPrerequis=Listbox(self.framePrerequis,bg="#AC30D6",height=3)
         self.listboxPrerequis.grid(column=0,row=1)
         self.labelTachePrerequis.grid(column=0,row=0)
         self.framePrerequis.grid(column=0,row=2)
         self.frameTaches.grid(column=0,row=4)
         self.scrollbar = Scrollbar(self, orient=VERTICAL)
         self.scrollbar.grid(column=1,row=4)
         self.listboxTaches=Listbox(self.frameTaches,bg="#AC30D6",yscrollcommand=self.scrollbar.set)
         self.listboxTaches.grid(column=0,row=1)
         self.scrollbar.config(command=self.listboxTaches.yview)
         self.buttonEnleverTache=Button(self,text="Enlever",command=self.enleverTache)
         self.buttonEnleverTache.grid(column=2,row=4)
         self.buttonFinirEtape=Button(self,text="Finaliser Etape",command=self.suivant)
         self.buttonFinirEtape.grid(column=0,row=5)
    def ajouterPrerequis(self):
        self.prerequis.append(self.vue.listeEtape[self.etape]["taches"][self.listboxTaches.index(ACTIVE)])
        self.listboxPrerequis.insert(END,self.listboxTaches.get(self.listboxTaches.curselection()))
    def enleverPrerequis(self):
        self.prerequis.pop(self.listboxPrerequis.index(ACTIVE))
        self.listboxPrerequis.delete(self.listboxPrerequis.index(ACTIVE))
    def ajouterTache(self):
        if(self.entryTache.get()!=""):
            self.listboxTaches.insert(END,self.entryTache.get())
            nouvelleTache={"nom":"","priorite":"","prerequis":"","proprietaire":""}
            nouvelleTache["nom"]=self.entryTache.get()
            nouvelleTache["priorite"]=self.spinBoxPriorite.get()
            if(len(self.listboxPrerequis.get(0, END))>0):
                nouvelleTache["prerequis"]=self.prerequis
            self.vue.listeEtape[self.etape]["taches"].append(nouvelleTache)
    def enleverTache(self):
        self.listboxTaches.delete(self.listboxTaches.index(ACTIVE))
    def suivant(self):
        self.listboxPrerequis.delete(0, END)
        self.listboxTaches.delete(0,END)
        self.vue.swapper(self.vue.frameProjetSuivant)  
        
         
               
class FrameProjet(Frame):
    def __init__(self,master,vue,**kw):
        self.vue=vue
        self.projet={}
        self.calendrierMois=["Janvier","Fevrier","Mars","Avril","Mai","Juin","Juillet","Aout","Septembre","Octobre","Novembre","Decembre"]
        self.joursParMois={"Janvier":31
                           ,"Fevrier":28
                           ,"Mars":31
                           ,"Avril":30
                           ,"Mai":31
                           ,"Juin":30
                           ,"Juillet":31
                           ,"Aout":31
                           ,"Septembre":30
                           ,"Octobre":31
                           ,"Novembre":30
                           ,"Decembre":31}
        Frame.__init__(self,master,**kw) #init de la classe dont j'herite
        self.labelNom=Label(self,text="Nom du Projet ",bg="#AC30D6")
        self.labelNom.grid(column=0,row=0,padx=10,pady=10)
        self.entryNom=Entry(self)
        self.entryNom.grid(column=1,row=0)
        self.labelMembre=Label(self,text="Membre a ajouter ",bg="#AC30D6")
        self.labelMembre.grid(column=0,row=1)
        self.entryMembre=Entry(self)
        self.entryMembre.grid(column=1,row=1)
        self.buttonAjouterMembre=Button(self,text="Ajouter",command=self.ajouterMembre)
        self.buttonAjouterMembre.grid(column=2,row=1,padx=10)
        self.frameMembres=Frame(self,width=150,height=100,bg="#AC30D6",relief=GROOVE,bd=5)
        self.frameMembres.grid_propagate(True)
        self.labelMembresTitre=Label(self.frameMembres,width=15,text="Membres",bd=4,bg="#AC30D6",relief=RIDGE)
        self.labelMembresTitre.grid(column=0,row=0,padx=10)
        self.frameMembres.grid(column=0,row=2)
        self.scrollbar = Scrollbar(self, orient=VERTICAL)
        self.scrollbar.grid(column=1,row=2)
        self.listboxMembres=Listbox(self.frameMembres,bg="#AC30D6",yscrollcommand=self.scrollbar.set)
        self.listboxMembres.grid(column=0,row=1)
        self.scrollbar.config(command=self.listboxMembres.yview)
        self.buttonEnleverMembre=Button(self,text="Enlever",command=self.enleverMembre)
        self.buttonEnleverMembre.grid(column=2,row=2)
        self.labelDebut=Label(self,text="Debut du Projet: ",bg="#AC30D6")
        self.labelDebut.grid(column=0,row=3)
        self.spinBoxMois=Spinbox(self,values=self.calendrierMois,command=self.dateUpdate)
        self.spinBoxMois.grid(column=0,row=4)
        self.spinBoxDate=Spinbox(self,from_=1 ,to=self.joursParMois[self.spinBoxMois.get()])
        self.spinBoxDate.grid(column=1,row=4)
        self.labelFin=Label(self,text="Fin du Projet",bg="#AC30D6")
        self.labelFin.grid(column=0,row=5)
        self.spinBoxMois1=Spinbox(self,values=self.calendrierMois,command=self.dateUpdate)
        self.spinBoxMois1.grid(column=0,row=6)
        self.spinBoxDate1=Spinbox(self,from_=1 ,to=self.joursParMois[self.spinBoxMois1.get()])
        self.spinBoxDate1.grid(column=1,row=6)
        self.buttonSuivant=Button(self,text="Debut du Projet: ",bg="#AC30D6",command=self.suivant)
        self.buttonSuivant.grid(column=0,row=7)
        self.buttonSauvegarderProjet=Button(self,text="Sauvegarde du Projet: ",bg="#AC30D6",command=self.sauvegarde)
        self.buttonSauvegarderProjet.grid(column=1,row=7)
    def suivant(self):
        self.projet["nom"]=self.entryNom.get()
        self.projet["membres"]=self.listboxMembres.get(0, END)
        self.projet["debut Projet"]=(self.spinBoxDate.get(),self.spinBoxMois.get())
        self.projet["fin Projet"]=(self.spinBoxDate1.get(),self.spinBoxMois1.get())
        self.vue.id=self.vue.parent.modele.sauvegardeNouveau(self.projet)
        self.projet.clear()
        self.vue.swapper(self.vue.frameProjetSuivant)   
    def dateUpdate(self):
        self.spinBoxDate1.config(from_=1 ,to=self.joursParMois[self.spinBoxMois1.get()])  
        self.spinBoxDate.config(from_=1 ,to=self.joursParMois[self.spinBoxMois.get()])  
    def ajouterMembre(self):
        if(self.entryMembre.get()!=""):
            self.listboxMembres.insert(END,self.entryMembre.get())
            self.vue.listeMembres.append(self.entryMembre.get())
    def enleverMembre(self):
        if(self.listeboxMembres.index(ACTIVE)):
            self.vue.listeMembres.pop(self.listboxMembres.index(ACTIVE))
            self.listboxMembres.delete(self.listboxMembres.index(ACTIVE))
    def sauvegarde(self):
        self.projet["nom"]=self.entryNom.get()
        self.projet["membres"]=self.listboxMembres.get(0, END)
        self.projet["debut Projet"]=(self.spinBoxDate.get(),self.spinBoxMois.get())
        self.projet["fin Projet"]=(self.spinBoxDate1.get(),self.spinBoxMois1.get())
        self.vue.id=self.vue.parent.modele.sauvegardeNouveau(self.projet)
        self.projet.clear()
        self.vue.menu()
        

