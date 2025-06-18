# mostrar_componentes muestra una lista de partes de una computadora
def mostrar_componentes(*componentes):  # acepta varios argumentos sin nombre
    print("Componentes del computador:")  # título
    for comp in componentes:  # recorre todos los componentes entregados
        print(f"- {comp}")  # imprime cada uno con guion

# prueba de la función mostrar_componentes
mostrar_componentes("Placa Madre", "Memoria RAM", "Disco Duro", "Tarjeta de Video")


# detalles_componente muestra información específica de un componente
def detalles_componente(nombre_componente, **detalles):  # recibe el nombre y otros datos nombrados
    print(f"\nDetalles del componente: {nombre_componente}")  # muestra qué componente es
    for clave, valor in detalles.items():  # recorre los detalles uno a uno
        print(f"{clave}: {valor}")  # muestra cada par clave: valor

# prueba de la función detalles_componente
detalles_componente("Memoria RAM", marca="Kingston", capacidad="8GB", velocidad="3200MHz")


# ensamblar_computadora recibe partes y datos del técnico
def ensamblar_computadora(*partes, **datos_tecnico):  # acepta srg y kwargs
    print("\nEnsamblaje del computador:")  # título de la sección
    print("Partes incluidas:")  # subtítulo
    for parte in partes:  # recorre la lista de partes
        print(f"- {parte}")  # imprime cada parte

    print("\nDatos del técnico:")  # título de los detalles del técnico
    for clave, valor in datos_tecnico.items():  # recorre los datos entregados
        print(f"{clave}: {valor}")  # imprime cada par clave: valor

# prueba de la función ensamblar_computadora
ensamblar_computadora(
    "Placa Madre", "Procesador", "Memoria RAM", "Fuente de Poder",
    tecnico="Maximiliano Reyes",
    fecha="11-06-2025",
    tipo_gabinete="ATX Mediano",
    lugar="Laboratorio"
)
