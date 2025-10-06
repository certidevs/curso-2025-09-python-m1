print("\n")
print("=" * 20)
print("ESTRUCTURAS CONTROL CONDICIONAL")
print("=" * 20)
print("\n")

print("\n")
print("=" * 20)
print("IF")
print("=" * 20)
print("\n")

edad = 20
print(f"Edad: {edad}")

if edad >= 18:
    print("Eres mayor de edad")
    
edad = 16
print(f"Edad: {edad}")

if edad >= 18:
    print("Eres mayor de edad")
    
edad = 18
print(f"Edad: {edad}")

if edad >= 18:
    print("Eres mayor de edad")


print("\n")

temperatura = 30
print(f"Temperatura: {temperatura}")

if temperatura > 25:
    print("Hace calor.")
    
    
temperatura = 20
print(f"Temperatura: {temperatura}")

if temperatura > 25:
    print("Hace calor.")


temperatura = 25
print(f"Temperatura: {temperatura}")

if temperatura > 25:
    print("Hace calor.")
    

print("\n")

edad = 18
print(f"Edad: {edad}")

if edad > 17:
    print("Eres mayor de edad")
    

print("\n")

hora = 10
print(f"Hora: {hora}")

if hora >= 6 and hora < 12:
    print("Buenos días")
    
# Horas que cumplen esta condición:
# 6, 7, 8, 9, 10 y 11


print("\n")

numero = 15
print(f"Número: {numero}")

if numero == 15:
    print("== El número es igual a 15")
    
if numero != 10:
    print("!= El número es diferente a 10")
    
if numero > 10:
    print("> El número es mayor que 10")
    
if numero < 20:
    print("< El número es menor que 20")
    
if numero >= 15:
    print(">= El número es mayor o igual que 15")
    
if numero <= 20:
    print("<= El número es menor o igual que 20")

print("\n")
print("=" * 20)
print("IF-ELSE")
print("=" * 20)
print("\n")

edad = 17
print(f"Edad: {edad}")

if edad >= 18:
    print("Puedes votar en las elecciones.")
else:
    print("Aún no tienes edad para votar.")


print("\n")

edad = 18
print(f"Edad: {edad}")

if edad >= 18:
    print("Puedes votar en las elecciones.")
else:
    print("Aún no tienes edad para votar.")

print("\n")

numero = 15
print(f"Número: {numero}")

if numero % 2 == 0:
    print("El número es par")
else:
    print("El número es impar.")

print("\n")
    
numero = 18
print(f"Número: {numero}")

if numero % 2 == 0:
    print("El número es par")
else:
    print("El número es impar.")


print("\n")
print("=" * 20)
print("IF-ELIF-ELSE")
print("=" * 20)
print("\n")

numero = 0
print(f"Número: {numero}")

if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")

print("\n")

numero = 8
print(f"Número: {numero}")

if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")


print("\n")

numero = -5
print(f"Número: {numero}")

if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")


print("\n")

numero = 0
print(f"Número: {numero}")

if numero > 0:
    print("El número es positivo.")
elif numero <= 0:
    print("El número es negativo.")
else:
    print("El número es cero.")


print("\n")
print("=" * 20)
print("MATCH-CASE")
print("=" * 20)
print("\n")

# fruta = input("Introduzca una fruta: ")
fruta = "manzana"

match fruta:
    case "manzana":
        print("La fruta es una manzana.")
    case "naranja":
        print("La fruta es una naranja.")
    case "plátano":
        print("La fruta es un plátano.")
    case _:
        print("Fruta desconocida.")

print("\n")

punto = (0, 0)
print(f"Punto: {punto}")

match punto:
    case (0, 0):
        print("El punto está en el origen.")
    case (0, y):
        print(f"El punto está en el eje Y en y={y}.")
    case (x, 0):
        print(f"El punto está en el eje X en x={x}.")
    case (x, y):
        print(f"El punto está en las coordenadas x={x}, y={y}.")


print("\n")

punto = (0, 5)
print(f"Punto: {punto}")

match punto:
    case (0, 0):
        print("El punto está en el origen.")
    case (0, y):
        print(f"El punto está en el eje Y en y={y}.")
    case (x, 0):
        print(f"El punto está en el eje X en x={x}.")
    case (x, y):
        print(f"El punto está en las coordenadas x={x}, y={y}.")


print("\n")

punto = (1, 1)
print(f"Punto: {punto}")

match punto:
    case (0, 0):
        print("El punto está en el origen.") 
    case (1, 1):
        print("El punto está en el punto x=1, y=1.")
    case (0, y):
        print(f"El punto está en el eje Y en y={y}.")
    case (x, 0):
        print(f"El punto está en el eje X en x={x}.")
    case (x, y):
        print(f"El punto está en las coordenadas x={x}, y={y}.")

print("\n")

edad = 20
print(f"Edad: {edad}")

match edad:
    case 100:
        print("Tienes 100 años.")
    case edad if edad < 18:
        print("Eres menor de edad.")
    case edad if edad == 18:
        print("Tienes exactamente 18 años.")
    case edad if edad > 18 and edad < 65:
        print("Eres adulto.")
    case edad if edad >= 65:
        print("Eres adulto mayor.")


print("\n")
print("=" * 20)
print("CONDICIONALES ANIDADOS")
print("=" * 20)
print("\n")

edad = 30
estado_civil = "soltero"
print(f"Edad: {edad}, Estado civil: {estado_civil}")

if edad >= 18:
    if estado_civil == "casado":
        print("Eres un adulto casado.")
    else:
        print("Eres un adulto soltero.")
else:
    print("Eres menor de edad.")
    
print("\n")

edad = 12
estado_civil = "casado"
print(f"Edad: {edad}, Estado civil: {estado_civil}")

if edad >= 18:
    if estado_civil == "casado":
        print("Eres un adulto casado.")
    else:
        print("Eres un adulto soltero.")
else:
    print("Eres menor de edad.")


print("\n")

edad = 30
estado_civil = "casado"
print(f"Edad: {edad}, Estado civil: {estado_civil}")

if edad >= 18:
    if estado_civil == "casado":
        print("Eres un adulto casado.")
    else:
        print("Eres un adulto soltero.")
else:
    print("Eres menor de edad.")


print("\n")
print("=" * 20)
print("CONDICIONAL TERNARIO")
print("=" * 20)
print("\n")

edad = 17
print(f"Edad: {edad}")

mensaje = "Eres mayor de edad." if edad >= 18 else "Eres menor de edad"

print(mensaje)

