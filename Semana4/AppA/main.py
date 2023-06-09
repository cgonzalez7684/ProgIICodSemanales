
altura = int(input("Ingrese la altura del triángulo: "))

#int(variable)
#float(variable)
#str(variable)

# Variable para controlar el número de asteriscos en cada fila
num_asteriscos = 1

# Variable para controlar el número de espacios en cada fila
num_espacios = altura - 1


# Bucle while para dibujar el triángulo
while altura > 0:
    # Imprimir espacios en blanco
    print(" " * num_espacios, end="")
    
    # Imprimir asteriscos
    print("*" * num_asteriscos)
    
    # Incrementar el número de asteriscos y decrementar el número de espacios para la siguiente fila
    num_asteriscos += 2
    num_espacios -= 1
    
    # Decrementar la altura del triángulo
    altura -= 1
    
print("\rFin del dibujo")    
