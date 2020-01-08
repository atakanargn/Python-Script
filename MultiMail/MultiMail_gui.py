#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QPlainTextEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'MultiMail'
        self.left = 128
        self.top = 128
        self.width = 640
        self.height = 480
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Butonlar
        self.btnGonder = QPushButton('Gönder', self)
        self.btnGonder.move(8,8)
        self.btnGonder.resize(128,24)

        self.btnBilgi = QPushButton('Bilgi', self)
        self.btnBilgi.move(8,8+32)
        self.btnBilgi.resize(128,24)

        self.btnCikis = QPushButton('Çıkış', self)
        self.btnCikis.move(8,8+64)
        self.btnCikis.resize(128,24)

        # Textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(8+128+8, 8)
        self.textbox.resize(256,24)
        self.textbox.setText("Excel file path")

        self.txtBody = QPlainTextEdit(self)
        self.txtBody.move(8+128+8, 8+32)
        self.txtBody.resize(256,196)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())