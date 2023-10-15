
from models import Cities
from flask import current_app

class CityPicklist():

    def __init__(self,cityQuery = None):
        self.app = current_app
        self.ubicaciones = cityQuery

    

    def getciudades(self):
        if self.ubicaciones is None:
            cities = ['city1']
        else: 
            cities = sorted(set(ubicacion.ciudad for ubicacion in self.ubicaciones))
        
        return cities

        #return [(city, city) for city in cities]

    def getprovincias(self):
        if self.ubicaciones is None:
            provincias = ['pronvince1']
        else:
            provincias = sorted(set(ubicacion.provincia for ubicacion in self.ubicaciones))

        return provincias
        #return [(provincia, provincia) for provincia in provincias]

    def getpaises(self):
        if self.ubicaciones is None:
            paises = ['pais1']
        else:
            paises =sorted(set(ubicacion.pais for ubicacion in self.ubicaciones))

        return paises
        #return [(pais, pais) for pais in paises]
    
    
    
   


tipoIdList = ['CC', 'CE', 'NIT','Pasaporte']
estadoList =[ 'A', 'I']
estadoInmuebleList =[ 'D', 'O', 'I']
tipoAlquilerList=[ 'Apartamento','Habitación', 'Local']