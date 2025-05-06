from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

import sys
from random import choice

window_titles = [
    "My App",
    "My App",
    "Still My App",
    "Still My App",
    "Wnat on earth",
    "What on earth",
    "This is surprising",
    "This is surprising",
    "Something went wrong",
]

app = QApplication(sys.argv)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.button = QPushButton("Press Me!")
        self.button.clicked.connect(self.button_was_clicked)
        self.windowTitleChanged.connect(self.on_window_title_changed)

        self.setCentralWidget(self.button)

    def button_was_clicked(self):
        print("Clicked!")
        new_window_title = choice(window_titles)
        print("Setting title: %s" % new_window_title)
        self.setWindowTitle(new_window_title)
        
    def on_window_title_changed(self, window_title):
        print("Window title changed: %s" % window_title)

        if window_title == "Something went wrong":
            self.button.setDisabled(True)

window = MainWindow()
window.show()

app.exec()