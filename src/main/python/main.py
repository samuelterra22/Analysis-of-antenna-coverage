#!/usr/bin/env python

import sys

from fbs_runtime.application_context.PyQt5 import ApplicationContext

from src.main.python.windows.main_window import MainWindow


def main_window():
    ctx = ApplicationContext()
    window = MainWindow()
    window.show()
    sys.exit(ctx.app.exec_())


if __name__ == "__main__":
    main_window()
