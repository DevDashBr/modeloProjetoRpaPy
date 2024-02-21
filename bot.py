import logging
import estrutura_arquivos_py.config as config
import estrutura_arquivos_py.funcoes as funcoes

logger = logging.getLogger(__name__)


def main():

    logger.info("Inicio da execução...")

    # Obter dicionário de Configuração
    dict_config = config.variaveis_config()
    print(dict_config)

    # Persistência do processamento
    tentativa = 0
    tentativas = 3
    while tentativa < tentativas:
        try:
            # Exemplo
            print("Seu código aqui...")

            funcoes.ObterDadosEntrada(dict_config)

            for indice, coluna in dict_config['dados_excel'].iterrows():
                numero_cte = coluna[3]
                print(numero_cte)

            break

        except Exception as e:

            print(f"Descrição do erro: {e}.")

            tentativa += 1
            print(f"Número da tentativa: {tentativa}")

            if tentativa >= tentativas:
                # Aqui você poderá implementar a lógica para notificar o cliente, por exemplo, envio de e-mail.
                print("Não foi possível realizar a execução do robô. Favor verificar!")

                break


if __name__ == '__main__':
    main()
