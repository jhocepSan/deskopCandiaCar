from PyQt6.QtWidgets import QApplication,QMainWindow,QToolTip,QDialog,QTableWidgetItem,QPushButton
from PyQt6.QtSvg import QSvgRenderer
from PyQt6.QtGui import QFont,QIcon,QPixmap,QPainter,QColor
from PyQt6.QtCore import QSize
from view.MainVentana import Ui_MainWindow
from ControlView.ModalRegistro import ModalRegistro
from ControlView.ModalUsuario import ModalUsuario
from ControlView.ModalLogin import ModalLogin
from functools import partial
import Clases.ComunicacionApi as ComunicacionApi
import Clases.Utils as utils
import Clases.UtilsMessage as msgUtils
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.SVG_BASE = utils.SVG_BASE
        self.api = ComunicacionApi.ComunicacionApi()
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
        self.ui.btnLoadClient.clicked.connect(self.cargarClientes)
        self.ui.btnAddClient.clicked.connect(self.mostrarModalRegistro)
        self.ui.btnNuevoUser.clicked.connect(self.mostrarModalUsuario)
        self.testLogin()
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
    def agregarTooltips(self):
        self.ui.btnMenu.setToolTip('Menu')
        self.ui.btnMenu.setIcon(self.svg_coloreado("list.svg","#220049",QSize(40,40)))
        self.ui.btnClientes.setToolTip('Clientes')
        self.ui.btnClientes.setIcon(self.svg_coloreado("people-group.svg","#5A0000",QSize(50,50)))
        self.ui.btnConfig.setToolTip('Configuraciones')
        self.ui.btnConfig.setIcon(self.svg_coloreado("screwdriver-wrench.svg","#5A0000",QSize(50,50)))
        self.ui.btnUsuarios.setToolTip('Usuarios')
        self.ui.btnUsuarios.setIcon(self.svg_coloreado("user-gear.svg","#5A0000",QSize(50,50)))
        self.ui.btnServicios.setToolTip('Servicios')
        self.ui.btnServicios.setIcon(self.svg_coloreado("arrows-turn-to-dots.svg","#5A0000",QSize(50,50)))
        self.ui.btnAddClient.setToolTip('Agregar Cliente')
        self.ui.btnAddClient.setIcon(self.svg_coloreado("user-plus.svg","#0F300E",QSize(50,50)))
        self.ui.btnLoadClient.setToolTip('Refrescar lista Clientes')
        self.ui.btnLoadClient.setIcon(self.svg_coloreado("arrows-spin.svg","#030464",QSize(50,50)))
        self.ui.bSearchClient.setToolTip('Buscar Cliente')
        self.ui.bSearchClient.setIcon(self.svg_coloreado("magnifying-glass.svg","#000000",QSize(50,50)))
        self.ui.expoCliPdf.setToolTip('Exportar Lista de Clientes PDF')
        self.ui.expoCliPdf.setIcon(self.svg_coloreado("file-pdf.svg","#7e1010",QSize(50,50)))
        self.ui.exExcCli.setToolTip('Exportar Lista de Clientes Excel')
        self.ui.exExcCli.setIcon(self.svg_coloreado("file-excel.svg","#104919",QSize(50,50)))
        self.ui.btnBuscarUser.setToolTip("Buscar Usuario De la lista")
        self.ui.btnBuscarUser.setIcon(self.svg_coloreado("magnifying-glass.svg","#000000",QSize(50,50)))
        self.ui.btnNuevoUser.setToolTip("Crear Nuevo Usuario")
        self.ui.btnNuevoUser.setIcon(self.svg_coloreado("user-plus.svg","#0F300E",QSize(50,50)))

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
        if val==1:
            self.cargarClientes()
            
    def cargarClientes(self):
        result = self.api.ObtenerUsuarios()
        if 'ok' in result:
            self.ui.tableWidget.clear()
            self.ui.tableWidget.setRowCount(len(result['ok']))
            self.ui.tableWidget.setColumnCount(9)
            self.ui.tableWidget.setHorizontalHeaderLabels(['ID',"NOMBRE USUARIO","CORREO","TIPO USARIO","ESTADO",'AP PERMISO',"","",""])
            for row,user in enumerate(result['ok']):
                boton = QPushButton("Ver")
                boton.setIcon(self.svg_coloreado("eye.svg","#000000",QSize(40,40)))
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
                botoneliminar.setIcon(self.svg_coloreado("trash-can.svg","#9E0101",QSize(40,40)))
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
                botoninactivar.setIcon(self.svg_coloreado("user-slash.svg","#DA6900",QSize(40,40)))
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
        elif 'detail' in result:
            msgUtils.mostrar_toast_error(self,"Error: "+str(result['detail']))
        else:
            msgUtils.mostrar_toast_error(self,"Error: "+str(result['error']))
    def mostrarModalRegistro(self):
        dialog = ModalRegistro()
        dialog.exec()
    def mostrarModalUsuario(self):
        dialog  = ModalUsuario()
        result = dialog.exec()
        if result == QDialog.DialogCode.Accepted:
            print("creado usuario")
            self.cargarClientes()
    def editarEstadoUser(self,dato,estado):
        result = self.api.CambiarEstadoUser({'id':dato['id'],'estado':estado})
        print(result)
        if 'ok' in result:
            msgUtils.mostrar_toast_correcto(self,result['ok'])
            self.cargarClientes()
        elif 'detail' in result:
            msgUtils.mostrar_toast_error(self,"Error: "+str(result['detail']))
        else:
            msgUtils.mostrar_toast_error(self,"Error: "+str(result['error']))
    def testLogin(self):
        session = utils.test_session_user()
        print(session)
    def verDetalle(self,dato):
        dialog = ModalUsuario(dato)
        result = dialog.exec()
        if result == QDialog.DialogCode.Accepted:
            self.cargarClientes()


                

if __name__ == "__main__":
    app = QApplication([])
    login = ModalLogin()
    if login.exec() == QDialog.DialogCode.Accepted:
        ventana = MainWindow()
        ventana.show()
        app.exec()
    else:
        print("Login cancelado")