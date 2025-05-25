"""
1.- REGISTRO DE ALUMNOS Y NUMEROS DE LISTA UNICOS
"""

print("Registro de alumnos. \n") #titulo de la actividad 1

registro_alumnos_numeros = [] #tupla vacia donde iran los nombres y numeros
numeros = set() #conjunto para guardar numeros y que no se repitan

while True: #bucle que permite seguir ingresando hasta que se escriba "salir"
    #variable nombre que obtiene su valor con un input
    nombre = input("Ingrese el nombre del alumno o escriba 'salir' para terminar: ")
    if nombre == "salir": #condicional si se escribe "salir" ocurrira una accion
        break #sale del bucle
    try: #inicia el try
        #variable que intenta conviertir lo que se ingresa a numero entero
        numero = int(input("Ingrese el numero de alumno: "))
        if numero in numeros: #verifica si hay un ya usado numero en la variable numeros
            print("El numero que ingreso ya fue usado.") #imprime un mensaje si la condicion se cumple
        else: #sino se cumple la condicion se realizara otra accion
            registro_alumnos_numeros.append((nombre, numero)) #agrega el nombre y numero a la tupla
            numeros.add(numero) #agrega el numero ingresado al conjunto
    except ValueError: #excepcion, si no se ingresa un numero
        print("Lo que ingreso no es un numero entero.") #imprime mensaje en la consola
    print() #imprime interlineado
