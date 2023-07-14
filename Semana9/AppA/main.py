lista_espera_aviones = []

def agregar_avion(numero_vuelo):
    lista_espera_aviones.append(numero_vuelo)
    print("Avión con número de vuelo", numero_vuelo, "agregado a la lista de espera.")

def mostrar_lista_espera():
    print("Aviones en espera:")
    for i, avion in enumerate(lista_espera_aviones):
        print(i+1, "-", avion)

def eliminar_avion(numero_vuelo):
    if numero_vuelo in lista_espera_aviones:
        lista_espera_aviones.remove(numero_vuelo)
        print("Avión con número de vuelo", numero_vuelo, "eliminado de la lista de espera.")
    else:
        print("El avión con número de vuelo", numero_vuelo, "no está en la lista de espera.")

def buscar_avion(numero_vuelo):
    if numero_vuelo in lista_espera_aviones:
        posicion = lista_espera_aviones.index(numero_vuelo) + 1
        print("El avión con número de vuelo", numero_vuelo, "está en la posición", posicion, "de la lista de espera.")
    else:
        print("El avión con número de vuelo", numero_vuelo, "no está en la lista de espera.")

def mostrar_cantidad_aviones():
    cantidad = len(lista_espera_aviones)
    print("Cantidad total de aviones en espera:", cantidad)

while True:
    print("\n--- Aeropuerto - Sistema de Control de Aviones ---")
    print("1. Agregar avión a la lista de espera")
    print("2. Mostrar lista de espera")
    print("3. Eliminar avión de la lista de espera")
    print("4. Buscar avión en la lista de espera")
    print("5. Mostrar cantidad total de aviones en espera")
    print("6. Salir del programa")
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        numero_vuelo = input("Ingrese el número de vuelo del avión: ")
        agregar_avion(numero_vuelo)
    elif opcion == "2":
        mostrar_lista_espera()
    elif opcion == "3":
        numero_vuelo = input("Ingrese el número de vuelo del avión que despegó: ")
        eliminar_avion(numero_vuelo)
    elif opcion == "4":
        numero_vuelo = input("Ingrese el número de vuelo del avión a buscar: ")
        buscar_avion(numero_vuelo)
    elif opcion == "5":
        mostrar_cantidad_aviones()
    elif opcion == "6":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, ingrese un número del 1 al 6.")
