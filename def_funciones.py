""" DEFINIR FUNCIONES

def saludar(nombre): #declara la funcion "saludar"
    print("¡Hola!, " + nombre + " ¿Cómo estás?") #imprime un mensaje concatenado con signo +

saludar("maxi") #llama a la funcion


def saludar(nombre): #declara la funcion "saludar"
    print(f"¡Hola!, {nombre} ¿Cómo estás?") #imprime un mensaje concatenado con llaves

saludar("Demian") #llama a la funcion
"""

""" FUNCIONES DE SUMA
def sumar(a,b):
    resultado = a + b
    return resultado
   
Total = sumar(2,4)
print("La suma es", Total)


def sumar(a,b):
    resultado = a + b
    return resultado
   
a = int(input("Ingrese un número:"))
b = int(input("Ingrese otro número:"))
Total = sumar(a, b)
print(f"El resultado de {a} + {b} es igual a {Total}")

"""

"""
def es_par(num):
    if num % 2 == 0:
        return True
    else:
        return False
   
print(es_par(4)) #verdadero
print(es_par(7)) #falso
print()

def es_par(numero):
    return numero % 2 == 0

print(f"¿Es par 4? {'Si' if es_par(4) else 'No'}")
print(f"¿Es par 7? {'Si' if es_par(7) else 'No'}")
"""

"""
def cuadrado(x):
    return x * x
def suma_de_cuadrados (a, b):
    return cuadrado(a) + cuadrado(b)
print(suma_de_cuadrados(2, 3))
"""

""" SUM
#Sumar elementos de una lista
numeros = [30, 4, 2025]
resultado = sum(numeros)
print("El resultado es: ", resultado)
"""

""" RANGE
valores = range(5)
print("Los valores existen son:", list(valores))

valores = range(2, 10, 2)
print("los valores que incluye el rango son: ", list(valores))
"""