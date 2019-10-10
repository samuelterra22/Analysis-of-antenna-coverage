from PyQt5 import uic
from PyQt5.QtWidgets import QDialog

HelpQDialog = uic.loadUiType("./views/help_dialog.ui")[0]


class HelpDialogClass(QDialog, HelpQDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
