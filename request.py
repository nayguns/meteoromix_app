import requests as req
import json

import proccess


def dados_geograficos_cidade(cidade: str, chave_api: str):
    """
    Esta função consulta via API dados da cidade requisitada pelo user.
    """
    consulta_cidade = req.get(f"http://api.openweathermap.org/geo/1.0/direct?q={cidade}&limit=5&appid={chave_api}")
    retorno_dados = consulta_cidade.json()
    return retorno_dados


def requisicao_previsao_tempo(latitude: str, longitude: str, chave_api_prev: str):
    """
    Esta função consulta via API previsão atual da cidade requisitada pelo user.
    """
    previsao_atual = req.get(f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={chave_api_prev}&units=metric&lang=pt_br')
    dados_previsao_atual = previsao_atual.json()
    return dados_previsao_atual


def requisicao_previsao_futura(latitude: str, longitude: str, chave_api_fut: str):
    """
    Esta função consulta via API previsão futura da cidade requisitada pelo user.
    """
    previsao_futura = req.get(f"https://api.openweathermap.org/data/2.5/forecast?lat={latitude}&lon={longitude}&appid={chave_api_fut}&units=metric&lang=pt_br")
    dados_previsao_futura = previsao_futura.json()
    return(dados_previsao_futura)


def extracao_dados_cidade(cidade: str, api_key_geo: str):
    """
    Esta função trata os dados para persistencia em arquivo.
    """

    dados_retorno = dados_geograficos_cidade(cidade, api_key_geo)

    dados = dados_retorno[0]
        
    nome_cidade = dados["name"]
    latitude = dados["lat"]
    longitude = dados["lon"]

    print(f"Cidade: {nome_cidade} | Latitude: {latitude}, Longitude: {longitude}")
    
    return latitude, longitude


def consulta_previsao_atual(cidade: str, chaves_api: dict):

    # Atribuição de chaves da API
    api_key_geo = chaves_api["api_geo"]
    api_key_cur = chaves_api["api_cur"]

    dados_cidade = extracao_dados_cidade(cidade, api_key_geo)
    latitude = dados_cidade[0]
    longitude = dados_cidade[1]

    previsao_atual = requisicao_previsao_tempo(latitude, longitude, api_key_cur)
    convert_prev_atual = json.dumps(previsao_atual, ensure_ascii = False, indent = 2)
    return convert_prev_atual


def consulta_previsao_futura(cidade: str, chaves_api: dict):

    # Atribuição de chaves da API
    api_key_geo = chaves_api["api_geo"]
    api_key_fut = chaves_api["api_for"]

    dados_cidade = extracao_dados_cidade(cidade, api_key_geo)
    latitude = dados_cidade[0]
    longitude = dados_cidade[1]

    previsao_futura = requisicao_previsao_futura(latitude, longitude, api_key_fut)
    convert_prev_futura = json.dumps(previsao_futura, ensure_ascii = False, indent = 2)
    return convert_prev_futura


def requisitar_previsao_atual(cidade, chave):

    result_consulta = consulta_previsao_atual(cidade, chave)
    retorno_dados = proccess.processar_dados_prev_atual(result_consulta)

    return retorno_dados


def requisitar_previsao_futura(cidade, chave):

    result_consulta = consulta_previsao_futura(cidade, chave)
    retorno_dados = proccess.criar_df_prev_futura(result_consulta)
    previsao_dias = proccess.previsao_proximos_dias(retorno_dados)
    
    proccess.grafico_resumo_dias(previsao_dias)

    return previsao_dias


def requisitar_previsao_dia(cidade, chave, data):

    result_consulta = consulta_previsao_futura(cidade, chave)
    retorno_dados = proccess.criar_df_prev_futura(result_consulta)
    consulta_dia = proccess.previsao_escolha_data(retorno_dados, data)
    
    proccess.grafico_variações_dia(consulta_dia, data)

    return consulta_dia


def acionar_alertas(opcao_alerta: int):
    """
    Este método tem função de acionar alertas para o usuário.\n
    Para tal, na chamada do método usar as opções conforme abaixo:

      [1] - Umidade baixa;\n
      [2] - Altas temperaturas;\n
      [3] - Baixas temperaturas;\n
      [4] - Ventos fortes;
    """
    if opcao_alerta == 1:
        proccess.alerta_umidade_baixa()
    elif opcao_alerta == 2:
        proccess.alerta_temperatura_alta()
    elif opcao_alerta == 3:
        proccess.alerta_temperatura_baixa()
    elif opcao_alerta == 4:
        proccess.alerta_ventos_fortes()