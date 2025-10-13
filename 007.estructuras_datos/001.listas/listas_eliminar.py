colores = ["rojo", "verde", "azul", "verde"]
colores.remove("verde")  # Elimina solo el primer "verde"
print(colores)  # ["rojo", "azul", "verde"]

print()

numeros = [10, 20, 30, 40]
ultimo = numeros.pop()  # Elimina y devuelve 40
print(ultimo)  # 40
print(numeros)  # [10, 20, 30]

segundo = numeros.pop(1)  # Elimina y devuelve 20
print(segundo)  # 20
print(numeros)  # [10, 30]

print()

mi_lista = [1, 2, 3, 4]
mi_lista.clear()
print(mi_lista)  # []