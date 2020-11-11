#!/usr/bin/env python

from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QProgressBar, QTableWidgetItem, QTableWidget, QLabel, QComboBox

from src.main.python.controllers.base_station_controller import BaseStationController
from src.main.python.controllers.settings_controller import SettingsController
from src.main.python.support.anatel import get_anatel_data
from src.main.python.support.constants import CURRENT_UF_ID
from src.main.python.support.region import get_ufs_initials, get_uf_by_id, get_counties, get_uf_code
from src.main.python.support.constants import CURRENT_COUNTY_ID

AnatelQDialog = uic.loadUiType("./views/anatel_dialog.ui")[0]


class AnatelDialogClass(QDialog, AnatelQDialog):
    """
    This class load the Anatel dialog pyqt component
    """

    def __init__(self, parent=None):
        """
        Anatel dialog class constructor
        :param parent:
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)

        self.__settings_controller = SettingsController()
        self.__base_station_controller = BaseStationController()

        self.init_ui_components()

    def get_current_uf_id(self):
        data = {
            'option': CURRENT_UF_ID,
        }
        res = self.__settings_controller.get(data)
        if res is not None:
            return res.value
        else:
            return -1

    def get_current_state_id(self):
        data = {
            'option': CURRENT_COUNTY_ID,
        }
        res = self.__settings_controller.get(data)
        if res is not None:
            return res.value
        else:
            return -1

    def init_ui_components(self):
        current_uf_id = self.get_current_uf_id()
        current_contry_id = self.get_current_state_id()
        print(current_uf_id)
        print(current_contry_id)

        self.fill_combo_box_state()

        current_index_uf = self.get_current_state_index(current_uf_id)
        self.combo_box_state.setCurrentIndex(current_index_uf)

        if current_index_uf != -1:
            self.fill_combo_box_country(self.combo_box_state.itemText(current_index_uf))
        else:
            self.combo_box_contry.addItems(["Select a UF first"])

        current_contry_uf = self.get_current_contry_index(current_contry_id)
        self.combo_box_contry.setCurrentIndex(current_contry_uf)

        self.combo_box_state.currentIndexChanged.connect(self.on_combo_box_state_changed)
        self.combo_box_contry.currentIndexChanged.connect(self.on_combo_box_contry_changed)

        self.update_database_button.clicked.disconnect()
        self.update_database_button.clicked.connect(self.on_update_database_button_clicked)

    def get_current_state_index(self, current_uf_id):
        self.combo_box_state: QComboBox
        if current_uf_id != -1:
            for count in range(self.combo_box_state.count()):
                if str(self.combo_box_state.itemData(count)) == current_uf_id:
                    return count
        return 0

    def get_current_contry_index(self, current_contry_id):
        self.combo_box_contry: QComboBox
        if current_contry_id != -1:
            for count in range(self.combo_box_contry.count()):
                if str(self.combo_box_contry.itemData(count)) == current_contry_id:
                    return count
        return 0

    @pyqtSlot(name="on_combo_box_state_changed")
    def on_combo_box_state_changed(self):
        self.combo_box_contry.clear()

        index = self.combo_box_state.currentIndex()

        if index != 0 and index != -1 and index is not None:
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

        self.combo_box_contry.setCurrentIndex(0)

    def __create_or_update_uf(self, uf_id):
        data = {
            'option': CURRENT_UF_ID,
            'value': uf_id
        }

        # The setting no exists, then store
        if not self.__settings_controller.get(data):
            result = self.__settings_controller.store(data)
            print('Result from store uf id: ' + str(result))
        else:
            # The setting exists, then update
            result = self.__settings_controller.update(data, None)
            print('Result from update uf id: ' + str(result))

    def __create_or_update_state(self, state_id):
        data = {
            'option': CURRENT_COUNTY_ID,
            'value': state_id
        }

        # The setting no exists, then store
        if not self.__settings_controller.get(data):
            result = self.__settings_controller.store(data)
            print('Result from store state id: ' + str(result))
        else:
            # The setting exists, then update
            result = self.__settings_controller.update(data, None)
            print('Result from update state id: ' + str(result))

    @pyqtSlot(name="on_combo_box_contry_changed")
    def on_combo_box_contry_changed(self):
        index = self.combo_box_contry.currentIndex()
        text = self.combo_box_contry.currentText()

        uf_id = self.combo_box_contry.itemData(index)
        self.__create_or_update_state(uf_id)

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

    def fill_combo_box_state(self):
        """
        This method fill the combo box country state according with all ufs
        :return:
        """
        self.combo_box_state: QComboBox
        ufs = get_ufs_initials()

        for uf in ufs:
            self.combo_box_state.addItem(uf, get_uf_code(uf))

    def fill_erb_table(self, erb_config):
        # delete all register from table
        self.anatel_table.setRowCount(0)

        self.anatel_table: QTableWidget

        self.anatel_table.removeRow(0)
        row_position = self.anatel_table.rowCount()

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
            self.progress_bar_anatel.setValue(round(((processed / total) * 100), 2))

        self.anatel_table.setDisabled(False)
        self.update_database_button.setDisabled(False)

    def save_offline_erb_data(self, erb_config):
        self.__base_station_controller.destroy_all()

        for row in erb_config.values:
            data = {
                "status": row[0],
                "entidade": row[1],
                "num_fistel": row[2],
                "num_servico": row[3],
                "num_ato_de_rf": row[4],
                "num_estacao": row[5],
                "endereco": row[6],
                "uf": row[7],
                "municipio": row[8],
                "emissao": row[9],
                "tecnologia": row[10],
                "frequencia_inicial": row[11],
                "frequencia_final": row[12],
                "azimute": row[13],
                "tipo_estacao": row[14],
                "classificacao_infra_fisica": row[15],
                "compartilhamento_infra_fisica": row[16],
                "disp_compartilhamento_infra": row[17],
                "tipo_antena": row[18],
                "homologacao_antena": row[19],
                "ganho_antena": row[20],
                "ganho_frente_costa": row[21],
                "angulo_meia_potencia": row[22],
                "elevacao": row[23],
                "polarizacao": row[24],
                "altura": row[25],
                "homologacao_transmissao": row[26],
                "potencia_transmisao": row[27],
                "latitude": row[28],
                "longitude": row[29],
                "data_primeiro_licenciamento": row[30],
            }
            print(data)
            self.__base_station_controller.store(data)

    @pyqtSlot(name="on_update_database_button_clicked")
    def on_update_database_button_clicked(self):
        """
        This method add Anatel antenna info rows in the table
        :return:
        """
        self.label_last_update: QLabel
        self.progress_bar_anatel: QProgressBar

        self.label_last_update.setText("Searching for information in the online database...")

        self.combo_box_state: QComboBox
        uf_sigle = self.combo_box_state.itemText(self.combo_box_state.currentIndex())
        country_code = self.combo_box_contry.itemData(int(self.combo_box_contry.currentIndex()))

        erb_config = get_anatel_data(uf_sigle, int(country_code))

        self.label_last_update.setText("Saving information offline")

        self.save_offline_erb_data(erb_config)
        self.fill_erb_table(erb_config)

        self.label_last_update.setText("Updated local database!")
