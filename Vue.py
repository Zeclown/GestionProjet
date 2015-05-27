from tkinter import *
class Vue():
    def __init__(self,parent,longueur,hauteur):
        self.parent=parent
        self.longueur=longueur
        self.hauteur=hauteur
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
           self.buttonFyall = Button(self.frameOuvrirProjet, text = "VELOCIRAPTOR!", bg="blue")
           self.buttonFyall.pack()
    def frameOuvrirProjet(self):
    	  self.swapper(self.frameOuvrirProjet)   

class FrameMenu(Frame):
    def __init__(self,master,vue,**kw):
        self.vue=vue
        Frame.__init__(self,master,**kw) #init de la classe dont j'herite
        self.BouttonCreer=Button(self,relief=RIDGE,overrelief=GROOVE,text="Nouveau Projet",bg="#AC30D6")
        self.BouttonCreer.pack(pady=20)
        self.BouttonOuvrir=Button(self,relief=RIDGE,overrelief=GROOVE,text="Projet Existant",bg="#AC30D6", command=self.vue.frameOuvrirProjet)
        self.BouttonOuvrir.pack()
    

        self.bouttonCreer=Button(self,relief=RIDGE,overrelief=GROOVE,text="Nouveau Projet",bg="#AC30D6",command=self.vue.nouveauProjet)
        self.bouttonCreer.pack(pady=20)
        self.bouttonOuvrir=Button(self,relief=RIDGE,overrelief=GROOVE,text="Projet Existant",bg="#AC30D6")
        self.bouttonOuvrir.pack()
class FrameProjet(Frame):
    def __init__(self,master,vue,**kw):
        self.vue=vue
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
        
    def ajouterMembre(self):
        if(self.entryMembre.get()!=""):
            self.listboxMembres.insert(END,self.entryMembre.get())
            self.vue.parent.ajouterMembre()
        
        

