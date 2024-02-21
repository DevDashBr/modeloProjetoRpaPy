import logging
import pandas as pd
import os

logger = logging.getLogger(__name__)


def ObterDadosEntrada(dict_config):

    logger.info("Obter os dados do arquivo de entrada...")

    caminho_arquivo_excel = dict_config['caminho_arquivo_excel']
    print(caminho_arquivo_excel)

    # Lista todos os arquivos no diretório
    arquivos_no_diretorio = os.listdir(caminho_arquivo_excel)

    # Filtra apenas os arquivos Excel
    arquivos_excel = [arquivo for arquivo in arquivos_no_diretorio if arquivo.endswith(
        '.xlsx') or arquivo.endswith('.xls')]

    for arquivo in arquivos_excel:
        # Caminho completo do arquivo
        caminho_completo = os.path.join(caminho_arquivo_excel, arquivo)

        # Carregar o arquivo Excel
        dados_excel = pd.read_excel(caminho_completo)
        dict_config['dados_excel'] = dados_excel
        print(dict_config['dados_excel'])
        dict_config['diretorio_completo_arquivo_excel'] = caminho_completo

    return (dict_config)
