from PyQt6.QtWidgets import QLabel,QWidget
from PyQt6.QtCore import Qt, QTimer

def mostrar_toast_error(parent: QWidget, texto: str, duracion_ms: int = 3000):
    toast = QLabel(parent)
    toast.setText(texto)
    toast.setStyleSheet("""
        QLabel {
            background-color: #d32f2f;
            color: white;
            padding: 10px;
            border-radius: 5px;
            font-weight: bold;
            border-color:#ffffff;
        }
    """)
    toast.setAlignment(Qt.AlignmentFlag.AlignCenter)
    toast.setWindowFlags(Qt.WindowType.ToolTip)
    toast.adjustSize()
    toast.move(parent.geometry().center() - toast.rect().center())
    toast.show()

    QTimer.singleShot(duracion_ms, toast.close)

def mostrar_toast_correcto(parent:QWidget,texto:str,duracion_ms:int=3000):
    toast = QLabel(parent)
    toast.setText(texto)
    toast.setStyleSheet("""
        QLabel {
            background-color:  #71ff9c;
            color:  #000000;
            padding: 10px;
            border-radius: 5px;
            font-weight: bold;
            border-color:#ffffff;
        }
    """)
    toast.setAlignment(Qt.AlignmentFlag.AlignCenter)
    toast.setWindowFlags(Qt.WindowType.ToolTip)
    toast.adjustSize()
    toast.move(parent.geometry().center() - toast.rect().center())
    toast.show()

    QTimer.singleShot(duracion_ms, toast.close)


def mostrar_WIP(parent:QWidget):
    toast = QLabel(parent)
    toast.setText("PROCESANDO...")
    toast.setStyleSheet("""
        QLabel {
            background-color:  #ffffff;
            color:  #000000;
            padding: 10px;
            border-radius: 5px;
            font-weight: bold;
            border-color:#ffffff;
        }
    """)
    toast.setAlignment(Qt.AlignmentFlag.AlignCenter)
    toast.setWindowFlags(Qt.WindowType.ToolTip)
    toast.adjustSize()
    toast.move(parent.geometry().center() - toast.rect().center())
    toast.show()
    return toast
