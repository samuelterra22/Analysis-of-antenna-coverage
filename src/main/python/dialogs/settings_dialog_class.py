#!/usr/bin/env python

from PyQt5 import uic
from PyQt5.QtWidgets import QDialog

SettingsQDialog = uic.loadUiType("./views/settings_dialog.ui")[0]


class SettingsDialogClass(QDialog, SettingsQDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
