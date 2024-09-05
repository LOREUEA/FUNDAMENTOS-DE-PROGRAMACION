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
