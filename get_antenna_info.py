import requests

# site: http://sistemas.anatel.gov.br/se/public/view/b/licenciamento.php

url_base = "http://sistemas.anatel.gov.br"
request_url = url_base + "/se/public/view/b/export_licenciamento.php"

parameters = {
    "skip": 0,  # quantidade de linhas a pular
    "filter": 1,  # se filtro aplicado ou nao
    "rpp": 50,  # quantidade por página
    "sort_0": 0,  # sort status
    "sort_1": 0,  # sort entidade
    "sort_2": 0,  # sort fistel
    "sort_3": 0,  # sort num servico
    "sort_4": 0,  # sort ato de rf
    "sort_5": 0,  # sort num estacao
    "sort_6": 0,  # sort endereco
    "sort_7": 0,  # sort sigla estado
    "sort_8": 0,  # sort cod cidade
    "sort_9": 0,  # sort emisao
    "sort_10": 0,  # sort freq inicial
    "sort_11": 0,  # sort frea final
    "sort_12": 0,  # sort azimute
    "sort_13": 0,  # sort tipo estacao
    "sort_14": 0,  # sort tipo antena
    "sort_15": 0,  # sort homologação antena
    "sort_16": 0,  # sort ganho antena
    "sort_17": 0,  # sort frente costa
    "sort_18": 0,  # sort angulo 1/p pot
    "sort_19": 0,  # sort elevação
    "sort_20": 0,  # sort polarização
    "sort_21": 0,  # sort altura antena
    "sort_22": 0,  # sort homologação transmissão
    "sort_23": 0,  # sort potencia transmitida
    "sort_24": 0,  # sort latitude
    "sort_25": 0,  # sort longitude
    "sort_26": 0,  # sort data primeiro licenciamento
    "fc_0": None,  # status
    "fc_1": None,  # entidade
    "fc_2": None,  # fistel
    "fc_3": None,  # num servico
    "fc_4": None,  # ato de rf
    "fc_5": None,  # num estacao
    "fc_6": None,  # endereco
    "fc_7": "MG",  # sigla estado
    "fc_8": 3138203,  # cod cidade
    "fc_9": None,  # emissao
    "fc_10": None,  # freq inicial
    "fc_11": None,  # freq final
    "fc_12": None,  # azimute
    "fc_13": None,  # tipo estacao
    "fc_14": None,  # tipo antena
    "fc_15": None,  # homologação ant
    "fc_16": None,  # ganho antena
    "fc_17": None,  # frente costa
    "fc_18": None,  # angulo 1/2 pot
    "fc_19": None,  # elevacao
    "fc_20": None,  # polarizacao
    "fc_21": None,  # altura antena
    "fc_22": None,  # homologação transmissão
    "fc_23": None,  # potencia transmitida
    "fc_24": None,  # latitude
    "fc_25": None,  # longitude
    "fc_26": None,  # data primeiro licenciamento
}

print("Realizando requisição com parâmetros informados...")
response = requests.post(
    request_url,
    data=parameters,
).json()

if len(response) == 1:
    redirect_url = response["redirectUrl"]
    file_name = redirect_url.split("=")[1] + ".zip"

    try:
        print("Por favor aguarde, realizando download do arquivo '%s'..." % file_name)
        r = requests.get(url_base + redirect_url, allow_redirects=True)
        open(file_name, "wb").write(r.content)
        print("Download realizado com sucesso!")
        print("Arquivo '%s' salvo com sucesso." % file_name)
    except requests.exceptions.RequestException as e:
        print(e)
        print("Ocorreu um erro ao realizar o download...")

else:
    print(response["title"])
    print(response["message"])
