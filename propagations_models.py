import math
from math import log10
from numba import jit


@jit
def log_distance_model(d, gamma=3, d0=1, pr_d0=-60, pt=-17):
    """
    Modelo logaritmo de perda baseado em resultados experimentais. Independe da frequência do sinal transmitido
    e do ganho das antenas transmissora e receptora.
    Livro Comunicações em Fio - Pricipios e Práticas - Rappaport (páginas 91-92).

    :param pr_d0:
    :param pt: Potência transmitida
    :param d0: Distância do ponto de referência d0.
    :param d: Distância que desejo calcular a perda do sinal.
    :param gamma: Valor da constante de propagação que difere para cada tipo de ambiente.
    :return: Retorna um float representando a perda do sinal entre a distância d0 e d.
    """
    return (pr_d0 - 10 * gamma * log10(d / d0)) - pt


@jit
def log_distance_v2_model(d, gamma=3, d0=10, pr_d0=-69, pt=-20):
    return (pr_d0 - 10 * gamma * log10(d / d0)) - pt


@jit
def tree_par_log_model(x):
    return -17.74321 - 15.11596 * math.log(x + 2.1642)


@jit
def two_par_logistic_model(pt_dbm, x):
    # https://en.wikipedia.org/wiki/Logistic_distribution#Related_distributions
    return pt_dbm - (-15.11596 * math.log10(x * 2.1642))


@jit
def four_par_log_model(pt_dbm, x):
    a = 79.500
    b = -38
    c = -100.000
    d = 0.0
    e = 0.005

    # https://en.wikipedia.org/wiki/Shifted_log-logistic_distribution
    return pt_dbm - (d + (a - d) / (pow((1 + pow((x / c), b)), e)))


@jit
def five_par_log_model(pt_dbm, x):
    a = 84.0
    b = -48
    c = -121.0
    d = -5.0
    e = 0.005
    # https://en.wikipedia.org/wiki/Shifted_log-logistic_distribution
    return pt_dbm - (d + (a - d) / (pow((1 + pow((x / c), b)), e)))


def cost231_path_loss(f, tx_h, rx_h, d, mode):
    """
    COST231 extension to HATA model
    http://morse.colorado.edu/~tlen5510/text/classwebch3.html
    :param f:       Carrier Frequency (1500 to 2000MHz)
    :param tx_h:    Base station height 30 to 200m
    :param rx_h:    Mobile station height 1 to 10m
    :param d:       Distance between Tx and Rx, 1-20km
    :param mode:    1 = URBAN, 2 = SUBURBAN, 3 = OPEN
    :return:        Path loss
    """
    c = 3  # 3dB for Urban
    lrx_h = math.log10(11.75 * rx_h)
    c_h = 3.2 * (lrx_h * lrx_h) - 4.97  # Large city(conservative)
    c0 = 69.55
    cf = 26.16
    if f > 1500:
        c0 = 46.3
        cf = 33.9

    if mode == 2:
        c = 0  # Medium city (average)
        lrx_h = math.log10(1.54 * rx_h)
        c_h = 8.29 * (lrx_h * lrx_h) - 1.1

    if mode == 3:
        c = -3  # Small city (Optimistic)
        c_h = (1.1 * math.log10(f) - 0.7) * rx_h - (1.56 * math.log10(f)) + 0.8

    log_f = math.log10(f)

    return c0 + (cf * log_f) - (13.82 * math.log10(tx_h)) - c_h + (44.9 - 6.55 * math.log10(tx_h)) * math.log10(d) + c


def ecc33_path_loss():
    pass


def egli_path_loss():
    pass


def ericsson_path_loss():
    pass


def fspl_path_loss():
    # https://github.com/Cloud-RF/Signal-Server/blob/master/models/fspl.cc
    pass


def hata_path_loss():
    pass


def sui_path_loss():
    pass
