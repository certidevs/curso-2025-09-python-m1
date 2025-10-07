
"""

Bucle while

Bucle indeterminado, porque se ejecuta en base a condiciones por lo que 
a priori podemos no saber cuántas veces se va a ejecutar.

Ideal para crear aplicaciones de consola (CLI apps)

No tiene do while como en Java, se podría emular con while True (bucle infinito)

Puede haber más de una condición en el while pero dificulta la lectura
"""
contador = -2

while contador < 10:
    print(contador)
    contador += 1
    
