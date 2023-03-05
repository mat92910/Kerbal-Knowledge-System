# This Python file uses the following encoding: utf-8
import sys
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QApplication, QMainWindow
from PyQt6 import QtWidgets, uic

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = uic.loadUi("KerbalKnowledgeSystem.ui")
    window.show()
    sys.exit(app.exec())
