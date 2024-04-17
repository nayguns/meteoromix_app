from tkinter import *
from tkinter import messagebox, ttk
from datetime import datetime, timedelta

import request
import results

data_list = [datetime.strftime(datetime.today().date() + timedelta(elem), "%d/%m/%Y") for elem in range(5)]


tela = Tk()
tela.geometry("400x200")
tela.title("Teste Combobox")


# Font style
fontTitle = ("Calibri", "18", "bold")
fontText = ("Calibri", "14")
fontBotao = ("Calibri", "12", "bold")


tituloTest = Label(tela, text="Teste com Combobox", font=fontTitle)
tituloTest.grid(column=0, row=0)

textTest = Label(tela, text="Texto apenas para estruturar frame", font=fontText)
textTest.grid(column=0, row=1)

testeData = Label(tela, text=data_list, font=fontText)
testeData.grid(column=0, row=2)

dataSelect = StringVar()
dias = ttk.Combobox(tela, textvariable=dataSelect, values=data_list, state="readonly")
dias.grid(column=0, row=3)


def dia_selecionado(event):
    mostrar_dia = Label(tela, text=dataSelect.get(), font=fontText)
    mostrar_dia.grid(column=0, row=4)

dias.bind('<<ComboboxSelected>>', dia_selecionado)

tela.mainloop()