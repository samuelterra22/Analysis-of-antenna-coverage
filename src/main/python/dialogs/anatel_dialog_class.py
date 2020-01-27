#!/usr/bin/env python

import time

from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QProgressBar

import threading

AnatelQDialog = uic.loadUiType("./views/anatel_dialog.ui")[0]


class AnatelDialogClass(QDialog, AnatelQDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)

        self.trigger_fill_progress_bar_thread()

        self.add_rows()

    def trigger_fill_progress_bar_thread(self):
        x = threading.Thread(target=self.fill_progress_bar)
        x.start()

    def fill_progress_bar(self):
        self.progress_bar_anatel: QProgressBar

        for i in range(101):
            self.progress_bar_anatel.setValue(i)
            time.sleep(0.1)

    def add_rows(self):
        # Remove first row (is empty)
        self.anatel_table.removeRow(0)
        # row_position = self.anatel_table.rowCount()
        # self.anatel_table.insertRow(row_position)
        # self.anatel_table.setItem(row_position, 0, QTableWidgetItem("vaca"))
