#!/usr/bin/env python

import sys

from PyQt5 import uic
from fbs_runtime.application_context.PyQt5 import ApplicationContext

from src.main.python.windows.main_window import MainWindow

Ui_MainWindow, QtBaseClass = uic.loadUiType("./views/main_window.ui")


def main_window():
    ctx = ApplicationContext()
    window = MainWindow()
    window.show()
    sys.exit(ctx.app.exec_())


if __name__ == '__main__':
    main_window()
