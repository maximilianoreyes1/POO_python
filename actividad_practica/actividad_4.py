"""
4.- Juego de Adivina el Número con Historial
"""

print("Juego de adivinar el numero.") #titulo de la actividad 4

intentos = [] #lista donde se guardaran los intentos
numero_adivinar = int(10) #el numero que se tiene que adivinar

while True: #bucle que se repetira hasta que el usuario acerte el numero
    try: #inicio del try para verificar que el usuario ingrese un numero entero
        numero = int(input("\nIntente adivinar el numero del 1 al 20: ")) #solicita un numero entero
        intentos.append(numero) #agrega el numero a la lista de intentos
        if numero > numero_adivinar:  #si el numero ingresado es mayor ocurrira una accion
            print("\nEl numero que ingreso es mayor al que hay que adivinar. Intentelo de nuevo.") #imprime mensaje
        elif numero < numero_adivinar: #segunda condicion, si el numero ingresado es menor al numero a adivinar
            print("\nEl numero que ingreso es menor al que hay que adivinar. Intentelo de nuevo.") #imprime mensaje
        else: #sino se cumple ninguna de las condiciones ocurrira otra accion
            print("¡Has adivinado el numero!") #imprime mensaje, ha adivinado el numero
            print() #interlineado
            break #sale del bucle
    except ValueError: #excepcion, si no se ingresa un numero entero
        print("Lo que ingreso no es un numero entero.") #imprime mensaje
    
print() #interlineado
print("Lista de numeros ingresados:", intentos) #imprime con mensaje con la lista de intentos
