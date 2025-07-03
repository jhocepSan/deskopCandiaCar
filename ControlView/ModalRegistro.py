from PyQt6.QtWidgets import QToolTip,QDialog, QLineEdit, QFileDialog, QSizePolicy
from PyQt6.QtSvg import QSvgRenderer
from PyQt6.QtGui import QFont,QIcon,QPixmap,QPainter,QColor
from PyQt6.QtCore import QSize, Qt
from view.ModalRegistro import Ui_Dialog
import Clases.Utils as utils
import Clases.UtilsMessage as messages
import os
from Clases.payloads.vehiculo import VehiculoModel
from Clases.enums import Color, IconSize
from Clases.services.cliente import NuevaPersona, searchCodigo
from Clases.services.vehiculo import buscar_vehiculo, registrar_vehiculo, getTipoVehiculos

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
        self.persona = None
        self.vehiculo = VehiculoModel()
        self.tipoVehiculos: list = None
        self.fotoplaca_filename: str = None
        self.fotovehiculo_filename: str = None

        self.ui.tabWidget.setCurrentIndex(0)
        self.ui.tabWidget.setTabEnabled(1,False)
        self.ui.tabWidget.setTabEnabled(2,False)
        self.iniciar_extras()
        self.load_default_previews()
        QToolTip.setFont(QFont('Arial', 10))
        self.ui.btnSalir.clicked.connect(self.cerrarDialogo)
        self.ui.btnSiguiente.clicked.connect(self.validateCliente)
        self.ui.btnBuscarCodigo.clicked.connect(self.buscarPorCodigo)
        self.ui.btnGenCodigo.clicked.connect(self.generarCodigo)
        self.ui.btnSubFplaca.clicked.connect(self.handle_subirfotoplaca)
        self.ui.btnSubFvehiculo.clicked.connect(self.handle_subirfotovehiculo)
        self.ui.btn_rm_fotoplaca.clicked.connect(self.handle_remove_fotoplaca)
        self.ui.btn_rm_fotovehiculo.clicked.connect(self.handle_remove_fotovehiculo)
        self.ui.btn_buscarplaca.clicked.connect(self.buscar_placavehiculo)

        self.handle_editFinish_vehiculo([self.ui.lineModelo,
                                         self.ui.linePlaca,
                                         self.ui.lineColor,
                                         self.ui.lineMotor,
                                         self.ui.lineKilome])
        self.fill_tipoVehiculos()

    def iniciar_extras(self):
        self.ui.tabWidget.setTabIcon(0, utils.get_icon("user"))
        self.ui.tabWidget.setTabIcon(1, utils.get_icon("car",))
        self.ui.btnBuscarCodigo.setToolTip("Buscar Codigo")
        self.ui.btnBuscarCodigo.setIcon(utils.get_icon("magnifying-glass",))
        self.ui.btn_buscarplaca.setIcon(utils.get_icon("magnifying-glass",))
        self.ui.btnFotoCliente.setToolTip("Tomar Foto Cliente")
        self.ui.btnFotoCliente.setIcon(utils.get_icon("camera",Color.PURPLE))
        self.ui.btnFotoPlaca.setToolTip("Tomar Foto Placa")
        self.ui.btnFotoPlaca.setIcon(utils.get_icon("camera",Color.PURPLE))
        self.ui.btnFotoVehi.setToolTip("Tomar Foto Vehiculo")
        self.ui.btnFotoVehi.setIcon(utils.get_icon("camera", Color.PURPLE))
        self.ui.btnSubirFcliente.setToolTip("Subir Foto Cliente")
        self.ui.btnSubirFcliente.setIcon(utils.get_icon("folder-open", Color.BLUE))
        self.ui.btnSubFplaca.setToolTip("Subir Foto Placa")
        self.ui.btnSubFplaca.setIcon(utils.get_icon("folder-open", Color.BLUE))
        self.ui.btnSubFvehiculo.setToolTip("Subir Foto Vehiculo")
        self.ui.btnSubFvehiculo.setIcon(utils.get_icon("folder-open", Color.BLUE))
        self.ui.btn_rm_fotoplaca.setIcon(utils.get_icon("trash-can", Color.BLUE))
        self.ui.btn_rm_fotovehiculo.setIcon(utils.get_icon("trash-can", Color.BLUE))
        self.ui.btnSalir.setToolTip("Salir Registro")
        self.ui.btnSalir.setIcon(utils.get_icon("circle-xmark", Color.CANCEL))
        self.ui.btnSiguiente.setToolTip("Ir al Siguiente")
        self.ui.btnSiguiente.setIcon(utils.get_icon("circle-arrow-right", Color.OK))
        self.ui.btnGenCodigo.setToolTip("Generar Codigo")
        self.ui.btnGenCodigo.setIcon(utils.get_icon("square-binary"))


    def load_default_previews(self):
        pixmap = QPixmap(utils.PATH_PH_IMAGE)
        self.ui.lb_fotoplacaPreview.setPixmap(pixmap)
        self.ui.lb_fotoplacaPreview.setScaledContents(True)
        self.ui.lb_fotoplacaPreview.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ui.lb_fotoplacaPreview.setSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)

        self.ui.lb_fotoPreview.setPixmap(pixmap)
        self.ui.lb_fotoPreview.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ui.lb_fotoPreview.setScaledContents(True)
        self.ui.lb_fotoPreview.setSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)

        self.ui.lb_fotocliente_preview.setPixmap(pixmap)
        self.ui.lb_fotocliente_preview.setScaledContents(True)
        self.ui.lb_fotocliente_preview.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ui.lb_fotocliente_preview.setSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        
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
        response = getTipoVehiculos()
        if response.error:
            messages.mostrar_toast_error(self, response.error)
            return
        else:
            self.tipoVehiculos = response.data 
            for tipo in response.data:
                self.ui.comboTipoVehiculo.addItem(tipo['nombre'])

    def clearMsgErr(self):
        self.ui.lb_valid_message.clear()

    def irARegistroVehiculo(self):
        self.ui.btnSiguiente.setToolTip("Guardar Vehiculo")
        self.ui.btnSiguiente.setIcon(utils.get_icon("circle-arrow-right", Color.OK))
        self.ui.btnSalir.setToolTip("Ir Atras")
        self.ui.btnSalir.setIcon(utils.get_icon("circle-arrow-left", Color.CANCEL))
        self.ui.btnSiguiente.clicked.connect(self.validateVehiculo)
        self.ui.btnSalir.clicked.connect(self.irAcliente)
        self.ui.tabWidget.setTabEnabled(1,True)
        self.ui.tabWidget.setCurrentIndex(1)

    def irARegistroDetalles(self):
        self.ui.tabWidget.setTabEnabled(2,True)
        self.ui.tabWidget.setCurrentIndex(2)

    def irAcliente(self):
        self.ui.btnSiguiente.setToolTip("Ir al Siguiente")
        self.ui.btnSiguiente.setIcon(utils.get_icon("circle-arrow-right", Color.OK))
        self.ui.btnSiguiente.clicked.connect(self.validateCliente)
        self.ui.btnSalir.setToolTip("Salir Registro")
        self.ui.btnSalir.setIcon(utils.get_icon("circle-xmark", Color.CANCEL))
        self.ui.btnSalir.clicked.connect(self.cerrarDialogo)
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
            self.ui.lb_valid_message.setText("La placa es requerido para registro")
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
        
        result = NuevaPersona({"nombres": nombres, 
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

    def buscar_placavehiculo(self):
        placa = self.ui.linePlaca.text()
        if placa:
            result = buscar_vehiculo(placa)
            if result.error:
                self.ui.lb_valid_message.setText(result.error)
            else:    
                self.vehiculo.id = result.data["id"]
                self.vehiculo.placa = result.data["placa"]
                self.vehiculo.modelo = result.data["modelo"]
                self.vehiculo.color = result.data["color"]
                self.vehiculo.foto = result.data["foto"]
                self.vehiculo.fotoplaca = result.data["fotoplaca"]
                self.vehiculo.km = result.data["km"]
                self.vehiculo.motor = result.data["motor"]
                self.vehiculo.tipoNombre = result.data["tipo"]["nombre"]
                self.vehiculo.tipoId = result.data["tipo"]["id"]
                
                self.ui.lineModelo.setText(self.vehiculo.modelo)
                self.ui.linePlaca.setText(self.vehiculo.placa)
                self.ui.lineColor.setText(self.vehiculo.color)
                self.ui.lineKilome.setText(self.vehiculo.km)
                self.ui.lineMotor.setText(self.vehiculo.motor)
                self.ui.comboTipoVehiculo.setCurrentText(self.vehiculo.tipoNombre)
            
                self.ui.lb_valid_message.clear
                
        else:
            self.ui.lb_valid_message.setText("Ingresar numero de placa")

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
            result = update_vehiculo(self.vehiculo)
        else:
            result = registrar_vehiculo(self.vehiculo)
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
        result = searchCodigo({'codigo':codigo})
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