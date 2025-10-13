
"""

Listas: [] o list()

* mutables: se pueden modificar, reordenar, añadir elementos, borrar


Métodos relevantes:

* Longitud: len()

CRUD: (Create, Read, Update, Delete):

* Acceso elementos: 
    * Primero: nombres[0]
    * Último: nombres[-1]
    * IndexError: list index out of range si ponemos un índice fuera del rango
* Slicing:
    * nombres[1:4] # el stop está excluido
    
* Mutar un elemento mediante asignación:
    * precios[0] = precios[0] * 1.21

* Añadir o combinar:
    * nombres.append("Patricia")
    * nombres.extend(['n1', 'n2']) también se pueden concatenar con el operador +
    * nombres.insert(index, 'bob')
    
* Eliminar elementos:
    * pop() quita y devuelve el último elemento
    * pop(0) quita y devuelve el primer elemento
    * remove(x) elimina la primera ocurrencia
    * del nombres[0]
    * nombres.clear()
    
* Recorrer: 
    * for nombre in nombres: print(nombre)
    * for index, nombre in enumerate(nombres): print(f"índice: {index}, nombre {nombre}")
    * for index in range(len(nombres1)): print(nombres1[index])

* Buscar:
    * 'Pepe' in nombres
    * nombres.index('María') devuelve el índica de la primera ocurrencia 
        * ValueError: 'Alan' is not in list
* Clonar:
    * copy()
    
* Ordenar:
    * sort()
    * reverse()
"""

lista_vacia = []
otra_lista_vacia = list()

nombres1 = ['Juan', 'Grajilla', 'Mike', 'Pepe', 'Reyes', 'Kary', 'Jaime']
nombres2 = ['Juan', 'Grajilla', 'Mike', 'Pepe', 'Reyes', 'Kary']

print(nombres1 * 2)

print()

mi_pajaro_favorito = nombres1[1]
print(mi_pajaro_favorito)

print()

ultimo_nombre = nombres1[-1]
print(ultimo_nombre)

print()

numeros = [10, 20, 30, 40, 50, 60, 70]

primeros_tres = numeros[0:3]
print(primeros_tres)

print()

compras = ["leche", "pan", "huevos", "frutas"]

if "pan" in compras:
    print("Pan está en la lista de compras")
    
if "queso" not in compras:
    print("Necesito añadir queso a la lista")

print()

tareas = ["estudiar", "hacer ejercicio", "programar", "descansar"]

cantidad_tareas = len(tareas)  # 4
print(cantidad_tareas)

posicion = tareas.index("programar")  # 2

print()

zurron = ["poción", "espada", "escudo", "poción", "armadura ligera", "poción"]
ocurrencias_pocion = zurron.count("poción")  # 3
print(f"{ocurrencias_pocion} poción(es)")

print()