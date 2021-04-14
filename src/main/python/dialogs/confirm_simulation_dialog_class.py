import datetime

from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QLabel

from base import context


class ConfirmSimulationDialogClass(QDialog):
    """
    This class load the help dialog pyqt component
    """

    def __init__(self, data: dict, parent=None):
        """
        Confirm Simulation dialog class constructor
        :param parent:
        """
        QDialog.__init__(self, parent)
        self.ui = uic.loadUi(context.get_resource("confirm_simulation_dialog.ui"), self)

        self.val = None
        simulation = data['simulation']
        print('propagation_model=', simulation['propagation_model'])
        print('environment=', simulation['environment'])

        transmitter = data['transmitter']
        print('entidade=', transmitter['entidade'])
        print('uf_municipio=', transmitter['uf_municipio'])
        print('endereco=', transmitter['endereco'])
        print('frequencia=', transmitter['frequencia'])
        print('ganho=', transmitter['ganho'])
        print('elevacao=', transmitter['elevacao'])
        print('polarizacao=', transmitter['polarizacao'])
        print('altura=', transmitter['altura'])
        print('latitude=', transmitter['latitude'])
        print('longitude=', transmitter['longitude'])

        receptor = data['receptor']
        print('altura=', receptor['altura'])
        print('ganho=', receptor['ganho'])
        print('sensibilidade=', receptor['sensibilidade'])

        heuristic = data['heuristic']
        print('temperatura_inicial=', heuristic['temperatura_inicial'])
        print('numero_maximo_iteracoes=', heuristic['numero_maximo_iteracoes'])
        print('numero_maximo_pertubacoes_por_iteracao=', heuristic['numero_maximo_pertubacoes_por_iteracao'])
        print('numero_maximo_sucessos_por_iteracao=', heuristic['numero_maximo_sucessos_por_iteracao'])
        print('alpha=', heuristic['alpha'])

        # Simulation details
        self.label_modelo_propagacao_value: QLabel
        self.label_ambiente_value: QLabel
        self.label_radio_maximo_value: QLabel

        # Transmissor
        self.label_entidade_value: QLabel
        self.label_uf_municipio_value: QLabel
        self.label_endereco_value: QLabel
        self.label_frequencia_value: QLabel
        self.label_ganho: QLabel
        self.label_elevacao_value: QLabel
        self.label_polarizacao_value: QLabel
        self.label_altura_value: QLabel
        self.label_latitude_value: QLabel
        self.label_longitude_value: QLabel

        # Meta-heuristic
        self.label_temperatura_inicial_value: QLabel
        self.label_num_maximo_iteracoes_value: QLabel
        self.label_num_maximo_pertubacoes_iteracao_value: QLabel
        self.label_num_maximo_sucessos_iteracao_value: QLabel
        self.label_alpha_value: QLabel

        # Receptor details
        self.label_bs_altura_value: QLabel
        self.label_bs_ganho_value: QLabel
        self.label_bs_sensibilidade_value: QLabel


        # ToDo: do this
        self.label_elevacao_value.setText("asdasd")

        # Confirm button
        self.btn_confirmar_simulacao.clicked.disconnect()
        self.btn_confirmar_simulacao.clicked.connect(self.on_btn_confirmar_simulacao_clicked)

        # Cancel button
        self.btn_cancelar_simulacao.clicked.disconnect()
        self.btn_cancelar_simulacao.clicked.connect(self.on_btn_cancelar_simulacao_clicked)

    def fill_data(self, data):
        pass
        # label_modelo_propagacao_value
        # label_ambiente_value
        # label_radio_maximo_value

        # label_entidade_value
        # label_uf_municipio_value
        # label_endereco_value
        # label_frequencia_value
        # label_ganho_value
        # label_elevacao_value
        # label_polarizacao_value
        # label_altura_value
        # label_latitude_value
        # label_longitude_value

        # label_bs_altura_value
        # label_bs_ganho_value
        # label_bs_sensibilidade_value

    @pyqtSlot(name="on_btn_confirmar_simulacao_clicked")
    def on_btn_confirmar_simulacao_clicked(self):
        """
        This method is called when confirm simulation button is clicked
        :return: None
        """
        print("Confirmation button!")
        self.val = 6666
        self.accept()

    @pyqtSlot(name="on_btn_cancelar_simulacao_clicked")
    def on_btn_cancelar_simulacao_clicked(self):
        """
        This method is called when cancel simulation button is clicked
        :return: None
        """
        print("Cancel button!")
        self.val = -123
        self.reject()
