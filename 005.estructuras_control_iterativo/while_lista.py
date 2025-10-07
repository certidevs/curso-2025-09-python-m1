
"""

Iterar una estructura de datos, por ejemplo una lista []

Itera la lista mientras la lista no esté vacía

La función pop() viene de las listas, y elimina y devuelve un elemento de la lista.

.pop(0) elimina el primero
.pop() elimina el último
"""

nombres = ["Kary", "Jorge", "Marcos"]

while nombres:
    nombre = nombres.pop(1)
    # if len(nombres) == 0:
    #     print("Ya no quedan mas nombres, este es el último:")
    print(nombre)
