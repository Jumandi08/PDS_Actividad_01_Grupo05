from abc import ABC, abstractmethod

from vehiculos import Auto, Camioneta, Camion, Vehiculo


class CreadorVehiculo(ABC):
    @abstractmethod
    def crearVehiculo(self, placa, marca, modelo, anioFabricacion, avaluo) -> Vehiculo:
        pass


class CreadorAuto(CreadorVehiculo):
    def crearVehiculo(self, placa, marca, modelo, anioFabricacion, avaluo) -> Vehiculo:
        return Auto(placa, marca, modelo, anioFabricacion, avaluo)


class CreadorCamioneta(CreadorVehiculo):
    def __init__(self, capacidad, uso):
        self._capacidad = capacidad
        self._uso = uso

    def crearVehiculo(self, placa, marca, modelo, anioFabricacion, avaluo) -> Vehiculo:
        return Camioneta(placa, marca, modelo, anioFabricacion, avaluo, self._capacidad, self._uso)


class CreadorCamion(CreadorVehiculo):
    def __init__(self, tonelaje, capacidadCarga):
        self._tonelaje = tonelaje
        self._capacidadCarga = capacidadCarga

    def crearVehiculo(self, placa, marca, modelo, anioFabricacion, avaluo) -> Vehiculo:
        return Camion(placa, marca, modelo, anioFabricacion, avaluo, self._tonelaje, self._capacidadCarga)
