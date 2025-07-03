from PyQt6.QtWidgets import QApplication,QMainWindow,QToolTip,QDialog,QLineEdit
from PyQt6.QtSvg import QSvgRenderer
from PyQt6.QtGui import QFont,QIcon,QPixmap,QPainter,QColor
from PyQt6.QtCore import QSize
from view.ModalUsuario import Ui_Dialog
import Clases.Utils as utils
import Clases.UtilsMessage as messages
from Clases.enums import Color
import os,re
import Clases.services.usuario as apiservice

class ModalUsuario(QDialog):
    def __init__(self,info=None):
        super().__init__()
        self.info_user=info
        self.is_edit=False
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
        self.configuracion_inical()
        self.ui.combTipoUser.addItems([p['nombre'] for p in utils.LIST_TIPO])
        self.ui.combUsoApp.addItems([p['nombre'] for p in utils.LIST_USO_APP])
        self.ui.btnSalir.clicked.connect(self.cerrarDialogo)
        self.ui.btnViewPass.clicked.connect(self.mostrarPassword)
        self.ui.btnGuardar.clicked.connect(self.guardarUsuario)
        self.cargarDatos()
    def configuracion_inical(self):
        self.ui.linePassword.setEchoMode(QLineEdit.EchoMode.Password)
        self.ui.linePasswordR.setEchoMode(QLineEdit.EchoMode.Password)
        self.ui.btnGuardar.setToolTip('Guardar Datos usuarios')
        self.ui.btnGuardar.setIcon(utils.get_icon("floppy-disk", Color.OK))
        self.ui.btnSalir.setToolTip('Salir del registro')
        self.ui.btnSalir.setIcon(utils.get_icon("circle-xmark", Color.CANCEL))
        self.ui.btnViewPass.setToolTip("Ver contraseña")
        self.ui.btnViewPass.setIcon(utils.get_icon("eye", Color.BLACK))
    def cerrarDialogo(self):
        self.reject()
    def mostrarPassword(self):
        tipo = self.ui.linePassword.echoMode()
        if tipo == QLineEdit.EchoMode.Password:
            self.ui.btnViewPass.setIcon(utils.get_icon("eye-slash", Color.BLACK))
            self.ui.linePassword.setEchoMode(QLineEdit.EchoMode.Normal)
            self.ui.linePasswordR.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.ui.btnViewPass.setIcon(utils.get_icon("eye", Color.BLACK))
            self.ui.linePassword.setEchoMode(QLineEdit.EchoMode.Password)
            self.ui.linePasswordR.setEchoMode(QLineEdit.EchoMode.Password)
    def cargarDatos(self):
        if self.info_user is not None:
            self.is_edit=True
            self.ui.frame_6.setVisible(False)
            self.ui.frame_8.setVisible(False)
            self.ui.lineEmail.setText(self.info_user['correo'])
            self.ui.lineNameUser.setText(self.info_user['nombre'])
            self.ui.combTipoUser.setCurrentIndex(next((item['id'] for item in utils.LIST_TIPO if item['tipo'] == self.info_user['tipo']), 0))
            self.ui.combUsoApp.setCurrentIndex(next((item['id'] for item in utils.LIST_USO_APP if item['tipo']==self.info_user['app']),0))
    def guardarUsuario(self):
        nombreUser = self.ui.lineNameUser.text()
        correo = self.ui.lineEmail.text()
        password = self.ui.linePassword.text()
        repassword = self.ui.linePasswordR.text()
        if (password == repassword and password!='' and repassword!='') or self.is_edit==True:
            if utils.es_correo_valido(correo):
                tipoApp = self.ui.combUsoApp.currentIndex()
                tipoUser = self.ui.combTipoUser.currentIndex()
                if tipoApp!=0 and tipoUser!=0:
                    if self.is_edit == False:
                        datos = {
                            'nombre':nombreUser,
                            'correo':correo,
                            'contrasenia':password,
                            'tipo':next((item['tipo'] for item in utils.LIST_TIPO if item['id'] == tipoUser), 'X'),
                            'app':next((item['tipo'] for item in utils.LIST_USO_APP if item['id'] == tipoApp), 'X')
                        }
                        print(datos)
                        result = apiservice.NuevoUsuario(datos)
                        print(result)
                        if result.data:
                            print("registro correto")
                            messages.mostrar_toast_correcto(self,"Registro correcto")
                            self.accept()
                        else:
                            messages.mostrar_toast_error(self,result.error)
                    else:
                        datos = {
                            'id':self.info_user['id'],
                            'nombre':nombreUser,
                            'correo':correo,
                            'tipo':next((item['tipo'] for item in utils.LIST_TIPO if item['id'] == tipoUser), 'X'),
                            'app':next((item['tipo'] for item in utils.LIST_USO_APP if item['id'] == tipoApp), 'X')
                        }
                        print(datos)
                        result = apiservice.ActualizarUsuario(datos)
                        print(result)
                        if result.data:
                            messages.mostrar_toast_correcto(self,"Datos del Usuario Actualizado")
                            self.accept()
                        else:
                            messages.mostrar_toast_error(self,result.error)
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