"""
5.- Organizador de Clubes Estudiantiles
"""
print("Organizar clubes de estudiantes.") #titulo de la actividad 5
print() #interlineado

club_basquetball = [("Maximiliano", 17), ("Vicente", 17), ("Juan", 16), ("Carlos", 15)] #lista del club de basqueball
club_voleyball = [("Max", 17), ("Maximiliano", 17), ("Damian", 17), ("Juan", 16)] #lista del club de voleyball
club_dibujo = [("Felipe", 18), ("Juan", 16), ("Max", 17), ("Maximiliano", 17)] #lista del club de dibujo

alumnos_basquetball = {alumno[0] for alumno in club_basquetball} #guarda a los alumnos del club de basket en un conjunto en un conjunto
alumnos_voleyball = {alumno[0] for alumno in club_voleyball} #guarda a los alumnos del club de voleyball en un conjunto
alumnos_dibujo = {alumno[0] for alumno in club_dibujo} #guarda a los alumnos del club de dibujo en un conjunto

alumnos_duplicados = set() #conjunto donde iran los alumnos que estan en varios clubes

for alumno in alumnos_basquetball: #revisa todos los alumnos del club de basket
    if alumno in alumnos_voleyball or alumno in alumnos_dibujo: #compara si hay algun alumno del club de basket en uno de los otros clubes
        alumnos_duplicados.add(alumno) #si se cumple la condicion se agrega a la lista de suplicados
        
for alumno in alumnos_voleyball: #revisa todos los alumnos del club de voley
    if alumno in alumnos_dibujo and alumno not in alumnos_basquetball: #compara con el club de dibujo y omite al de basket para omitir los que ya se duplicaron en el club de basket
        alumnos_duplicados.add(alumno) #si esque hay un alumno duplicado se agrega al conjunto de duplicados

print("Estudiantes que están en más de un club:") #imprime mensaje
for alumno in alumnos_duplicados: #busca todos los alumnos en la lista de duplicados
    print("-", alumno) #imprime todos los alumnos que esten en varios clubes