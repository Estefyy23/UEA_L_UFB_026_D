"""
Este código muestra cómo escribir en un archivo de texto,
 leerlo línea por línea e imprimir su contenido en la
 consola. Además, utiliza el contexto with para asegurar
 que los archivos se cierren adecuadamente,
"""
# Inicio el programa.
#Escribir en el archivo
# Se abre el archivo my_notes.txt.
with open("my_notes.txt", "w") as my_notes:
    # Se Escriben notas en el archivo
    my_notes.write("Hola me gusta programar \n")
    my_notes.write("Soy estudiante de uea \n")
    my_notes.write("Este es el último trabajo\n")

# Se realiza la lectura del archivo
print("Leyendo los archivos de se encuentra en my_notes.txt: \n ")

with open("my_notes.txt", "r") as my_notes:
    # Leer e imprimir líneas
    line = my_notes.readline()
    while line:
        print(line.strip())
        line = my_notes.readline()

# cerrar el archivo
my_notes.close()
