from archivos import cargar_datos, exportar_reporte
from consultas import filtrar_por_continente, ordenar_paises, buscar_pais, agregar_pais, actualizar_pais
from estadisticas import mostrar_estadisticas

listas_paises = []
opcion = 0

def salir_sistema(lista):
    print("Cerrando sesion...")
    print("...")
    print("...")
    print("Sesion cerrada")

def mostrar_menu():
    print("\n--- MENÚ DEL TPI ---")
    print("1. Cargar datos desde CSV")
    print("2. Filtrar por continente")
    print("3. Ordenar países")
    print("4. Buscar país")
    print("5. Mostrar estadísticas")
    print("6. Exportar reporte")
    print("7. Agregar un nuevo país")
    print("8. Actualizar población/superficie de un país")
    print("9. Salir del sistema")

# --- Ejecución del Programa ---
while opcion != 9:
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
            exportar_reporte(listas_paises)
        elif opcion == 7:
            agregar_pais(listas_paises)
        elif opcion == 8:
            actualizar_pais(listas_paises)
        elif opcion == 9: 
            salir_sistema(listas_paises)
            break
        else: 
            print("Opción inválida. Elija un número del 1 al 9.")
            
    except ValueError:
        print("Error: Por favor, ingrese un número entero del 1 al 9.")