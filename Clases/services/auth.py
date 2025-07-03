from Clases.ComunicacionApi import send_request, HttpMethod

def IniciarSesion(datos):
    return send_request(HttpMethod.POST, '/auth/signin', datos)
