#!/usr/bin/env python

from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QComboBox

from src.main.python.utils.region import get_ufs_initials, get_counties

SettingsQDialog = uic.loadUiType("./views/settings_dialog.ui")[0]


class SettingsDialogClass(QDialog, SettingsQDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)

        self.fill_combo_box_country_state()

        self.combo_box_country_state.currentTextChanged.connect(self.on_combo_box_country_state_changed)

        self.combo_box_country_county.currentTextChanged.connect(self.on_combo_box_country_county_changed)

    def on_combo_box_country_state_changed(self, value):
        self.combo_box_country_county.clear()
        if value is not "Select":
            self.fill_combo_box_country_county(value)

    def on_combo_box_country_county_changed(self, value):
        # Do something
        pass

    def fill_combo_box_country_county(self, uf):
        self.combo_box_country_county: QComboBox
        counties = get_counties(uf)
        for county in counties:
            self.combo_box_country_county.addItem(county[0])

    def fill_combo_box_country_state(self):
        self.combo_box_country_state: QComboBox
        ufs = get_ufs_initials()
        self.combo_box_country_state.addItem("Select", -1)

        for uf in ufs:
            self.combo_box_country_state.addItem(uf)
