from PyQt6.QtWidgets import QApplication,QMainWindow,QToolTip,QDialog,QLineEdit
from PyQt6.QtSvg import QSvgRenderer
from PyQt6.QtGui import QFont,QIcon,QPixmap,QPainter,QColor
from PyQt6.QtCore import QSize
from view.ModalLogin import Ui_Dialog
from Clases.services.auth import IniciarSesion
from Clases.enums import Color, IconSize
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
        #self.ui.lineEmail.setText("jjchsan")
        #self.ui.linePassword.setText("Sajhy##")
        self.configuracion_inicial()
        self.ui.btnSalir.clicked.connect(self.cerrarDialogo)
        self.ui.btnEntrar.clicked.connect(self.checkLogin)
    def configuracion_inicial(self):
        self.ui.btnEntrar.setToolTip('Iniciar Ingreso al Sistema')
        self.ui.btnEntrar.setIcon(utils.get_icon("right-to-bracket", Color.OK))
        self.ui.btnSalir.setToolTip('Salir del registro')
        self.ui.btnSalir.setIcon(utils.get_icon("circle-xmark", Color.CANCEL))
        self.ui.linePassword.setEchoMode(QLineEdit.EchoMode.Password)
    def cerrarDialogo(self):
        self.reject()
    def checkLogin(self):
        correo = self.ui.lineEmail.text()
        password = self.ui.linePassword.text()
        if correo!='' and password!='':
            result = IniciarSesion({'usuario':correo,'contrasena':password})
            if result.data:
                self.ui.frameMsg.setStyleSheet("background-color: #84fc93; border-radius: 10px;color:#000000")  
                self.ui.textMsg.setText("Inicio de Sesion Correcto...") 
                utils.save_session_user({'usuario':result.data['ok']})
                info = utils.get_data_token({'usuario':result.data['ok']})
                print(info)
                if info['app']=='D' or info['app']=='T':
                    self.accept() 
                else:
                    self.ui.frameMsg.setStyleSheet("background-color: #fc8484; border-radius: 10px;")
                    self.ui.textMsg.setText("Consulte sus permisos a jjchsan@gmail.com")
            else:
                self.ui.frameMsg.setStyleSheet("background-color: #fc8484; border-radius: 10px;")    
                self.ui.textMsg.setText("Error: "+result['detail'])
        else:
            self.ui.frameMsg.setStyleSheet("background-color: #fc8484; border-radius: 10px;")
            if correo=='':
                self.ui.textMsg.setText("Ingrese su correo Electrónico, para entrar al sistema")
            else:
                self.ui.textMsg.setText("Ingrese su contraseña, para entrar al sistema")