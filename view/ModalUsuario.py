# Form implementation generated from reading ui file 'view/ModalUsuario.ui'
#
# Created by: PyQt6 UI code generator 6.9.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(502, 333)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(parent=Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(parent=self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(2, 0, 2, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(parent=self.frame_2)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lineNameUser = QtWidgets.QLineEdit(parent=self.frame_2)
        self.lineNameUser.setObjectName("lineNameUser")
        self.horizontalLayout_2.addWidget(self.lineNameUser)
        self.horizontalLayout_2.setStretch(0, 4)
        self.horizontalLayout_2.setStretch(1, 7)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_4 = QtWidgets.QFrame(parent=self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(parent=self.frame_4)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.lineEmail = QtWidgets.QLineEdit(parent=self.frame_4)
        self.lineEmail.setObjectName("lineEmail")
        self.horizontalLayout_3.addWidget(self.lineEmail)
        self.horizontalLayout_3.setStretch(0, 4)
        self.horizontalLayout_3.setStretch(1, 7)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_6 = QtWidgets.QFrame(parent=self.frame)
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setContentsMargins(2, 0, 2, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(parent=self.frame_6)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.frame_9 = QtWidgets.QFrame(parent=self.frame_6)
        self.frame_9.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(3)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.linePassword = QtWidgets.QLineEdit(parent=self.frame_9)
        self.linePassword.setObjectName("linePassword")
        self.horizontalLayout_8.addWidget(self.linePassword)
        self.btnViewPass = QtWidgets.QPushButton(parent=self.frame_9)
        self.btnViewPass.setText("")
        self.btnViewPass.setObjectName("btnViewPass")
        self.horizontalLayout_8.addWidget(self.btnViewPass)
        self.horizontalLayout_4.addWidget(self.frame_9)
        self.horizontalLayout_4.setStretch(0, 4)
        self.horizontalLayout_4.setStretch(1, 7)
        self.verticalLayout.addWidget(self.frame_6)
        self.frame_8 = QtWidgets.QFrame(parent=self.frame)
        self.frame_8.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_8.setLineWidth(1)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_7.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_6 = QtWidgets.QLabel(parent=self.frame_8)
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.linePasswordR = QtWidgets.QLineEdit(parent=self.frame_8)
        self.linePasswordR.setObjectName("linePasswordR")
        self.horizontalLayout_7.addWidget(self.linePasswordR)
        self.horizontalLayout_7.setStretch(0, 4)
        self.horizontalLayout_7.setStretch(1, 7)
        self.verticalLayout.addWidget(self.frame_8)
        self.frame_3 = QtWidgets.QFrame(parent=self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.combTipoUser = QtWidgets.QComboBox(parent=self.frame_3)
        self.combTipoUser.setObjectName("combTipoUser")
        self.horizontalLayout_5.addWidget(self.combTipoUser)
        self.horizontalLayout_5.setStretch(0, 4)
        self.horizontalLayout_5.setStretch(1, 7)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_7 = QtWidgets.QFrame(parent=self.frame)
        self.frame_7.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(parent=self.frame_7)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.combUsoApp = QtWidgets.QComboBox(parent=self.frame_7)
        self.combUsoApp.setObjectName("combUsoApp")
        self.horizontalLayout_6.addWidget(self.combUsoApp)
        self.horizontalLayout_6.setStretch(0, 4)
        self.horizontalLayout_6.setStretch(1, 7)
        self.verticalLayout.addWidget(self.frame_7)
        self.verticalLayout_2.addWidget(self.frame)
        self.frame_5 = QtWidgets.QFrame(parent=Dialog)
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 9)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.btnSalir = QtWidgets.QPushButton(parent=self.frame_5)
        self.btnSalir.setIconSize(QtCore.QSize(25, 25))
        self.btnSalir.setObjectName("btnSalir")
        self.horizontalLayout.addWidget(self.btnSalir)
        self.btnGuardar = QtWidgets.QPushButton(parent=self.frame_5)
        self.btnGuardar.setIconSize(QtCore.QSize(25, 25))
        self.btnGuardar.setObjectName("btnGuardar")
        self.horizontalLayout.addWidget(self.btnGuardar)
        self.horizontalLayout.setStretch(0, 3)
        self.verticalLayout_2.addWidget(self.frame_5)
        self.verticalLayout_2.setStretch(0, 4)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Usuario Sistema"))
        self.label.setText(_translate("Dialog", "Nombre usuario"))
        self.label_2.setText(_translate("Dialog", "Correo"))
        self.label_4.setText(_translate("Dialog", "Contraseña"))
        self.label_6.setText(_translate("Dialog", "Confimar contraseña"))
        self.label_3.setText(_translate("Dialog", "Tipo usuario"))
        self.label_5.setText(_translate("Dialog", "Uso aplicacion"))
        self.btnSalir.setText(_translate("Dialog", "Cancelar"))
        self.btnGuardar.setText(_translate("Dialog", "Guardar"))
