from PyQt6.QtWidgets import QApplication, QMainWindow, QListWidget

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

        widget = QListWidget()
        widget.addItems(["One", "Two", "Three"])

        widget.currentItemChanged.connect(self.index_changed)
        widget.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(widget)

    def index_changed(self, i):
        print(i.text())

    def text_changed(self, s):
        print(s)

window = MainWindow()
window.show()

app.exec()