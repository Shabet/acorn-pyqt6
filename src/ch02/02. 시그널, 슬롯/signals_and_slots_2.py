from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

import sys

app = QApplication(sys.argv)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.button = QPushButton("Press Me!")
        self.button.clicked.connect(self.button_was_clicked)

        self.setCentralWidget(self.button)

    def button_was_clicked(self):
        self.button.setText("You already clicked me.")
        self.button.setEnabled(False)

window = MainWindow()
window.show()

app.exec()