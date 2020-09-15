#!/usr/bin/env python

import sys

from fbs_runtime.application_context.PyQt5 import ApplicationContext

from support.database import create_tables
from windows.main_window import MainWindow


def main_window():
    """
    This method load main window and load application context
    :return: None
    """
    ctx = ApplicationContext()
    window = MainWindow()
    window.show()
    sys.exit(ctx.app.exec_())


if __name__ == "__main__":
    """
    Main method, the application start in this code point.
    This method creates all database tables and open main window
    """
    create_tables()
    main_window()
