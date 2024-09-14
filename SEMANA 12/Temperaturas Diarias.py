# Matriz 3D para datos de temperaturas
# Primera dimensión: Ciudades (3 paises)
# Segunda dimensión: Semanas (4 semanas)
# Tercera dimensión: Días de la semana (7 días)
from os import linesep

temperaturas = [
    [ #Quito
        [ #Primer semana
            {"day": "Lunes", "temp": 21},
            {"day": "Martes", "temp": 18},
            {"day": "Miercoles", "temp": 20},
            {"day": "Jueves", "temp": 21},
            {"day": "Viernes", "temp": 22},
            {"day": "Sabado", "temp": 17},
            {"day": "Domingo", "temp": 19},
        ],
        [ #Segunda semana
            {"day": "Lunes", "temp": 23},
            {"day": "Martes", "temp": 19},
            {"day": "Miercoles", "temp": 18},
            {"day": "Jueves", "temp": 20},
            {"day": "Viernes", "temp": 20},
            {"day": "Sabado", "temp": 18},
            {"day": "Domingo", "temp": 21},
        ],
        [ #Tercera semana
            {"day": "Lunes", "temp": 22},
            {"day": "Martes", "temp": 17},
            {"day": "Miercoles", "temp": 21},
            {"day": "Jueves", "temp": 17},
            {"day": "Viernes", "temp": 17},
            {"day": "Sabado", "temp": 22},
            {"day": "Domingo", "temp": 20},
        ],
        [ #Cuarta semana
            {"day": "Lunes", "temp": 20},
            {"day": "Martes", "temp": 18},
            {"day": "Miercoles", "temp": 22},
            {"day": "Jueves", "temp": 19},
            {"day": "Viernes", "temp": 22},
            {"day": "Sabado", "temp": 21},
            {"day": "Domingo", "temp": 24},
        ],
    ],
    [ #Cuenca
        [ #Primer semana
            {"day": "Lunes", "temp": 21},
            {"day": "Martes", "temp": 25},
            {"day": "Miercoles", "temp": 23},
            {"day": "Jueves", "temp": 19},
            {"day": "Viernes", "temp": 27},
            {"day": "Sabado", "temp": 25},
            {"day": "Domingo", "temp": 26},
        ],
        [ #Segunda semana
            {"day": "Lunes", "temp": 22},
            {"day": "Martes", "temp": 26},
            {"day": "Miercoles", "temp": 19},
            {"day": "Jueves", "temp": 20},
            {"day": "Viernes", "temp": 21},
            {"day": "Sabado", "temp": 22},
            {"day": "Domingo", "temp": 23},
        ],
        [ #Tercera semana
            {"day": "Lunes", "temp": 24},
            {"day": "Martes", "temp": 24},
            {"day": "Miercoles", "temp": 23},
            {"day": "Jueves", "temp": 28},
            {"day": "Viernes", "temp": 26},
            {"day": "Sabado", "temp": 21},
            {"day": "Domingo", "temp": 22},
        ],
        [ #Cuarta semana
            {"day": "Lunes", "temp": 22},
            {"day": "Martes", "temp": 22},
            {"day": "Miercoles", "temp": 23},
            {"day": "Jueves", "temp": 24},
            {"day": "Viernes", "temp": 24},
            {"day": "Sabado", "temp": 21},
            {"day": "Domingo", "temp": 22},
        ],
    ],
    [ #Otavalo
        [ #Primer semana
            {"day": "Lunes", "temp": 32},
            {"day": "Martes", "temp": 32},
            {"day": "Miercoles", "temp": 33},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 32},
            {"day": "Sabado", "temp": 33},
            {"day": "Domingo", "temp": 31},
        ],
        [ #Segunda semana
            {"day": "Lunes", "temp": 31},
            {"day": "Martes", "temp": 30},
            {"day": "Miercoles", "temp": 32},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 32},
            {"day": "Sabado", "temp": 32},
            {"day": "Domingo", "temp": 33},
        ],
        [ #Tercera semana
            {"day": "Lunes", "temp": 32},
            {"day": "Martes", "temp": 34},
            {"day": "Miercoles", "temp": 31},
            {"day": "Jueves", "temp": 34},
            {"day": "Viernes", "temp": 32},
            {"day": "Sabado", "temp": 31},
            {"day": "Domingo", "temp": 32},
        ],
        [ #Cuarta semana
            {"day": "Lunes", "temp": 32},
            {"day": "Martes", "temp": 32},
            {"day": "Miercoles", "temp": 33},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 34},
            {"day": "Sabado", "temp": 31},
            {"day": "Domingo", "temp": 22},
        ]
    ]
]

# Calcular el promedio de temperaturas por ciudades y semanas
def calcular_promedio_temperaturas(ciudad, semana):
    total_temp = sum(dia["temp"] for dia in semana)
    promedio_temperatura = total_temp / len(semana)
    return promedio_temperatura

#Imprimir promedio de temperaturas por ciudad y semana
ciudades = ["Quito", "Cuenca", "Otavalo"]

for i, ciudad in enumerate(temperaturas):
    print(f"Promedio de temperaturas para {ciudades[i]}")
    for j, semana in enumerate(ciudad):
        promedio = calcular_promedio_temperaturas(ciudad, semana)
        print(f" Semana {j+1}: {promedio:.2f}grados")

# Menú interactivo
# Definimos las ciudades
ciudades = ["Quito", "Cuenca", "Otavalo"]


# Función para imprimir las temperaturas de la ciudad seleccionada
def imprimir_temperaturas(ciudad):
    for semana_indice, semana in enumerate(temperaturas[ciudad]):
        print(f"\nSemana {semana_indice + 1}:")
        for dia in semana:
            print(f"  {dia['día']}: {dia['temp']} grados")


# Menú para seleccionar la ciudad
while True:
    print("\nSeleccione la ciudad:")
    print("1. Quito")
    print("2. Cuenca")
    print("3. Otavalo")
    print("4. Salir")

    opcion = input("Ingrese la opción deseada (1-4): ")

    if opcion == "1":
        ciudad = 0  # Quito
        print(temperaturas)
        print(ciudad)
    elif opcion == "2":
        ciudad = 1  # Cuenca
        print(temperaturas)
        print(ciudad)
    elif opcion == "3":
        ciudad = 2  # Otavalo
        print(temperaturas)
        print(ciudad)
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("No se encuentra la opción.")

    # Continuar el ciclo
    continue

# Función para calcular la temperatura promedio de las ciudades en un período de tiempo
def calcular_promedio(ciudad):
    for semana_indice, semana in enumerate(ciudad, start=1):
        suma = sum(dia["temp"] for dia in semana)
        promedio = suma / len(semana)
        print(f"Semana {semana_index}: Promedio de temperaturas: {promedio:}")

#Menú interactivo 2
while True:
    print("\nSeleccione la ciudad:")
    print("1. Quito")
    print("2. Cuenca")
    print("3. Otavalo")
    print("4. Salir")

    opcion = input("Ingrese la ciudad: ")
    if opcion == "1":
        calcular_promedio(temperaturas[0])
    elif opcion == "2":
        calcular_promedio(temperaturas[1])
    elif opcion == "3":
        calcular_promedio(temperaturas[2])
    elif opcion == "4":
        print("Saliendo del programa...")
