import csv

def cargar_datos(lista):
    try:
        lista.clear() 
        
        with open("paises.csv", mode="r", encoding="utf-8") as archivo:
            print("¡Archivo abierto con éxito!")
            lector = csv.DictReader(archivo)
            
            for fila in lector:
                pais_limpio = {}
                for clave, valor in fila.items():
                    pais_limpio[clave.strip()] = valor.strip()
                
                lista.append(pais_limpio)
            
            print(f"¡Éxito! Se cargaron {len(lista)} países.")

    except FileNotFoundError:
        print("Error: No se encontró el archivo 'paises.csv' en la carpeta raíz.")
        

def exportar_reporte(lista):
    try:
        with open("paises.csv", "w") as archivo:  #abrimos el archivo en modo escritura (w)
            archivo.write("nombre,poblacion,superficie,continente\n") #primera fila
            
            for pais in lista:  #recorremos la lista
                linea = (f"{pais['nombre']},{pais['poblacion']},{pais['superficie']}, {pais['continente']}\n")  #convertimos el diccionario en texto y agregamos con write
                archivo.write(linea)

        print("Reporte exportado correctamente")

    except:
        print("Error al exportar el archivo")