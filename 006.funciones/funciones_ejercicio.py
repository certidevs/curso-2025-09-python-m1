
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
    PI = 3.14159
    
    
    # 2. Calcular el área usando la fórmula: π * radio²
    area = PI * (radio ** 2)    
    
    # 3. Devolver el resultado
    return area
    


print("=== PRUEBAS DE LA FUNCIÓN ===")

# Prueba 1: radio = 5
radio1 = 5
# Llamar a la función y guardar el resultado
area1 = calcular_area_circulo(radio1)

print(f"Radio: {radio1} -> Área: {area1}")

# Prueba 2: radio = 3
radio2 = 3
# Llamar a la función y guardar el resultado
area2 = calcular_area_circulo(radio2)

print(f"Radio: {radio2} -> Área: {area2}")

# Prueba 3: radio = 10.5
radio3 = 10.5
# Llamar a la función y guardar el resultado
area3 = calcular_area_circulo(radio3)

print(f"Radio: {radio3} -> Área: {area3}")

print("\n=== MODO INTERACTIVO ===")
# Solicitar al usuario un radio y calcular su área
radio_input = input("Introduce un valor para el radio: ")

# Convertir la entrada a número decimal
radio_usuario = float(radio_input)

# Llamar a la función con el radio del usuario
area_usuario = calcular_area_circulo(radio_usuario)

print(f"El área de un círculo con radio {radio_usuario} es: {area_usuario}")