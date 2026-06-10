import csv

listas_paises = []
opcion = 0


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
            print("Próximamente opción 2...")
        elif opcion == 3:  
            print("Próximamente opción 3...")
        elif opcion == 4:  
            print("Próximamente opción 4...")
        elif opcion == 5:  
            print("Próximamente opción 5...")
        elif opcion == 6: 
            print("Próximamente opción 6...")
        elif opcion == 7: 
            print("Saliendo del sistema... ")
        else: 
            print("Opción inválida. Elija un número del 1 al 7.")
            
    except ValueError:
        print("Error: Por favor, ingrese un número entero del 1 al 7.")