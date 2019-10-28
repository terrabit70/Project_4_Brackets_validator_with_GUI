#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication
from gui import Window

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = Window()
    sys.exit(app.exec_()) 
