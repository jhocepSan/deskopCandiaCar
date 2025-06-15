import requests,json
class ComunicacionApi(object):
    def __init__(self):
        self.url = "http://192.168.1.9:4001"
    def ObtenerUsuarios(self):
        try:
            result = requests.get(self.url+"/usuario/getUsuarios",timeout=5)
            if result.status_code == 200:
                return result.json()
            else:
                return result.json()
        except (requests.RequestException,requests.ConnectTimeout):
            return {'error':'No hay conexion a la api'}