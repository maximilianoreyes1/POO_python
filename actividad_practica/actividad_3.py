"""
3.- Clasificador de Palabras Únicas y Repetidas
"""
print("\nClasificador de palabras unicas y repetidas.\n") #titulo de la actividad 3

palabras = [] #lista de palabras

while True: #bluce necesario para pedir varias palabras
    palabra = input("Ingrese, escribe 'salir' para terminar: ") #solicita una palabra o "salir"
    if palabra == "salir": #si se escribe "salir" ocurrira una accion
        break #se saldra del bucle
    palabras.append(palabra) #agrega la palabra a la lista

palabras_unicas = set() #crea conjunto donde iran las palabras unicas
palabras_repetidas = set() #crea conjunto donde iran las palabras repetidas

for palabra in palabras: #bucle que itera los elementos en la lista palabras
    if palabra in palabras_unicas: #si esta la palabra ingresada en la lista de palabras ocurrira una accion
        palabras_unicas.remove(palabra) #quita la palabra del conjunto de palabras unicas
        palabras_repetidas.add(palabra) #agrega la palabra al conjunto de palabras repetidas
    elif palabra not in palabras_repetidas: #sino esta la palabra en el conjunto de palabras repetidas ocurrira una accion
        palabras_unicas.add(palabra) #agrega la palabra al conjunto de palabras unicas

print("\nPalabras únicas:", palabras_unicas) #imprime el conjunto de palabras unicas
print("Palabras repetidas:", palabras_repetidas, "\n") #imprime el conjunto de palabras repetidas
