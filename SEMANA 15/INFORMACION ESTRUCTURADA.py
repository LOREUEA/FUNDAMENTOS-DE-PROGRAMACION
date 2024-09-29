#Diccionario informacion personal

informacion_personal ={
    "nombre" : "Adriana Mendez",
    "edad": "35",
    "ciudad": "Quito",
    "profesion": "Doctora",
}

print(informacion_personal)
print("Nombre: " ,informacion_personal["nombre"])
print("Edad: " ,informacion_personal["edad"])
print("Ciudad: " ,informacion_personal["ciudad"])
print("Profesion: " ,informacion_personal["profesion"])
print("--------------------- SEGUNDA INSTRUCCION----------------")
#Cambio de clave en ciudad
informacion_personal["ciudad"] = "Cuenca"
print(informacion_personal)
print("Nombre: " ,informacion_personal["nombre"])
print("Edad: " ,informacion_personal["edad"])
print("Ciudad: " ,informacion_personal["ciudad"])
print("Profesion: " ,informacion_personal["profesion"])
print("--------------------------------------------------------")
#Agregar nueva clave-valor a la "profesion"
informacion_personal["profesion"] = "Ingeniera"
print(informacion_personal)
print("Nombre: " ,informacion_personal["nombre"])
print("Edad: " ,informacion_personal["edad"])
print("Ciudad: " ,informacion_personal["ciudad"])
print("Profesion: " ,informacion_personal["profesion"])
print("--------------------- TERCERA INSTRUCCION----------------")
# Verificar la clave "telefono" sino existe agregarla
informacion_personal["telefono"] = "0986410982"
print("Telefono:",informacion_personal["telefono"])
print("--------------------- CUARTA INSTRUCCION----------------")
# Eliminar clave edad
del informacion_personal["edad"]
print("Datos generales:",informacion_personal)




