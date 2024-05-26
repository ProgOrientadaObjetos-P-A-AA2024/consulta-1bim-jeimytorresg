import sys
import os
sys.path.append(os.path.abspath("C:\\Users\\USUARIO\\Desktop\\consulta-1bim-jeimytorresg\\ejemplos_clases_constructores"))

from Propietario import Propietario


class Terreno:
    costo: 4500
    propietario = Propietario("Juan", 20)

    def __init__(self, c, p):
        self.costo = c
        self.propietario = p

    def establecerCosto(self, n):
        self.costo = n

    def obtenerCosto(self):
        return self.costo

    def establecerPropietario(self, p):
        self.propietario = p

    def obtenerPropietario(self):
        return self.propietario