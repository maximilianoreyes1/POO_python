estudiantes = [
    {"nombre": "Martin", "nota": 50},
    {"nombre": "Carlos", "nota": 62},
    {"nombre": "Juan", "nota": 70},
    {"nombre": "Roberto", "nota": 38},
    {"nombre": "David", "nota": 40}
    ]

#Ingresar estudiantes
print("Ingresa nuevos estudiantes")


try:
    nombre = input("Nombre del estudiante: ")
    nota = int(input(f"Nota de {nombre}: "))
    estudiantes.append({"nombre": nombre, "nota": nota})
except ValueError:
    print("Por favor, ingresa una nota válida (número).")

suma_notas = 0
mejor_estudiante = ""
mejor_nota = 0
peor_nota = 70
peor_estudiante = ""

estudiantes.append({"nombre": "Erick", "nota": 60})
estudiantes.append({"nombre": "Benjamin", "nota": 45})
estudiantes.append({"nombre": "Max", "nota": 37})

for estudiante in estudiantes:
    nombre = estudiante["nombre"]
    nota = estudiante["nota"]
    
    suma_notas += nota
    
    if nota > mejor_nota:
        mejor_nota = nota
        mejor_estudiante = nombre
        
    if nota < peor_nota:
        peor_nota = nota
        peor_estudiante = nombre
        
    promedio = suma_notas / len(estudiantes)
    
print(f"El promedio de notas es: {promedio:.2f}")
print(f"El estudiante con la mejor nota es {mejor_estudiante} con {mejor_nota}")
print(f"El estudiante con la peor nota es {peor_estudiante} con {peor_nota}")

print("\nEstudiantes por encima del del promedio:")
for estudiante in estudiantes:
    if estudiante["nota"] > promedio:
        print(f"-{estudiante['nombre']} ({estudiante['nota']})")
        
print("\nEstudiantes por abajo del encima del promedio:")
for estudiante in estudiantes:
    if estudiante["nota"] < promedio:
        print(f"-{estudiante['nombre']} ({estudiante['nota']})")