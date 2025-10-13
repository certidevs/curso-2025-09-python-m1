frutas = ["manzana", "plátano", "naranja", "uva"]
print(frutas)

for fruta in frutas:
    print(f"Me gusta comer {fruta}")

print()

tareas = ["estudiar", "hacer ejercicio", "programar"]
print(tareas)

for indice, tarea in enumerate(tareas):
    print(f"Tarea {indice + 1}: {tarea}")

print()

# Comenzando desde 1 para una numeración más natural
for num, tarea in enumerate(tareas, 1):
    print(f"Tarea {num}: {tarea}")

print()

numeros = [10, 20, 30, 40, 50]

for i in range(len(numeros)):
    print(f"Posición {i}: {numeros[i]}")

print()

colores = ["rojo", "verde", "azul", "amarillo"]

for color in reversed(colores):
    print(color)

print()

numeros = [1, 2, 3, 4, 5]
print(numeros)

# Crear una nueva lista con los cuadrados
cuadrados = [num * num for num in numeros]
print(cuadrados)  # [1, 4, 9, 16, 25]

# Filtrar solo los números pares
pares = [num for num in numeros if num % 2 == 0]
print(pares)  # [2, 4]

print()

nombres = ["Ana", "Carlos", "Elena"]
edades = [28, 32, 25]
ciudades = ["Madrid", "Barcelona", "Sevilla"]

for nombre, edad, ciudad in zip(nombres, edades, ciudades):
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")

print()

compras = ["pan", "leche", "huevos", "frutas"]
i = 0

while i < len(compras):
    print(f"Debo comprar: {compras[i]}")
    i += 1

print()