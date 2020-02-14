#!/usr/bin/env python

from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QComboBox

from src.main.python.utils.region import get_ufs_initials, get_counties

SettingsQDialog = uic.loadUiType("./views/settings_dialog.ui")[0]


class SettingsDialogClass(QDialog, SettingsQDialog):
    """
    This class load the settings dialog pyqt component
    """
    def __init__(self, parent=None):
        """
        Settings dialog class constructor
        :param parent:
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)

        self.fill_combo_box_country_state()

        self.combo_box_country_state.currentTextChanged.connect(self.on_combo_box_country_state_changed)

        self.combo_box_country_county.currentTextChanged.connect(self.on_combo_box_country_county_changed)

    def on_combo_box_country_state_changed(self, value):
        """
        This method is fired when combo box country state is changed
        :param value:
        :return:
        """
        self.combo_box_country_county.clear()
        if value is not "Select":
            self.fill_combo_box_country_county(value)

    def on_combo_box_country_county_changed(self, value):
        """
        This method is fired when combo box county state is changed
        :param value:
        :return:
        """
        # Do something
        pass

    def fill_combo_box_country_county(self, uf):
        """
        This method fill the combo box country county according to uf
        :param uf:
        :return:
        """
        self.combo_box_country_county: QComboBox
        counties = get_counties(uf)
        for county in counties:
            self.combo_box_country_county.addItem(county[0])

    def fill_combo_box_country_state(self):
        """
        This method fill the combo box country state according with all ufs
        :return:
        """
        self.combo_box_country_state: QComboBox
        ufs = get_ufs_initials()
        self.combo_box_country_state.addItem("Select", -1)

        for uf in ufs:
            self.combo_box_country_state.addItem(uf)
