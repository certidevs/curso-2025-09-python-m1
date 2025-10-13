original = [1, 2, 3]
print(original)
copia = original.copy()
print(copia)

print()

copia.append(4)
print(original)  # [1, 2, 3] - No se modifica
print(copia)     # [1, 2, 3, 4]

print()