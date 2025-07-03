from Clases.ComunicacionApi import send_request, HttpMethod

def ActualizarUsuario(datos):
    return send_request(HttpMethod.POST, '/usuario/update', datos)

def CambiarEstadoUser(datos):
    return send_request(HttpMethod.POST, '/usuario/changeEstado', datos)

def ObtenerUsuarios():
    return send_request(url="/usuario")

def NuevoUsuario(datos):
    return send_request(HttpMethod.POST, '/usuario', datos)
