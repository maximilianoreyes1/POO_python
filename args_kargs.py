# Función que recibe una cantidad variable de componentes y los muestra
def mostrar_componentes(*componentes):
    # Imprime el título
    print("=== Componentes de la computadora ===")
    # Recorre cada componente recibido y lo imprime
    for componente in componentes:
        print(f"- {componente}")

# Ejemplo de uso
mostrar_componentes("CPU", "RAM", "Disco Duro", "Tarjeta Gráfica")
