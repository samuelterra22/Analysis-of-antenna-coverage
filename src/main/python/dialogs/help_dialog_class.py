#!/usr/bin/env python

from PyQt5 import uic
from PyQt5.QtWidgets import QDialog

HelpQDialog = uic.loadUiType("./views/help_dialog.ui")[0]


class HelpDialogClass(QDialog, HelpQDialog):
    """
    This class load the help dialog pyqt component
    """
    def __init__(self, parent=None):
        """
        Help dialog class constructor
        :param parent:
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
