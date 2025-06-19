import os #importa la libreria os
ruta_carpeta = "C://clase" #crea una variable con la ruta de lacarpeta

os.makedirs(ruta_carpeta) #llama una funcion desde la libreria os, crea la carpeta si es que no existe
print(f"La carpeta fue creada con éxito en: {ruta_carpeta}") #imprime un mensaje
    
#  texto original
texto = """AEn el futuro brillante vivía la familia Supersónico, con su perro Astro y el robot RobotinaU.
ASúper Sónico volaba a su trabajo en un platillo, mientras Ultra Sónico hacía las compras con solo presionar un botónU.
ALucero Sónico soñaba con ser cantante galáctica, y Cometín Sónico inventaba robots para no hacer la tarea.
AUn día, Astro se perdió entre satélites y meteoritosJ.
ATodos lo buscaron con su nave turbo y, al encontrarlo, hicieron una fiesta entre estrellasK.
ADesde entonces, los Supersónicos valoraron más estar juntos que cualquier tecnología8."""

ruta_archivo = "C:/clase/datos.txt" #variable con la ruta del archivo

with open(ruta_archivo, 'w') as archivo: #abre el archivo de texto, si no existe lo crea, tambien lo sobreescribe y le asigna la variable "archivo"
    archivo.write(texto) #sobreescribe el archivo de texto con el cuento
    
with open(ruta_archivo, 'r') as archivo: #abre el archivo y lo lee
    lineas = archivo.readlines() #lee linea por linea el archivo y las guarda como lista en la variable "lineas"
    
nuevas_lineas = [linea.lstrip("A") for linea in lineas] #variable que guarda las lineas del texto sin las "A" del principio de cada linea

nuevas_lineas2 = [linea.rstrip("UJK8.\n") for linea in nuevas_lineas] #variable que guarda las lineas del texto sin los caracteres "UJK8.\n" del principio de cada linea

with open(ruta_archivo, 'w') as archivo: #abre el archivo de texto y lo sobreescribe y le asigna la variable "archivo"
    archivo.writelines(linea + '\n' for linea in nuevas_lineas2) #sobreescribe el archivo con las lineas de "nuevas_lineas2" y agrega los saltos de lineas que se quitaron antes
    
print(nuevas_lineas2) #imprime mensaje con el texto corregido