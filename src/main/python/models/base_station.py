#!/usr/bin/env python
import datetime

from src.main.python.models.base_model import BaseModel
from peewee import *


class BaseStation(BaseModel):
    """
    This class is the base station model for storage data in database
    """
    status = CharField()
    entidade = CharField()
    num_fistel = CharField()
    num_servico = CharField()
    num_ato_de_rf = CharField()
    num_estacao = CharField()
    endereco = CharField()
    uf = CharField()
    municipio = CharField()
    emissao = CharField()
    tecnologia = CharField()
    frequencia_inicial = CharField()
    frequencia_final = CharField()
    azimute = CharField()
    tipo_estacao = CharField()
    classificacao_infra_fisica = CharField()
    compartilhamento_infra_fisica = CharField()
    disp_compartilhamento_infra = CharField()
    tipo_antena = CharField()
    homologacao_antena = CharField()
    ganho_antena = CharField()
    ganho_frente_costa = CharField()
    angulo_meia_potencia = CharField()
    elevacao = CharField()
    polarizacao = CharField()
    altura = CharField()
    homologacao_transmissao = CharField()
    potencia_transmissao = CharField()
    latitude = CharField()
    longitude = CharField()
    data_primeiro_licenciamento = CharField()

    created_at = DateTimeField(default=datetime.datetime.now)
