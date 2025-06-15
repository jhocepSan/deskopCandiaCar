from PyQt6.QtWidgets import QApplication,QMainWindow,QToolTip
from PyQt6.QtGui import QFont
from view.MainVentana import Ui_MainWindow
import Clases.ComunicacionApi as ComunicacionApi
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
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
    def agregarTooltips(self):
        self.ui.btnMenu.setToolTip('Menu')
        self.ui.btnClientes.setToolTip('Clientes')
        self.ui.btnConfig.setToolTip('Configuraciones')
        self.ui.btnUsuarios.setToolTip('Usuarios')
        self.ui.btnServicios.setToolTip('Servicios')
        self.ui.btnAddClient.setToolTip('Agregar Cliente')
        self.ui.btnLoadClient.setToolTip('Refrescar lista Clientes')
        self.ui.bSearchClient.setToolTip('Buscar Cliente')
        self.ui.expoCliPdf.setToolTip('Exportar Lista de Clientes PDF')
        self.ui.exExcCli.setToolTip('Exportar Lista de Clientes Excel')
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

if __name__ == "__main__":
    app = QApplication([])
    ventana = MainWindow()
    ventana.show()
    app.exec()