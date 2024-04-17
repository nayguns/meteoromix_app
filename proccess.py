import json
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import messagebox
import seaborn as sns


def processar_dados_prev_atual(dados):

    dados_prev_temp = json.loads(dados)["main"]

    dados_to_return = {
        'temperatura' : round(dados_prev_temp["temp"]),
        'sens_termica' : round(dados_prev_temp["feels_like"]),
        'temp_minima' : float(dados_prev_temp["temp_min"]),
        'temp_maxima' : float(dados_prev_temp["temp_max"]),
        'umidade_ar' : float(dados_prev_temp["humidity"]),
        'descricao_ceu' : json.loads(dados)["weather"][0]["description"],
        'cidade' : json.loads(dados)["name"],
        'vel_vento': round(float(json.loads(dados)["wind"]["speed"]) * 3.6, 1),
        'classifica_vento':  escala_classificacao_ventos(float(json.loads(dados)["wind"]["speed"]) * 3.6)
    }

    return dados_to_return


# ----------


def extract_dados_de_previsao(dados):
    return{
        "data_hora" : dados["dt_txt"],
        "dados_temp" : dados["main"],
        "clima" : dados["weather"][0]["description"],
        "vel_vento" : round(float(dados["wind"]["speed"]) * 3.6, 1),
        'classifica_vento':  escala_classificacao_ventos(float(dados["wind"]["speed"]) * 3.6)
    }


def processar_dados_prev_futura(dados):

    dados_prev_futura = json.loads(dados)["list"]

    result_processamento = [extract_dados_de_previsao(elem) for elem in dados_prev_futura]

    return result_processamento


def criar_df_prev_futura(dados):

    dados_df = processar_dados_prev_futura(dados)

    df = pd.DataFrame(dados_df)
    df["data"] = pd.to_datetime(df["data_hora"]).dt.date
    df["hora"] = pd.to_datetime(df["data_hora"]).dt.time

    df_dados_temp = pd.json_normalize(df["dados_temp"])

    df_to_normalize = [
        df[["data", "hora"]],
        df_dados_temp[["temp", "feels_like", "temp_min", "temp_max", "humidity"]],
        df[["clima", "vel_vento", "classifica_vento"]]
    ]

    df_previsao_tempo = pd.concat(df_to_normalize, axis = 1)
    df_previsao_tempo["data"] = pd.to_datetime(df_previsao_tempo["data"])

    df_previsao_tempo = df_previsao_tempo.rename(columns={
        "temp" : "temperatura",
        "feels_like" : "sensação_termica",
        "humidity": "umidade_ar"
    })

    return df_previsao_tempo


## Análises de previsão do tempo

## Previsão dos próximos dias


def previsao_proximos_dias(dataframe):

    dados_previsao_tempo = dataframe.groupby("data")[["temperatura", "sensação_termica", "umidade_ar", "vel_vento"]].agg({
        "temperatura": "mean",
        "sensação_termica": "mean",
        "umidade_ar": "mean",
        "vel_vento": "mean",
    }).round({"temperatura": 2, "sensação_termica": 2, "umidade_ar": 1, "vel_vento": 2})

    dados_previsao_tempo = dados_previsao_tempo.reset_index()

    return dados_previsao_tempo


## Previsão da data escolhida pelo user


def previsao_escolha_data(dataframe, data):

    resultado_previsao = dataframe.loc[dataframe.data == data]

    # print(resultado_previsao)

    return resultado_previsao


## Gráficos


def grafico_resumo_dias(dataframe):

    fig, ax = plt.subplots(figsize=(6, 3), layout='constrained')
    
    categories = dataframe["data"]

    ax.bar(categories, dataframe["temperatura"])
    ax.set_title("Previsão do tempo")
    ax.set_ylabel("Temperatura em (°C)")

    # plt.figure(figsize=(8, 5))
    # plots = sns.barplot(x="data", y="temperatura", data=dataframe)
    # for bar in plots.patches:

    #     plots.annotate(format(bar.get_height(), '.2f'),
    #                    (bar.get_x() + bar.get_width() /2,
    #                     bar.get_height()), ha='center', va='center',
    #                     size=10, xytext=(0, 8),
    #                     textcoords='offset points')
        
    # # plt.xlabel("Datas", size=14)
    # plt.ylabel("Temperatura em (°C)", size=5)
    # plt.title("Previsão do tempo")

    grafico = plt.show()

    return grafico


def grafico_variações_dia(dataframe, data):

    hora = [str(elem) for elem in dataframe["hora"]]
    temperatura = dataframe["temperatura"]
    dia = data
    
    fig, ax = plt.subplots(figsize=(10, 5), layout='constrained')

    ax.plot(hora, temperatura, linestyle='-', marker='o', color='green')
    ax.set(
        ylabel="Temperaturas",
        title=f"Previsão de temperaturas do dia: {dia}"
    )

    grafico = plt.show()

    return grafico


# Categoria ventos

def escala_classificacao_ventos(vel_vento: float):

    if vel_vento < 1:
        classific_vento = "Calmo"
    elif ((vel_vento > 1) and (vel_vento < 5)):
        classific_vento = "Aragem"
    elif ((vel_vento > 5) and (vel_vento < 11)):
        classific_vento = "Brisa leve"
    elif ((vel_vento > 11) and (vel_vento < 19)):
        classific_vento = "Brisa fraca"
    elif ((vel_vento > 19) and (vel_vento < 28)):
        classific_vento = "Brisa moderada"
    elif ((vel_vento > 28) and (vel_vento < 38)):
        classific_vento = "Brisa forte"
    elif ((vel_vento > 38) and (vel_vento < 49)):
        classific_vento = "Vento fresco"
    elif ((vel_vento > 49) and (vel_vento < 61)):
        classific_vento = "Vento forte"
    elif ((vel_vento > 61) and (vel_vento < 74)):
        classific_vento = "Ventania"
    elif ((vel_vento > 74) and (vel_vento < 88)):
        classific_vento = "Ventania forte"
    elif ((vel_vento > 88) and (vel_vento < 102)):
        classific_vento = "Tempestade"
    elif ((vel_vento > 102) and (vel_vento < 117)):
        classific_vento = "Tempestade violenta"
    elif vel_vento > 117:
        classific_vento = "Furacão"
        
    return classific_vento



# Alertas


def alerta_umidade_baixa():

    messagebox.showwarning('MeteoromixApp',\
                        'Cuidado, a umidade do ar baixa!\nProcure se hidratar bastante.')
    

def alerta_temperatura_alta():

    messagebox.showwarning('MeteoromixApp',\
                           'Cuidado, temperatura alta!\nProcure utilizar protetor solar e evitar muito tempo de exposição ao Sol.')
    

def alerta_temperatura_baixa():

    messagebox.showwarning('MeteoromixApp',\
                           'Cuidado com a baixa temperatura!\nProcure se agasalhar bem.')
    

def alerta_ventos_fortes():

    messagebox.showwarning('MeteoromixApp',\
                           'Cuidado com ventos fortes vindo por aí!')