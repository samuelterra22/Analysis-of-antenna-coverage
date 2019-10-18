#!/usr/bin/env python

from PyQt5 import uic
from PyQt5.QtWidgets import QDialog

AboutQDialog = uic.loadUiType("./views/about_dialog.ui")[0]


class AboutDialogClass(QDialog, AboutQDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
