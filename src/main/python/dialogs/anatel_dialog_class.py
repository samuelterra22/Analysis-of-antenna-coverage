#!/usr/bin/env python

import time

from PyQt5 import uic
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

        self.trigger_fill_progress_bar_thread()

        self.add_rows()

    def trigger_fill_progress_bar_thread(self):
        """
        This method run the thread to fill progressbar
        :return:
        """
        x = threading.Thread(target=self.fill_progress_bar)
        x.start()

    def fill_progress_bar(self):
        """
        This method fill the progressbar fired for thread
        :return:
        """
        self.progress_bar_anatel: QProgressBar

        for i in range(101):
            self.progress_bar_anatel.setValue(i)
            time.sleep(0.1)

    def add_rows(self):
        """
        This method add anatel antenna info rows in the table
        :return:
        """

        self.anatel_table: QTableWidget

        # Remove first row (is empty)
        self.anatel_table.removeRow(0)
        row_position = self.anatel_table.rowCount()
        qtd_columns = self.anatel_table.columnCount()

        for i in range(16):
            row = row_position+i
            self.anatel_table.insertRow(row)

            self.anatel_table.setItem(row, 0, QTableWidgetItem(str(i)))
            self.anatel_table.setItem(row, 1, QTableWidgetItem("LIC-LIC-01"))
            self.anatel_table.setItem(row, 2, QTableWidgetItem("TELEFÔNICA BRASIL S.A."))
            self.anatel_table.setItem(row, 3, QTableWidgetItem("50409146285"))
            self.anatel_table.setItem(row, 4, QTableWidgetItem("010"))
            self.anatel_table.setItem(row, 5, QTableWidgetItem("59072012"))
            self.anatel_table.setItem(row, 6, QTableWidgetItem("687462363"))
            self.anatel_table.setItem(row, 7, QTableWidgetItem("UFLA - PRÓXIMO AO PRÉDIO DE CIENCIAS DA SOLO,S/N,CAMPUS UFLA"))
            self.anatel_table.setItem(row, 8, QTableWidgetItem("MG"))
            self.anatel_table.setItem(row, 9, QTableWidgetItem("Lavras"))