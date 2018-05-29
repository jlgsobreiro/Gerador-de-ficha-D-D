from tkinter import *
from tkinter import ttk
import generator.randomHeroGenerator as hg


def Cumprimente():
    hello.set("Olá, você!")


def right_of(ui_item):
    return ui_item.winfo_reqwidth() + int(ui_item.place_info()['x']), ui_item.place_info()['y']


def left_of(ui_item):
    return -ui_item.winfo_reqwidth() + int(ui_item.place_info()['x']),ui_item.place_info()['y']


def above_of(ui_item):
    return ui_item.place_info()['x'],-ui_item.winfo_reqheight() + int(ui_item.place_info()['y'])


def under_of(ui_item):
    return ui_item.place_info()['x'],ui_item.winfo_reqheight() + int(ui_item.place_info()['y'])


gui = Tk()
gui.title("Py5 - Python + Tkinter")
gui.geometry("600x400")

labelNome = Label(gui, text="Nome:")
labelNome.place(x=0, y=0)

labelClasse = Label(gui, text="Classe:")
labelClasse.place(x=0, y=30)

labelRaca = Label(gui, text="Raca:")
labelRaca.place(x=0, y=60)

nome_entrada = Entry(gui, width=10)
nome_entrada.place(x=right_of(labelNome)[0],y=right_of(labelNome)[1])

listaClasse = StringVar()
comboClasse = ttk.Combobox(gui, textvariable=listaClasse, text="Classes")
comboClasse["values"] = hg.classeLista()
comboClasse.place(x=right_of(labelClasse)[0],y=right_of(labelClasse)[1])

listaRaca = StringVar()
comboRaca = ttk.Combobox(gui, textvariable=listaRaca, text="Raca")
comboRaca["values"] = hg.racaLista()
comboRaca.place(x=right_of(labelRaca)[0],y=right_of(labelRaca)[1])

btn = Button(gui, text="Cumprimente", command=Cumprimente)
btn.place(x=right_of(comboRaca)[0],y=(under_of(comboRaca)[1]+10))

hello = StringVar()
lbl = Label(gui, textvariable=hello)
lbl.place(x=under_of(btn)[0],y=(under_of(btn)[1]))

gui.mainloop()
