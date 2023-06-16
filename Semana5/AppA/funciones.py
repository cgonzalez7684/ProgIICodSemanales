def elevarPotenciaA(base,exponente = 2):    
    resultado = 1
    for n in range(exponente):
        resultado *= base 
    return resultado 

def elevarPotenciaB(base,exponente):    
    return base ** exponente

#elevarPotencia(2,3,3,5,5,6)
def elevarPotenciaC(*args):
    resultado = 1
    for n in range(args[1]):
        resultado *= args[0]     
    return resultado

def elevarPotenciaD(**Kwargs):
    resultado = 1
    for n in range(Kwargs['exponente']):
        resultado *= Kwargs['base']     
    return resultado

#resultadoElevarPotencia = elevarPotenciaB(2,3)
#resultadoElevarPotencia = elevarPotenciaB(exponente= 3, base = 2)
#resultadoElevarPotencia = elevarPotenciaD(exponente= 3, base = 2, color = 'Azul')

#resultadoElevarPotencia = elevarPotenciaC(2,3,5,6,7,100,'A',True)

#print("Resultado ",resultadoElevarPotencia)

#base = int(input("Favor ingresar base"))
#exponente = int(input("Favor ingresar exponente"))

#resultadoElevarPotencia = elevarPotencia(2)



#str String - Cadena Texto
#El numero 2 elevado a la pontencia 3 da como resultado 8
#etiqueta = "El numero {0} elevado a la potencia {1} da como resultado {2}"
#imprimirEtiqueta = etiqueta.format(2,3,resultadoElevarPotencia)

#print(imprimirEtiqueta)

#input()

    
    
#Queremo elevar 2 a la potencia 3
#2 * 2 * 2 = 8  




    
    