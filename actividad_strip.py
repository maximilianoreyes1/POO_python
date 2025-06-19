"""import os #importa la libreria os
ruta_carpeta = "C://clase" #crea una variable con la ruta de lacarpeta

os.makedirs(ruta_carpeta) #llama una funcion desde la libreria os, crea la carpeta si es que no existe
print(f"La carpeta fue creada con éxito en: {ruta_carpeta}") #imprime un mensaje"""
    
texto = """AEn el futuro brillante vivía la familia Supersónico, con su perro Astro y el robot RobotinaU.
ASúper Sónico volaba a su trabajo en un platillo, mientras Ultra Sónico hacía las compras con solo presionar un botónU.
ALucero Sónico soñaba con ser cantante galáctica, y Cometín Sónico inventaba robots para no hacer la tarea.
AUn día, Astro se perdió entre satélites y meteoritosJ.
ATodos lo buscaron con su nave turbo y, al encontrarlo, hicieron una fiesta entre estrellasK.
ADesde entonces, los Supersónicos valoraron más estar juntos que cualquier tecnología8."""

ruta_archivo = "C:/clase/datos.txt"

with open(ruta_archivo, 'w') as archivo:
    archivo.write(texto)
    
with open(ruta_archivo, 'r') as archivo:
    lineas = archivo.readlines()
    
nuevas_lineas = [linea.lstrip("A") for linea in lineas]

nuevas_lineas2 = [linea.rstrip("UJK8") for linea in nuevas_lineas]

with open(ruta_archivo, 'w') as archivo:
    archivo.writelines(nuevas_lineas2)
    
print(nuevas_lineas)