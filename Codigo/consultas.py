def filtrar_por_continente(lista):
    print("Acá va la lógica del filtro...")
    if len(lista) == 0:
        print("Error: Primero debe cargar los datos con la opción 1")
        return

    continente_buscado = input("Ingrese el continente a filtrar: ").strip().lower()

    for pais in lista:
        if pais["continente"].lower() == continente_buscado:
            print("Datos del país encontrados:", pais)


def buscar_pais(lista):
    if len(lista) == 0:
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


def agregar_pais(lista):
    print("Cargar nuevo Pais")
    nombre = input("Ingrese el nombre del país: ").strip()
    while nombre == "":
        nombre = input("El nombre no puede estar vacío. Ingrese nombre: ").strip()
        
    continente = input("Ingrese el continente: ").strip()
    while continente == "":
        continente = input("El continente no puede estar vacío. Ingrese continente: ").strip()
        
    # Validamos que la población sea un número entero válido
    while True:
        try:
            poblacion = int(input("Ingrese la población (solo números): "))
            if poblacion >= 0:
                break
            print("La población no puede ser negativa.")
        except ValueError:
            print("Error: Por favor, ingrese un número entero válido.")
            
    # Validamos que la superficie sea un número válido
    while True:
        try:
            superficie = float(input("Ingrese la superficie en km2 (solo números): "))
            if superficie >= 0:
                break
            print("La superficie no puede ser negativa.")
        except ValueError:
            print("Error: Por favor, ingrese un número numérico válido.")

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": str(poblacion),
        "superficie": str(superficie),
        "continente": continente
    }
    
    lista.append(nuevo_pais)
    print(f"¡Éxito! El país '{nombre}' fue agregado a la lista en memoria.")


def actualizar_pais(lista):
    if len(lista) == 0:
        print("Primero debes cargar los datos con la opción 1.")
        return

    nombre_buscado = input("Ingrese el nombre del país que desea modificar: ").strip().lower()
    encontrado = False

    for pais in lista:
        if pais["nombre"].strip().lower() == nombre_buscado:
            encontrado = True
            print(f"\nPaís encontrado: {pais['nombre']} ({pais['continente']})")
            print(f"Datos actuales -> Población: {pais['poblacion']} | Superficie: {pais['superficie']}")
            
            # Modificamos Población
            while True:
                try:
                    nueva_pob = int(input("Nueva población (solo números): "))
                    if nueva_pob >= 0:
                        pais["poblacion"] = str(nueva_pob)
                        break
                    print("La población no puede ser negativa.")
                except ValueError:
                    print("Error: Ingrese un número entero válido.")

            # Modificamos Superficie
            while True:
                try:
                    nueva_sup = float(input("Nueva superficie en km2 (solo números): "))
                    if nueva_sup >= 0:
                        pais["superficie"] = str(nueva_sup)
                        break
                    print("La superficie no puede ser negativa.")
                except ValueError:
                    print("Error: Ingrese un número válido.")
                    
            print(f"¡Datos de '{pais['nombre']}' actualizados correctamente!")
            break # Cortamos el bucle porque ya lo encontramos y modificamos

    if not encontrado:
        print("No se encontró ningún país con ese nombre exacto para modificar.")