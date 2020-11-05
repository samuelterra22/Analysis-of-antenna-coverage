#!/usr/bin/env python

import time

from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QProgressBar, QTableWidgetItem, QTableWidget

import threading

AnatelQDialog = uic.loadUiType("./views/anatel_dialog.ui")[0]


class AnatelDialogClass(QDialog, AnatelQDialog):
    """
    This class load the anatel dialog pyqt component
    """

    def __init__(self, parent=None):
        """
        Anatel dialog class constructor
        :param parent:
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)

        self.combo_box_state.addItems(["Java", "C#", "Python"])
        self.combo_box_state.currentIndexChanged.connect(self.on_combo_box_state_changed)

        self.combo_box_contry.addItems(["Java", "C#", "Python"])
        self.combo_box_contry.currentIndexChanged.connect(self.on_combo_box_contry_changed)

        self.fill_anatel_table_rows()

        self.update_database_button.clicked.disconnect()
        self.update_database_button.clicked.connect(self.on_update_database_button_clicked)

    @pyqtSlot(name="on_combo_box_state_changed")
    def on_combo_box_state_changed(self, i):
        print("Items in the list 'combo_box_state' are :")

        for count in range(self.combo_box_state.count()):
            print(self.combo_box_state.itemText(count))
        print("Current index", i, "selection changed ", self.combo_box_state.currentText())

    @pyqtSlot(name="on_combo_box_contry_changed")
    def on_combo_box_contry_changed(self, i):
        print("Items in the list 'combo_box_contry' are :")

        for count in range(self.combo_box_contry.count()):
            print(self.combo_box_contry.itemText(count))
        print("Current index", i, "selection changed ", self.combo_box_contry.currentText())

    def disable_ui_components(self):
        self.anatel_table.setDisabled(True)
        self.update_database_button.setDisabled(True)
        self.combo_box_state.setDisabled(True)
        self.combo_box_contry.setDisabled(True)

    def enable_ui_components(self):
        self.anatel_table.setDisabled(False)
        self.update_database_button.setDisabled(False)
        self.combo_box_state.setDisabled(False)
        self.combo_box_contry.setDisabled(False)

    @pyqtSlot(name="on_update_database_button_clicked")
    def on_update_database_button_clicked(self):
        """
        This method is called when calculate menu button is clicked
        :return: None
        """

        x = threading.Thread(target=self.fill_progress_bar)
        x.start()

    def fill_progress_bar(self):
        """
        This method fill the progressbar fired for thread
        :return:
        """
        self.progress_bar_anatel: QProgressBar

        self.disable_ui_components()

        # delete all register from table
        self.anatel_table.setRowCount(0)

        for i in range(101):
            self.progress_bar_anatel.setValue(i)
            time.sleep(0.07)

        self.anatel_table.setDisabled(False)
        self.update_database_button.setDisabled(False)

        self.fill_anatel_table_rows()

    def fill_anatel_table_rows(self):
        """
        This method add Anatel antenna info rows in the table
        :return:
        """

        self.anatel_table: QTableWidget
        # self.anatel_table.removeRow()

        # Remove first row (is empty)
        self.anatel_table.removeRow(0)
        row_position = self.anatel_table.rowCount()
        qtd_columns = self.anatel_table.columnCount()

        configs = [
            (
                "123",
                "STATUS",
                "ENTIDADE",
                "FISTEL",
                "NUM SERVICO",
                "ATO DE RF",
                "NUM ESTACAO",
                "ENDERECO",
                "UF",
                "MUNICIPIO",
                "EMISSAO",
                "FREQ INICIAL",
                "FREQ FINAL",
                "AZIMUTE",
                "TIPO ESTACAO",
                "TIPO ANTENA",
                "HOMOLOGACAO ANTENA",
                "GANHO ANTENA",
                "FRENTE COSTA",
                "ANGULO 1/2 POT",
                "ELEVACAO",
                "POLARIZACAO",
                "ALTURA ANTENA",
                "HOMOLOGACAO TRANSMISSAO",
                "LATITUDE",
                "LONGITUDE",
                "DATA PRIMEIRO LICENCIAMENTO",
            )
        ]

        for row_count, config in enumerate(configs):
            row = row_position + row_count
            self.anatel_table.insertRow(row)

            for col_count, config_item in enumerate(config):
                self.anatel_table.setItem(row, col_count, QTableWidgetItem(config_item))
