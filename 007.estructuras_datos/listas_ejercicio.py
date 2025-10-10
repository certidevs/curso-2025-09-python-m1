
"""
Crea una función llamada filtrar_mayores que reciba dos parámetros: 
una lista de números enteros y un valor umbral. 
La función debe devolver una nueva lista que contenga solo los números 
de la lista original que sean mayores que el valor umbral.

Por ejemplo:

Si llamamos filtrar_mayores([5, 10, 15, 20], 12) debe devolver [15, 20]
Si llamamos filtrar_mayores([1, 2, 3], 5) debe devolver [] (lista vacía)
Puedes empezar creando una función que reciba los dos parámetros y 
luego utilizar un bucle para recorrer la lista original y añadir a una 
nueva lista solo los elementos que cumplan la condición.
"""

def filtrar_mayores(lista, umbral):
    """
    Filtra los números de una lista que son mayores que un valor umbral dado.
    
    Args:
        lista (list): Lista de números enteros a filtrar.
        umbral (int): Valor umbral para la comparación.
        
    Returns:
        list: Nueva lista con los números mayores que el umbral.
    """
    resultado = []
    
    # ...