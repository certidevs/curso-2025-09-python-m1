
"""
Formatear cadenas de texto strings para introducir datos de variables en los string

Muy útil para aplicaciones de consola y para logging

Día: martes 07/10/2025 09:12
"""

# con una variable
precio = 55
descripcion = "El producto vale {} €"
print(descripcion.format(precio))


# con más de una variable
cantidad = 5
id = 34
precio = 54
descripcion = "Compra de {} piezas de producto con id {} a precio {:.2f} €"
print(descripcion.format(cantidad, id, precio))

# f-string es la forma moderna o rápida de formatear textos:

print(f"Compra de {cantidad} piezas a precio {precio:.2f} €")