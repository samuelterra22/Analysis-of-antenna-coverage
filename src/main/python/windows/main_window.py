#!/usr/bin/env python

import io
import sys
from math import pi, cos

import folium
import numpy as np
import matplotlib
import matplotlib.cm
from srtm import Srtm1HeightMapCollection
from srtm.base_coordinates import RasterBaseCoordinates
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QComboBox
from PyQt5 import QtCore, QtWidgets
from haversine import haversine, Unit

from src.main.python.models.base_station import BaseStation
from src.main.python.controllers.base_station_controller import BaseStationController
from src.main.python.dialogs.alert_dialog_class import AlertDialogClass
from src.main.python.dialogs.about_dialog_class import AboutDialogClass
from src.main.python.dialogs.anatel_dialog_class import AnatelDialogClass
from src.main.python.dialogs.settings_dialog_class import SettingsDialogClass
from src.main.python.dialogs.help_dialog_class import HelpDialogClass
from src.main.python.dialogs.confirm_simulation_dialog_class import ConfirmSimulationDialogClass
from src.main.python.support.propagation_models import cost231_path_loss
from src.main.python.support.constants import UFLA_LAT_LONG_POSITION
from support.anatel import dms_to_dd
from support.physical_constants import r_earth

Ui_MainWindow, QtBaseClass = uic.loadUiType("./views/main_window.ui")


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Main application class. This class load the main window
    """

    def __init__(self, parent=None):
        """
        Main window constructor
        :param parent:
        """
        # Init UI
        super().__init__()
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self._init_rf_map()
        # self.init_mos_map()

        # Calculate button
        self.button_calculate.clicked.disconnect()
        self.button_calculate.clicked.connect(self.on_button_calculate_clicked)

        self.__base_station_controller = BaseStationController()

        # Menus
        self.init_menus()

        # Tab components
        self.init_transmitter_components()
        self.init_antenna_components()
        self.init_model_components()
        self.init_output_components()

    def init_output_components(self) -> None:
        self.combo_box_output_colour_scheme: QComboBox
        self.combo_box_output_colour_scheme.addItems([])
        self.combo_box_output_colour_scheme.currentIndexChanged.connect(
            self.on_combo_box_output_colour_scheme_changed)

    def init_model_components(self) -> None:
        self.combo_box_propagation_model: QComboBox
        self.combo_box_propagation_model.addItems([])
        self.combo_box_propagation_model.currentIndexChanged.connect(
            self.on_combo_box_propagation_model_changed)

        self.combo_box_environment: QComboBox
        self.combo_box_environment.addItems([])
        self.combo_box_environment.currentIndexChanged.connect(
            self.on_combo_box_environment_changed)

    def init_antenna_components(self) -> None:
        self.combo_box_antenna_antenna_polarisation: QComboBox
        self.combo_box_antenna_antenna_polarisation.addItems([])
        self.combo_box_antenna_antenna_polarisation.currentIndexChanged.connect(
            self.on_combo_box_antenna_antenna_polarisation_changed)

    def init_transmitter_components(self) -> None:
        # For select a ERB
        self.combo_box_anatel_base_station: QComboBox

        self.fill_combo_box_anatel_base_station()
        self.combo_box_anatel_base_station.currentIndexChanged.connect(self.on_combo_box_anatel_base_station_changed)

        # For custom simulation
        self.combo_box_tx_coordinates: QComboBox
        self.combo_box_tx_coordinates.addItems([])
        self.combo_box_tx_coordinates.currentIndexChanged.connect(self.on_combo_box_tx_coordinates_changed)

    def fill_combo_box_anatel_base_station(self) -> None:
        db_configs = self.__base_station_controller.get_all_distinct()

        if db_configs is not None:
            for i, config in enumerate(db_configs):
                config: BaseStation
                self.combo_box_anatel_base_station.addItem(config.entidade + " - " + config.endereco, config.id)

    @pyqtSlot(name="on_combo_box_output_colour_scheme_changed")
    def on_combo_box_output_colour_scheme_changed(self) -> None:
        print("Items in the list 'combo_box_output_colour_scheme' are :")
        index = self.combo_box_output_colour_scheme.currentIndex()
        text = self.combo_box_output_colour_scheme.currentText()

        for count in range(self.combo_box_output_colour_scheme.count()):
            print(self.combo_box_output_colour_scheme.itemText(count))
        print("Current index", index, "selection changed ", text)

    @pyqtSlot(name="on_combo_box_environment_changed")
    def on_combo_box_environment_changed(self) -> None:
        print("Items in the list 'combo_box_environment' are :")
        index = self.combo_box_environment.currentIndex()
        text = self.combo_box_environment.currentText()

        for count in range(self.combo_box_environment.count()):
            print(self.combo_box_environment.itemText(count))
        print("Current index", index, "selection changed ", text)

    @pyqtSlot(name="on_combo_box_propagation_model_changed")
    def on_combo_box_propagation_model_changed(self) -> None:
        print("Items in the list 'combo_box_propagation_model' are :")
        index = self.combo_box_propagation_model.currentIndex()
        text = self.combo_box_propagation_model.currentText()

        for count in range(self.combo_box_propagation_model.count()):
            print(self.combo_box_propagation_model.itemText(count))
        print("Current index", index, "selection changed ", text)

    @pyqtSlot(name="on_combo_box_antenna_antenna_polarisation_changed")
    def on_combo_box_antenna_antenna_polarisation_changed(self) -> None:
        print("Items in the list 'combo_box_antenna_antenna_polarisation' are :")
        index = self.combo_box_antenna_antenna_polarisation.currentIndex()
        text = self.combo_box_antenna_antenna_polarisation.currentText()

        for count in range(self.combo_box_antenna_antenna_polarisation.count()):
            print(self.combo_box_antenna_antenna_polarisation.itemText(count))
        print("Current index", index, "selection changed ", text)

    @pyqtSlot(name="on_combo_box_anatel_base_station_changed")
    def on_combo_box_anatel_base_station_changed(self) -> None:
        print("Items in the list 'combo_box_anatel_base_station' are :")
        self.combo_box_anatel_base_station: QComboBox
        index = self.combo_box_anatel_base_station.currentIndex()
        data = self.combo_box_anatel_base_station.itemData(index)

        erb = self.__base_station_controller.get_by_id(data)
        self.add_erb_map(erb)
        self.add_erb_in_details(erb)

    def add_erb_map(self, base_station: BaseStation) -> None:
        erb_location = (str(dms_to_dd(base_station.latitude)), str(dms_to_dd(base_station.longitude)))

        m = folium.Map(
            location=erb_location,
            zoom_start=16,
            control_scale=True
        )

        folium.Marker(
            location=erb_location,
            popup=base_station.entidade,
            draggable=False,
            icon=folium.Icon(prefix='glyphicon', icon='tower')
        ).add_to(m)

        data = io.BytesIO()
        m.save(data, close_file=False)

        self.web_view.setHtml(data.getvalue().decode())

    def add_erb_in_details(self, base_station: BaseStation) -> None:
        self.label_anatel_entity_value.setText(base_station.entidade)
        self.label_anatel_station_number_value.setText(base_station.num_estacao)
        self.label_anatel_uf_value.setText(base_station.uf)
        self.label_anatel_contry_value.setText(base_station.municipio)
        self.label_anatel_address_value.setText(base_station.endereco)
        self.label_anatel_final_frequency_value.setText(base_station.frequencia_final)
        self.label_anatel_initial_frequency_value.setText(base_station.frequencia_inicial)
        self.label_anatel_azimute_value.setText(base_station.azimute)
        self.label_anatel_gain_antenna_value.setText(base_station.ganho_antena)
        self.label_anatel_front_back_value.setText(base_station.ganho_frente_costa)
        self.label_anatel_half_pot_value.setText(base_station.angulo_meia_potencia)
        self.label_anatel_elevation_value.setText(base_station.elevacao)
        self.label_anatel_polarization_value.setText(base_station.polarizacao)
        self.label_anatel_height_antenna_value.setText(base_station.altura)
        self.label_anatel_power_transmission_value.setText(base_station.potencia_transmissao)
        self.label_anatel_latitude_value.setText(str(dms_to_dd(base_station.latitude)))
        self.label_anatel_longitude_value.setText(str(dms_to_dd(base_station.longitude)))
        self.label_anatel_first_licensing_value.setText(base_station.data_primeiro_licenciamento)

    @pyqtSlot(name="on_combo_box_tx_coordinates_changed")
    def on_combo_box_tx_coordinates_changed(self) -> None:
        print("Items in the list 'combo_box_tx_coordinates' are :")
        index = self.combo_box_tx_coordinates.currentIndex()
        text = self.combo_box_tx_coordinates.currentText()

        for count in range(self.combo_box_tx_coordinates.count()):
            print(self.combo_box_tx_coordinates.itemText(count))
        print("Current index", index, "selection changed ", text)

    def init_menus(self) -> None:
        self.menu_action_exit.triggered.disconnect()
        self.menu_action_exit.triggered.connect(self.on_menu_exit_triggered)

        self.menu_action_anatel_base.triggered.disconnect()
        self.menu_action_anatel_base.triggered.connect(self.on_menu_anatel_base_triggered)

        self.menu_action_settings.triggered.disconnect()
        self.menu_action_settings.triggered.connect(self.on_menu_settings_triggered)

        self.menu_action_about.triggered.disconnect()
        self.menu_action_about.triggered.connect(self.on_menu_about_triggered)

        self.menu_action_help.triggered.disconnect()
        self.menu_action_help.triggered.connect(self.on_menu_help_triggered)

    def calc_distance(self, point_1: tuple, point_2: tuple, unit=Unit.METERS) -> float:
        return haversine(point_1, point_2, unit=unit)

    def _init_rf_map(self) -> None:
        m = folium.Map(
            location=UFLA_LAT_LONG_POSITION,
            zoom_start=16,
            control_scale=True
        )

        data = io.BytesIO()
        m.save(data, close_file=False)

        self.web_view.setHtml(data.getvalue().decode())

    def required_fields_filed(self) -> bool:
        if self.combo_box_anatel_base_station.currentIndex() == 0:
            AlertDialogClass("Selecione uma ERB", "ERB não selecionada! Selecione uma ERB para continuar...").exec_()
            return False

        if self.combo_box_antenna_antenna_polarisation.currentIndex() == 0:
            AlertDialogClass("Selecione uma polarização", "Polarização não selecionada! Selecione uma polarização "
                                                          "para continuar...").exec_()
            return False

        if self.combo_box_propagation_model.currentIndex() == 0:
            AlertDialogClass("Selecione um modelo de propagação", "Modelo de propagação não selecionado! Selecione um "
                                                                  "modelo de propagação para continuar...").exec_()
            return False

        if self.combo_box_environment.currentIndex() == 0:
            AlertDialogClass("Selecione um ambiente", "Ambiente de propagação não selecionado! Selecione um ambiente "
                                                      "de propagação para continuar...").exec_()
            return False

        if self.combo_box_output_colour_scheme.currentIndex() == 0:
            AlertDialogClass("Selecione um esquema de cores", "Esquema de cores da propagação não selecionada! "
                                                              "Selecione um esquema de cores da propagação para "
                                                              "continuar...").exec_()
            return False

        if not self.input_output_radius.text():
            AlertDialogClass("Raio Simulação", "Raio máximo de propagação não informado! Informe um raio máximo de "
                                               "propagação para continuar...").exec_()
            return False

        if not self.input_rx_height.text():
            AlertDialogClass("Altura RX", "Altura da antena receptora não informada! Informe uma altura para "
                                          "continuar...").exec_()
            return False

        if not self.input_rx_gain.text():
            AlertDialogClass("Ganho RX",
                             "Ganho da antena receptora não informado! Informe o ganho para continuar...").exec_()
            return False

        if not self.input_rx_sensitivity.text():
            AlertDialogClass("Sensibilidade RX",
                             "Sensibilidade da antena receptora não informada! Informe a Sensibilidade para "
                             "continuar...").exec_()
            return False

        return True

    @pyqtSlot(name="on_button_calculate_clicked")
    def on_button_calculate_clicked(self) -> None:
        """
        This method is called when calculate menu button is clicked
        :return: None
        """
        print("Calculate button!")

        # if not self.required_fields_filed():
        #     return

        data = {
            "simulation": {
                "propagation_model": "Hata",
                "environment": "",
                "max_ray": ""
            },
            "transmitter": {
                "entidade": "",
                "uf_municipio": "",
                "endereco": "",
                "frequencia": "",
                "ganho": "",
                "elevacao": "",
                "polarizacao": "",
                "altura": "",
                "latitude": "",
                "longitude": "",
            },
            "receptor": {
                "altura": "",
                "ganho": "",
                "sensibilidade": "",
            },
        }

        confirm_simulation_dialog = ConfirmSimulationDialogClass(data)
        confirm_simulation_dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        confirm_simulation_dialog.setModal(True)
        confirm_simulation_dialog.setFixedSize(confirm_simulation_dialog.size())

        if confirm_simulation_dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.simulated()

    def get_new_lat_lng(self, latitude: float, longitude: float, dx: float = 3, dy: float = 3) -> tuple:
        new_latitude = latitude + (round(dy / r_earth, 6)) * (round(180 / pi, 6))
        new_longitude = longitude + (round(dx / r_earth, 6)) * (round(180 / pi, 6)) / cos(round(latitude * pi / 180, 6))
        return tuple((round(new_latitude, 6), round(new_longitude, 6)))

    def simulated(self) -> None:
        self.combo_box_anatel_base_station: QComboBox
        index = self.combo_box_anatel_base_station.currentIndex()
        data = self.combo_box_anatel_base_station.itemData(index)

        srtm1_data = Srtm1HeightMapCollection()
        srtm1_data.build_file_index()
        srtm1_data.load_area(RasterBaseCoordinates.from_file_name("S22W045"),
                             RasterBaseCoordinates.from_file_name("S22W046"))

        base_station_selected: BaseStation
        base_station_selected = self.__base_station_controller.get_by_id(data)

        ERB_LOCATION = (dms_to_dd(base_station_selected.latitude), dms_to_dd(base_station_selected.longitude))
        altitude_tx = srtm1_data.get_altitude(latitude=ERB_LOCATION[0], longitude=ERB_LOCATION[1])

        transmitted_power = float(base_station_selected.potencia_transmissao)

        bm_max_sensitivity = -60
        bm_min_sensitivity = -160

        n_lats, n_lons = (500, 500)
        dy, dx = 6, 6  # 3km

        new_latitude1 = ERB_LOCATION[0] + (round(dy / r_earth, 6)) * (round(180 / pi, 6))
        new_longitude1 = ERB_LOCATION[1] + (round(dx / r_earth, 6)) * (round(180 / pi, 6)) / cos(
            round(ERB_LOCATION[0] * pi / 180, 6))

        new_latitude2 = ERB_LOCATION[0] - (round(dy / r_earth, 6)) * (round(180 / pi, 6))
        new_longitude2 = ERB_LOCATION[1] - (round(dx / r_earth, 6)) * (round(180 / pi, 6)) / cos(
            round(ERB_LOCATION[0] * pi / 180, 6))

        lat_bounds = (new_latitude1, new_latitude2)
        long_bounds = (new_longitude1, new_longitude2)

        lats_deg = np.linspace((lat_bounds[0]), (lat_bounds[1]), n_lats)
        lons_deg = np.linspace((long_bounds[0]), (long_bounds[1]), n_lons)

        lats_in_rad = np.deg2rad(lats_deg)
        longs_in_rad = np.deg2rad(lons_deg)

        lons_mesh, lats_mesh = np.meshgrid(longs_in_rad, lats_in_rad)

        lats_mesh_deg = np.rad2deg(lats_mesh)
        lons_mesh_deg = np.rad2deg(lons_mesh)

        propagation_matrix = np.empty([n_lats, n_lons])
        for i, point_long in enumerate(lons_deg):
            for j, point_lat in enumerate(lats_deg):
                point = (point_lat, point_long)
                altitude_rx = srtm1_data.get_altitude(latitude=point_lat, longitude=point_long)
                # print(str(point), "=", str(a))

                distance = self.calc_distance(point, ERB_LOCATION)

                random_bs_h = 0
                random_rx_h = 0

                bs_h = float(base_station_selected.altura) + random_bs_h  # float(altitude_tx)
                rx_h = 2 + random_rx_h  # float(altitude_rx)

                path_loss = cost231_path_loss(float(base_station_selected.frequencia_inicial), bs_h, rx_h, distance, 2)

                received_power = transmitted_power - path_loss

                propagation_matrix[i][j] = received_power

                print(received_power)
                # if received_power >= SENSITIVITY:
                #     propagation_matrix[i][j] = received_power
                # else:
                #     propagation_matrix[i][j] = 0

        print(propagation_matrix.shape)

        color_map = matplotlib.cm.get_cmap('YlOrBr')
        # color_map = matplotlib.cm.get_cmap('YlOrRd')
        # color_map = matplotlib.cm.get_cmap('plasma')
        # color_map = matplotlib.cm.get_cmap('spring')
        # color_map = matplotlib.cm.get_cmap('summer')
        # color_map = matplotlib.cm.get_cmap('gist_ncar') # <
        # color_map = matplotlib.cm.get_cmap('nipy_spectral')
        # color_map = matplotlib.cm.get_cmap('jet')
        # color_map = matplotlib.cm.get_cmap('Wistia')
        # color_map = matplotlib.cm.get_cmap('copper')
        # color_map = matplotlib.cm.get_cmap('Oranges')
        # color_map = matplotlib.cm.get_cmap('hot')
        # color_map = matplotlib.cm.get_cmap('RdPu')
        # color_map = matplotlib.cm.get_cmap('Blues')
        # color_map = matplotlib.cm.get_cmap('BuPu')
        # color_map = matplotlib.cm.get_cmap('OrRd')
        # color_map = matplotlib.cm.get_cmap('Greens')

        print(propagation_matrix.min())
        print(propagation_matrix.max())

        normed_data = (propagation_matrix - bm_min_sensitivity) / (bm_max_sensitivity - bm_min_sensitivity)
        colored_data = color_map(normed_data)

        m = folium.Map(
            location=ERB_LOCATION,
            zoom_start=16,
            control_scale=True
        )

        folium.raster_layers.ImageOverlay(
            image=colored_data,
            bounds=[[lats_mesh_deg.min(), lons_mesh_deg.min()], [lats_mesh_deg.max(), lons_mesh_deg.max()]],
            mercator_project=True,

            opacity=0.6,
            interactive=True,
            cross_origin=False,
        ).add_to(m)

        folium.Marker(
            location=ERB_LOCATION,
            popup=base_station_selected.entidade,
            draggable=False,
            icon=folium.Icon(prefix='glyphicon', icon='tower')
        ).add_to(m)

        data = io.BytesIO()
        m.save(data, close_file=False)

        self.web_view.setHtml(data.getvalue().decode())

    @pyqtSlot(name="on_menu_anatel_base_triggered")
    def on_menu_anatel_base_triggered(self) -> None:
        """
        This method is called when calculate button is clicked
        :return: None
        """
        anatel_dialog = AnatelDialogClass(self)
        anatel_dialog.setModal(True)
        anatel_dialog.setFixedSize(anatel_dialog.size())
        anatel_dialog.show()

    @pyqtSlot(name="on_menu_settings_triggered")
    def on_menu_settings_triggered(self) -> None:
        """
        This method is called when settings menu button is clicked
        :return: None
        """
        settings_dialog = SettingsDialogClass(self)
        settings_dialog.setModal(True)
        settings_dialog.show()

    @pyqtSlot(name="on_menu_about_triggered")
    def on_menu_about_triggered(self) -> None:
        """
        This method is called when about menu button is clicked
        :return: None
        """
        about_dialog = AboutDialogClass(self)
        about_dialog.setModal(True)
        about_dialog.show()

    @pyqtSlot(name="on_menu_help_triggered")
    def on_menu_help_triggered(self) -> None:
        """
        This method is called when help menu button is clicked
        :return: None
        """
        help_dialog = HelpDialogClass(self)
        help_dialog.setModal(True)
        help_dialog.show()

    @pyqtSlot(name="on_menu_exit_triggered")
    def on_menu_exit_triggered(self) -> None:
        """
        This method is called when exit menu button is clicked
        :return: None
        """
        sys.exit()
