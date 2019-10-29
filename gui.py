#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QFileDialog, QApplication, QWidget, QGridLayout, QLabel
from PyQt5.QtWidgets import QLineEdit, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from validator import Validator

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.textToValidation = ''
        self.brackets = ''
        self.bracketsLabel = QLabel('Input brackets for validation:', self)
        self.textLabel = QLabel('Input text or open file:', self)
        self.inputBracketsLineEdit = QLineEdit()
        self.inputTextEdit = QTextEdit()
        self.validateButton = QPushButton('Validate text')
        self.initUI()

    def initUI(self):

        exitAction = QAction(QIcon('resources/exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        openAction = QAction(QIcon('resources/open.png'), 'Open file', self)
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open file for validation')
        openAction.triggered.connect(self.OpenFile)

        howToUseAction = QAction(QIcon('resources/how_to.png'), 'How to use', self)
        howToUseAction.setStatusTip('How to use validator')
        howToUseAction.triggered.connect(self.InfoWindow)

        self.validateButton.clicked.connect(self.validate_text)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openAction)
        fileMenu.addAction(exitAction)

        aboutMenu = menubar.addMenu('&About')
        aboutMenu.addAction(howToUseAction)

        w = QWidget()
        grid = QGridLayout(w)
        grid.setSpacing(5)
        grid.addWidget(self.bracketsLabel, 1, 0)
        grid.addWidget(self.inputBracketsLineEdit, 2, 0)
        grid.addWidget(self.textLabel, 3, 0)
        grid.addWidget(self.inputTextEdit, 4, 0)
        grid.addWidget(self.validateButton, 5, 0)
        w.setLayout(grid)
        self.setCentralWidget(w)

        #self.setGeometry(300, 300, 300, 450)
        self.setFixedSize(300, 450)
        self.setWindowTitle('GUI Validator')
        self.show()

    def InfoWindow(self):
            QMessageBox.information(self, 'How to use', 'For using this validator you should do:\n'
                                                        '1) Input brackets to validation, without spaces, punctuation marks etc.\n'
                                                        'For example: "()[]{}"\n'
                                                        '2) Write text into textfield or open text file\n'
                                                        '3) Press "Validate text" button')

    def OpenFile(self):
        fileName = QFileDialog.getOpenFileName(self, 'Open file', '')
        file = open(fileName[0], 'r')
        with file:        
            data = file.read()
            self.inputTextEdit.setText(data)

    def validate_text(self):
        brackets = self.inputBracketsLineEdit.text()
        if len(brackets) % 2 != 0 or brackets == '':
            QMessageBox.warning(self, 'Alarm', 'Incorrect number of brackets')

        validator = Validator(brackets)
        self.inputTextEdit.setText(validator.validate(self.inputTextEdit.toPlainText()))


