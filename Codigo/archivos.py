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