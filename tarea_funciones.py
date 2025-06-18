"""
Diseñar funciones y utilizar estructuras de control
Maximiliano Reyes 4°C
"""

def numero_mayor(): #define la función "numero mayor a 10"
    print("Determinar si un número es mayor, menor o igual a 10") #Titulo de la funcion
    print() #interlineado
    
    while True: #Abre bucle while
        try: #Inicia el try
            valor = input("Introduce un número: ") #Crea variable con valor ingresado del usuario
            num = int(valor) #Asigna el valor de la variable "valor" a la variable "num" como numero entero
            break #sale del bucle "try" y pasa al siguiente
        except ValueError: #excepcion por si hay un valor que no es un numero entero
            print("Lo que usted ingresó no es un número válido. Intente nuevamente.") #imprime mensaje
    
    if num > 10: #condicion si el numero es mayor a 10
        print("El número es mayor a 10") #imprime mensaje
    elif num == 10: #condicion si es que no se cumple la primera
        print("El número es 10") #imprime mensaje
    else: #condicion si no se cumplen las anteriores 2
        print("El número es menor a 10") #imprime un mensaje
        
numero_mayor() #llama a la funcion "numero_mayor"
print()

def numero_mayor_decimal(): #define la función "numero mayor a 10 con decimales"
    print("Determinar si un número es mayor, menor o igual a 10 con decimales") #Titulo de la funcion
    print() #interlineado
    
    while True: #Abre bucle while
        try: #Inicia el try
            valor = input("Introduce un número: ") #Crea variable con valor ingresado del usuario
            num = float(valor) #Asigna el valor de la variable "valor" a la variable "num" como numero decimal
            break #sale del bucle "try" y pasa a la siguiente linea
        except ValueError: #excepcion por si hay un valor que no es un numero decimal
            print("Lo que usted ingresó no es un número decimal válido. Intente nuevamente.") #imprime mensaje
    
    if num > 10: #condicion si el numero es mayor a 10
        print("El número es mayor a 10") #imprime mensaje
    elif num == 10: #condicion si es que no se cumple la primera
        print("El número es 10") #imprime mensaje
    else: #condicion si no se cumplen las anteriores 2
        print("El número es menor a 10") #imprime un mensaje
        
numero_mayor_decimal() #llama a la funcion "numero_mayor_decimal"
print()

def area_triangulo(): #define funcion "area_triangulo"
    print("Calcular el área de un triángulo")
    print()
    
    while True: #Abre bucle while
        try: #Inicia el try
            base = int(input("Ingrese la base del triángulo: ")) #inicia la variable base
            altura = int(input("Ingrese la altura del triángulo: ")) #inicia la variable altura
            break #sale del bucle "try" y pasa a la siguiente linea
        except ValueError: #excepcion por si hay un valor que no es un numero entero
            print("Lo que usted ingresó no es un número entero válido. Intente nuevamente.") #imprime mensaje
            
    area = base * altura / 2 #calcula el area
    print(f"El área del triangulo es {area}") #imprime un mensaje llamando a la variable "area"
            
area_triangulo()
print()            

def nombre_edad():
    print("Recibir nombre y edad") #imprime mensaje
    print() #imprime interlineado
    
    nombre = input("Ingrese su nombre: ") #inicia variable nombre
    
    while True:
        try:
            edad = int(input("Ingrese su cantidad de años: "))
            break
        except ValueError:
            print("Lo que usted ingresó no es un número entero")
            
    print(f"Hola, {nombre}. Me alegra que tengas {edad} años.")
    
nombre_edad()