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

# Calcular el promedio por ciudades y semanas
def calcular_promedio(temperaturas,ciudad_idx):
    ciudad = temperaturas[ciudad_idx]
    suma_temperaturas = 0
    total_dias = 0

    #Recorrer semanas
    for semana in ciudad:
        for dia in semana:
            suma_temperaturas += dia["temp"]
            total_dias += 1
    #Calcular promedio
    promedio = suma_temperaturas / total_dias
    return promedio

#Función para calcular el promedio de temperaturas por ciudad y semana
#def calcular_promedio(ciudad)
#   for semana_index, semana in enumerate(ciudad, start= 1:
#       suma = sum(dia["temp] for dia in semana
#       promedio = suma / len(semana)
#       print(f"Semana {semana_index}: Promedio de temperatura: {promedio: .2f}")

# Menú interactivo
# Definimos las ciudades
while True:
    print("Seleccione la ciudad")
    print("1 - Quito")
    print("2 - Cuenca")
    print("3 - Otavalo")
    print("4 - Salir")

    opcion = input("Ingrese la opción deseada (1-4): ")
    if opcion == "1":
        promedio = calcular_promedio(temperaturas, ciudad_idx = 0)
        print(f"Promedio = : {promedio:2f}")

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
