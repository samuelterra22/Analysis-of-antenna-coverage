#!/usr/bin/env python

from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QComboBox

from src.main.python.utils.region import get_ufs_initials, get_counties

SettingsQDialog = uic.loadUiType("./views/settings_dialog.ui")[0]


class SettingsDialogClass(QDialog, SettingsQDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)

        self.fill_combo_box_regiao_estado()

        self.combo_box_regiao_estado.currentTextChanged.connect(self.on_combo_box_regiao_estado_changed)

        # combo_box_regiao_municipio

    def on_combo_box_regiao_estado_changed(self, value):
        if value is not "Select":
            self.fill_combo_box_regiao_municipio(value)

    def fill_combo_box_regiao_municipio(self, uf):
        self.combo_box_regiao_municipio: QComboBox
        counties = get_counties(uf)
        for county in counties:
            self.combo_box_regiao_municipio.addItem(county[0])

    def fill_combo_box_regiao_estado(self):
        self.combo_box_regiao_estado: QComboBox
        ufs = get_ufs_initials()
        self.combo_box_regiao_estado.addItem("Select", -1)

        for uf in ufs:
            self.combo_box_regiao_estado.addItem(uf)
