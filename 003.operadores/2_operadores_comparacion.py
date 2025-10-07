"""
Operadores de comparación:

> (mayor que, greater than, gt)
< (menor que, less than, lt)
>= (mayor o igual que)
<= (menor o igual que)
== (igual que)
!= (distinto que)

No confundir con la asignación =

Devuelven un boolean: True o False

"""

precio_producto_a = 15
precio_producto_b = 10

es_mas_barato = precio_producto_b < precio_producto_a
print(f"¿El producto B es más barato que el A? {es_mas_barato}")

print(10 == 15)