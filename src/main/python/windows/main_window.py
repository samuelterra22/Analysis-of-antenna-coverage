#!/usr/bin/env python

import io
import math
import sys
import time
from math import pi, cos, exp

import random
import copy

import folium
import numpy as np
import matplotlib
import matplotlib.cm
import matplotlib.pyplot as plt

from PyQt5 import uic, QtWebEngineWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QComboBox, QLineEdit, QLabel
from PyQt5 import QtCore, QtWidgets
from folium import Map
from numpy.core.multiarray import ndarray
from typing import Tuple, List, Dict, Union, Any

from models.base_station import BaseStation
from controllers.base_station_controller import BaseStationController
from dialogs.alert_dialog_class import AlertDialogClass
from dialogs.about_dialog_class import AboutDialogClass
from dialogs.anatel_dialog_class import AnatelDialogClass
from dialogs.settings_dialog_class import SettingsDialogClass
from dialogs.help_dialog_class import HelpDialogClass
from dialogs.confirm_simulation_dialog_class import ConfirmSimulationDialogClass
from support.propagation_models import cost231_path_loss
from support.constants import UFLA_LAT_LONG_POSITION, MIN_SENSITIVITY, bm_min_sensitivity, bm_max_sensitivity
from support.core import calculates_distance_between_coordinates, get_altitude, get_coordinate_in_circle
from support.physical_constants import r_earth

from base import context


class MainWindow(QMainWindow):
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
        self.ui = uic.loadUi(context.get_resource("main_window.ui"), self)

        # Init controllers
        self.__base_station_controller = BaseStationController()

        # Init main map
        self.__init_rf_map()

        # Link calculate button with method
        self.button_calculate.clicked.disconnect()
        self.button_calculate.clicked.connect(self.on_button_calculate_clicked)

        # Init tha application menus
        self.__init_menus()

        # init tab components
        self.init_transmitter_components()
        self.init_receptor_components()
        self.init_model_components()
        self.init_simulated_annealing_components()
        self.init_output_components()

        self.min_altitude = None
        self.max_altitude = None

        self.set_default_values()

        self.sub_area_bounds = [
            (-21.252142, -44.984765),
            (-21.252142, -45.013754),
            (-21.238862, -45.013754),
            (-21.238862, -44.984765),
        ]

    def set_default_values(self):
        # Transmissor tab
        self.combo_box_anatel_base_station: QComboBox
        self.combo_box_anatel_base_station.setCurrentIndex(14)

        # Receptor tab
        self.input_rx_height: QLineEdit
        self.input_rx_gain: QLineEdit
        self.input_rx_sensitivity: QLineEdit

        self.input_rx_height.setText("1")
        self.input_rx_gain.setText("1")
        self.input_rx_sensitivity.setText("-180")

        # Propagation model tab
        self.combo_box_propagation_model: QComboBox
        self.combo_box_environment: QComboBox

        self.combo_box_propagation_model.setCurrentIndex(1)
        self.combo_box_environment.setCurrentIndex(1)

        # Meta-heuristic tab
        self.input_sa_temp_initial: QLineEdit
        self.input_sa_num_max_iterations: QLineEdit
        self.input_sa_num_max_perturbation_per_iteration: QLineEdit
        self.input_sa_num_max_success_per_iteration: QLineEdit
        self.input_sa_alpha: QLineEdit

        self.input_sa_temp_initial.setText("200.0")
        self.input_sa_num_max_iterations.setText("3")
        self.input_sa_num_max_perturbation_per_iteration.setText("5")
        self.input_sa_num_max_success_per_iteration.setText("140")
        self.input_sa_alpha.setText("0.85")

        # Output tab
        self.combo_box_output_colour_scheme: QComboBox
        self.input_output_radius: QLineEdit

        self.combo_box_output_colour_scheme.setCurrentIndex(2)
        self.input_output_radius.setText("60")

    def init_simulated_annealing_components(self) -> None:
        self.input_sa_temp_initial: QLineEdit
        self.input_sa_num_max_iterations: QLineEdit
        self.input_sa_num_max_perturbation_per_iteration: QLineEdit
        self.input_sa_num_max_success_per_iteration: QLineEdit
        self.input_sa_alpha: QLineEdit

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

    def init_receptor_components(self) -> None:
        self.input_rx_height: QLineEdit
        self.input_rx_gain: QLineEdit
        self.input_rx_sensitivity: QLineEdit

    def init_transmitter_components(self) -> None:
        # For select a ERB
        self.combo_box_anatel_base_station: QComboBox

        self.fill_combo_box_anatel_base_station()
        self.combo_box_anatel_base_station.currentIndexChanged.connect(self.on_combo_box_anatel_base_station_changed)

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

    @pyqtSlot(name="on_combo_box_anatel_base_station_changed")
    def on_combo_box_anatel_base_station_changed(self) -> None:
        print("Items in the list 'combo_box_anatel_base_station' are :")
        self.combo_box_anatel_base_station: QComboBox
        index = self.combo_box_anatel_base_station.currentIndex()
        data = self.combo_box_anatel_base_station.itemData(index)

        erb = self.__base_station_controller.get_by_id(data)
        print("Index: " + str(index))
        print(erb.endereco)
        self.add_erb_map(erb)
        self.add_erb_in_details(erb)

    @pyqtSlot(name="on_combo_box_tx_coordinates_changed")
    def on_combo_box_tx_coordinates_changed(self) -> None:
        print("Items in the list 'combo_box_tx_coordinates' are :")
        index = self.combo_box_tx_coordinates.currentIndex()
        text = self.combo_box_tx_coordinates.currentText()

        for count in range(self.combo_box_tx_coordinates.count()):
            print(self.combo_box_tx_coordinates.itemText(count))
        print("Current index", index, "selection changed ", text)

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

    @pyqtSlot(name="on_button_calculate_clicked")
    def on_button_calculate_clicked(self) -> None:
        """
        This method is called when calculate menu button is clicked
        :return: None
        """
        print("Calculate button!")

        # Check if input fields is fillers
        if not self.required_fields_fillers():
            return

        base_station_selected = self.get_bs_selected()
        propagation_model_selected = self.get_propagation_model_selected()

        data = {
            "simulation": {
                "propagation_model": propagation_model_selected['text'],
                "environment": str(self.combo_box_environment.currentText()),
                "max_ray": str(self.input_output_radius.text()) + "m"
            },
            "transmitter": {
                "entidade": str(base_station_selected.entidade),
                "uf_municipio": str(base_station_selected.uf),
                "endereco": str(base_station_selected.endereco)[0:35] + "...",
                "frequencia": str(base_station_selected.frequencia_inicial),
                "potencia_transmissao": str(base_station_selected.potencia_transmissao) + "W",
                "ganho": str(base_station_selected.ganho_antena) + "dBi",
                "elevacao": str(base_station_selected.elevacao),
                "polarizacao": str(base_station_selected.polarizacao),
                "altura": str(base_station_selected.altura) + "m",
                "latitude": str(base_station_selected.latitude),
                "longitude": str(base_station_selected.longitude),
            },
            "receptor": {
                "altura": str(self.input_rx_height.text()) + "m",
                "ganho": str(self.input_rx_gain.text()) + "dBi",
                "sensibilidade": str(self.input_rx_sensitivity.text()) + "dBm",
            },
            "heuristic": {
                "solucao_inicial": "(" + str(base_station_selected.latitude) + ", " + str(
                    base_station_selected.longitude) + ")",
                "temperatura_inicial": self.input_sa_temp_initial.text(),
                "numero_maximo_iteracoes": self.input_sa_num_max_iterations.text(),
                "numero_maximo_pertubacoes_por_iteracao": self.input_sa_num_max_perturbation_per_iteration.text(),
                "numero_maximo_sucessos_por_iteracao": self.input_sa_num_max_success_per_iteration.text(),
                "alpha": self.input_sa_alpha.text(),
            },
        }

        confirm_simulation_dialog = ConfirmSimulationDialogClass(data)
        confirm_simulation_dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        confirm_simulation_dialog.setModal(True)
        confirm_simulation_dialog.setFixedSize(confirm_simulation_dialog.size())

        if confirm_simulation_dialog.exec_() == QtWidgets.QDialog.Accepted:
            start = time.time()
            self.run_simulation()
            end = time.time()

            self.label_geral_info_1: QLabel
            self.label_geral_info_1.setText("Simulação executada em %s segundos" % round(end - start, 2))

    def add_erb_map(self, base_station: BaseStation) -> None:
        erb_location = (str(base_station.latitude), str(base_station.longitude))

        m = self.get_folium_map(location=erb_location)

        # html = f"""
        #         <h1> {base_station.entidade}</h1>
        #         <p>You can use any html here! Let's do a list:</p>
        #         <ul>
        #             <li>Latitude: {base_station.latitude}</li>
        #             <li>Longitude: {base_station.longitude}</li>
        #         </ul>
        #         """
        # iframe = folium.IFrame(html=html, width=200, height=200)
        # popup = folium.Popup(iframe, max_width=2650)

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
        self.label_anatel_latitude_value.setText(str(base_station.latitude))
        self.label_anatel_longitude_value.setText(str(base_station.longitude))
        self.label_anatel_first_licensing_value.setText(base_station.data_primeiro_licenciamento)

    def __init_menus(self) -> None:
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

    def __init_rf_map(self) -> None:
        m = self.get_folium_map(UFLA_LAT_LONG_POSITION)

        data = io.BytesIO()
        m.save(data, close_file=False)

        self.web_view.setHtml(data.getvalue().decode())

    @staticmethod
    def get_folium_map(location=UFLA_LAT_LONG_POSITION, tiles="cartodb positron", zoom_start=16, control_scale=True) \
            -> Map:
        # tiles = "Stamen Terrain"
        return folium.Map(
            location=location,
            tiles=tiles,
            zoom_start=zoom_start,
            control_scale=control_scale
        )

    def required_fields_fillers(self) -> bool:
        title = None
        message = None

        if self.combo_box_anatel_base_station.currentIndex() == 0:
            title = "Selecione uma ERB"
            message = "ERB não selecionada! Selecione uma ERB para continuar..."

        if self.combo_box_propagation_model.currentIndex() == 0:
            title = "Selecione um modelo de propagação"
            message = "Modelo de propagação não selecionado! Selecione um modelo de propagação para continuar..."

        if self.combo_box_environment.currentIndex() == 0:
            title = "Selecione um ambiente"
            message = "Ambiente de propagação não selecionado! Selecione um ambiente de propagação para continuar..."

        if self.combo_box_output_colour_scheme.currentIndex() == 0:
            title = "Selecione um esquema de cores"
            message = "Esquema de cores não selecionada! Selecione um esquema de cores da propagação para continuar..."

        if not self.input_output_radius.text():
            title = "Raio Simulação"
            message = "Raio máximo de propagação não informado! Informe um raio máximo de propagação para continuar..."

        if not self.input_rx_height.text():
            title = "Altura RX"
            message = "Altura da antena receptora não informada! Informe uma altura para continuar..."

        if not self.input_rx_gain.text():
            title = "Ganho RX"
            message = "Ganho da antena receptora não informado! Informe o ganho para continuar..."

        if not self.input_rx_sensitivity.text():
            title = "Sensibilidade RX"
            message = "Sensibilidade da antena receptora não informada! Informe a Sensibilidade para continuar..."

        if title is not None and message is not None:
            AlertDialogClass(title, message).exec_()
            return False

        return True

    def get_bs_selected(self) -> BaseStation:
        self.combo_box_anatel_base_station: QComboBox
        index = self.combo_box_anatel_base_station.currentIndex()
        data = self.combo_box_anatel_base_station.itemData(index)

        base_station_selected: BaseStation
        return self.__base_station_controller.get_by_id(data)

    def get_propagation_model_selected(self) -> Dict[str, Union[int, Any]]:
        self.combo_box_propagation_model: QComboBox
        index = self.combo_box_propagation_model.currentIndex()
        data = self.combo_box_propagation_model.itemData(index)
        text = self.combo_box_propagation_model.currentText()

        return {
            'index': index,
            'data': data,
            'text': text
        }

    @staticmethod
    def objective_function(propagation_matrix: ndarray) -> float:
        fo_value = 0
        total_of_points = len(propagation_matrix) * len(propagation_matrix[0])

        print(total_of_points)

        for line in propagation_matrix:
            for value in line:
                if value >= MIN_SENSITIVITY:
                    fo_value += 1

        coverage_percent = (fo_value / total_of_points) * 100  # porcentagem de cobertura
        shadow_percent = 100 - coverage_percent  # porcentagem de sombra

        fo_alpha = 7
        return (fo_alpha * coverage_percent) - ((10 - fo_alpha) * shadow_percent)  # pesos 7 pra 3

    @staticmethod
    def __get_simulation_bounds(lat: float, long: float, dx: float, dy: float) \
            -> Tuple[Tuple[float, float], Tuple[float, float]]:

        new_latitude1 = lat + (round(dy / r_earth, 6)) * (round(180 / pi, 6))
        new_longitude1 = long + (round(dx / r_earth, 6)) * (round(180 / pi, 6)) / cos(round(lat * pi / 180, 6))

        new_latitude2 = lat - (round(dy / r_earth, 6)) * (round(180 / pi, 6))
        new_longitude2 = long - (round(dx / r_earth, 6)) * (round(180 / pi, 6)) / cos(round(lat * pi / 180, 6))

        lat_bounds = (round(new_latitude1, 6), round(new_latitude2, 6))
        long_bounds = (round(new_longitude1, 6), round(new_longitude2, 6))

        return lat_bounds, long_bounds

    def FindPoint(self, x1, y1, x2, y2, x, y):
        # print(x1, y1, x2, y2, x, y)

        if (x > x1 and x < x2 and y > y1 and y < y2):
            return True
        else:
            return False

    def is_point_inside_sub_area(self, point: Tuple) -> bool:
        # point = Feature(geometry=Point(point))
        # polygon = Polygon([self.sub_area_bounds])
        # return boolean_point_in_polygon(point, polygon)
        return self.FindPoint(-21.250078, -45.004024, -21.241697, -44.995849, round(point[0], 6), round(point[1], 6))

    @staticmethod
    def percentage(percent: float, whole: float) -> float:
        return (percent * whole) / 100.0

    def simulates_propagation(self, base_station_selected: BaseStation, lats_deg: ndarray, longs_deg: ndarray) -> ndarray:
        erb_location = (base_station_selected.latitude, base_station_selected.longitude)

        transmitted_power = float(base_station_selected.potencia_transmissao)

        altitude_tx = get_altitude(lat=erb_location[0], long=erb_location[1])

        if self.max_altitude is None and self.min_altitude is None:
            self.min_altitude = math.inf
            self.max_altitude = - math.inf
            for i, point_long in enumerate(longs_deg):
                for j, point_lat in enumerate(lats_deg):
                    altitude_point_terrain = get_altitude(lat=point_lat, long=point_long)

                    if altitude_point_terrain < self.min_altitude:
                        self.min_altitude = altitude_point_terrain

                    if altitude_point_terrain > self.max_altitude:
                        self.max_altitude = altitude_point_terrain

            print("self.min_altitude=", self.min_altitude)
            print("self.max_altitude=", self.max_altitude)

        propagation_matrix = np.empty([len(longs_deg), len(lats_deg)])
        for i, point_long in enumerate(longs_deg):
            for j, point_lat in enumerate(lats_deg):
                mobile_base_location = (point_lat, point_long)

                altitude_rx = get_altitude(lat=point_lat, long=point_long)

                distance = calculates_distance_between_coordinates(mobile_base_location, erb_location)

                tx_h = (float(base_station_selected.altura) + altitude_tx) - self.min_altitude
                rx_h = (2 + altitude_rx) - self.min_altitude

                # calculate the path loss using a propagation model
                path_loss = cost231_path_loss(float(base_station_selected.frequencia_inicial), tx_h, rx_h, distance, 2)

                received_power = transmitted_power - path_loss

                if self.is_point_inside_sub_area(mobile_base_location):
                    propagation_matrix[i][j] = received_power + self.percentage(10, abs(received_power))
                else:
                    propagation_matrix[i][j] = received_power

                # print(received_power)
                # if received_power >= MIN_SENSITIVITY:
                #     propagation_matrix[i][j] = received_power
                # else:
                #     propagation_matrix[i][j] = 0 # bm_min_sensitivity or bm_max_sensitivity

        return propagation_matrix

    def print_simulation_result(self, propagation_matrix: ndarray, lats_deg: ndarray, longs_deg: ndarray,
                                base_station_selected: BaseStation) -> None:

        erb_location = (base_station_selected.latitude, base_station_selected.longitude)

        lats_in_rad = np.deg2rad(lats_deg)
        longs_in_rad = np.deg2rad(longs_deg)

        longs_mesh, lats_mesh = np.meshgrid(longs_in_rad, lats_in_rad)

        lats_mesh_deg = np.rad2deg(lats_mesh)
        longs_mesh_deg = np.rad2deg(longs_mesh)

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

        # dados normatizados
        normed_data = (propagation_matrix - bm_min_sensitivity) / (bm_max_sensitivity - bm_min_sensitivity)
        colored_data = color_map(normed_data)

        m = self.get_folium_map(location=erb_location)

        folium.raster_layers.ImageOverlay(
            image=np.flip(colored_data, 1),
            bounds=[[lats_mesh_deg.min(), longs_mesh_deg.min()], [lats_mesh_deg.max(), longs_mesh_deg.max()]],
            mercator_project=True,
            opacity=0.6,
            interactive=True,
            cross_origin=False,
        ).add_to(m)

        folium.Marker(
            location=erb_location,
            popup=base_station_selected.entidade,
            draggable=False,
            icon=folium.Icon(prefix='glyphicon', icon='tower')
        ).add_to(m)

        data = io.BytesIO()
        m.save(data, close_file=False)

        self.web_view.setHtml(data.getvalue().decode())

    def run_simulation(self) -> None:
        optimize_solution = True

        base_station_selected = self.get_bs_selected()

        erb_location = (base_station_selected.latitude, base_station_selected.longitude)

        # get simulation bounds
        dy, dx = 6, 6  # 3km
        lat_bounds, long_bounds = self.__get_simulation_bounds(erb_location[0], erb_location[1], dx, dy)

        # get coordinates list
        n_lats, n_longs = (500, 500)
        lats_deg = np.linspace((lat_bounds[0]), (lat_bounds[1]), n_lats)
        longs_deg = np.linspace((long_bounds[0]), (long_bounds[1]), n_longs)

        # lats_deg = [round(la, 6) for la in lats_deg]
        # longs_deg = [round(lo, 6) for lo in longs_deg]

        # Get matrix result for matrix coordinates
        propagation_matrix = self.simulates_propagation(base_station_selected, lats_deg, longs_deg)

        # print(propagation_matrix)
        print('propagation_matrix.shape', propagation_matrix.shape)
        print('objective_function', self.objective_function(propagation_matrix))

        #  Show simulation map
        self.print_simulation_result(propagation_matrix, lats_deg, longs_deg, base_station_selected)

        if optimize_solution:
            problem = (base_station_selected, longs_deg, lats_deg)

            # Run simulated annealing
            # self.simulated_annealing(problem=problem, M=600, P=5, L=240, T0=300.0, alpha=.85)
            best, _, FOs = self.simulated_annealing(problem=problem, M=3, P=5, L=140, T0=200.0, alpha=.85)

            #  print best solution found
            matrix_solution = self.simulates_propagation(best, lats_deg, longs_deg)
            self.print_simulation_result(matrix_solution, lats_deg, longs_deg, best)

            print("(best.latitude, best.longitude)=", (best.latitude, best.longitude))

            if FOs:
                # Plot the objective function line chart
                print("\n... gerando gráfico do comportamento da FO.")
                plt.plot(FOs)
                plt.title("Comportamento do Simulated Annealing")
                plt.ylabel('Valor da FO')
                plt.xlabel('Solução candidata')
                plt.show()

        print("End of simulation!")

    def evaluate_solution(self, point: BaseStation, longs_deg: ndarray, lats_deg: ndarray) -> float:
        matrix_solution = self.simulates_propagation(point, lats_deg, longs_deg)

        return self.objective_function(matrix_solution)

    @staticmethod
    def disturb_solution(solution: BaseStation, disturbance_radius: float = 460) -> BaseStation:
        """
        Disturb a specific solution
        :param solution: A base station solution
        :param disturbance_radius: The ray of disturbance in meters
        :return: Return the base station with a new position (lat long)
        """
        latitude = solution.latitude
        longitude = solution.longitude

        new_coordinates = get_coordinate_in_circle(latitude, longitude, disturbance_radius)

        solution.latitude = new_coordinates[0]
        solution.longitude = new_coordinates[1]

        return solution

    def simulated_annealing(self, problem, M: int, P: int, L: int, T0: float, alpha: float) \
            -> Tuple[BaseStation, float, List[float]]:
        """
        :param problem: Dados do problema principal
        :param M: Número máximo de iterações.
        :param P: Número máximo de Perturbações por iteração.
        :param L: Número máximo de sucessos por iteração.
        :param T0: Temperatura inicial.
        :param alpha: Factor de redução da temperatura.
        :return: Retorna um ponto (tupla de coordenadas) sendo a mais indicada.
        """

        # Get problem parameters
        base_station_selected, longs_deg, lats_deg = problem

        FOs = []

        # cria Soluções (posições) iniciais com pontos aleatórios para os APs
        s = base_station_selected

        s0 = s
        print("Solução inicial: " + str((s0.latitude, s0.longitude)))

        result_fo = self.evaluate_solution(s, longs_deg, lats_deg)

        f_s = result_fo

        T = T0
        j = 1

        # Store the BEST solution found
        best_fs = f_s
        best_erb = s0

        # Loop principal – Verifica se foram atendidas as condições de termino do algoritmo
        while True:
            i = 1
            n_success = 0

            # Loop Interno – Realização de perturbação em uma iteração
            while True:

                # Get a different position to ERB
                initial_solution = self.disturb_solution(s)

                # Get objective function value
                result_fo = self.evaluate_solution(initial_solution, longs_deg, lats_deg)

                f_si = result_fo

                # Verificar se o retorno da função objetivo está correto. f(x) é a função objetivo
                delta_fi = f_si - f_s

                # Minimização: delta_fi >= 0
                # Maximização: delta_fi <= 0
                # Teste de aceitação de uma nova solução
                if (delta_fi <= 0) or (exp(-delta_fi / T) > random.random()):

                    s = copy.deepcopy(initial_solution)
                    f_s = f_si

                    n_success = n_success + 1

                    if f_s > best_fs:
                        best_fs = f_s
                        best_erb = copy.deepcopy(initial_solution)

                    FOs.append(f_s)

                i = i + 1

                if (n_success >= L) or (i > P):
                    break

            # Atualização da temperatura (Decaimento geométrico)
            T = alpha * T

            # Atualização do contador de iterações
            j = j + 1

            if (n_success == 0) or (j > M):
                break

            print('T=', T)
            print('n_success=', n_success)
            print('j=', j)
            print('best_fs=', best_fs)

        FOs.append(best_fs)
        print('FOs=', str(FOs))

        return best_erb, best_fs, FOs
