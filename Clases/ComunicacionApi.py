import requests,json
import Clases.Utils as utils
class ComunicacionApi(object):
    def __init__(self):
        self.url = utils.URL_SERVER
    def ObtenerUsuarios(self):
        try:
            result = requests.get(self.url+"/usuario",timeout=5)
            if result.status_code == 200:
                return result.json()
            else:
                return result.json()
        except (requests.RequestException,requests.ConnectTimeout):
            return {'error':'No hay conexion a la api'}
    def NuevoUsuario(self,datos):
        try:
            result = requests.post(self.url+'/usuario',timeout=5,json=datos)
            if result.status_code == 200:
                return result.json()
            else:
                return result.json()
        except (requests.RequestException,requests.ConnectTimeout):
            return {'error':"No hay conexion a la api"}
    def IniciarSesion(self,datos):
        try:
            result = requests.post(self.url+'/auth/signin',timeout=5,json=datos)
            if result.status_code == 200:
                return result.json()
            else:
                return result.json()
        except (requests.RequestException,requests.ConnectTimeout):
            return {'error':"No hay conexion a la api"}
    def ActualizarUsuario(self,datos):
        try:
            result = requests.post(self.url+'/usuario/update',timeout=5,json=datos)
            if result.status_code ==200:
                return result.json()
            else:
                return result.json()
        except (requests.RequestException,requests.ConnectTimeout):
            return {'error':"No hay conexion a la api"}
    def CambiarEstadoUser(self,datos):
        try:
            result = requests.post(self.url+'/usuario/changeEstado',timeout=5,json=datos)
            if result.status_code ==200:
                return result.json()
            else:
                return result.json()
        except (requests.RequestException,requests.ConnectTimeout):
            return {'error':"No hay conexion a la api"}