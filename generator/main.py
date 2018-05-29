from tkinter import *
from tkinter import ttk
import generator.randomHeroGenerator as hg

def Cumprimente():
    hello.set("Olá, você!")

gui = Tk()

gui.title("Py5 - Python + Tkinter")
gui.geometry("600x400")

txt = Entry(gui, width=10)
txt.place(x=0, y=0)

btn = Button(gui, text="Cumprimente", command=Cumprimente)
btn.place(x=0, y=25)

listaClasse = StringVar()
comboClasse = ttk.Combobox(gui, textvariable=listaClasse,text="Classes")
comboClasse["values"] = hg.classeLista()
comboClasse.place(x=0,y=50)

listaRaca = StringVar()
comboRaca = ttk.Combobox(gui, textvariable=listaRaca,text="Raca")
comboRaca["values"] = hg.racaLista()
comboRaca.place(x=0,y=75)

hello = StringVar()
lbl = Label(gui, textvariable=hello)
lbl.place(x=0,y=100)

gui.mainloop()