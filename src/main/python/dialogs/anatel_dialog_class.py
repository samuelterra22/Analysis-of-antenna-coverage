from PyQt5 import uic
from PyQt5.QtWidgets import QDialog

AnatelQDialog = uic.loadUiType("./views/anatel_dialog.ui")[0]


class AnatelDialogClass(QDialog, AnatelQDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
