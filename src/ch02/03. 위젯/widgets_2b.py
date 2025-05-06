from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel

import os
import sys

base_path = os.path.dirname(__file__)
print("Current working folder:", os.getcwd())
print("Paths are relative to:", base_path)

app = QApplication(sys.argv)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        widget = QLabel("Hello")
        widget.setPixmap(QPixmap(os.path.join(base_path, "otje.jpg")))
        widget.setScaledContents(True)

        self.setCentralWidget(widget)

window = MainWindow()
window.show()

app.exec()