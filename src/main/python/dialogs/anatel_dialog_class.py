#!/usr/bin/env python

from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QProgressBar, QTableWidgetItem, QTableWidget, QLabel, QComboBox

from src.main.python.controllers.settings_controller import SettingsController
from src.main.python.support.anatel import get_anatel_data
from src.main.python.support.constants import CURRENT_UF_ID
from src.main.python.support.region import get_ufs_initials, get_uf_by_id, get_counties

AnatelQDialog = uic.loadUiType("./views/anatel_dialog.ui")[0]


class AnatelDialogClass(QDialog, AnatelQDialog):
    """
    This class load the anatel dialog pyqt component
    """

    def __init__(self, parent=None):
        """
        Anatel dialog class constructor
        :param parent:
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)

        self.__controller = SettingsController()

        self.init_ui_components()

    def init_ui_components(self):
        self.combo_box_state.addItems(get_ufs_initials())
        self.combo_box_state.currentIndexChanged.connect(self.on_combo_box_state_changed)

        self.combo_box_contry.addItems(["Select a UF first"])
        self.combo_box_contry.currentIndexChanged.connect(self.on_combo_box_contry_changed)

        self.update_database_button.clicked.disconnect()
        self.update_database_button.clicked.connect(self.on_update_database_button_clicked)

    @pyqtSlot(name="on_combo_box_state_changed")
    def on_combo_box_state_changed(self):
        # reset combo box
        self.combo_box_contry.clear()
        self.combo_box_contry.addItems(["Select a UF first"])

        print("Items in the list 'combo_box_state' are :")
        index = self.combo_box_state.currentIndex()
        text = self.combo_box_state.currentText()

        if index != 0:
            uf_id = self.combo_box_state.itemData(index)
            self.__create_or_update_uf(uf_id)
            uf_initial = get_uf_by_id(uf_id)
            self.fill_combo_box_country(uf_initial)

    def fill_combo_box_country(self, uf):
        """
        This method fill the combo box country county according to uf
        :param uf:
        :return:
        """
        self.combo_box_contry: QComboBox
        counties = get_counties(uf)
        for county in counties:
            self.combo_box_contry.addItem(county[0], county[1])

    def __create_or_update_uf(self, uf_id):
        data = {
            'option': CURRENT_UF_ID,
            'value': uf_id
        }

        # The setting no exists, then store
        if not self.__controller.get(CURRENT_UF_ID):
            result = self.__controller.store(data)
            print('Result from store: ' + str(result))
        else:
            # The setting exists, then update
            result = self.__controller.update(data, None)
            print('Result from update: ' + str(result))

    @pyqtSlot(name="on_combo_box_contry_changed")
    def on_combo_box_contry_changed(self):
        print("Items in the list 'combo_box_contry' are :")
        index = self.combo_box_contry.currentIndex()
        text = self.combo_box_contry.currentText()

        for count in range(self.combo_box_contry.count()):
            print(self.combo_box_contry.itemText(count))
        print("Current index", index, "selection changed ", text)

    def disable_ui_components(self):
        self.anatel_table.setDisabled(True)
        self.update_database_button.setDisabled(True)
        self.combo_box_state.setDisabled(True)
        self.combo_box_contry.setDisabled(True)

    def enable_ui_components(self):
        self.anatel_table.setDisabled(False)
        self.update_database_button.setDisabled(False)
        self.combo_box_state.setDisabled(False)
        self.combo_box_contry.setDisabled(False)

    @pyqtSlot(name="on_update_database_button_clicked")
    def on_update_database_button_clicked(self):
        """
        This method add Anatel antenna info rows in the table
        :return:
        """
        self.label_last_update: QLabel
        self.progress_bar_anatel: QProgressBar

        self.label_last_update.setText("Searching for information in the online database...")

        # delete all register from table
        self.anatel_table.setRowCount(0)

        self.anatel_table: QTableWidget

        self.anatel_table.removeRow(0)
        row_position = self.anatel_table.rowCount()

        erb_config = get_anatel_data()

        self.label_last_update.setText("Saving information offline")

        total = erb_config.shape[0]
        processed = 0

        for i, row in erb_config.iterrows():
            table_row_count = row_position + i
            self.anatel_table.insertRow(table_row_count)

            self.anatel_table.setItem(table_row_count, 0, QTableWidgetItem(str(table_row_count)))
            table_column_count = 1
            for column, column_data in row.iteritems():
                self.anatel_table.setItem(table_row_count, table_column_count, QTableWidgetItem(str(column_data)))
                table_column_count = table_column_count + 1

            processed = processed + 1
            self.progress_bar_anatel.setValue(round(((processed/total) * 100), 2))

        self.anatel_table.setDisabled(False)
        self.update_database_button.setDisabled(False)

        self.label_last_update.setText("Updated local database!")
