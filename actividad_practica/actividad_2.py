"""
2.- Verificador de Votación en Club Escolar Temas: tuplas, listas, if, for, try
"""

print("\nVerificar quienes pueden votar en una eleccion del club\n") #imprime titulo de la actividad 2

registro_personas_edad = [] #tupla de personas y su edad
pueden_votar = [] #lista de personas que si pueden votar

for i in range(3): #bucle for que se repite 3 veces
    nombre = input(f"Ingrese el nombre de la persona {i + 1}: ") #pide el ingreso del nombre de la persona, aumenta uno por cada iteracion del bucle
    try: #inializa el try
        edad = int(input("Ingrese su cantidad de años: ")) #pide la edad
        if edad >= 14: #condiciona, si es igual o mayor a 14
            pueden_votar.append((nombre)) #si es mayor agrega el valor a la lista "pueden_votar"
            print("Usted si puede votar en la eleccion del club") #imprime mensaje si es que puede votar
        else: #sino se cumple la condicion ocurrira otra accion
            print("Usted no puede votar.") #imprime que no puede votar
    except ValueError: # excepcion si hay un error en el valor del numero entero
        print("Lo que ingreso no es un numero entero.") #imprime mensaje
        edad = None #no le asigna edad, ya que no es un numero entero lo que se ingreso
    registro_personas_edad.append((nombre, edad)) #agrega el nombre y la edad de la persona
    print() #interlineado
    
print("Personas que pueden votar:", pueden_votar) #imprime la lista de personas que pueden votar
print() #imprime interlineado
