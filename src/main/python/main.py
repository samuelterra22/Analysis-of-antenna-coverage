from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QMainWindow
from fbs_runtime.application_context.PyQt5 import ApplicationContext

import sys

AnatelQDialog = uic.loadUiType("./views/anatel_dialog.ui")[0]
AboutQDialog = uic.loadUiType("./views/about_dialog.ui")[0]
HelpQDialog = uic.loadUiType("./views/help_dialog.ui")[0]

Ui_MainWindow, QtBaseClass = uic.loadUiType("./views/main_window.ui")


class AboutDialogClass(QDialog, AboutQDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)


class HelpDialogClass(QDialog, HelpQDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)


class AnatelDialogClass(QDialog, AnatelQDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)


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


    @pyqtSlot()
    def on_button_calculate_clicked(self):
        print("Calculate button!")

    @pyqtSlot()
    def on_menu_action_anatel_base_triggered(self):
        dialog = AnatelDialogClass(self)
        dialog.setModal(True)
        dialog.show()

    @pyqtSlot()
    def on_menu_about_triggered(self):
        dialog = AboutDialogClass(self)
        dialog.setModal(True)
        dialog.show()

    @pyqtSlot()
    def on_menu_help_triggered(self):
        dialog = HelpDialogClass(self)
        dialog.setModal(True)
        dialog.show()

    @pyqtSlot()
    def on_menu_exit_triggered(self):
        sys.exit()


def main_window():
    ctx = ApplicationContext()
    window = MainWindow()
    window.show()
    sys.exit(ctx.app.exec_())


if __name__ == '__main__':
    main_window()
