from PyQt6.QtWidgets import QApplication,QMainWindow,QToolTip,QDialog
from PyQt6.QtSvg import QSvgRenderer
from PyQt6.QtGui import QFont,QIcon,QPixmap,QPainter,QColor
from PyQt6.QtCore import QSize
from view.ModalUsuario import Ui_Dialog
import os

class ModalUsuario(QDialog):
    def __init__(self):
        super().__init__()
        self.SVG_BASE = "./public/fontawesome-free-6.7.2-desktop/svgs/solid/"
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setStyleSheet("""
            QToolTip {
                background-color: #333;
                color: white;
                border: 1px solid white;
                padding: 4px;
                border-radius: 4px;
            }
        """)
    