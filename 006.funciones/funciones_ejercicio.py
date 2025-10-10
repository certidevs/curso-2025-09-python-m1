
"""
Crea una función llamada calcular_area_circulo que reciba como parámetro el radio de un círculo y devuelva su área. Recuerda que el área de un círculo se calcula como π multiplicado por el radio al cuadrado (π * r²). Utiliza el valor 3.14159 para π.

La función debe:

Aceptar un parámetro numérico (el radio)
Calcular el área usando la fórmula correcta
Devolver el resultado como un número decimal
"""


print("=== PROGRAMA: CALCULADORA DE ÁREA DE CÍRCULO ===\n")

# Definir la función calcular_area_circulo
def calcular_area_circulo(radio):
    
    # 1. Definir el valor de pi
    # Escribe aquí tu código
    PI = 3.14
    
    
    # 2. Calcular el área usando la fórmula: π * radio²
    # Escribe aquí tu código
    area = PI * (radio ** 2)    
    
    # 3. Devolver el resultado
    # Escribe aquí tu código
    return area
    


print("=== PRUEBAS DE LA FUNCIÓN ===")

# Prueba 1: radio = 5
radio1 = 5
# Llamar a la función y guardar el resultado
# Escribe aquí tu código
area1 = calcular_area_circulo(radio1)

print(f"Radio: {radio1} -> Área: {area1}")

# Prueba 2: radio = 3
radio2 = 3
# Llamar a la función y guardar el resultado
# Escribe aquí tu código


print(f"Radio: {radio2} -> Área: {area2}")

# Prueba 3: radio = 10.5
radio3 = 10.5
# Llamar a la función y guardar el resultado
# Escribe aquí tu código


print(f"Radio: {radio3} -> Área: {area3}")

print("\n=== MODO INTERACTIVO ===")
# Solicitar al usuario un radio y calcular su área
# Escribe aquí tu código para pedir el radio al usuario

# Convertir la entrada a número decimal
# Escribe aquí tu código


# Llamar a la función con el radio del usuario
# Escribe aquí tu código


print(f"El área de un círculo con radio {radio_usuario} es: {area_usuario}")