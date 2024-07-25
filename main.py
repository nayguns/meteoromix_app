import os
from dotenv import load_dotenv
import matplotlib.pyplot as plt

import request as requ
import results
import proccess as prc
import menu

load_dotenv(override=True)

#chave = os.getenv("API_KEY_GEO")

chaves_api = {
    'api_geo' : os.getenv("API_KEY_GEO"),
    'api_cur' : os.getenv("API_KEY_CURRENT"),
    'api_for' : os.getenv("API_KEY_FORECAST")
}

# teste commit
def main():

    cidade = input(str("Qual cidade/município deseja consultar a previsão do tempo? ").capitalize())
    escolha_selecao = 0

    while escolha_selecao != 0:

        escolha_selecao = menu.menu_selecao_user()

        if escolha_selecao == 1:
            results.user_consulta_atual(cidade, chaves_api)
            pass
        elif escolha_selecao == 2:
            results.user_consulta_futura(cidade, chaves_api)
            pass
        elif escolha_selecao == 3:
            results.user_consulta_prev_fut_esc_data(cidade, chaves_api)
            pass
        elif escolha_selecao == 0:
            print("Obrigado!")
        else:
            print("Opção inválida, tente novamente!")


    # results.user_consulta_prev_fut_esc_data(cidade, chaves_api)



if __name__ == "__main__":
    main()