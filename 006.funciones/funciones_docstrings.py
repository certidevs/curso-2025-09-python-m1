
# funciones que devuelven números

# función que devuelve un precio con IVA

def calcular_iva(precio):
    """
    Calcula el IVA de un precio dado.
    
    Obtiene el 21 % de un precio.
    
    Args:
        precio: precio mayor que cero
        
    Returns:
        El IVA en punto flotante (float)
        
    Ejemplo:
        >>> calcular_iva(100)
        21
    """
    return precio * 0.21


microfono_precio = 100
microfono_iva = calcular_iva(microfono_precio)
print(f"precio original: {microfono_precio}")
print(f"IVA del producto: {microfono_iva}")

print(f"Precio final: {microfono_precio + microfono_iva}")