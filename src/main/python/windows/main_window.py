#!/usr/bin/env python

import io
import sys
import random
import folium
import numpy as np
import matplotlib
import matplotlib.cm

from PyQt5 import uic
from pyqtlet import L, MapWidget
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QComboBox
from haversine import haversine, Unit

from src.main.python.dialogs.about_dialog_class import AboutDialogClass
from src.main.python.dialogs.anatel_dialog_class import AnatelDialogClass
from src.main.python.dialogs.settings_dialog_class import SettingsDialogClass
from src.main.python.dialogs.help_dialog_class import HelpDialogClass
from support.propagation_models import cost231_path_loss

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

        # Menus
        self.init_menus()

        # Tab components
        self.init_transmitter_components()
        self.init_antenna_components()
        self.init_model_components()
        self.init_output_components()

    def init_output_components(self):
        self.combo_box_output_colour_scheme: QComboBox
        self.combo_box_output_colour_scheme.addItems([])
        self.combo_box_output_colour_scheme.currentIndexChanged.connect(
            self.on_combo_box_output_colour_scheme_changed)


    def init_model_components(self):
        self.combo_box_propagation_model: QComboBox
        self.combo_box_propagation_model.addItems([])
        self.combo_box_propagation_model.currentIndexChanged.connect(
            self.on_combo_box_propagation_model_changed)

        self.combo_box_environment: QComboBox
        self.combo_box_environment.addItems([])
        self.combo_box_environment.currentIndexChanged.connect(
            self.on_combo_box_environment_changed)

    def init_antenna_components(self):
        self.combo_box_antenna_antenna_polarisation: QComboBox
        self.combo_box_antenna_antenna_polarisation.addItems([])
        self.combo_box_antenna_antenna_polarisation.currentIndexChanged.connect(
            self.on_combo_box_antenna_antenna_polarisation_changed)

    def init_transmitter_components(self):
        self.combo_box_anatel_base_station: QComboBox
        self.combo_box_anatel_base_station.addItems([])
        self.combo_box_anatel_base_station.currentIndexChanged.connect(self.on_combo_box_anatel_base_station_changed)

        self.combo_box_tx_coordinates: QComboBox
        self.combo_box_tx_coordinates.addItems([])
        self.combo_box_tx_coordinates.currentIndexChanged.connect(self.on_combo_box_tx_coordinates_changed)

    @pyqtSlot(name="on_combo_box_output_colour_scheme_changed")
    def on_combo_box_output_colour_scheme_changed(self):
        print("Items in the list 'combo_box_output_colour_scheme' are :")
        index = self.combo_box_output_colour_scheme.currentIndex()
        text = self.combo_box_output_colour_scheme.currentText()

        for count in range(self.combo_box_output_colour_scheme.count()):
            print(self.combo_box_output_colour_scheme.itemText(count))
        print("Current index", index, "selection changed ", text)

    @pyqtSlot(name="on_combo_box_environment_changed")
    def on_combo_box_environment_changed(self):
        print("Items in the list 'combo_box_environment' are :")
        index = self.combo_box_environment.currentIndex()
        text = self.combo_box_environment.currentText()

        for count in range(self.combo_box_environment.count()):
            print(self.combo_box_environment.itemText(count))
        print("Current index", index, "selection changed ", text)

    @pyqtSlot(name="on_combo_box_propagation_model_changed")
    def on_combo_box_propagation_model_changed(self):
        print("Items in the list 'combo_box_propagation_model' are :")
        index = self.combo_box_propagation_model.currentIndex()
        text = self.combo_box_propagation_model.currentText()

        for count in range(self.combo_box_propagation_model.count()):
            print(self.combo_box_propagation_model.itemText(count))
        print("Current index", index, "selection changed ", text)

    @pyqtSlot(name="on_combo_box_antenna_antenna_polarisation_changed")
    def on_combo_box_antenna_antenna_polarisation_changed(self):
        print("Items in the list 'combo_box_antenna_antenna_polarisation' are :")
        index = self.combo_box_antenna_antenna_polarisation.currentIndex()
        text = self.combo_box_antenna_antenna_polarisation.currentText()

        for count in range(self.combo_box_antenna_antenna_polarisation.count()):
            print(self.combo_box_antenna_antenna_polarisation.itemText(count))
        print("Current index", index, "selection changed ", text)

    @pyqtSlot(name="on_combo_box_anatel_base_station_changed")
    def on_combo_box_anatel_base_station_changed(self):
        print("Items in the list 'combo_box_anatel_base_station' are :")
        index = self.combo_box_anatel_base_station.currentIndex()
        text = self.combo_box_anatel_base_station.currentText()

        for count in range(self.combo_box_anatel_base_station.count()):
            print(self.combo_box_anatel_base_station.itemText(count))
        print("Current index", index, "selection changed ", text)

    @pyqtSlot(name="on_combo_box_tx_coordinates_changed")
    def on_combo_box_tx_coordinates_changed(self):
        print("Items in the list 'combo_box_tx_coordinates' are :")
        index = self.combo_box_tx_coordinates.currentIndex()
        text = self.combo_box_tx_coordinates.currentText()

        for count in range(self.combo_box_tx_coordinates.count()):
            print(self.combo_box_tx_coordinates.itemText(count))
        print("Current index", index, "selection changed ", text)

    def init_menus(self):
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

    def calc_distance(self, point_1, point_2, unit=Unit.METERS):
        return haversine(point_1, point_2, unit=unit)

    def _init_rf_map(self):
        m = folium.Map(
            location=(-21.226244, -44.978407),
            zoom_start=16,
            control_scale=True
        )

        data = io.BytesIO()
        m.save(data, close_file=False)

        self.web_view.setHtml(data.getvalue().decode())

    @pyqtSlot(name="on_button_calculate_clicked")
    def on_button_calculate_clicked(self):
        """
        This method is called when calculate menu button is clicked
        :return: None
        """
        print("Calculate button!")

        ERB_LOCATION = (-21.226244, -44.978407)

        transmitted_power = 1872.500  # 74.471580313
        SENSITIVITY = -134

        n = 0.00

        n_lats, n_lons = (4, 4)
        lat_bounds = (-21.211645, -21.246091)
        long_bounds = (-44.995876, -44.954157)

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
                distance = self.calc_distance(ERB_LOCATION, point)

                path_loss = cost231_path_loss(transmitted_power, 56, 1, distance, 2)
                received_power = transmitted_power - path_loss

                propagation_matrix[i][j] = received_power
                # if received_power >= SENSITIVITY:
                #     propagation_matrix[i][j] = received_power
                # else:
                #     propagation_matrix[i][j] = 0

        print(propagation_matrix.shape)

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
        color_map = matplotlib.cm.get_cmap('OrRd')

        normed_data = (propagation_matrix - propagation_matrix.min()) / (
                propagation_matrix.max() - propagation_matrix.min())
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
            popup='Estação Rádio Base Vivo',
            draggable=False,
            icon=folium.Icon(prefix='glyphicon', icon='tower')
        ).add_to(m)

        data = io.BytesIO()
        m.save(data, close_file=False)

        self.web_view.setHtml(data.getvalue().decode())

    @pyqtSlot(name="on_menu_anatel_base_triggered")
    def on_menu_anatel_base_triggered(self):
        """
        This method is called when calculate button is clicked
        :return: None
        """
        anatel_dialog = AnatelDialogClass(self)
        anatel_dialog.setModal(True)
        anatel_dialog.setFixedSize(anatel_dialog.size())
        anatel_dialog.show()

    @pyqtSlot(name="on_menu_settings_triggered")
    def on_menu_settings_triggered(self):
        """
        This method is called when settings menu button is clicked
        :return: None
        """
        settings_dialog = SettingsDialogClass(self)
        settings_dialog.setModal(True)
        settings_dialog.show()

    @pyqtSlot(name="on_menu_about_triggered")
    def on_menu_about_triggered(self):
        """
        This method is called when about menu button is clicked
        :return: None
        """
        about_dialog = AboutDialogClass(self)
        about_dialog.setModal(True)
        about_dialog.show()

    @pyqtSlot(name="on_menu_help_triggered")
    def on_menu_help_triggered(self):
        """
        This method is called when help menu button is clicked
        :return: None
        """
        help_dialog = HelpDialogClass(self)
        help_dialog.setModal(True)
        help_dialog.show()

    @pyqtSlot(name="on_menu_exit_triggered")
    def on_menu_exit_triggered(self):
        """
        This method is called when exit menu button is clicked
        :return: None
        """
        sys.exit()
