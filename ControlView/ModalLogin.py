from PyQt6.QtWidgets import QApplication,QMainWindow,QToolTip,QDialog,QLineEdit
from PyQt6.QtSvg import QSvgRenderer
from PyQt6.QtGui import QFont,QIcon,QPixmap,QPainter,QColor
from PyQt6.QtCore import QSize
from view.ModalLogin import Ui_Dialog
from Clases.ComunicacionApi import ComunicacionApi
import Clases.Utils as utils
import Clases.UtilsMessage as messages
import os,re

class ModalLogin(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.SVG_BASE = utils.SVG_BASE
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
        self.api = ComunicacionApi()
        self.configuracion_inicial()
        self.ui.btnSalir.clicked.connect(self.cerrarDialogo)
    def svg_coloreado(self,filename, color_hex, size=QSize(32, 32)):
        full_path = os.path.join(self.SVG_BASE, filename)
        renderer = QSvgRenderer(full_path)
        pixmap = QPixmap(size)
        pixmap.fill(QColor("transparent"))
        painter = QPainter(pixmap)
        renderer.render(painter)
        painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceIn)
        painter.fillRect(pixmap.rect(), QColor(color_hex))
        painter.end()
        return QIcon(pixmap)
    def configuracion_inicial(self):
        self.ui.btnEntrar.setToolTip('Iniciar Ingreso al Sistema')
        self.ui.btnEntrar.setIcon(self.svg_coloreado("right-to-bracket.svg","#8AFF72",QSize(40,40)))
        self.ui.btnSalir.setToolTip('Salir del registro')
        self.ui.btnSalir.setIcon(self.svg_coloreado("circle-xmark.svg","#D37575",QSize(40,40)))
    def cerrarDialogo(self):
        self.reject()
