
import csv

listas_paises = []
opcion = 0


def salir_sistema(lista):
    print("Cerrando sesion...")
    print("...")
    print("...")
    print("Sesion cerrada")
    
    



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




def buscar_pais(lista):
    if len(listas_paises) == 0:
        print("Primero debes cargar los datos")
        return

    nombre_buscado = input("Ingrese el nombre del pais: ").strip().lower() #para que saque espacios y pase a minusculas
    encontrado = False  # Para saber si lo encontramos o no 

    for pais in lista: #recorre cada pais
        if nombre_buscado in pais["nombre"].strip().lower():  #Busca el nombre exacto o coincidencia parcial 
            print(f"Nombre: {pais['nombre']}")
            print(f"Poblacion: {pais['poblacion']}")
            print(f"Superficie: {pais['superficie']}")
            print(f"Continente: {pais['continente']}")
            encontrado = True  #Si encotramos True

    if encontrado == False:  #Si no encontramos False
        print("No se encontro el pais")
    

def ordenar_paises(lista):

    print("Ordenar por: ")
    print("1. Nombre")
    print("2.Poblacion")
    print("3.Superficie ")

    opcion1 = input("Elegi opcion: (1/2/3): ")

    print("Orden: (1/2)")
    print("1. Ascendente")
    print("2. Descendente")

    orden = input("Elegi orden: ")

    n = len(lista) #tamaño de la lista (cuantos hay)

    for i in range(n): #se repite segun el tamaño de lista 
        for j in range(0, n - 1 -i): #metodo burbuja #compara de a pares j = actual j+1 = siguiente

            if opcion1 == "1":
                a = lista[j]["nombre"] #lista actual j
                b = lista[j + 1]["nombre"] #lista siguiente j + 1

            elif opcion1 == "2":
                a = int(lista[j]["poblacion"])
                b = int(lista[j + 1]["poblacion"])

            elif opcion1 == "3":
                a = float(lista[j]["superficie"])
                b = float(lista[j + 1]["superficie"])
            else:
                print("Opcion invalida")
                return
            
            if (orden == "1" and a > b) or (orden == "2" and a < b): #si es ascendente(1) intercambia a > b o descendente(2) a < b
               #intercambio de posiciones
                aux = lista[j]  #guardo valor de lista[j] en variable temporal
                lista[j] = lista [j+ 1] #reemplaza lista[j] con el contenido lista[j+1]
                lista[j + 1] = aux   ##coloca el valor guardado dentro de lista[j+1]
               

    print("Lista ordenada: ")
    for pais in lista:
        print(pais)



def filtrar_por_continente(lista):
    print("Acá va la lógica del filtro...")
    if len(lista) == 0:
        print("Error: Primero debe cargar los datos con la opción 1")
        return

    continente_buscado = input("Ingrese el continente a filtrar: ").strip().lower()

    for pais in lista:
        if pais["continente"].lower() == continente_buscado:
            print("Datos del país encontrados:", pais)

def cargar_datos(lista):
    try:
        lista.clear() 
        
        with open("paises.csv", mode="r", encoding="utf-8") as archivo:
            print("¡Archivo abierto con éxito!")
            lector = csv.DictReader(archivo)
            for fila in lector:
                lista.append(fila)
            
            print(f"¡Éxito! Se cargaron {len(lista)} países.")

    except FileNotFoundError:
        print("Error: No se encontró el archivo 'paises.csv' en esta carpeta.")

def mostrar_menu():
    print("\n--- MENÚ DEL TPI ---")
    print("1. Cargar datos desde CSV")
    print("2. Filtrar por continente")
    print("3. Ordenar países")
    print("4. Buscar país")
    print("5. Mostrar estadísticas")
    print("6. Exportar reporte")
    print("7. Salir del sistema")


while opcion != 7:
    try:
        mostrar_menu()
        opcion = int(input("Seleccione una opcion: "))
        
        if opcion == 1:
            cargar_datos(listas_paises)
        elif opcion == 2:  
            filtrar_por_continente(listas_paises)
        elif opcion == 3:  
            ordenar_paises(listas_paises)
        elif opcion == 4:  
            buscar_pais(listas_paises)
        elif opcion == 5:  
            mostrar_estadisticas(listas_paises)
        elif opcion == 6: 
            print("Próximamente opción 6...")
        elif opcion == 7: 
            salir_sistema(listas_paises)
            break
        else: 
            print("Opción inválida. Elija un número del 1 al 7.")
            
    except ValueError:
        print("Error: Por favor, ingrese un número entero del 1 al 7.")