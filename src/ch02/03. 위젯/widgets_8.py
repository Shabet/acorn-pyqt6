from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QSlider

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

        widget = QSlider()

        widget.setMinimum(-10)
        widget.setMaximum(3)

        widget.setSingleStep(3)

        widget.valueChanged.connect(self.value_changed)
        widget.sliderMoved.connect(self.slider_moved)
        widget.sliderPressed.connect(self.slider_pressed)
        widget.sliderReleased.connect(self.slider_released)

        self.setCentralWidget(widget)

    def value_changed(self, i):
        print(i)

    def slider_moved(self, i):
        print("Slider moved to", i)

    def slider_pressed(self):
        print("Slider pressed!")

    def slider_released(self):
        print("Slider released!")

window = MainWindow()
window.show()

app.exec()