# Lista de tareas pendientes, ejemplo de listas anidadas
def menu():
    print("""
    1) Agregar Tareas
    2) Completar Tareas
    3) Mostrar Tareas Pendientes
    0) Salir
    """)
    opcion = int(input("Ingrese un valor: "))
    return opcion
def mostrarTareas(tareas):
    for i in range(len(tareas)):
        tarea = tareas[i]
        estado = "[X]" if tarea[1] else "[ ]"
        print(f"{i+1} {estado} {tarea[0]}")

def agregarTarea(tareas):
    tareaNueva = input("Ingrese el nombre de la tarea nueva: ")
    tareas.append([tareaNueva, False])

def completarTareas(tareas):
    mostrarTareas(tareas)
    num = int(input("Ingrese el numero de la tarea a completar: "))
    tareas[num-1][1] = True


tareas = []
while True:
    opcion = menu()
    if opcion == 1:
        agregarTarea(tareas)
    elif opcion == 2:
        completarTareas(tareas)
    elif opcion == 3:
        mostrarTareas(tareas)
    elif opcion == 0:
        break
    else:
        print("Opcion fuera de rango")