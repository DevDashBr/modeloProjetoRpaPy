def variaveis_config():

    dict_vars = {}

    # Diretório Chrome Driver
    chrome_driver_path = "C:\Chrome\chromedriver.exe"
    dict_vars['chrome_driver_path'] = chrome_driver_path

    # Web Site
    url_cliente = 'https://url_cliente.com.br/'
    dict_vars['url_cliente'] = url_cliente

    # Credenciais de acesso
    usuario = 'exemplo@triasoftware.com.br'
    dict_vars['usuario'] = usuario
    senha = 'exemplo@1234'
    dict_vars['senha'] = senha

    # Arquivo Base de Extrada (Excel)
    caminho_arquivo_excel = r"C:\RpaDev"
    dict_vars['caminho_arquivo_excel'] = caminho_arquivo_excel

    # Credenciais de e-mail
    de_email = 'exemplo@triasoftware.com.br'
    dict_vars['de_email'] = de_email
    senha_email = 'exemplo@1234'
    dict_vars['senha_email'] = senha_email

    return dict_vars
