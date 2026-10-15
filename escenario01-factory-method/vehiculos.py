from abc import ABC, abstractmethod
from datetime import date


class Vehiculo(ABC):
    def __init__(self, placa, marca, modelo, anioFabricacion, avaluo):
        self._placa = placa
        self._marca = marca
        self._modelo = modelo
        self._anioFabricacion = anioFabricacion
        self._avaluo = avaluo

    def _antiguedad(self):
        return date.today().year - self._anioFabricacion

    @abstractmethod
    def calcularCostoMatricula(self):
        pass


class Auto(Vehiculo):
    def calcularCostoMatricula(self):
        return self._avaluo * 0.015 + 10 * self._antiguedad()


class Camioneta(Vehiculo):
    RECARGO_POR_USO = {"personal": 0.0, "trabajo": 0.02, "carga": 0.05}

    def __init__(self, placa, marca, modelo, anioFabricacion, avaluo, capacidad, uso):
        super().__init__(placa, marca, modelo, anioFabricacion, avaluo)
        self._capacidad = capacidad
        self._uso = uso

    def calcularCostoMatricula(self):
        base = self._avaluo * 0.015 + 10 * self._antiguedad()
        return base + self._avaluo * self.RECARGO_POR_USO[self._uso]


class Camion(Vehiculo):
    def __init__(self, placa, marca, modelo, anioFabricacion, avaluo, tonelaje, capacidadCarga):
        super().__init__(placa, marca, modelo, anioFabricacion, avaluo)
        self._tonelaje = tonelaje
        self._capacidadCarga = capacidadCarga

    def calcularCostoMatricula(self):
        return self._avaluo * 0.02 + 20 * self._tonelaje + 0.5 * self._capacidadCarga
