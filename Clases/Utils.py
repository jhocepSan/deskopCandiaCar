import re

URL_SERVER = 'http://192.168.1.9:4001'
SVG_BASE = "./public/fontawesome-free-6.7.2-desktop/svgs/solid/"
LIST_TIPO=[
    {'id':0,'nombre':'NINGUNO','tipo':''},
    {'id':1,'nombre':'ADMINISTRADOR','tipo':'A'},
    {'id':2,'nombre':'USUARIO','tipo':'U'},
    {'id':3,'nombre':'CLIENTE','tipo':'C'}
]
LIST_USO_APP = [
    {'id':0,'nombre':'NINGUNO','tipo':''},
    {'id':1,'nombre':'USO ESCRITORIO','tipo':'E'},
    {'id':2,'nombre':'USO WEB','tipo':'W'},
    {'id':3,'nombre':'USO APP','tipo':'A'},
    {'id':4,'nombre':'TODOS','tipo':'T'}
]

def es_correo_valido(correo: str) -> bool:
    patron = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    return re.match(patron, correo) is not None