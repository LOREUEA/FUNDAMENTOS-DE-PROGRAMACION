# Modo de apertura: "w"
# Archivo my_notes.txt
texto = open('my_notes.txt','w')
print(texto)
#Crearemos lineas
linea1= texto.write("Hola bellezas\n")
linea2= texto.write("Quiero recordarles que son seres hermosos, valientes y superpoderosos\n")
linea3= texto.write("Y que no se deben detener hasta que logren terminar la carrera y se sientan orgullosos de ustedes mismos.\n")
linea4= texto.write("Y que todo el esfuerzo y sacrificio de hoy, es la recompensa de un mañana.\n")

#Cerramos el archivo
texto.close()

#Modo de apertura: "r"
texto= open('my_notes.txt','r')
texto.seek(0)
linea1= texto.read()
linea2= texto.read()
linea3= texto.read()
liena4= texto.read()
#imprimimos para verificar que cumpla con las instrucciones de la tarea
print(linea1,linea2,linea3,liena4)
#Cerramos el archivo
texto.close()

