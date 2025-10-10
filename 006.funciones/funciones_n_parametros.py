
# Crear una función que reciba un numero de inicio y un numero de fin
# y devuelva una lista con numeros: [inicio, 2, 3, 4, 5, 6 ... fin]
# Pista: usar range()

def crear_lista_numeros(inicio, fin):
    return list(range(inicio, fin + 1))


lista1 = crear_lista_numeros(1, 5)
print(lista1) # [1, 2, 3, 4, 5]

lista2 = crear_lista_numeros(1, 10)
print(lista2) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista3 = crear_lista_numeros(5, 20)
print(lista3) # [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]