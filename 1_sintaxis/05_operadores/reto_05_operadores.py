print("=== CALCULADORA DE IMC ===\n")

# 1. Declara dos variables: 'peso' con valor 70 (en kilogramos) y 'altura' con valor 1.75 (en metros)
peso = 70

# Escribe aquí tu código para la variable altura
altura = 1.75

print("=== DATOS INGRESADOS ===")
print(f"Peso: {peso} kg")
print(f"Altura: {altura} m")

print("\n=== CÁLCULO DEL IMC ===")

# 2. Calcula el IMC utilizando la fórmula: peso / (altura ** 2)
# 3. Almacena el resultado en una variable llamada 'imc'
imc = peso / (altura ** 2)

# 4. Redondea el resultado a dos decimales usando la función round()
imc_redondeado = round(imc, 2)

print("=== RESULTADO ===")
# 5. Imprime el resultado con un mensaje descriptivo
print(f"Tu Índice de Masa Corporal (IMC) es: {imc_redondeado}")