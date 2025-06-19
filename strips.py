"""
    FUNCION STRIP()
"""

""" ELIMINAR LOS ESPACIOS DE LOS LATERALES
texto = " 4° de programacion "
print(texto)

limpiar = texto.strip()
print(f"{limpiar}")
"""

""" ELIMINAR LOS CARACTERES LATERALES SELECIONADOS EN EL STRIP
texto = "-4° de programacion!"
print(texto)

limpiar = texto.strip("!")
print(f"{limpiar}")

limpiar = texto.strip("-,!")
print(f"{limpiar}")

numeros = "B12345A"
print(numeros)

limpiar_num = numeros.strip("B,A")
print(f"{limpiar_num}")
"""