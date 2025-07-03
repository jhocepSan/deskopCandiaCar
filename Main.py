from PyQt6.QtWidgets import QApplication,QMainWindow,QToolTip,QDialog,QTableWidgetItem,QPushButton
from PyQt6.QtSvg import QSvgRenderer
from PyQt6.QtGui import QFont,QIcon,QPixmap,QPainter,QColor
from PyQt6.QtCore import QSize
from view.MainVentana import Ui_MainWindow
from ControlView.ModalRegistro import ModalRegistro
from ControlView.ModalUsuario import ModalUsuario
from ControlView.ModalLogin import ModalLogin
from functools import partial
import Clases.services.cliente as clienteapi
import Clases.services.usuario as usuarioapi
import Clases.Utils as utils
import Clases.UtilsMessage as msgUtils
import os
from Clases.enums import Color, IconSize
from enum import Enum
class Vista(Enum):
    USUARIO = 1
    CLIENTE = 3
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.SVG_BASE = utils.SVG_BASE
        self.ui = Ui_MainWindow()
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
        QToolTip.setFont(QFont('Arial', 10))
        self.agregarTooltips()
        self.ui.btnMenu.clicked.connect(self.toggleMenu)
        self.ui.btnClientes.clicked.connect(lambda:self.mostrarVista(3))
        self.ui.btnConfig.clicked.connect(lambda:self.mostrarVista(2))
        self.ui.btnServicios.clicked.connect(lambda:self.mostrarVista(0))
        self.ui.btnUsuarios.clicked.connect(lambda:self.mostrarVista(1))
        self.ui.btn_add.clicked.connect(self.show_registerModal)
        self.ui.btn_refrescar.clicked.connect(self.refresh_view)
        
        self.testLogin()
    def agregarTooltips(self):
        self.ui.btnMenu.setToolTip('Menu')
        self.ui.btnMenu.setIcon(utils.get_icon("list", Color.RED_DARK))
        self.ui.btnClientes.setToolTip('Clientes')
        self.ui.btnClientes.setIcon(utils.get_icon("people-group", Color.RED_DARK))
        self.ui.btnConfig.setToolTip('Configuraciones')
        self.ui.btnConfig.setIcon(utils.get_icon("screwdriver-wrench", Color.RED_DARK))
        self.ui.btnUsuarios.setToolTip('Usuarios')
        self.ui.btnUsuarios.setIcon(utils.get_icon("user-gear", Color.RED_DARK))
        self.ui.btnServicios.setToolTip('Servicios')
        self.ui.btnServicios.setIcon(utils.get_icon("arrows-turn-to-dots", Color.RED_DARK))
        self.ui.btn_refrescar.setIcon(utils.get_icon("arrows-spin", Color.BLUE))
        self.ui.bSearchClient.setToolTip('Buscar Cliente')
        self.ui.bSearchClient.setIcon(utils.get_icon("magnifying-glass"))
        self.ui.expoCliPdf.setToolTip('Exportar Lista de Clientes PDF')
        self.ui.expoCliPdf.setIcon(utils.get_icon("file-pdf", Color.RED))
        self.ui.exExcCli.setToolTip('Exportar Lista de Clientes Excel')
        self.ui.exExcCli.setIcon(utils.get_icon("file-excel", Color.GREEN))
        self.ui.btn_add.setIcon(utils.get_icon("user-plus", Color.GREEN))

    def toggleMenu(self):
        tamanio = self.ui.SideBar.minimumWidth()
        if tamanio!=50:
            self.ui.SideBar.setMinimumWidth(50)
            self.ui.label.setVisible(False)
            self.ui.btnMenu.setText('')
            self.ui.btnClientes.setText('')
            self.ui.btnConfig.setText('')
            self.ui.btnServicios.setText('')
            self.ui.btnUsuarios.setText('')
        else:
            self.ui.SideBar.setMinimumWidth(200)
            self.ui.label.setVisible(True)
            self.ui.btnMenu.setText('Menu')
            self.ui.btnClientes.setText('CLIENTES')
            self.ui.btnConfig.setText('CONFIG...')
            self.ui.btnServicios.setText('SERVICIOS')
            self.ui.btnUsuarios.setText('USUARIOS')
    def mostrarVista(self,val):
        self.ui.stackedWidget.setCurrentIndex(val)
        if val == Vista.USUARIO.value:
            self.cargarUsarios()
            self.ui.bSearchClient.setToolTip("Buscar usuario")
            self.ui.btn_refrescar.setToolTip('Refrescar lista usuarios')
            self.ui.btn_add.setToolTip("Crear nuevo usuario")
        elif val == Vista.CLIENTE.value:
            self.cargarClientes()
            self.ui.bSearchClient.setToolTip('Buscar cliente')
            self.ui.btn_refrescar.setToolTip('Refrescar lista clientes')
            self.ui.btn_add.setToolTip("Crear nuevo cliente")
        else:
            pass

    def refresh_view(self):
        if self.ui.stackedWidget.currentIndex() == Vista.USUARIO.value:
            self.cargarUsarios()
        elif self.ui.stackedWidget.currentIndex() == Vista.CLIENTE.value:
            self.cargarClientes()
        else:
            pass

    def cargarClientes(self):
        result = clienteapi.ObtenerClientes()
        if result.data:
            self.ui.listaClientes.clear()
            self.ui.listaClientes.setRowCount(len(result.data['ok']))
            self.ui.listaClientes.setColumnCount(11)
            self.ui.listaClientes.setHorizontalHeaderLabels(['ID','CODIGO',"NOMBRES","APELLIDOS","DIRECCION","TELEFONO",'AP PERMISO',"","",""])
            for row,cliente in enumerate(result.data['ok']):
                self.ui.listaClientes.setItem(row,0,QTableWidgetItem(str(cliente['idpersona'])))
                self.ui.listaClientes.setItem(row,1,QTableWidgetItem(cliente['codigo']))
                self.ui.listaClientes.setItem(row,2,QTableWidgetItem(cliente['nombres']))
                self.ui.listaClientes.setItem(row,3,QTableWidgetItem(cliente['apellidos']))
                self.ui.listaClientes.setItem(row,4,QTableWidgetItem(cliente['direccion']))
                self.ui.listaClientes.setItem(row,5,QTableWidgetItem(str(cliente['telefono'])))
        print(result)

    def cargarUsarios(self):
        result = usuarioapi.ObtenerUsuarios()
        if result.data:
            self.ui.tableWidget.clear()
            self.ui.tableWidget.setRowCount(len(result.data['ok']))
            self.ui.tableWidget.setColumnCount(9)
            self.ui.tableWidget.setHorizontalHeaderLabels(['ID',"NOMBRE USUARIO","CORREO","TIPO USARIO","ESTADO",'AP PERMISO',"","",""])
            for row,user in enumerate(result.data['ok']):
                boton = QPushButton("Ver")
                boton.setIcon(utils.get_icon("eye"))
                boton.setStyleSheet("""QPushButton{
                    border-radius: 12px;
                    color:rgb(255, 255, 255);
                    font-weight: bold;
                    background-color:rgb(186, 186, 186);
                    padding: 7px 7px;
                    text-align: center;
                    text-decoration: none;
                    font-size: 16px;
                    }
                    QPushButton:hover{
                    font-weight: bold;
                    background-color: #04AA6D; /* Green */
                    color: white;
                    }""")
                boton.clicked.connect(partial(self.verDetalle,user))
                boton.setToolTip("Ver detalles Usuario")
                botoneliminar = QPushButton('')
                botoneliminar.setIcon(utils.get_icon("trash-can",Color.RED))
                botoneliminar.setStyleSheet("""QPushButton{
                    border-radius: 12px;
                    color:rgb(255, 255, 255);
                    font-weight: bold;
                    background-color:rgb(186, 186, 186);
                    padding: 7px 7px;
                    text-align: center;
                    text-decoration: none;
                    font-size: 16px;
                    }
                    QPushButton:hover{
                    font-weight: bold;
                    background-color: #04AA6D; /* Green */
                    color: white;
                    }""")
                botoneliminar.setToolTip("Eliminar Usuario")
                botoninactivar = QPushButton('')
                botoninactivar.setIcon(utils.get_icon("user-slash"))
                botoninactivar.setStyleSheet("""QPushButton{
                    border-radius: 12px;
                    color:rgb(255, 255, 255);
                    font-weight: bold;
                    background-color:rgb(186, 186, 186);
                    padding: 7px 7px;
                    text-align: center;
                    text-decoration: none;
                    font-size: 16px;
                    }
                    QPushButton:hover{
                    font-weight: bold;
                    background-color: #04AA6D; /* Green */
                    color: white;
                    }""")
                botoninactivar.setToolTip("Inactivar Usuario del sistema")
                botoninactivar.clicked.connect(partial(self.editarEstadoUser,user,'I'))
                botoneliminar.clicked.connect(partial(self.editarEstadoUser,user,'E'))
                self.ui.tableWidget.setItem(row,0,QTableWidgetItem(str(user['id'])))
                self.ui.tableWidget.setItem(row,1,QTableWidgetItem(user['nombre']))
                self.ui.tableWidget.setItem(row,2,QTableWidgetItem(user['correo']))
                self.ui.tableWidget.setItem(row,3,QTableWidgetItem(user['nametipo']))
                self.ui.tableWidget.setItem(row,4,QTableWidgetItem(user['nameestado']))
                self.ui.tableWidget.setItem(row,5,QTableWidgetItem(user['nameapp']))
                self.ui.tableWidget.setCellWidget(row,6,boton)
                self.ui.tableWidget.setCellWidget(row,7,botoninactivar)
                self.ui.tableWidget.setCellWidget(row,8,botoneliminar)
        else:
            msgUtils.mostrar_toast_error(self,"Error: "+str(result.error))

    def show_registerModal(self):
        if self.ui.stackedWidget.currentIndex() == Vista.USUARIO.value:
            dialog  = ModalUsuario()
            result = dialog.exec()
            if result == QDialog.DialogCode.Accepted:
                print("creado usuario")
                self.cargarUsarios()
        elif self.ui.stackedWidget.currentIndex() == Vista.CLIENTE.value:
            dialog = ModalRegistro()
            dialog.exec()
        else:
            pass

    def editarEstadoUser(self,dato,estado):
        result = usuarioapi.CambiarEstadoUser({'id':dato['id'],'estado':estado})
        print(result)
        if result.data:
            msgUtils.mostrar_toast_correcto(self,result.data['ok'])
            self.cargarUsarios()
        else:
            msgUtils.mostrar_toast_error(self,"Error: "+str(result.error))
    def testLogin(self):
        session = utils.test_session_user()
        print(session)
    def verDetalle(self,dato):
        dialog = ModalUsuario(dato)
        result = dialog.exec()
        if result == QDialog.DialogCode.Accepted:
            self.cargarUsarios()


                

if __name__ == "__main__":
    app = QApplication([])
    login = ModalLogin()
    if login.exec() == QDialog.DialogCode.Accepted:
        ventana = MainWindow()
        ventana.show()
        app.exec()
    else:
        print("Login cancelado")