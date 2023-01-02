import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window title
        self.setWindowTitle("Interface Application")

        # Set the window size
        self.setGeometry(100, 100, 400, 400)

        # Prevent the user from resizing the window
        self.setFixedSize(self.size())

        # Set the window to be in kiosk mode
        self.setWindowState(Qt.WindowFullScreen)

        # Create the central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create the layout for the central widget
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Load the four images
        image_1 = QPixmap("image1.png")
        image_2 = QPixmap("image2.png")
        image_3 = QPixmap("image3.png")

