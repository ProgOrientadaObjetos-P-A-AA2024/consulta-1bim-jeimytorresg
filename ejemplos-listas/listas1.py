# Ordenar de menor a mayor una lista ingresada por teclado
lista = []
for i in range(6):
    valor = int(input("Ingrese un valor: "))
    lista.append(valor)
for i in range(len(lista)):
    for j in range(0,len(lista) - 1):
        if lista[j] > lista[j+1]:
            aux = lista[j]
            lista[j] = lista[j+1]
            lista[j+1] = aux

print(lista)