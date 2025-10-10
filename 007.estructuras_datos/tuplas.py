
"""

Creación: () o tuple()

* inmutables

Ideal:
* resultados de consultas SELECT a base de datos



"""

cliente = (1, 'cliente@gmail.com', 1500.0)

print(cliente[1])

# TypeError: 'tuple' object does not support item assignment
# cliente[1] = 'modificado@gmail.com'

print(type(cliente))