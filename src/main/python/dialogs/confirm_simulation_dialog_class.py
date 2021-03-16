#!/usr/bin/env python

from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

ConfirmSimulationQDialog = uic.loadUiType("./views/confirm_simulation_dialog.ui")[0]


class ConfirmSimulationDialogClass(QDialog, ConfirmSimulationQDialog):
    """
    This class load the help dialog pyqt component
    """

    def __init__(self, data, parent=None):
        """
        Confirm Simulation dialog class constructor
        :param parent:
        """
        QDialog.__init__(self, parent)
        self.val = None
        self.setupUi(self)
        print(data)

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
