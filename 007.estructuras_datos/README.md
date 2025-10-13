
* listas: []
* tuplas: ()
* diccionarios: {}
* conjuntos: {}


## Listas

Colecciones ordenadas y mutables de elementos

### Características

* Se pueden modificar (agregar, eliminar, cambiar elementos)
* Mantienen el orden
* Permiten elementos duplicados
* Se accede a los elementos mediante índices (comenzando en 0)
* Se definen con corchetes `[]` o la función `list()`

#### Ejemplo

```python
lista = [1, 2, 3, 4, 5]
lista.append(6)
lista[0] = 10
```


## Tuplas

Colecciones ordenada e inmutables de elementos

### Características

* NO se pueden modificar después de crear
* Mantienen el orden
* Permiten elementos duplicados
* Se definen con paréntesis `()`

#### Ejemplo

```python
tupla = (1, 2, 3, 4, 5)
# tupla[0] = 10 # ERROR: No se puede modificar
```


## Diccionarios

Colecciones de pares clave-valor

### Características

* Acceso por clave, no por índice
* Mutables (se puede modificar)
* Claves únicas, valores pueden repetirse
* Se definen con llaves `{}` o `dict()`

#### Ejemplo

```python
diccionario = {
    "nombre": "Grajilla", 
    "edad": 27, 
    "ciudad": "Jaén"}
diccionario["edad"] = 28 # Modifica valor
diccionario["profesion"] = "Programador" # Agrega nueva clave

customer = {
"id": 1,
"name": "John Doe",
"age": 30,
"is_verified": True,
"balance": 100.5,
"tags": ["premium", "active"],
"address": {
"street": "123 Main St",
"city": "Anytown",
"zip": "12345"
}
}

customer["age"] = 31 # Modificar valor (forma 1)
customer.update({"age": 31}) # Modificar valor (forma 2)

customer["address"]["street"] = "Otra Calle" # Modificar valor (forma 1)
customer["address"].update({"street": "Otra Calle Más"}) # Modificar valor (forma 2)
```


## Conjuntos (sets)

Colecciones no ordenadas de elementos únicos

### Características

* No permiten elementos duplicados
* No mantienen orden
* Mutables (se pueden modificar)
* Se definen con llaves `{}` o `set()`

#### Ejemplo

```python
conjunto = {1, 2, 3, 4, 5}
conjunto.add(6) # Agregar elemento
conjunto.discard(3) # Eliminar elemento
```