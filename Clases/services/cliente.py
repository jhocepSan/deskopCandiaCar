from Clases.ComunicacionApi import send_request, HttpMethod

def NuevaPersona(datos):
    print(datos)
    return send_request(HttpMethod.POST, '/persona', datos)


def searchCodigo(codigo):
    return send_request(HttpMethod.POST, '/persona/buscarCodigo', codigo)

def ObtenerClientes():
     return send_request(url="/persona",)
