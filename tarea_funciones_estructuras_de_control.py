"""
Diseñar funciones y utilizar estructuras de control
Maximiliano Reyes 4°C
"""

def numero_mayor(): #define la funcion "numero mayor a 10"
    print("Determinar si un nÃºmero es mayor, menor o igual a 10") #Titulo de la funcion
    print() #interlineado
    
    while True: #Abre bucle while
        try: #Inicia el try
            valor = input("Introduce un nÃºmero: ") #Crea variable con valor ingresado del usuario
            num = int(valor) #Asigna el valor de la variable "valor" a la variable "num" como numero entero
            break #sale del bucle "try" y pasa al siguiente
        except ValueError: #excepcion por si hay un valor que no es un numero entero
            print("Lo que usted ingresó no es un numero valido. Intente nuevamente.") #imprime mensaje
    
    if num > 10: #condicion si el numero es mayor a 10
        print("El numero es mayor a 10") #imprime mensaje
    elif num == 10: #condicion si es que no se cumple la primera
        print("El numero es 10") #imprime mensaje
    else: #condicion si no se cumplen las anteriores 2
        print("El numero es menor a 10") #imprime un mensaje
        
numero_mayor() #llama a la funcion "numero_mayor"
print()

def numero_mayor_decimal(): #define la funcion "numero mayor a 10 con decimales"
    print("Determinar si un numero es mayor, menor o igual a 10 con decimales") #Titulo de la funcion
    print() #interlineado
    
    while True: #Abre bucle while
        try: #Inicia el try
            valor = input("Introduce un nÃºmero: ") #Crea variable con valor ingresado del usuario
            num = float(valor) #Asigna el valor de la variable "valor" a la variable "num" como numero decimal
            break #sale del bucle "try" y pasa a la siguiente linea
        except ValueError: #excepcion por si hay un valor que no es un numero decimal
            print("Lo que usted ingreso no es un numero decimal valido. Intente nuevamente.") #imprime mensaje
    
    if num > 10: #condicion si el numero es mayor a 10
        print("El numero es mayor a 10") #imprime mensaje
    elif num == 10: #condicion si es que no se cumple la primera
        print("El nnumero es 10") #imprime mensaje
    else: #condicion si no se cumplen las anteriores 2
        print("El numero es menor a 10") #imprime un mensaje
        
numero_mayor_decimal() #llama a la funcion "numero_mayor_decimal"
print()

def area_triangulo(): #define funcion "area_triangulo"
    print("Calcular el area de un triangulo")
    print()
    
    while True: #Abre bucle while
        try: #Inicia el try
            base = int(input("Ingrese la base del triangulo: ")) #inicia la variable base
            altura = int(input("Ingrese la altura del triangulo: ")) #inicia la variable altura
            break #sale del bucle "try" y pasa a la siguiente linea
        except ValueError: #excepcion por si hay un valor que no es un numero entero
            print("Lo que usted ingreso no es un numero entero vÃ¡lido. Intente nuevamente.") #imprime mensaje
            
    area = base * altura / 2 #calcula el area
    print(f"El area del triangulo es {area}") #imprime un mensaje llamando a la variable "area"
            
area_triangulo()
print()            

def nombre_edad():
    print("Recibir nombre y edad") #imprime mensaje
    print() #imprime interlineado
    
    nombre = input("Ingrese su nombre: ") #inicia variable nombre
    
    while True: #Inicia un bucle while
        try: #inicia el try
            edad = int(input("Ingrese su cantidad de años: ")) #crea la variable "edad"
            break #sale del bucle "try" y pasa a la siguiente linea
        except ValueError: #excepcion por si hay un valor que no es un numero entero
            print("Lo que usted ingreso no es un numero entero") #imprime mensaje
            
    print(f"Hola, {nombre}. Me alegra que tengas {edad} años.") #imprime mensaje

nombre_edad() #llama a la función para que se muestre en la consola
print()

def sum_num():
    print("Sumar una x cantidad de números")
    print()
    
    cantidad = int(input("¿Cuántos números quieres sumar?: ")) #pide al usuario la cantidad de números que se van a almacenar
    numeros = [] #lista para guardar los datos

    for i in range(cantidad): #bucle que se repite la cantidad de veces que se ingreso
        num = int(input(f"Ingresa el número {i + 1}: ")) #pide al usuario que ingrese un número entero y lo guarda en num
        numeros.append(num) #agrega el número a la lista

    total = sum(numeros) #suma todos los datos dentro de la lista
    print("La suma es:", total) #imprime el resultado en la consola

sum_num() #llama a la funcion
