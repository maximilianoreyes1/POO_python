#InformaciÃ³n de la biclioteca del Vate
nombre_biblioteca = "Biblioteca Escolar Vate" #variable nombre de biblioteca
capacidad_maxima = 1500 #variable de la capacidad mÃ¡xima
libros_disponibles = 1223 #cantidad de libros disponibles

#Libro destacado del mes
libro_destacado = { #conjunto con las caracteristicas del libro destacado
    "Titulo": "La Conspiracion", 
    "Autor": "Dan Brown",
    "Año": 2001,
    "Genero": "Novela",
    "Disponible": True
}

#Lista de categorias de libros
categorias = ["Ficcion", "No ficcion", "Ciencia", "Historia", "Matematicas"]

#Horario de atecion (hora de apertura, hora de cierre)
horario = (9, 17)

#Conjunto de rut de estudiantes con pretamos activos
estudiantes_con_prestamos = {12345678, 23456789, 34567890}

print(nombre_biblioteca)#imprime el nombre de la biblioteca
print()#espacio de interlineado
print("Libros disponibles:", libros_disponibles) #muestra los libros disponibles
print()

categorias.append("Programacion") #añade la categoria programacion a los libros

print("Hora de apertura:", horario[0], "\nHora de cierre:", horario[1]) #imprime la hora de apertura y cierre
print()

estudiantes_con_prestamos.add(12280919) #añade el rut de un estudiante a la lista

libro_destacado["Disponible"] = False #cambia el valor "disponible" a False

print("Libro destacado del mes: ") #imprime encabezado de las caracteristicas del libro
for clave, valor in libro_destacado.items(): #itera las claves y valores del libro destacado
    print(clave, valor) #imprime las claves y valores del libro destacado