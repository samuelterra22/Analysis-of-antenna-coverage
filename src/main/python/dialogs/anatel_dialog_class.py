#!/usr/bin/env python
import time

from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QProgressBar, QTableWidgetItem, QTableWidget, QLabel

from support.anatel import get_anatel_data

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

        self.init_ui_components()

    def init_ui_components(self):
        self.combo_box_state.addItems(["Java", "C#", "Python"])
        self.combo_box_state.currentIndexChanged.connect(self.on_combo_box_state_changed)

        self.combo_box_contry.addItems(["Java", "C#", "Python"])
        self.combo_box_contry.currentIndexChanged.connect(self.on_combo_box_contry_changed)

        self.update_database_button.clicked.disconnect()
        self.update_database_button.clicked.connect(self.on_update_database_button_clicked)

    @pyqtSlot(name="on_combo_box_state_changed")
    def on_combo_box_state_changed(self, i):
        print("Items in the list 'combo_box_state' are :")

        for count in range(self.combo_box_state.count()):
            print(self.combo_box_state.itemText(count))
        print("Current index", i, "selection changed ", self.combo_box_state.currentText())

    @pyqtSlot(name="on_combo_box_contry_changed")
    def on_combo_box_contry_changed(self, i):
        print("Items in the list 'combo_box_contry' are :")

        for count in range(self.combo_box_contry.count()):
            print(self.combo_box_contry.itemText(count))
        print("Current index", i, "selection changed ", self.combo_box_contry.currentText())

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
        # for i in range(101):
        #     self.progress_bar_anatel.setValue(i)
        #     time.sleep(0.07)

        # self.disable_ui_components()

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
