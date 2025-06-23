import requests, json
from requests.exceptions import HTTPError
import Clases.Utils as utils
from Clases.ApiResponse import ApiResponse
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
        try:
            response = requests.post(self.url+'/persona', timeout=5, json=datos)
            response.raise_for_status()
            response = response.json()
            return ApiResponse(data=response['ok'])
        except HTTPError as err:
            print(f"error en registro de persona: {err}")
            #mejorar manejo error BAD request
            if err.response.status_code == 400:
                return ApiResponse(error=err.response.text)
            else:
                return ApiResponse(error="Error con el servidor")
        except Exception as err:
            print(f"error: {err}")
            return ApiResponse(error="Error conectando al servidor")
        