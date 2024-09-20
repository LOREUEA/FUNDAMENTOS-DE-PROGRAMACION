# Función para calculo de descuento
def calcular_descuento(monto_total,porcentaje):
    descuento = monto_total * porcentaje / 100
    return descuento

monto_total= 1320
descuento = calcular_descuento(850, 20)
print(descuento)

