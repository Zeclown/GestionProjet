from tkinter import *
class App():
    def __init__(self, master):
        frameOuvrirProjet = Frame(master, width=5000, height=5000, bg="red")
        frameOuvrirProjet.pack()
        buttonFyall = Button(frameOuvrirProjet, text = "VELOCIRAPTOR!", bg="blue")
        buttonFyall.pack()
root = Tk()
root.title("Fuck y'all")
app = App(root)
root.mainloop()
