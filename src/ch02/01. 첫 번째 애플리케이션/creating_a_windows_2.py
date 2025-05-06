from PyQt6.QtWidgets import QApplication, QPushButton

import sys

app = QApplication(sys.argv)

window = QPushButton("Click me")
window.show()

app.exec()

