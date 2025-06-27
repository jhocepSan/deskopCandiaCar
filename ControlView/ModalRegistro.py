from PyQt6.QtWidgets import QToolTip,QDialog, QLineEdit, QFileDialog, QSizePolicy
from Clases.ComunicacionApi import ComunicacionApi
from PyQt6.QtSvg import QSvgRenderer
from PyQt6.QtGui import QFont,QIcon,QPixmap,QPainter,QColor
from PyQt6.QtCore import QSize
from view.ModalRegistro import Ui_Dialog
import Clases.Utils as utils
import Clases.UtilsMessage as messages
import os
from Clases.payloads.vehiculo import VehiculoModel
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
        self.vehiculo = VehiculoModel()
        self.tipoVehiculos: list = None
        self.fotoplaca_filename: str = None
        self.fotovehiculo_filename: str = None

        self.ui.tabWidget.setCurrentIndex(0)
        self.ui.tabWidget.setTabEnabled(1,False)
        self.ui.tabWidget.setTabEnabled(2,False)
        self.iniciar_extras()
        QToolTip.setFont(QFont('Arial', 10))
        self.ui.btnSalir.clicked.connect(self.cerrarDialogo)
        self.ui.btnAtrasVeh.clicked.connect(self.irAcliente)
        self.ui.btnSiguiente.clicked.connect(self.validateCliente)
        self.ui.btnBuscarCodigo.clicked.connect(self.buscarPorCodigo)
        self.ui.btnGenCodigo.clicked.connect(self.generarCodigo)
        self.ui.btnGuardarVehiculo.clicked.connect(self.validateVehiculo)
        self.ui.btnSubFplaca.clicked.connect(self.handle_subirfotoplaca)
        self.ui.btnSubFvehiculo.clicked.connect(self.handle_subirfotovehiculo)
        self.ui.btn_rm_fotoplaca.clicked.connect(self.handle_remove_fotoplaca)
        self.ui.btn_rm_fotovehiculo.clicked.connect(self.handle_remove_fotovehiculo)

        self.handle_editFinish_vehiculo([self.ui.lineModelo,
                                         self.ui.linePlaca,
                                         self.ui.lineColor,
                                         self.ui.lineMotor,
                                         self.ui.lineKilome])
        self.fill_tipoVehiculos()

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
        self.ui.btnFotoPlaca.setIcon(self.svg_coloreado("camera.svg","#271068",QSize(15,15)))
        self.ui.btnFotoVehi.setToolTip("Tomar Foto Vehiculo")
        self.ui.btnFotoVehi.setIcon(self.svg_coloreado("camera.svg","#271068",QSize(15,15)))
        self.ui.btnSubirFcliente.setToolTip("Subir Foto Cliente")
        self.ui.btnSubirFcliente.setIcon(self.svg_coloreado("folder-open.svg","#0E394B",QSize(40,40)))
        self.ui.btnSubFplaca.setToolTip("Subir Foto Placa")
        self.ui.btnSubFplaca.setIcon(self.svg_coloreado("folder-open.svg","#0E394B",QSize(15,15)))
        self.ui.btnSubFvehiculo.setToolTip("Subir Foto Vehiculo")
        self.ui.btnSubFvehiculo.setIcon(self.svg_coloreado("folder-open.svg","#0E394B",QSize(15,15)))
        self.ui.btn_rm_fotoplaca.setIcon(self.svg_coloreado("trash-can.svg","#0E394B",QSize(15,15)))
        self.ui.btn_rm_fotovehiculo.setIcon(self.svg_coloreado("trash-can.svg","#0E394B",QSize(15,15)))
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

    def handle_remove_fotoplaca(self):
        self.ui.lb_fotoplacaPath.clear()
        self.ui.lb_fotoplacaPreview.clear()

    def handle_remove_fotovehiculo(self):
        self.ui.lb_fotoPath.clear()
        self.ui.lb_fotoPreview.clear()

    def handle_subirfotoplaca(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Open File",
            "",
            "JPG Files (*.jpg);;JPEG Files (*.jpeg);;PNG Files (*.png)"
        )
        pixmap = QPixmap(file_path)
        if pixmap.isNull():
            print(f"Error: Could not load image from {file_path}")
        self.fotoplaca_filename = os.path.basename(file_path)
        self.ui.lb_fotoplacaPath.setText(file_path)
        self.ui.lb_fotoplacaPreview.setPixmap(pixmap)
        self.ui.lb_fotoplacaPreview.setScaledContents(True)
        self.ui.lb_fotoplacaPreview.setSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)

    def handle_subirfotovehiculo(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Open File",
            "",
            "JPG Files (*.jpg);;JPEG Files (*.jpeg);;PNG Files (*.png)"
        )
        pixmap = QPixmap(file_path)
        if pixmap.isNull():
            print(f"Error: Could not load image from {file_path}")
        self.ui.lb_fotoPath.setText(file_path)
        self.ui.lb_fotoPreview.setPixmap(pixmap)
        self.ui.lb_fotoPreview.setScaledContents(True)
        self.ui.lb_fotoPreview.setSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)

    def handle_editFinish_vehiculo(self, fields: list[QLineEdit]):
        for field in fields:
            field.editingFinished.connect(self.clearMsgErr)

    def fill_tipoVehiculos(self):
        response = self.api.getTipoVehiculos()
        if response.error:
            messages.mostrar_toast_error(self, response.error)
            return
        else:
            self.tipoVehiculos = response.data 
            for tipo in response.data:
                self.ui.comboTipoVehiculo.addItem(tipo['nombre'])

    def clearMsgErr(self):
        self.ui.lb_msg_err.clear()

    def irARegistroVehiculo(self):
        self.ui.tabWidget.setTabEnabled(1,True)
        self.ui.tabWidget.setCurrentIndex(1)

    def irARegistroDetalles(self):
        self.ui.tabWidget.setTabEnabled(2,True)
        self.ui.tabWidget.setCurrentIndex(2)

    def irAcliente(self):
        self.ui.tabWidget.setCurrentIndex(0)

    def validateCliente(self):
        if self.ui.lineCodigoCli.text()=='':
            self.ui.framValid.setStyleSheet("background-color: #fc8484; border-radius: 10px;")
            self.ui.lb_valid_message.setText("El codigo es requerido para registro")
            self.ui.lineCodigoCli.setFocus()
            return
        if self.ui.lineNombres.text() == "" or self.ui.lineApellidos.text() == "":
            self.ui.framValid.setStyleSheet("background-color: #fc8484; border-radius: 10px;")
            self.ui.lb_valid_message.setText("Campos requeridos vacios")
            self.ui.lineNombres.setFocus()
            return
        self.guardarDatosCliente()

    def validateVehiculo(self):
        if self.ui.linePlaca.text()=='':
            self.ui.framValid.setStyleSheet("background-color: #fc8484; border-radius: 10px;")
            self.ui.lb_msg_err.setText("La placa es requerido para registro")
            self.ui.linePlaca.setFocus()
            return
        self.guardarDatosVehiculo()

    def guardarDatosCliente(self):
        if self.persona:
            self.irARegistroVehiculo()
            return
        nombres = self.ui.lineNombres.text()        
        apellidos = self.ui.lineApellidos.text()        
        telefono = self.ui.lineTelefono.text()        
        direccion = self.ui.lineDireccion.text()        
        codigo = self.ui.lineCodigoCli.text()
        
        loading = messages.mostrar_WIP(self)
        
        result = self.api.NuevaPersona({"nombres": nombres, 
                                            "apellidos": apellidos,
                                            "telefono": telefono,
                                            "direccion": direccion,
                                            "codigo": codigo})
        if result.error:
            loading.close()
            messages.mostrar_toast_error(self, result.error)
        else:    
            self.ui.framValid.setStyleSheet("background-color: #84fc93; border-radius: 10px;")
            self.ui.lb_valid_message.setText("Guardado Correctamente")
            self.persona = result.data
            loading.close()
            messages.mostrar_toast_correcto(self, "Registro correcto")
            self.irARegistroVehiculo()

    def guardarDatosVehiculo(self):
        self.vehiculo.modelo = self.ui.lineModelo.text()
        self.vehiculo.placa = self.ui.linePlaca.text()
        self.vehiculo.color = self.ui.lineColor.text()
        self.vehiculo.motor = self.ui.lineMotor.text()
        self.vehiculo.km = self.ui.lineKilome.text()
        self.vehiculo.tipoNombre = self.ui.comboTipoVehiculo.currentText()
        self.vehiculo.fotoplaca = os.path.basename(self.ui.lb_fotoplacaPath.text())
        self.vehiculo.foto = os.path.basename(self.ui.lb_fotoPath.text())
        tipoId = [tipo['id'] for tipo in self.tipoVehiculos if tipo['nombre'] == self.vehiculo.tipoNombre]
        self.vehiculo.tipoId = tipoId.pop() if tipoId else None

        loading = messages.mostrar_WIP(self)
        if self.vehiculo.fotoplaca:
            utils.upload_photo_to_public(self.ui.lb_fotoplacaPath.text())
        if self.vehiculo.foto:
            utils.upload_photo_to_public(self.ui.lb_fotoPath.text())

        if self.vehiculo.id:
            result = self.api.update_vehiculo(self.vehiculo)
        else:
            result = self.api.registrar_vehiculo(self.vehiculo)
        if result.error:
            loading.close()
            messages.mostrar_toast_error(self, result.error)
        else:    
            loading.close()
            self.vehiculo.id = self.vehiculo.id if self.vehiculo.id else result.data['id']
            messages.mostrar_toast_correcto(self, "Se guardo correctamente")
            self.irARegistroDetalles()

    def buscarPorCodigo(self):
        codigo = self.ui.lineCodigoCli.text()
        if codigo =='':
            messages.mostrar_toast_error(self,"No hay Cliente, con el codigo quer busca ...")
            return
        result = self.api.searchCodigo({'codigo':codigo})
        if result.error:
            messages.mostrar_toast_error(self,result.error)
        else:
            self.ui.lineNombres.setText(result.data['nombres'])
            self.ui.lineApellidos.setText(result.data['apellidos'])
            self.ui.lineDireccion.setText(result.data['direccion'])
            self.ui.lineTelefono.setText(result.data['telefono'])
            self.persona = result.data
    def generarCodigo(self):
        pass