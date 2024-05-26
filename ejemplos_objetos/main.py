import sys
import os
# determina la ruta base para poder clonar el proyecto en otro dispositivo
base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'ejemplos_clases_constructores'))
sys.path.append(base_path)
from Terreno import Terreno
from Propietario import Propietario

# Crear un objeto de tipo Propietario
prop1 = Propietario("Juan", 30)
# Enviar parametros para crear un objeto de tipo Terreno
terreno1 = Terreno(2000, prop1)

print(f"Nombre del propietario: {terreno1.obtenerPropietario().obtenerNombre()}")
print(f"Costo del terreno: {terreno1.obtenerCosto()}")