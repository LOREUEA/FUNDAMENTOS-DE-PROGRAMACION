# Función para calculo de descuento
def calcular_descuento(precio_producto,porcentaje):

    descuento = precio_producto * porcentaje / 100
    return descuento

# Emisión de nota de venta
precio_producto = 1320
descuento = calcular_descuento(precio_producto,20)
print("Total nota de venta")
print(f"Subtotal: {precio_producto}")
print(f"Descuento 20% : {descuento}")
print(f"Total:", precio_producto - descuento)

print("*******************************************")

monto_total2= float(input("Ingrese el valor total del producto: "))
descuento2 = calcular_descuento(monto_total2,30)
iva2 = monto_total2 * 0.15
print("Total factura")
print(f"Subtotal: {monto_total2}")
print(f"Descuento 30% : {descuento2}")
print(f"Iva 15% :{iva2}")
print(f"Total:", monto_total2 - descuento2 - iva2)
