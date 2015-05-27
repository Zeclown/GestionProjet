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
    def menu(self):
        for i in range(self.longueur):
            self.canevas.create_line(self.longueur,0,i*10,self.hauteur,fill="#AC30D6")
        for i in range(self.hauteur):
            self.canevas.create_line(0,self.hauteur,self.longueur,i*20,fill="#AC30D6")
        self.frameMenu=FrameMenu(self.canevas,self,bg="#AC30D6",height=200,width=200,bd=9,relief=GROOVE)
        self.frameMenu.pack_propagate(False)
        self.frameMenu.pack()
        self.root.mainloop()
class FrameMenu(Frame):
    def __init__(self,master,vue,**kw):
        self.vue=vue
        Frame.__init__(self,master,**kw) #init de la classe dont j'herite
        self.BouttonCreer=Button(self,relief=RIDGE,overrelief=GROOVE,text="Nouveau Projet",bg="#AC30D6")
        self.BouttonCreer.pack(pady=20)
        self.BouttonOuvrir=Button(self,relief=RIDGE,overrelief=GROOVE,text="Projet Existant",bg="#AC30D6")
        self.BouttonOuvrir.pack()
        