#import funciones as fn
from funciones import elevarPotenciaB as eleB

def Main():
    print("Opcion #1: Calculo de Tasa")
    print("Opcion #2: Imprima reporte")
    print("Opcion #3: Salir del sistema")
    try:
        while True: 
            tecla = input("Digitar opcion: ")
            if (not(tecla.isdigit())):
                print('Debe digitar un numero')
                continue
            i = int(tecla)
            if i == 1:
                print('Elevar numero a la potencia')   
                #n = fn.elevarPotenciaB(2,3)                    
                n = eleB(2,3)
                print("El resultado final es ",n)
            elif i==2:
                print('Imprimiendo reporte....')           
            elif i==3:
                break
            else:
                print('Opcion invalida')
                continue 
    except BaseException:
        print("Finalizó el programa, cualquier tecla para cerrar ventanda...")
        input()
        #Mostrar un mensaje de error amigable al usuario "Favor contacar admistrador..."
        #Registrar error en bitacora txt / registrado bd (el momento/usuario/error tecnico / los datos)
        #Notifación error


if __name__ == '__main__':
    Main()
    
