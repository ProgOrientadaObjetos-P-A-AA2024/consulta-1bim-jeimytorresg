class Propietario:
    nombre = "Juan"
    edad = 30

    def __init__(self, n, e):
        self.nombre = n
        self.e = e

    def establecerNombre(self, n):
        self.nombre = n

    def obtenerNombre(self):
        return self.nombre

    def establecerEdad(self, n):
        self.edad = n

    def obtenerEdad(self):
        return self.edad