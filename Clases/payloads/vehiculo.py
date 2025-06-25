class VehiculoCreate:
	def __init__(self, modelo:str=None, placa:str=None, color:str=None, tipoId:int=None, 
              tipoNombre:str=None, motor:str=None, km:str=None, fotoplaca:str=None, foto:str=None):
		self.modelo = modelo
		self.placa = placa
		self.color = color
		self.tipoId = tipoId
		self.tipoNombre = tipoNombre
		self.motor = motor
		self.km = km
		self.fotoplaca = fotoplaca
		self.foto = foto
