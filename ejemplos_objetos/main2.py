class Profesor:
    def __init__(self):
        self.nombre = "Juan"
        self.edad = 30
    def establecerNombre(self, n):
        self.nombre = n
    def obtenerNombre(self):
        return self.nombre
    def establecerEdad(self, n):
        self.edad = n
    def obtenerEdad(self):
        return self.edad

class Materia:
    def __init__(self):
        self.nombre = "Calculo"
        profesor1 = Profesor()
        self.profesor = profesor1
    def establecerNombre(self, n):
        self.nombre = n
    def obtenerNombre(self):
        return self.nombre
    def establecerProfesor(self, n):
        self.profesor = n
    def obtenerProfesor(self):
        return self.profesor


materia1 = Materia()
profesor1 = Profesor()
profesor1.establecerNombre("Maria Ruiz")
materia1.establecerProfesor(profesor1)
print(f"Nombre de la Materia: {materia1.obtenerNombre()}")
print(f"Nombre del Profesor: {materia1.obtenerProfesor().obtenerNombre()}")
print(f"Edad del Profesor: {materia1.obtenerProfesor().obtenerEdad()}")