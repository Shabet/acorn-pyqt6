from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QSpinBox

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

        widget = QSpinBox()
        widget.setMinimum(-10)
        widget.setMaximum(3)

        widget.setPrefix("$")
        widget.setSuffix(" €")
        widget.setSingleStep(3)

        widget.valueChanged.connect(self.value_changed)
        widget.textChanged.connect(self.text_changed)

        self.setCentralWidget(widget)

    def value_changed(self, i):
        print(i)

    def text_changed(self, s):
        print(s)

window = MainWindow()
window.show()

app.exec()