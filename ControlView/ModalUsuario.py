from PyQt6.QtWidgets import QApplication,QMainWindow,QToolTip,QDialog,QLineEdit
from PyQt6.QtSvg import QSvgRenderer
from PyQt6.QtGui import QFont,QIcon,QPixmap,QPainter,QColor
from PyQt6.QtCore import QSize
from view.ModalUsuario import Ui_Dialog
from Clases.ComunicacionApi import ComunicacionApi
import Clases.Utils as utils
import Clases.UtilsMessage as messages
import os,re

class ModalUsuario(QDialog):
    def __init__(self):
        super().__init__()
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
        self.configuracion_inical()
        self.ui.combTipoUser.addItems([p['nombre'] for p in utils.LIST_TIPO])
        self.ui.combUsoApp.addItems([p['nombre'] for p in utils.LIST_USO_APP])
        self.ui.btnSalir.clicked.connect(self.cerrarDialogo)
        self.ui.btnViewPass.clicked.connect(self.mostrarPassword)
        self.ui.btnGuardar.clicked.connect(self.guardarUsuario)
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
    def configuracion_inical(self):
        self.ui.linePassword.setEchoMode(QLineEdit.EchoMode.Password)
        self.ui.linePasswordR.setEchoMode(QLineEdit.EchoMode.Password)
        self.ui.btnGuardar.setToolTip('Guardar Datos usuarios')
        self.ui.btnGuardar.setIcon(self.svg_coloreado("floppy-disk.svg","#8AFF72",QSize(40,40)))
        self.ui.btnSalir.setToolTip('Salir del registro')
        self.ui.btnSalir.setIcon(self.svg_coloreado("circle-xmark.svg","#D37575",QSize(40,40)))
        self.ui.btnViewPass.setToolTip("Ver contraseña")
        self.ui.btnViewPass.setIcon(self.svg_coloreado("eye.svg","#000000",QSize(40,40)))
    def cerrarDialogo(self):
        self.reject()
    def mostrarPassword(self):
        tipo = self.ui.linePassword.echoMode()
        if tipo == QLineEdit.EchoMode.Password:
            self.ui.btnViewPass.setIcon(self.svg_coloreado("eye-slash.svg","#000000",QSize(40,40)))
            self.ui.linePassword.setEchoMode(QLineEdit.EchoMode.Normal)
            self.ui.linePasswordR.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.ui.btnViewPass.setIcon(self.svg_coloreado("eye.svg","#000000",QSize(40,40)))
            self.ui.linePassword.setEchoMode(QLineEdit.EchoMode.Password)
            self.ui.linePasswordR.setEchoMode(QLineEdit.EchoMode.Password)
    
    def guardarUsuario(self):
        nombreUser = self.ui.lineNameUser.text()
        correo = self.ui.lineEmail.text()
        password = self.ui.linePassword.text()
        repassword = self.ui.linePasswordR.text()
        if password == repassword:
            if utils.es_correo_valido(correo):
                tipoApp = self.ui.combUsoApp.currentIndex()
                tipoUser = self.ui.combTipoUser.currentIndex()
                if tipoApp!=0 and tipoUser!=0:
                    datos = {
                        'nombre':nombreUser,
                        'correo':correo,
                        'contrasenia':password,
                        'tipo': tipoUser,
                        'app': tipoApp
                    }
                    print("empezando a registrar")
                    result = self.api.NuevoUsuario(datos)
                    if 'ok' in result:
                        print("registro correto")
                        messages.mostrar_toast_correcto(self,"Registro correcto")
                    else:
                        print(result['error'])
                else:
                    if tipoApp==0:
                        messages.mostrar_toast_error(self,"No eligio tipo de aplicacion")
                    if tipoUser==0:
                        messages.mostrar_toast_error(self,"No elegiste el tipo de usuario")
                    print("no eligio tipo usuario")
            else:
                messages.mostrar_toast_error(self,"El correo no es valido")
                print("correo no valido")
        else:
            messages.mostrar_toast_error(self,"Las Contraseñas no son iguales")
            print("Las contraseñas no son iguales")