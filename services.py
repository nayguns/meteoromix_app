## Funções para gravar e acessar retorno de API em arquivos.

def gravar_dados(dados, nome_arquivo = 'data/retorno_api.json'):
    """
    Esta função tem objetivo de gravar dados já estruturados(dict)
    de retorno de API.
    Deve se especificar nome do arquivo, caminho e extensão corretos.
    """
    with open(nome_arquivo, "w") as archive:
        archive.write(dados)
        archive.close()


def ler_dados(arquivo: str):
    """
    Função para acessar dados gravados em arquivos.
    Deve-se especificar o nome, caminho e extensão correto do arquivo.
    """
    with open(arquivo, "r") as archive:
        dados = archive.read()
        return dados