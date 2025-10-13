tareas = ["estudiar", "ejercicio"]
tareas.append("programar")
print(tareas)  # ["estudiar", "ejercicio", "programar"]

print()

compras = ["pan", "huevos"]
compras.insert(1, "leche")  # Inserta en la posición 1
print(compras)  # ["pan", "leche", "huevos"]

print()

frutas = ["manzana", "plátano"]
mas_frutas = ["naranja", "uva"]
frutas.extend(mas_frutas)
print(frutas)  # ["manzana", "plátano", "naranja", "uva"]

print()

lista1 = [1, 2, 3]
lista2 = [4, 5]

# Con append, añade la lista completa como un único elemento
lista1.append(lista2)
print(lista1)  # [1, 2, 3, [4, 5]]

# Con extend, añade cada elemento individualmente
lista1 = [1, 2, 3]  # Reiniciamos la lista
lista1.extend(lista2)
print(lista1)  # [1, 2, 3, 4, 5]