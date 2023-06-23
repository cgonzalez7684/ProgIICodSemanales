listadoAutos = ["Toyota","Toyota","Nissan","Hyundai"] #list 

for auto in listadoAutos:
    print(auto)
    
cantidadAutos = len(listadoAutos)  

print("Cantidad de elementos {0}".format(cantidadAutos))  

aux = listadoAutos.count("Toyota")

print("Cantidad de Toyotas en la lista {0}".format(aux))

listadoAutos[1] = "Mazda"

for auto in listadoAutos:
    print(auto)

print("------------------------------")
    
listadoAutos.insert(0,"Ferrari") 

for auto in listadoAutos:
    print(auto)   
    
print("------------------------------") 
    
listadoAutos.insert(4,"Renault")   

for auto in listadoAutos:
    print(auto)
    
print("------------------------------") 

listadoAutos.append("Bosh")       

for auto in listadoAutos:
    print(auto)
    
print("------------------------------") 

autoBuscado = "Bosh"
seEncontro = autoBuscado in listadoAutos

print("Se encuentra {0} en la coleccion?? Respueta: {1}".format(autoBuscado,seEncontro))

print("------------------------------") 

if (seEncontro):
    listadoAutos.remove(autoBuscado)
    
for auto in listadoAutos:
    print(auto)   

print("------------------------------") 

try:
    
    indice = listadoAutos.index("Toyota")    
    
    if (indice > 0):
        listadoAutos[indice] = listadoAutos[indice].upper()
        
        for auto in listadoAutos:
            print(auto)  
        
except BaseException:
    print("El elemento no se encuentra en la coleccion")
    
print("------------------------------") 

del listadoAutos[4]    

for auto in listadoAutos:
    print(auto)
    
#del listadoAutos    
    
#for auto in listadoAutos:
#    print(auto)   

print("------------------------------") 

listadoAutos.sort()

for auto in listadoAutos:
    print(auto)    


print("------------------------------vacia") 

listadoAutos.clear()

for auto in listadoAutos:
    print(auto)  