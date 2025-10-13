def filtrar_mayores(lista, umbral):
    """
    Filtra los números de una lista que son mayores que un valor umbral dado.
    
    Args:
        lista (list): Lista de números enteros a filtrar.
        umbral (int): Valor umbral para la comparación.
        
    Returns:
        list: Nueva lista con los números mayores que el umbral.
    """
    # Se inicialza una lista vacía para guardar los números que cumplan la condición
    resultado = []
    
    # Recorremos cada número de la lista
    for n in lista:
        # Comprobamos si el número es mayor al umbral
        if n > umbral:
            # Si se cumple, se añade a la lista de resultado
            resultado.append(n)
    
    return resultado

# Ejemplos de uso
if __name__ == "__main__":
    print(filtrar_mayores([5, 10, 15, 20], 12))  # Debe devolver [15, 20]
    print(filtrar_mayores([1, 2, 3], 5))         # Debe devolver [] (lista vacía)
    
# ------------------------------

# COMPRENSIÓN DE LISTAS

def filtrar_mayores(lista, umbral):
    return [n for n in lista if n > umbral]

# Ejemplos de uso
if __name__ == "__main__":
    print(filtrar_mayores([5, 10, 15, 20], 12))  # Debe devolver [15, 20]
    print(filtrar_mayores([1, 2, 3], 5))         # Debe devolver [] (lista vacía)