from tkinter import *
class Vue():
    def __init__(self,parent,longueur,hauteur):
        self.parent=parent
        self.longueur=longueur
        self.hauteur=hauteur
        self.listeMembres=[]
        self.root=Tk()
        self.root.resizable(0,0)
        self.root.title("Project Manager 1337")
        self.canevas=Canvas(self.root, bd=-2,width=self.longueur,height=self.hauteur,bg="black")
        self.canevas.pack()
        self.canevas.pack_propagate(False)
        self.frameMenu=FrameMenu(self.canevas,self,bg="#AC30D6",height=200,width=200,bd=9,relief=GROOVE)
        self.frameMenu.pack_propagate(False)
        self.frameProjet=FrameProjet(self.canevas,self,bg="#AC30D6",height=self.hauteur-18,width=self.longueur-18,bd=9,relief=GROOVE)
        self.creerFrameOuvrirProjet()
        
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
           self.buttonLoad = Button(self.frameOuvrirProjet, text = "LOAD", bg="pink")
           self.buttonLoad.pack(side=LEFT,padx=20)
           self.buttonDelete = Button(self.frameOuvrirProjet, text = "DELETE")
           self.buttonDelete.pack(side=LEFT,padx=20)
    def frameOuvrirProjet(self):
    	  self.swapper(self.frameOuvrirProjet)   
    
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
class FrameProjet(Frame):
    def __init__(self,master,vue,**kw):
        self.vue=vue
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
    def suivant(self):
        self.projet={}
        self.projet["nom"]=self.entryNom.get()
        self.projet["membres"]=self.listboxMembres.get(0, END)
        self.projet["Debut Projet"]=(self.spinBoxDate.get(),self.spinBoxMois.get())
        self.projet["Fin Projet"]=(self.spinBoxDate1.get(),self.spinBoxMois1.get())   
    def dateUpdate(self):
        self.spinBoxDate1.config(from_=1 ,to=self.joursParMois[self.spinBoxMois1.get()])  
        self.spinBoxDate.config(from_=1 ,to=self.joursParMois[self.spinBoxMois.get()])  
    def ajouterMembre(self):
        if(self.entryMembre.get()!=""):
            self.listboxMembres.insert(END,self.entryMembre.get())
            self.vue.listeMembres.append(self.entryMembre.get())
    def enleverMembre(self):
        self.vue.listeMembres.pop(self.listboxMembres.index(ACTIVE))
        self.listboxMembres.delete(self.listboxMembres.index(ACTIVE))
        
        

