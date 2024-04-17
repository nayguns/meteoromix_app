def menu_selecao_user():

    print("\n    Meteoromix - App")

    # cidade = input(str("Qual cidade/município deseja consultar a previsão do tempo? ").capitalize())

    selecao_menu = int(input("""
          Escolha uma das opções abaixo:
                             
            1 - Consultar previsão do tempo atual.
            2 - Consultar previsão dos próximos dias.
            3 - Consultar previsão do tempo com data escolhida.

            9 - Para sair da aplicação.
            """))
    
    return selecao_menu