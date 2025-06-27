import re,os,json,jwt, shutil

URL_SERVER = 'http://192.168.1.9:4001'
RUTA_SESSION = './public/carCandi.json'
SVG_BASE = "./public/fontawesome-free-6.7.2-desktop/svgs/solid/"
LIST_TIPO=[
    {'id':0,'nombre':'NINGUNO','tipo':''},
    {'id':1,'nombre':'ADMINISTRADOR','tipo':'A'},
    {'id':2,'nombre':'USUARIO','tipo':'U'},
    {'id':3,'nombre':'CLIENTE','tipo':'C'}
]
LIST_USO_APP = [
    {'id':0,'nombre':'NINGUNO','tipo':''},
    {'id':1,'nombre':'USO ESCRITORIO','tipo':'D'},
    {'id':2,'nombre':'USO WEB','tipo':'W'},
    {'id':3,'nombre':'USO APP','tipo':'A'},
    {'id':4,'nombre':'TODOS','tipo':'T'}
]
SECRET_APP ='jj@ch'
public_path_vehiculos = os.path.abspath("./public/vehiculos/")
def es_correo_valido(correo: str) -> bool:
    patron = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    return re.match(patron, correo) is not None

def test_session_user() -> bool:
    if os.path.exists(RUTA_SESSION):
        with open(RUTA_SESSION,'r') as f:
            result = json.load(f)
            info = jwt.decode(result['usuario'],SECRET_APP,algorithms=["HS256"])
            return info
    return None

def get_data_token(dato):
    info = jwt.decode(dato['usuario'],SECRET_APP,algorithms=["HS256"])
    return info
def save_session_user(usuario) -> bool:
    try:
        with open(RUTA_SESSION, 'w') as f:
            json.dump(usuario, f)
        return True
    except:
        return False

def upload_photo_to_public(file_path: str):
    try:
        shutil.copy(file_path, public_path_vehiculos)
    except FileNotFoundError as e:
        print(f"Error: Specified file or directory not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
