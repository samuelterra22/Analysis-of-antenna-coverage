#!/usr/bin/env python

import sys

from PyQt5 import uic
from pyqtlet import L, MapWidget
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow

from src.main.python.dialogs.about_dialog_class import AboutDialogClass
from src.main.python.dialogs.anatel_dialog_class import AnatelDialogClass
from src.main.python.dialogs.settings_dialog_class import SettingsDialogClass
from src.main.python.dialogs.help_dialog_class import HelpDialogClass

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
        QMainWindow.__init__(self, parent)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.init_coverage_map()
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

    def init_coverage_map(self):
        self.coverage_map_widget = MapWidget()
        self.vertical_layout_coverage_map.addWidget(self.coverage_map_widget)

        # Working with the maps with pyqtlet
        self.coverage_map = L.map(self.coverage_map_widget)
        self.coverage_map.setView([-21.2284575, -44.9753476], 16)
        L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png').addTo(self.coverage_map)

        self.coverage_marker = L.marker([-21.2284575, -44.9753476])
        self.coverage_marker.bindPopup('Maps are a treasure.')
        self.coverage_map.addLayer(self.coverage_marker)

        self.coverage_marker = L.circleMarker([-21.227026, -44.9778903], {
            'color': '#a31286',
            'fillOpacity': 0.3,
            'stroke': 0,
            'weight': 3
        })
        self.coverage_map.addLayer(self.coverage_marker)

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
