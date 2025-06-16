from PyQt6.QtWidgets import QApplication,QMainWindow,QToolTip,QDialog
from PyQt6.QtSvg import QSvgRenderer
from PyQt6.QtGui import QFont,QIcon,QPixmap,QPainter,QColor
from PyQt6.QtCore import QSize
from view.MainVentana import Ui_MainWindow
from view.ModalRegistro import Ui_Dialog
import Clases.ComunicacionApi as ComunicacionApi
import os
class ModalRegistro(QDialog):
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
        self.ui.tabWidget.setCurrentIndex(0)
        self.ui.tabWidget.setTabEnabled(1,False)
        self.ui.tabWidget.setTabEnabled(2,False)
        self.iniciar_extras()
        QToolTip.setFont(QFont('Arial', 10))
        self.ui.btnSalir.clicked.connect(self.cerrarDialogo)
        self.ui.btnGuardarCli.clicked.connect(self.guardarCliente)
        self.ui.btnAtrasVeh.clicked.connect(self.irAcliente)
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
    def iniciar_extras(self):
        self.ui.tabWidget.setTabIcon(0,self.svg_coloreado("user.svg","#ffffff"))
        self.ui.tabWidget.setTabIcon(1,self.svg_coloreado("car.svg","#ffffff"))
        self.ui.btnBuscarCodigo.setToolTip("Buscar Codigo")
        self.ui.btnBuscarCodigo.setIcon(self.svg_coloreado("magnifying-glass.svg","#000000",QSize(40,40)))
        self.ui.btnFotoCliente.setToolTip("Tomar Foto Cliente")
        self.ui.btnFotoCliente.setIcon(self.svg_coloreado("camera.svg","#271068",QSize(40,40)))
        self.ui.btnFotoPlaca.setToolTip("Tomar Foto Placa")
        self.ui.btnFotoPlaca.setIcon(self.svg_coloreado("camera.svg","#271068",QSize(40,40)))
        self.ui.btnFotoVehi.setToolTip("Tomar Foto Vehiculo")
        self.ui.btnFotoVehi.setIcon(self.svg_coloreado("camera.svg","#271068",QSize(40,40)))
        self.ui.btnSubirFcliente.setToolTip("Subir Foto Cliente")
        self.ui.btnSubirFcliente.setIcon(self.svg_coloreado("folder-open.svg","#0E394B",QSize(40,40)))
        self.ui.btnSubFplaca.setToolTip("Subir Foto Placa")
        self.ui.btnSubFplaca.setIcon(self.svg_coloreado("folder-open.svg","#0E394B",QSize(40,40)))
        self.ui.btnSubFvehiculo.setToolTip("Subir Foto Vehiculo")
        self.ui.btnSubFvehiculo.setIcon(self.svg_coloreado("folder-open.svg","#0E394B",QSize(40,40)))
        self.ui.btnSalir.setToolTip("Salir Registro")
        self.ui.btnSalir.setIcon(self.svg_coloreado("circle-xmark.svg","#D37575",QSize(40,40)))
        self.ui.btnGuardarCli.setToolTip("Ir al Siguiente")
        self.ui.btnGuardarCli.setIcon(self.svg_coloreado("circle-arrow-right.svg","#80D375",QSize(40,40)))
        self.ui.btnGenCodigo.setToolTip("Generar Codigo")
        self.ui.btnGenCodigo.setIcon(self.svg_coloreado("square-binary.svg","#000000",QSize(40,40)))
        self.ui.btnAtrasVeh.setToolTip("Ir Atras")
        self.ui.btnAtrasVeh.setIcon(self.svg_coloreado("circle-arrow-left.svg","#D37575",QSize(40,40)))
        self.ui.btnGuardarVehiculo.setToolTip("Guardar Vehiculo")
        self.ui.btnGuardarVehiculo.setIcon(self.svg_coloreado("circle-arrow-right.svg","#80D375",QSize(40,40)))
    def cerrarDialogo(self):
        self.reject()
    def guardarCliente(self):
        self.ui.tabWidget.setTabEnabled(1,True)
        self.ui.tabWidget.setCurrentIndex(1)
    def irAcliente(self):
        self.ui.tabWidget.setCurrentIndex(0)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.SVG_BASE = "./public/fontawesome-free-6.7.2-desktop/svgs/solid/"
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
        self.ui.btnClientes.clicked.connect(lambda:self.mostrarVista(2))
        self.ui.btnConfig.clicked.connect(lambda:self.mostrarVista(1))
        self.ui.btnServicios.clicked.connect(lambda:self.mostrarVista(0))
        self.ui.btnUsuarios.clicked.connect(lambda:self.mostrarVista(3))
        self.ui.btnLoadClient.clicked.connect(self.cargarClientes)
        self.ui.btnAddClient.clicked.connect(self.mostrarModalRegistro)
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
    def cargarClientes(self):
        result = self.api.ObtenerUsuarios()
        print(result)
    def mostrarModalRegistro(self):
        dialog = ModalRegistro()
        dialog.exec()

if __name__ == "__main__":
    app = QApplication([])
    ventana = MainWindow()
    ventana.show()
    app.exec()