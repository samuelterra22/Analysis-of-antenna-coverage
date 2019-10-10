import sys

from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow

from src.main.python.dialogs.about_dialog_class import AboutDialogClass
from src.main.python.dialogs.anatel_dialog_class import AnatelDialogClass
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
        self.menu_action_anatel_base.triggered.connect(self.on_menu_action_anatel_base_triggered)
        self.menu_action_about.triggered.connect(self.on_menu_about_triggered)
        self.menu_action_help.triggered.connect(self.on_menu_help_triggered)

    @pyqtSlot(name='on_button_calculate_clicked')
    def on_button_calculate_clicked(self):
        print("Calculate button!")

    @pyqtSlot(name='on_menu_action_anatel_base_triggered')
    def on_menu_action_anatel_base_triggered(self):
        dialog = AnatelDialogClass(self)
        dialog.setModal(True)
        dialog.show()

    @pyqtSlot(name='on_menu_about_triggered')
    def on_menu_about_triggered(self):
        dialog = AboutDialogClass(self)
        dialog.setModal(True)
        dialog.show()

    @pyqtSlot(name='on_menu_help_triggered')
    def on_menu_help_triggered(self):
        dialog = HelpDialogClass(self)
        dialog.setModal(True)
        dialog.show()

    @pyqtSlot(name='on_menu_exit_triggered')
    def on_menu_exit_triggered(self):
        sys.exit()
