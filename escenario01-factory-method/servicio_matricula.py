from creadores import CreadorVehiculo
from vehiculos import Vehiculo


class ServicioMatricula:
    def calcularMatricula(self, creador: CreadorVehiculo, placa, marca, modelo, anioFabricacion, avaluo):
        vehiculo: Vehiculo = creador.crearVehiculo(placa, marca, modelo, anioFabricacion, avaluo)
        return vehiculo.calcularCostoMatricula()
