import time

from PyQt5 import uic
from PyQt5.QtWidgets import QDialog

import threading

AnatelQDialog = uic.loadUiType("./views/anatel_dialog.ui")[0]


class AnatelDialogClass(QDialog, AnatelQDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)

        self.trigger_fill_progress_bar_thread()

    def trigger_fill_progress_bar_thread(self):
        x = threading.Thread(target=self.fill_progress_bar)
        x.start()

    def fill_progress_bar(self):
        for i in range(101):
            self.progress_bar_anatel.setValue(i)
            self.progress_bar_anatel.setLabel("aasdasd")
            time.sleep(0.1)