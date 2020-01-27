#!/usr/bin/env python

import sys

from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow

from src.main.python.dialogs.about_dialog_class import AboutDialogClass
from src.main.python.dialogs.anatel_dialog_class import AnatelDialogClass
from src.main.python.dialogs.settings_dialog_class import SettingsDialogClass
from src.main.python.dialogs.help_dialog_class import HelpDialogClass

Ui_MainWindow, QtBaseClass = uic.loadUiType("./views/main_window.ui")


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Calculate button
        self.button_calculate.clicked.connect(self.on_button_calculate_clicked)

        # Menus
        self.menu_action_exit.triggered.connect(self.on_menu_exit_triggered)
        self.menu_action_anatel_base.triggered.connect(self.on_menu_anatel_base_triggered)
        self.menu_action_settings.triggered.connect(self.on_menu_settings_triggered)
        self.menu_action_about.triggered.connect(self.on_menu_about_triggered)
        self.menu_action_help.triggered.connect(self.on_menu_help_triggered)

    @pyqtSlot(name='on_button_calculate_clicked')
    def on_button_calculate_clicked(self):
        print("Calculate button!")

    @pyqtSlot(name='on_menu_action_anatel_base_triggered')
    def on_menu_anatel_base_triggered(self):
        anatel_dialog = AnatelDialogClass(self)
        anatel_dialog.setModal(True)
        anatel_dialog.show()

    @pyqtSlot(name='on_menu_action_settings_triggered')
    def on_menu_settings_triggered(self):
        settings_dialog = SettingsDialogClass(self)
        settings_dialog.setModal(True)
        settings_dialog.show()

    @pyqtSlot(name='on_menu_about_triggered')
    def on_menu_about_triggered(self):
        about_dialog = AboutDialogClass(self)
        about_dialog.setModal(True)
        about_dialog.show()

    @pyqtSlot(name='on_menu_help_triggered')
    def on_menu_help_triggered(self):
        help_dialog = HelpDialogClass(self)
        help_dialog.setModal(True)
        help_dialog.show()

    @pyqtSlot(name='on_menu_exit_triggered')
    def on_menu_exit_triggered(self):
        sys.exit()
