import requests
from requests import RequestException

import src.main.python.utils.constants as constants

uf_list = {
    "RO": 11,
    "RR": 14,
    "AP": 16,
    "TO": 17,
    "PI": 22,
    "RN": 24,
    "PE": 26,
    "BA": 29,
    "RJ": 33,
    "SC": 42,
    "MT": 51,
    "AL": 27,
    "MG": 31,
    "PR": 41,
    "MS": 50,
    "DF": 53,
    "AC": 12,
    "AM": 13,
    "PA": 15,
    "MA": 21,
    "CE": 23,
    "PB": 25,
    "SE": 28,
    "ES": 32,
    "SP": 35,
    "RS": 43,
    "GO": 52,
}


def get_ufs_initials():
    return sorted(uf_list.keys())


def get_uf_code(uf):
    return uf_list.get(uf)


def get_counties(uf):
    url_base = (
        "http://sistemas.anatel.gov.br/se/eApp/forms/b/jf_getMunicipios.php?CodUF="
    )
    uf_code = get_uf_code(uf)

    if uf_code:
        url = url_base + str(uf_code)
        try:
            return requests.get(url=url).json()
        except RequestException as e:
            return constants.REQUEST_ERROR
    else:
        return constants.INVALID_UF
