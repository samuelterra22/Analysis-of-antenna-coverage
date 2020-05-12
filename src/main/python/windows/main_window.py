#!/usr/bin/env python

import io
import sys
import random
import folium

from PyQt5 import uic
from pyqtlet import L, MapWidget
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from folium.plugins import HeatMap
from random import randrange
from haversine import haversine, Unit

from src.main.python.dialogs.about_dialog_class import AboutDialogClass
from src.main.python.dialogs.anatel_dialog_class import AnatelDialogClass
from src.main.python.dialogs.settings_dialog_class import SettingsDialogClass
from src.main.python.dialogs.help_dialog_class import HelpDialogClass
from support.color import get_color_of_interval
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

        self._init_map()
        # self.init_mos_map()

        # Calculate button
        self.button_calculate.clicked.connect(self.on_button_calculate_clicked)

        # Menus
        self.menu_action_exit.triggered.connect(self.on_menu_exit_triggered)
        self.menu_action_anatel_base.triggered.connect(
            self.on_menu_anatel_base_triggered
        )
        self.menu_action_settings.triggered.connect(self.on_menu_settings_triggered)
        self.menu_action_about.triggered.connect(self.on_menu_about_triggered)
        self.menu_action_help.triggered.connect(self.on_menu_help_triggered)

    def generate_random_data(self, lat, lon):
        dec_lat = (random.random() / 100) * random.choice([-1, 1])
        dec_lon = (random.random() / 100) * random.choice([-1, 1])

        return [round(lat + dec_lat, 15), round(lon + dec_lon, 15)]

    def set_zoom_warning(self, zoom):
        if zoom < 6:
            print('Woah buddy. You\'re flying pretty high. Hope you don\'t have vertigo..')
        else:
            print('Yup, no worries. A fall from here shoudn\'t hurt... too much.')

    def set_warnings(self):
        self.map.getZoom(self.set_zoom_warning)

    def _get_marker_radius(self, value):
        # We want the marker size to be exponential to the number
        power = (1 / 3)
        MAX_SIZE = 1  # ?
        return MAX_SIZE * (value ** power) / (self.highIncidents ** power)

    def on_map_clicked(self, event):
        print(event)

    def on_map_zoomed(self, event):
        print(event)

    def _init_map_leaf(self):
        self.map_widget = MapWidget()
        self.vertical_layout_coverage_map.addWidget(self.map_widget)

        self.map = L.map(self.map_widget)
        # {
        #     'minOpacity': 0.05,
        #     'maxZoom': 18,
        #     'radius': 25,
        #     'blur': 15,
        #     'max': 1.0
        # }
        self.map.setView([-21.2284575, -44.9753476], 16)

        # self.map.clicked.connect(self.on_map_clicked)
        # self.map.zoom.connect(self.on_map_zoomed)

        # self.map.getBounds(lambda bounds: print(bounds))

        # self.set_warnings()

        # L.tileLayer('http://{s}.tile.openstreetmap.de/{z}/{x}/{y}.png').addTo(self.map)
        # L.tileLayer('http://{s}.tile.stamen.com/watercolor/{z}/{x}/{y}.png', {'noWrap': 'true'}).addTo(self.map)
        # L.tileLayer('https://stamen-tiles-{s}.a.ssl.fastly.net/toner/{z}/{x}/{y}.png').addTo(self.map)

        L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png').addTo(self.map)

        for _ in range(50):
            coo = self.generate_random_data(-21.227026, -44.9778903)
            self.marker = L.circleMarker(coo, {
                'color': "red",
                'opacity': 0.5,
                # 'fillOpacity': 0.9,
                # 'stroke': 1,
                # 'weight': 10,
                # 'lineCap': 'round',
                # 'fillColor': "lightgreen",
                # 'radius': 25,  # self._get_marker_radius(0)
            })

            self.marker.bindPopup('coo')
            self.map.addLayer(self.marker)

        self.marker = L.circleMarker([-21.227026, -44.9778903], {
            'color': '#a31286',
            'fillOpacity': 0.3,
            'stroke': 0,
            'weight': 3
        })

        self.map.clicked.connect(lambda x: print(x))

        self.map.addLayer(self.marker)

    def calc_distance(self, point_1, point_2, unit=Unit.METERS):
        return haversine(point_1, point_2, unit=unit)

    def _init_map(self):
        ERB_LOCATION = [-21.226244, -44.978407]
        m = folium.Map(
            location=ERB_LOCATION,
            zoom_start=16,
            control_scale=True
        )

        data = []

        for _ in range(1800):
            random_location = self.generate_random_data(ERB_LOCATION[0], ERB_LOCATION[1])
            distance = self.calc_distance(tuple(ERB_LOCATION), tuple(random_location))

            pr = cost231_path_loss(1820, 30, 1, distance, 2)

            random_location.append(18820 - pr)
            data.append(random_location)

        max_v = max([value[2] for value in data])
        min_v = min([value[2] for value in data])

        for d in data:
            color = get_color_of_interval(d[2], min_value=min_v, max_value=max_v)

            coordinate = [d[0], d[1]]

            folium.Circle(
                location=tuple(coordinate),
                radius=10,
                # popup=('PR => %.4f ' % (d[2])),
                # tooltip=('PR => %.4f ' % (d[2])),
                fill=True,
                color=str(color)
            ).add_to(m)

        folium.Marker(
            location=ERB_LOCATION,
            popup='Estação Rádio Base Vivo',
            draggable=False,
            icon=folium.Icon(prefix='glyphicon', icon='tower')
        ).add_to(m)

        # HeatMap(
        #     data=data_color,
        #     name='heatmap',
        #     min_opacity=0.5,
        #     max_zoom=18,
        #     min_val=min_v,
        #     max_val=max_v,
        #     radius=15,
        #     blur=15,
        #     gradient={0.4: 'blue', 0.65: 'lime', 1: 'red'},
        #     overlay=True,
        #     control=True,
        #     show=True
        # ).add_to(m)

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

    @pyqtSlot(name="on_menu_anatel_base_triggered")
    def on_menu_anatel_base_triggered(self):
        """
        This method is called when calculate button is clicked
        :return: None
        """
        anatel_dialog = AnatelDialogClass(self)
        anatel_dialog.setModal(True)
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
