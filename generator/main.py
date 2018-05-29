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

def rightOf(uiItem):
    return uiItem.winfo_reqwidth()+uiItem.place_info()['x']
def leftOf(uiItem):
    return -uiItem.winfo_reqwidth()+uiItem.place_info()['x']
def aboveOf(uiItem):
    return uiItem.winfo_reqheight()+uiItem.place_info()['y']
def underOf(uiItem):
    return -uiItem.winfo_reqheight()+uiItem.place_info()['y']

labelNome = Label(gui,text="Nome:")
labelNome.place(x=30,y=0)
print(labelNome.winfo_reqheight(),labelNome.place_info()['x'])
labelClasse = Label(gui,text="Classe:")
print(labelClasse.winfo_reqwidth())
labelClasse.place(x=0,y=30)
labelRaca = Label(gui,text="Raca:")
print(labelRaca.winfo_reqwidth())
labelRaca.place(x=0,y=60)
gui.mainloop()