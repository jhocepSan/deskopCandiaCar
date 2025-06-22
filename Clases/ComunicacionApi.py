import requests, json
import Clases.Utils as utils
class ComunicacionApi(object):
    def __init__(self):
        self.url = utils.URL_SERVER

    def ObtenerUsuarios(self):
        try:
            result = requests.get(self.url+"/usuario/getUsuarios",timeout=5)
            if result.status_code == 200:
                return result.json()
            else:
                return result.json()
        except (requests.RequestException,requests.ConnectTimeout):
            return {'error':'No hay conexion a la api'}

    def NuevoUsuario(self,datos):
        try:
            print(datos)
            #result = requests.post(self.url+'/auth/signin',timeout=5,json=datos)
            #if result.status_code == 200:
            #    return result.json()
            #else:
            #    return result.json()
            return {'ok':'ok'}
        except (requests.RequestException,requests.ConnectTimeout):
            return {'error':"No hay conexion a la api"}

    def NuevaPersona(self, datos):
        print(datos)
        result = requests.post(self.url+'/persona', timeout=5, json=datos)
        result = result.json()
        return result['ok']
