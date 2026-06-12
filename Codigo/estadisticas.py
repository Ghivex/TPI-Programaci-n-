def mostrar_estadisticas(lista):

    if len(lista) == 0:   #validar datos, si esta vacia cargar datos 
        print("Primero debes cargar los datos")
        return
    
    mayor_poblacion = lista[0] #mayor y menor 
    menor_poblacion = lista[0] #primer pais 

    suma_poblacion = 0    #variables acumuladoras 
    suma_superficie = 0
    contador = 0
    
    continentes = {} #diccionario vacio 



    for pais in lista: #recorre los paises de la lista
        if pais["poblacion"] > mayor_poblacion["poblacion"]: #mayor poblacion
            mayor_poblacion = pais

        if pais["poblacion"] < menor_poblacion["poblacion"]: #menor poblacion
            menor_poblacion = pais 
        
        suma_poblacion += int(pais["poblacion"]) #sumar valores  y agrega a suma_poblacion
        suma_superficie += float(pais["superficie"])   #suma y agrega a suma_superficie
        contador += 1 #el contador cuenta los paises recorridos


        cont = pais["continente"] #guarda el continente del pais actual en la variable cont
        if cont in continentes: #verifica si el continente existe ya en continentes
            continentes[cont] += 1  #si el continente ya existe suma 1
        else:
            continentes[cont] = 1  #si no existe lo crea con 1 

    #Promedios: suma / cantidad 
    promedio_poblacion = suma_poblacion / contador
    promedio_superficie = suma_superficie / contador

    #resultado
    print("Mayor poblacion", mayor_poblacion["nombre"])
    print("Menor poblacion:", menor_poblacion["nombre"])
    print("Promedio poblacion:", promedio_poblacion)
    print("Promedio superficie:", promedio_superficie)

    print("Cantidad de paises por continente: ")  
    for cont, cantidad in continentes.items(): #items para que devuelva pares # cont guarda la clave(continente) # cantidad guarda el valor (cantidad)
        print(cont, ":", cantidad) 
