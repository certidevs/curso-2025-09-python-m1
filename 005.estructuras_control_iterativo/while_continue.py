

"""
Explorar la keyword "continue" permite saltar a la siguiente iteración
de un bucle sin ejecutar el código que hay después.

a diferencia de break, continue no rompe el bucle no salimos del bucle
simplemente salta a la siguiente iteración

Imprime números impares
"""

numero = 0

while numero < 10:
    numero += 1
    if numero % 2 == 0: # comprobar si el número es par
        continue
    
    print(f"Número impar {numero}")