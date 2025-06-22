from PyQt6.QtWidgets import QApplication,QMainWindow,QToolTip,QDialog
from Clases.ComunicacionApi import ComunicacionApi
from PyQt6.QtSvg import QSvgRenderer
from PyQt6.QtGui import QFont,QIcon,QPixmap,QPainter,QColor
from PyQt6.QtCore import QSize
from view.ModalRegistro import Ui_Dialog
import Clases.Utils as utils
import Clases.UtilsMessage as messages
import os
from requests import RequestException

class ModalRegistro(QDialog):
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
        self.persona = None

        self.ui.tabWidget.setCurrentIndex(0)
        self.ui.tabWidget.setTabEnabled(1,False)
        self.ui.tabWidget.setTabEnabled(2,False)
        self.iniciar_extras()
        QToolTip.setFont(QFont('Arial', 10))
        self.ui.btnSalir.clicked.connect(self.cerrarDialogo)
        self.ui.btnSiguiente.clicked.connect(self.irARegistroVehiculo)
        self.ui.btnAtrasVeh.clicked.connect(self.irAcliente)
        self.ui.btnGuardarCliente.clicked.connect(self.validateCliente)

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
        self.ui.btnSiguiente.setToolTip("Ir al Siguiente")
        self.ui.btnSiguiente.setIcon(self.svg_coloreado("circle-arrow-right.svg","#80D375",QSize(40,40)))
        self.ui.btnGenCodigo.setToolTip("Generar Codigo")
        self.ui.btnGenCodigo.setIcon(self.svg_coloreado("square-binary.svg","#000000",QSize(40,40)))
        self.ui.btnAtrasVeh.setToolTip("Ir Atras")
        self.ui.btnAtrasVeh.setIcon(self.svg_coloreado("circle-arrow-left.svg","#D37575",QSize(40,40)))
        self.ui.btnGuardarVehiculo.setToolTip("Guardar Vehiculo")
        self.ui.btnGuardarVehiculo.setIcon(self.svg_coloreado("circle-arrow-right.svg","#80D375",QSize(40,40)))

    def cerrarDialogo(self):
        self.reject()

    def irARegistroVehiculo(self):
        self.ui.tabWidget.setTabEnabled(1,True)
        self.ui.tabWidget.setCurrentIndex(1)

        if self.persona:
            self.ui.lb_idPersona_value.setText(str(self.persona['idpersona']))
            self.ui.lb_personaNombres_value.setText(self.persona['nombres'])
            self.ui.lb_personaApellidos_value.setText(self.persona['apellidos'])

    def irAcliente(self):
        self.ui.tabWidget.setCurrentIndex(0)

    def validateCliente(self):
        if self.ui.lineNombres.text() == "" or self.ui.lineApellidos.text() == "":
            self.ui.lb_valid_message.setText("Campos requeridos vacios")
            self.ui.lineNombres.setFocus()
            return
        self.guardarDatosCliente()

    def guardarDatosCliente(self):
        self.ui.lb_valid_message.setText("Campos requeridos vacios")
        
        nombres = self.ui.lineNombres.text()        
        apellidos = self.ui.lineApellidos.text()        
        telefono = self.ui.lineTelefono.text()        
        direccion = self.ui.lineDireccion.text()        
        codigo = self.ui.lineCodigoCli.text()
        
        loading = messages.mostrar_WIP(self)
        try:
            result = self.api.NuevaPersona({"nombres": nombres, 
                                            "apellidos": apellidos,
                                            "telefono": telefono,
                                            "direccion": direccion,
                                            "codigo": codigo})
            self.persona = result
            loading.close()
            messages.mostrar_toast_correcto(self, "Registro correcto")
            self.irARegistroVehiculo()
            self.ui.lineNombres.clear()
            self.ui.lineApellidos.clear()
            self.ui.lineTelefono.clear()
            self.ui.lineDireccion.clear()
            self.ui.lineCodigoCli.clear()
        except RequestException as e:
            loading.close()
            print(f"error en registro de persona: {e}")
            messages.mostrar_toast_error(self, "Error al registar persona")
