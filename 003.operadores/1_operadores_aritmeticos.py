print("\n")
print("=" * 20)
print("OPERADORES ARITMÉTICOS")
print("=" * 20)
print("\n")
"""
Operadores aritméticos para operaciones matemáticas básicas
"""

precio_manzanas = 3
precio_naranjas = 5
total_frutas = precio_manzanas + precio_naranjas
print(f"Total de la compra: {total_frutas} euros")

dinero_entregado = 20
dinero_producto = 13
cambio = dinero_entregado - dinero_producto
print(f"Su cambio es: {cambio} euros")

precio_unitario = 5
cantidad = 3
precio_total = precio_unitario * cantidad
print(f"Precio por {cantidad} unidades: {precio_total} euros")

pizza = 8 / 2
print(f"8 / 2 = {pizza}")

horas_totales = 90
horas_por_dia = 24
dias_completos = horas_totales // horas_por_dia
print(f"Días completos: {dias_completos} días")

horas_restantes = horas_totales % horas_por_dia
print(f"Horas restantes: {horas_restantes} horas")

lado = 4
area = lado ** 2
print(f"El área del cuadrado es: {area} unidades cuadradas")

numero = 25
raiz_cuadrada = numero ** 0.5
print(f"La raíz cuadrada de {numero} es: {raiz_cuadrada}")

numero = 27
raiz_cubica = numero ** (1/3)
print(f"La raíz cúbica de {numero} es: {raiz_cubica}")

resultado = 0.1 + 0.2
print(f"0.1 + 0.2 = {resultado}")

resultado_redondeado = round(resultado, 2)
print(f"Redondeado a 2 decimales: {resultado_redondeado}")