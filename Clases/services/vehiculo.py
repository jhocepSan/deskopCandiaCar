from Clases.payloads.vehiculo import VehiculoModel
from Clases.ComunicacionApi import send_request, HttpMethod

def registrar_vehiculo(datos: VehiculoModel):
    datos = datos.__dict__
    print(datos)
    return send_request(HttpMethod.POST, '/vehiculo', datos)

def buscar_vehiculo(placa: str):
    return send_request(url='/vehiculo/?placa=' + placa)

def update_vehiculo(datos: VehiculoModel):
    datos = datos.__dict__
    print(datos)
    return send_request(HttpMethod.PUT, '/vehiculo', datos)

def getTipoVehiculos():
    return send_request(url="/vehiculo/tipos")
