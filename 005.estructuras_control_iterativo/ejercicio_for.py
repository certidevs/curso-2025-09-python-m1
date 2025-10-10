"""
Crea un programa que genere un patrón triangular de números donde cada fila muestre 
los números desde 1 hasta el número de la fila. El programa debe solicitar al usuario 
un número entero positivo que representará la altura del triángulo (número de filas).

Por ejemplo, si el usuario introduce 5, el resultado debe ser:

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

Utiliza un bucle for anidado junto con la función range() para generar este patrón. 
Asegúrate de que los números en cada fila estén separados por un espacio.
"""
print("=== PROGRAMA: GENERADOR DE PATRÓN TRIANGULAR ===\n")

# Solicitar al usuario la altura del triángulo
# Escribe aquí tu código para pedir el número al usuario
altura = input("Introduce la altura del triángulo")

# Convertir la entrada a número entero
# Escribe aquí tu código para la conversión
altura_int = int(altura)

print(f"\nGenerando patrón triangular de altura {altura}:")
print("-" * 30)

# Generar el patrón usando bucles for anidados
# Bucle externo: para cada fila (desde 1 hasta la altura)
# Escribe aquí tu código para el bucle externo
# for 

    # Bucle interno: para cada número en la fila actual (desde 1 hasta el número de fila)
    # Escribe aquí tu código para el bucle interno
    # for...

        # Imprimir cada número seguido de un espacio (sin salto de línea)
        # Escribe aquí tu código para imprimir el número


    # Después de completar una fila, hacer un salto de línea
    # Escribe aquí tu código para el salto de línea


print("-" * 30)
print("Patrón completado!")