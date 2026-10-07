# main.py - Componente Inicial
def mensaje_bienvenida():
    print("--- Sistema Inicializado ---")
    print("Versión base cargada correctamente.")

# --- NUEVA FUNCIONALIDAD: feature-interfaz ---
def mostrar_menu():
    print("\n=========================")
    print("     MENÚ PRINCIPAL      ")
    print("=========================")
    print("1. Iniciar proceso")
    print("2. Ver estado del sistema")
    print("3. Configuración")
    print("4. Salir")
    print("=========================")

def procesar_opcion(opcion):
    if opcion == "1":
        print(">> Iniciando el proceso principal...")
    elif opcion == "2":
        print(">> Todos los sistemas funcionando al 100%.")
    elif opcion == "3":
        print(">> Cargando configuraciones...")
    elif opcion == "4":
        print(">> Cerrando sesión. ¡Hasta luego!")
    else:
        print(">> Error: Opción no válida.")

def iniciar_interfaz():
    mostrar_menu()
    opcion_elegida = "1" 
    print(f"Usuario seleccionó: {opcion_elegida}")
    procesar_opcion(opcion_elegida)

if __name__ == "__main__":
    mensaje_bienvenida()
    iniciar_interfaz()