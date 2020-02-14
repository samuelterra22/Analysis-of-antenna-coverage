#!/usr/bin/env python

from PyQt5 import uic
from PyQt5.QtWidgets import QDialog

AboutQDialog = uic.loadUiType("./views/about_dialog.ui")[0]


class AboutDialogClass(QDialog, AboutQDialog):
    """
    This class load the about dialog pyqt component
    """
    def __init__(self, parent=None):
        """
        About dialog class constructor
        :param parent:
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
