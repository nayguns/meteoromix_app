import request

CONST_UMIDADE_BAIXA = 20
CONST_ALTA_TEMPERATURA = 38
CONST_BAIXA_TEMPERATURA = 10
CONST_VELOCIDADE_VENTO = 50

def retorno_tela_previsao_atual(cidade, temperatura, temp_minima, temp_maxima, sens_termica, umidade_ar, descricao_ceu, vel_vento, classifica_vento):

    print(f'''
          Hoje na cidade de {cidade} o clima está assim:
          
           -> Temperatura atual: {temperatura}°C,
           -> Com previsão de variação entre: {temp_minima:,.1f}°C - {temp_maxima:,.1f}°C.
           -> Porém, a sensação térmica é de: {sens_termica}°C,
           -> E a umidade relativa do ar é de {umidade_ar:,.1f}%.
           -> A velocidade do vento está a {vel_vento:,.1f}Km/h, classificado como {classifica_vento}
           -> Ah, propósito, não sei se reparou mas hoje o céu está {descricao_ceu}''')
    
    str_previsao = f'''
          Hoje na cidade de {cidade} o clima está assim:
          
           -> Temperatura atual: {temperatura}°C,
           -> Com previsão de variação entre: {temp_minima:,.1f}°C - {temp_maxima:,.1f}°C.
           -> Porém, a sensação térmica é de: {sens_termica}°C,
           -> E a umidade relativa do ar é de {umidade_ar:,.1f}%.
           -> A velocidade do vento está a {vel_vento:,.1f}Km/h, classificado como {classifica_vento}
           -> Ah, propósito, não sei se reparou mas hoje o céu está {descricao_ceu}'''
    
    return str_previsao
    

def user_consulta_atual(cidade, chave):

    inp = request.requisitar_previsao_atual(cidade, chave)
    
    previsao = retorno_tela_previsao_atual(
        inp["cidade"],
        inp["temperatura"],
        inp["temp_minima"],
        inp["temp_maxima"],
        inp["sens_termica"],
        inp["umidade_ar"],
        inp["descricao_ceu"],
        inp["vel_vento"],
        inp["classifica_vento"]
    )

    if inp["umidade_ar"] <= CONST_UMIDADE_BAIXA:
        request.acionar_alertas(1)
    elif inp["temperatura"] >= CONST_ALTA_TEMPERATURA:
        request.acionar_alertas(2)
    elif inp["temperatura"] <= CONST_BAIXA_TEMPERATURA:
        request.acionar_alertas(3)
    elif inp["vel_vento"] >= CONST_VELOCIDADE_VENTO:
        request.acionar_alertas(4)

    return previsao


def user_consulta_futura(cidade, chave):

    inp2 = request.requisitar_previsao_futura(cidade, chave)

    alta_temp = inp2.loc[inp2.temperatura >= CONST_ALTA_TEMPERATURA]
    umidade_baixa = inp2.loc[inp2.umidade_ar <= CONST_UMIDADE_BAIXA]
    baixa_temp = inp2.loc[inp2.temperatura <= CONST_BAIXA_TEMPERATURA]
    ventos = inp2.loc[inp2.vel_vento >= CONST_VELOCIDADE_VENTO]

    if len(umidade_baixa) >= 1:
        request.acionar_alertas(1)
    elif len(alta_temp) >= 1:
        request.acionar_alertas(2)
    elif len(baixa_temp) >= 1:
        request.acionar_alertas(3)
    elif len(ventos) >= 1:
        request.acionar_alertas(4)


def user_consulta_prev_fut_esc_data(cidade, chave, data_consulta):

    # data_consulta = data_consulta = input(str("Informe uma data que deseja ver a previsão do tempo: "))

    inp3 = request.requisitar_previsao_dia(cidade, chave, data_consulta)

    alta_temp = inp3.loc[inp3.temperatura >= CONST_ALTA_TEMPERATURA]
    umidade_baixa = inp3.loc[inp3.umidade_ar <= CONST_UMIDADE_BAIXA]
    baixa_temp = inp3.loc[inp3.temperatura <= CONST_BAIXA_TEMPERATURA]
    ventos = inp3.loc[inp3.vel_vento >= CONST_VELOCIDADE_VENTO]

    if len(umidade_baixa) >= 1:
        request.acionar_alertas(1)
    elif len(alta_temp) >= 1:
        request.acionar_alertas(2)
    elif len(baixa_temp) >= 1:
        request.acionar_alertas(3)
    elif len(ventos) >= 1:
        request.acionar_alertas(4)