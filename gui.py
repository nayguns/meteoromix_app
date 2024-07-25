from tkinter import *
from tkinter import messagebox, ttk
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

import results

load_dotenv(override=True)

chaves_api = {
    'api_geo' : os.getenv("API_KEY_GEO"),
    'api_cur' : os.getenv("API_KEY_CURRENT"),
    'api_for' : os.getenv("API_KEY_FORECAST")
}

listaDatas = [datetime.strftime(datetime.today().date() + timedelta(elem), "%d/%m/%Y") for elem in range(5)]


def selecionar_data(event):

    dataSelecionada = dataSelect.get()
    return dataSelecionada

    # data_escolhida = Label(window, text=dataSelect.get(), font=fontText)
    # data_escolhida.grid(column=0, row=11)


def consulta_previsao():

    cidade = input_cidade.get()
    chaves = chaves_api
    opcaoSelect = opcaoValue.get()

    if opcaoSelect == 1:
        previsao_tempo = results.user_consulta_atual(cidade, chaves)
        retorno_consulta["text"] = previsao_tempo

    elif opcaoSelect == 2:
        previsao_futura = results.user_consulta_futura(cidade, chaves)
        retorno_consulta["text"] = previsao_futura

    elif opcaoSelect == 3:
        
        req_data.grid(column=0, row=9)
        
        diasLista.grid(column=0, row=10)
        dataSelecionada = diasLista.bind('<<ComboboxSelected>>', selecionar_data)
        print(dataSelecionada)
        retorno_consulta["text"] = f"Opção 3 selecionada {dataSelecionada}"

    else:
        retorno_consulta["text"] = "Opção inválida, tente outra vez!"





# Tela
window = Tk()
window.title("Meteoromix App")
window.geometry("600x400")

# Font style
fontTitle = ("Calibri", "18", "bold")
fontText = ("Calibri", "14")
fontBotao = ("Calibri", "12", "bold")

# Title
title_app = Label(window, text="MeteoromixApp", font=fontTitle)
title_app.grid(column=0, row=0)

texto_cidade = Label(window, text="Qual cidade/município deseja consultar a previsão do tempo?", font=fontText)
texto_cidade.grid(column=0, row=1)

input_cidade = Entry(window, width=30)
input_cidade.grid(column=0, row=2)

# Options
opcaoValue = IntVar()
opcaoValue.set(1)

opcaoTitle = Label(window, text="Opções para consultar previsão do tempo", font=fontText)
opcaoTitle.grid(column=0, row=3)

opcaoConsultaAtual = Radiobutton(window, text="Consultar previsão atual", variable=opcaoValue, font=fontText, value=1)
opcaoConsultaAtual.grid(column=0, row=4)
opcaoConsultaFutura = Radiobutton(window, text="Consultar previsão do tempo dos próximos 5 dias.", variable=opcaoValue, font=fontText, value=2)
opcaoConsultaFutura.grid(column=0, row=5)
opcaoConsultaDia = Radiobutton(window, text="Consultar previsão do tempo de uma data específica", variable=opcaoValue, font=fontText, value=3)
opcaoConsultaDia.grid(column=0, row=6)

botao_consulta = Button(window, text="Consultar previsão do tempo", command=consulta_previsao, font=fontBotao)
botao_consulta.grid(column=0, row=7)

req_data = Label(window, text="Informe a data que deseja consultar previsao do tempo", font=fontText)
dataSelect = StringVar()
diasLista = ttk.Combobox(window, textvariable=dataSelect, values=listaDatas, state="readonly")


# Resultado
retorno_consulta = Label(window, text="", font=fontText)
retorno_consulta.grid(column=0, row=8)


window.mainloop()