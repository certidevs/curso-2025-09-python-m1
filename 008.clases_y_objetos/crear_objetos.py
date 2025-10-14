"""
Constructor: método especial que se ejecuta automáticamente cuando creamos un nuevo objeto.

El método __init__ se ejecuta automáticamente al crear el objeto y sirve para dejar el objeto con datos  iniciales.
"""

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

persona1 = Persona("Carla", 50)

"""
El parámetro self es una referencia al objeto que se está creando o manipulando.
"""

class Libro:
    # atributos: titulo, autor, numero de paginas
    # metodos: abrir, leer, cerrar, subrayar
    def __init__(self, titulo, autor, numero_paginas=None):
        self.titulo = titulo
        self.autor = autor
        self.numero_paginas = numero_paginas
        self.abierto = False
    
    def abrir(self):
        self.abierto = True
        print(f"Se ha abierto {self.titulo}")
    
    def cerrar(self):
        self.abierto = False
        print(f"Se ha cerrado {self.titulo}")

# libro_python = Libro()
libro = Libro("The Pillars of the Earth", "Ken Follett", 1000)

otro_libro = Libro("The Evening and the Morning", "Ken Follet")