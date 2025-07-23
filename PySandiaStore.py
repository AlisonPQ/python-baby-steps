# Función para imprimir el banner del programa
def imprimir_banner(): 
    print(r"""
  ____        ____                  _ _         ____  _                 
 |  _ \ _   _/ ___|  __ _ _ __   __| (_) __ _  / ___|| |_ ___  _ __ ___ 
 | |_) | | | \___ \ / _` | '_ \ / _` | |/ _` | \___ \| __/ _ \| '__/ _ \
 |  __/| |_| |___) | (_| | | | | (_| | | (_| |  ___) | || (_) | | |  __/
 |_|    \__, |____/ \__,_|_| |_|\__,_|_|\__,_| |____/ \__\___/|_|  \___|
        |___/                                                           
                         ____  _             _   _   _ _                          
                        |__ / | |__ ___  ___| | | |_(_| |___                      
                         |_ \ | '_ (_-< / -_| | | / | | / _ \                     
                        |___/ |_.__/__/ \___|_| |_\_|_|_\___/
""")
    
ARCHIVO_VENTAS = "ventas.csv"
PRECIO_POR_KILO = 3  # Precio fijo en Bs por kilo

locations = [
    ("La Paz", 28.21, 15.5),
    ("Cochabamba", 25.28, 14.3),
    ("Santa Cruz", 21.7, 12.6),
    ("Oruro", 20.8, 13.2),
    ("Potosi", 22.1, 13.6),
    ("Tarija", 21.5, 13.4)
]

# Función para inicializar el archivo de ventas
def inicializar_archivo():
    # Abrimos en modo 'a' para crear el archivo si no existe
    archivo = open(ARCHIVO_VENTAS, "a")
    archivo.close()

    # Abrimos en modo 'r' para leer su contenido
    archivo = open(ARCHIVO_VENTAS, "r")
    contenido = archivo.read()
    archivo.close()

    # Si está vacío, escribimos el encabezado
    if contenido == "":
        archivo = open(ARCHIVO_VENTAS, "a")
        archivo.write("peso,precio_por_kilo,total\n")
        archivo.close()

# Función para registrar una venta
def registrar_venta(): 
    peso = input("¿Cuántos kilos de sandía se vendieron? ")

    # Verificamos que el peso sea un número entero
    if peso.isdigit(): 
        with open(ARCHIVO_VENTAS, "a") as archivo:
            peso_int = int(peso)
            total = peso_int * PRECIO_POR_KILO
            archivo.write(f"{peso_int},{PRECIO_POR_KILO},{total}\n")
        print(f"✅ Venta registrada: {peso_int} kg a {PRECIO_POR_KILO} Bs/kg = {total} Bs")
    else:
        print("❌ Ingresa un número entero válido.")

# Función para buscar tiendas por departamento
def buscar_tiendas(): 
    ciudad = input("¿En qué departamento quieres buscar tiendas? ")
    encontrado = False

    for location in locations:
        if location[0].lower() == ciudad.lower():
            print(f"✅ Tienda encontrada: {location}")
            encontrado = True

    if not encontrado:
        print("❌ No hay tiendas en ese departamento.")

# Función para mostrar el registro de ventas
def mostrar_registro_ventas():
    print("\n📒 REGISTRO DE VENTAS:")
    with open(ARCHIVO_VENTAS, "r") as archivo:
        lineas = archivo.readlines()

    if len(lineas) <= 1:
        print("No hay ventas registradas.")
        return

    for i, linea in enumerate(lineas[1:], 1):  # saltar encabezado
        peso, precio, total = linea.strip().split(",")
        print(f"{i}. Peso: {peso} kg | Precio: {precio} Bs/kg | Total: {total} Bs")

# Función para mostrar el menú de opciones
def mostrar_menu():
    print("\n--- MENÚ DE SANDÍAS ---")
    print("1. Registrar venta")
    print("2. Buscar tiendas")
    print("3. Ver registro de ventas")
    print("4. Salir")

# Función principal del programa
def main():
    imprimir_banner()
    inicializar_archivo()

    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-4): ")

        if opcion == "1":
            registrar_venta()
        elif opcion == "2":
            buscar_tiendas()
        elif opcion == "3":
            mostrar_registro_ventas()
        elif opcion == "4":
            print("Gracias por visitar PySandia Store, hasta pronto! 🍉")
            break
        else:
            print("❌ Opción no válida.")

# Llamamos a la función principal para ejecutar el programa
main()
