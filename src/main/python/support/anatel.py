from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen
import pandas as pd

# site: https://sistemas.anatel.gov.br/se/public/view/b/licenciamento.php
import requests


def get_anatel_data():
    """
    Get ERB info in Anatel online database
    :return: Pandas object
    """
    url_base = "http://sistemas.anatel.gov.br"
    request_url = url_base + "/se/public/view/b/export_licenciamento.php"

    parameters = {
        "qidx": 0,
        "skip": 0,  # quantidade de linhas a pular
        "filter": 1,  # se filtro aplicado ou nao
        "rpp": 50,  # quantidade por página
        "sort_0": 0,  # status
        "sort_1": 0,  # entidade
        "sort_2": 0,  # fistel
        "sort_3": 0,  # num servico
        "sort_4": 0,  # ato de rf
        "sort_5": 0,  # num estacao
        "sort_6": 0,  # endereco
        "sort_7": 0,  # UF
        "sort_8": 0,  # Municipio
        "sort_9": 0,  # emissao
        "sort_10": 0,  # tecnologia
        "sort_11": 0,  # freq ini
        "sort_12": 0,  # freq final
        "sort_13": 0,  # azimute
        "sort_14": 0,  # tipo estacao
        "sort_15": 0,  # classificacao infra fisica
        "sort_16": 0,  # compatilhamentro infa fisica
        "sort_17": 0,  # disp compartilhamento infra
        "sort_18": 0,  # tipo antena
        "sort_19": 0,  # homologacao antena
        "sort_20": 0,  # ganho antena
        "sort_21": 0,  # frente costa
        "sort_22": 0,  # angulo meia potencia
        "sort_23": 0,  # elevacao
        "sort_24": 0,  # polarizacao
        "sort_25": 0,  # altura antena
        "sort_26": 0,  # homologacao transmissao
        "sort_27": 0,  # potencia transmissao
        "sort_28": 0,  # latitude
        "sort_29": 0,  # longitude
        "sort_30": 0,  # data primeiro licenciamento
        "fc_0": None,  # status
        "fc_1": None,  # entidade
        "fc_2": None,  # fistel
        "fc_3": None,  # num servico
        "fc_4": None,  # ato de rf
        "fc_5": None,  # num estacao
        "fc_6": None,  # endereco
        "fc_7": "MG",  # UF
        "fc_8": 3138203,  # Municipio
        "fc_9": None,  # emissao
        "fc_10": None,  # tecnologia
        "fc_11": None,  # freq ini
        "fc_12": None,  # freq final
        "fc_13": None,  # azimute
        "fc_14": None,  # tipo estacao
        "fc_15": None,  # classificacao infra fisica
        "fc_16": None,  # compatilhamentro infa fisica
        "fc_17": None,  # dissicao compartilhamento infra
        "fc_18": None,  # tipo antena
        "fc_19": None,  # homologacao antena
        "fc_20": None,  # ganho antena
        "fc_21": None,  # frente costa
        "fc_22": None,  # angulo meia potencia
        "fc_23": None,  # elevacao
        "fc_24": None,  # polarizacao
        "fc_25": None,  # altura antena
        "fc_26": None,  # homologacao transmissao
        "fc_27": None,  # potencia transmissao
        "fc_28": None,  # latitude
        "fc_29": None,  # longitude
        "fc_30": None,  # data primeiro licenciamento
        "wfid": "licencas",
        "view": 0
    }

    print("Performing request with informed parameters ...")
    response = requests.post(
        request_url,
        data=parameters,
    ).json()

    if len(response) == 1:
        redirect_url = response["redirectUrl"]
        file_name = redirect_url.split("=")[1] + ".zip"

        try:
            print("Please wait, downloading the file '%s'..." % file_name)

            with urlopen(url_base + redirect_url) as f:
                with BytesIO(f.read()) as b, ZipFile(b) as myzipfile:
                    foofile = myzipfile.open(myzipfile.namelist()[0])
                    df = pd.read_csv(foofile, encoding="ISO-8859-1")

            print("Download successful!")
            return df
        except requests.exceptions.RequestException as e:
            print(e)
            print("An error occurred while downloading ...")

    else:
        print(response["title"])
        print(response["message"])
