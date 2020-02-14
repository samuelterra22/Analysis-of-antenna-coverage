#!/usr/bin/env python

import time

from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QProgressBar

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
        # Remove first row (is empty)
        self.anatel_table.removeRow(0)
        # row_position = self.anatel_table.rowCount()
        # self.anatel_table.insertRow(row_position)
        # self.anatel_table.setItem(row_position, 0, QTableWidgetItem("vaca"))
