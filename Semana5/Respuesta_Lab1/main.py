def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

limite = int(input("Ingrese un número límite: "))

print("Números pares hasta el límite:", limite)

for num in range(2, limite+1):
    if es_par(num):
        print(num)
