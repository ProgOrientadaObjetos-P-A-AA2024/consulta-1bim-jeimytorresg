import sys
import os

sys.path.append(os.path.abspath("C:\\Users\\USUARIO\\"
                                "Desktop\\consulta-1bim-jeimytorresg\\"
                                "ejemplos_clases_constructores"))
from Terreno import Terreno
from Propietario import Propietario

prop1 = Propietario("Juan", 30)

terreno1 = Terreno(2000, prop1)

print(f"Nombre del propietario: {terreno1.obtenerPropietario().obtenerNombre()}")
print(f"Costo del terreno: {terreno1.obtenerCosto()}")