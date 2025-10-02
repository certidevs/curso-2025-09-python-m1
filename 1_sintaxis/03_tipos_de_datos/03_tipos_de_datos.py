print("NÚMEROS ENTEROS")
print("=" * 20)
print("\n")

edad = 25
temperatura_bajo_cero = -10
poblacion_mundial = 8_000_000_000

print(f"Edad: {edad}")
print("Edad: " + str(edad))
print(f"Temperatura bajo cero: {temperatura_bajo_cero}")
print(f"Población mundial: {poblacion_mundial}")

numero_grande = 123456789012345678901234567890
print(f"Número grande: {numero_grande}")
print(f"Número grande + 1: {numero_grande + 1}")

print("\n")
print("=" * 20)
print("NÚMEROS DECIMALES (FLOAT)")
print("=" * 20)
print("\n")

altura = 1.74
pi = 3.141592654
temperatura = 36.6

resultado_flotante = 0.1 + 0.2
print(f"0.1 + 0.2 = {resultado_flotante}")

import math
es_aproximadamente_igual = math.isclose(0.1 + 0.2, 0.3)
print(f"¿0.1 + 0.2 es APROXIMADAMENTE igual a 0.3? {es_aproximadamente_igual}")

print("\n")
print("=" * 20)
print("NÚMEROS COMPLEJOS")
print("=" * 20)
print("\n")

complejo = 3 + 4j
print(f"Número complejo: {complejo}")
print(f"Parte real: {complejo.real}")
print(f"Parte imaginaria: {complejo.imag}")

print("\n")
print("=" * 20)
print("OPERACIONES")
print("=" * 20)
print("\n")

suma = 5 + 3
resta = 10 - 4
multiplicacion = 3 * 7
division = 20 / 4

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")

redondeo_decimal = round(3.141592654, 2)
print(f"Redondeo a 2 decimales: {redondeo_decimal}")

print("\n")
print("=" * 20)
print("CONVERSIONES")
print("=" * 20)
print("\n")

edad_aproximada = int(27.9999999)
print(f"Edad aproximada: {edad_aproximada}")

precio_exacto = float(20)
print(f"Precio exacto: {precio_exacto}")

cantidad = int("15")
medida = float("7.5")

print("\n")
print("=" * 20)
print("NÚMEROS ALEATORIOS")
print("=" * 20)
print("\n")

import random

dado = random.randint(1, 6)
print(f"Tirar un dado de 4: {random.randint(1, 4)}")
print(f"Tirar un dado de 6: {dado}")
print(f"Tirar un dado de 8: {random.randint(1, 8)}")
print(f"Tirar un dado de 10: {random.randint(1, 10)}")
print(f"Tirar un dado de 12: {random.randint(1, 12)}")
print(f"Tirar un dado de 20: {random.randint(1, 20)}")

print("\n")
print("=" * 20)
print("TEXTO (STRING)")
print("=" * 20)
print("\n")

nombre_simple = 'Ana'
mensaje = "Hola, ¿cómo estás?"
descripcion = """Este es un texto
que ocupa varias
líneas"""

print(nombre_simple)
print(mensaje)
print(descripcion)

palabra = "Hola"
letra_L = palabra[2]
print(letra_L)

print("\n")
print("=" * 20)
print("MÉTODOS DE CADENAS")
print("=" * 20)
print("\n")

genero = "Corvus"
especie = "Monedula"
especie_minusculas = especie.lower()

nombre_cientifico = genero + " " + especie_minusculas
print(nombre_cientifico)

print("\n")
print("=" * 20)
print("BÚSQUEDA EN CADENAS")
print("=" * 20)
print("\n")

frase = "Me encantan las aves"

contiene_ave = "aves" in frase
print(f"Frase: {frase}")
print(contiene_ave)

print("\n")
print("=" * 20)
print("FORMATEO DE CADENAS")
print("=" * 20)
print("\n")

nombre = "Grajilla"
edad = 27
mensaje = f"Hola, me llamo {nombre} y tengo {edad} años"

print(mensaje)

print(f"Me encanta el ave {nombre}")

print("\n")
print("=" * 20)
print("FORMATEO DE CADENAS")
print("=" * 20)
print("\n")

# Salto de línea \n
print("Primera línea\nSegunda línea")

# Tabulación \t
print("Nombre:\tJuan")

# Comillas dentro de comillas \"
print("Él dijo: \"Hola\"")
print('Ella respondió: \'Adiós\'')

# Barra invertida \\
print("Ruta de Windows: C:\\Usuarios\\Juan")

print("\n")
print("=" * 20)
print("CONVERSIONES")
print("=" * 20)
print("\n")

edad = 25
edad_texto = str(edad)
print("Edad: " + edad_texto)

print("\n")
print("=" * 20)
print("BOOLEAN")
print("=" * 20)
print("\n")

esta_lloviendo = True
print(f"¿Está lloviendo? {esta_lloviendo}")

es_fin_de_semana = False
print(f"¿Es fin de semana? {es_fin_de_semana}")

print("\n")
print("=" * 20)
print("CONVERSIONES")
print("=" * 20)
print("\n")

print(bool(0))
print(bool(42))
print(bool("")) 
print(bool("Hola")) 
print(bool([])) 
print(bool([1, 2, 3]))