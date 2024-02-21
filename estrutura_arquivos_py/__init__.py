import sys

print(f'Versão do python: {sys.version_info.major}')

# Verificar se as bibliotecas utilizadas pelo projeto estão instaladas
try:
    # Exemplo
    import logging
    print("A biblioteca logging está instalada!")
except Exception as e:
    print("A biblioteca logging não está instalada. Favor verificar!")
    raise Exception(f"Descrição do erro: {e}.")
