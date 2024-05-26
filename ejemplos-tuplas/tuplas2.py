# Ingresar una tupla por teclado y un numero
# Buscar cuantas veces se repite ese numero en la tupla
tupla = []
n = (int(input("Ingrese el tamaño: ")))
for i in range(n):
    valor = int(input("Ingrese un numero: "))
    tupla.append(valor) # no se puede ingresar valores a una tupla, por
                 # lo tanto, se inicializa una lista y se convierte a tupla

tupla = tuple(tupla) # conviertiendola en tupla

numero = int(input("Ingrese el numero a buscar: "))

c = tupla.count(numero)

if c == 0:
    print("No se encontró ese valor en la tupla")
else: print(f"El valor {numero} se repitio {c} veces")