# Form implementation generated from reading ui file 'view/ModalLogin.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(399, 300)
        Dialog.setStyleSheet("QDialog{\n"
"background:rgb(85, 85, 85);\n"
"}\n"
"")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(parent=Dialog)
        self.frame.setStyleSheet("QLabel{\n"
"color:rgb(245, 245, 245);\n"
"font:77 10pt \'Arial Black\';\n"
"}\n"
"QPushButton{\n"
"border-radius: 12px;\n"
"color:rgb(238, 238, 238);\n"
"background-color:rgb(186, 186, 186);\n"
"padding: 7px 7px;\n"
"  text-align: center;\n"
"  font-size: 16px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #04AA6D; /* Green */\n"
"color: white;\n"
"}\n"
"QLineEdit{\n"
"padding: 12px 20px;\n"
"margin: 8px 0;\n"
"border: 2px solid #fff;\n"
"border-radius: 5px;\n"
"font:77 12px \'Arial Black\';\n"
"color:rgb(238, 238, 238);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_3 = QtWidgets.QFrame(parent=self.frame)
        self.frame_3.setStyleSheet("QLabel{\n"
"    font-size:18px;\n"
"    font-weight: bold;\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.labelIcono = QtWidgets.QLabel(parent=self.frame_3)
        self.labelIcono.setText("")
        self.labelIcono.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelIcono.setObjectName("labelIcono")
        self.verticalLayout_3.addWidget(self.labelIcono)
        self.label_2 = QtWidgets.QLabel(parent=self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.verticalLayout_3.setStretch(0, 8)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.frame_5 = QtWidgets.QFrame(parent=self.frame)
        self.frame_5.setStyleSheet("")
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setContentsMargins(-1, 1, -1, 1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(parent=self.frame_5)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.frame_5)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.horizontalLayout_2.setStretch(0, 3)
        self.horizontalLayout_2.setStretch(1, 8)
        self.verticalLayout_2.addWidget(self.frame_5)
        self.frame_4 = QtWidgets.QFrame(parent=self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setContentsMargins(-1, 1, -1, 1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(parent=self.frame_4)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.frame_4)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_3.addWidget(self.lineEdit_2)
        self.horizontalLayout_3.setStretch(0, 3)
        self.horizontalLayout_3.setStretch(1, 8)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.verticalLayout_2.setStretch(0, 5)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(parent=Dialog)
        self.frame_2.setStyleSheet("QLabel{\n"
"color:rgb(245, 245, 245);\n"
"font:77 10pt \'Arial Black\';\n"
"}\n"
"QPushButton{\n"
"border-radius: 12px;\n"
"color:rgb(238, 238, 238);\n"
"background-color:rgb(186, 186, 186);\n"
"padding: 7px 7px;\n"
"  text-align: center;\n"
"  font-size: 16px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #04AA6D; /* Green */\n"
"color: white;\n"
"}\n"
"QLineEdit{\n"
"padding: 12px 20px;\n"
"margin: 8px 0;\n"
"border: 2px solid #fff;\n"
"border-radius: 5px;\n"
"font:77 12px \'Arial Black\';\n"
"color:rgb(238, 238, 238);\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(-1, 1, -1, 1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnSalir = QtWidgets.QPushButton(parent=self.frame_2)
        self.btnSalir.setStyleSheet("QPushButton{\n"
"background:rgb(175, 28, 35)\n"
"}")
        self.btnSalir.setObjectName("btnSalir")
        self.horizontalLayout.addWidget(self.btnSalir)
        self.btnEntrar = QtWidgets.QPushButton(parent=self.frame_2)
        self.btnEntrar.setStyleSheet("QPushButton{\n"
"    background:rgb(75, 181, 96);\n"
"}")
        self.btnEntrar.setObjectName("btnEntrar")
        self.horizontalLayout.addWidget(self.btnEntrar)
        self.verticalLayout.addWidget(self.frame_2)
        self.verticalLayout.setStretch(0, 8)
        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "LOGIN"))
        self.label_2.setText(_translate("Dialog", "Sistema Candia Car"))
        self.label_3.setText(_translate("Dialog", "CORREO"))
        self.label_4.setText(_translate("Dialog", "CONTRASEÑA"))
        self.btnSalir.setText(_translate("Dialog", "SALIR"))
        self.btnEntrar.setText(_translate("Dialog", "ENTRAR"))
