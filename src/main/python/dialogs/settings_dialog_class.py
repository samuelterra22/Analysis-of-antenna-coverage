#!/usr/bin/env python

from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QComboBox

from src.main.python.utils.region import get_ufs_initials, get_counties, get_uf_code, get_uf_by_id

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

        self.combo_box_country_state.currentIndexChanged.connect(self.on_combo_box_country_state_changed)

        self.combo_box_country_county.currentIndexChanged.connect(self.on_combo_box_country_county_changed)

    def on_combo_box_country_state_changed(self, index):
        """
        This method is fired when combo box country state is changed
        :param value:
        :return:
        """
        self.combo_box_country_county.clear()
        if index is not 0:
            uf_id = self.combo_box_country_state.itemData(index)
            uf_initial = get_uf_by_id(uf_id)
            self.fill_combo_box_country_county(uf_initial)

    def on_combo_box_country_county_changed(self, index):
        """
        This method is fired when combo box county state is changed
        :param int index: Index of county in combo_box_country_county component
        :return: None
        """
        county_id = self.combo_box_country_county.itemData(index)

    def fill_combo_box_country_county(self, uf):
        """
        This method fill the combo box country county according to uf
        :param uf:
        :return:
        """
        self.combo_box_country_county: QComboBox
        counties = get_counties(uf)
        for county in counties:
            self.combo_box_country_county.addItem(county[0], county[1])

    def fill_combo_box_country_state(self):
        """
        This method fill the combo box country state according with all ufs
        :return:
        """
        self.combo_box_country_state: QComboBox
        ufs = get_ufs_initials()
        self.combo_box_country_state.addItem("Select", -1)

        for uf in ufs:
            self.combo_box_country_state.addItem(uf, get_uf_code(uf))
