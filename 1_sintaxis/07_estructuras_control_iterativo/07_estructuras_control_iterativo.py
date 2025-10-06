print("\n")
print("=" * 20)
print("ESTRUCTURAS CONTROL ITERATIVO")
print("=" * 20)
print("\n")

print("\n")
print("=" * 20)
print("BUCLES FOR")
print("=" * 20)
print("\n")

frutas = ["manzana", "banana", "cereza"]
print(f"Lista de frutas: {frutas}")

for fruta in frutas:
    print(fruta)

print("\n")
print("=" * 20)
print("RANGE")
print("=" * 20)
print("\n")

for i in range(5):
    print(i)
    
print("\n")

for i in range(3, 8):
    print(i)
    
print("\n")

for i in range (2, 11, 2):
    print(i)
    
print("\n")

for i in range(5, 0, 1):
    print(i)
    
print("\n")

# cuenta atrás hasta 0
for i in range(5, -1, -1):
    print(i)

print("\n")
print("=" * 20)
print("ITERAR SOBRE ÍNDICES")
print("=" * 20)
print("\n")

nombres = ["Ana", "Carlos", "Elena"]
print(f"Lista de nombres: {nombres}")

for i in range(len(nombres)):
    print(f"Posición {i}: {nombres[i]}")

print("\n")

for indice, nombre in enumerate(nombres):
    print(f"Posición {indice}: {nombre}")

print("\n")
print("=" * 20)
print("BUCLES WHILE")
print("=" * 20)
print("\n")

