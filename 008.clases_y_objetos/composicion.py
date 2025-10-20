"""
Uno a Uno (One to One):
    Un ciudadano español tiene UN DNI. Y ese DNI pertenece sólo a UN ciudadano español.
"""

# crear las clases
class Ciudadano:
    def __init__(self, id, nombre, apellido, edad):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.dni = None
        
class DNI:
    def __init__(self, id, numero):
        self.id = id
        self.numero = numero

# crear los objetos
ciudadano1 = Ciudadano(1, "Grajilla", "Occidental", 27)
dni1 = DNI(1, "12345678Z")

# asignar la referencia
ciudadano1.dni = dni1


"""
Uno a Muchos (One to Many):
    Una categoría puede tener MUCHOS productos. Y un producto sólo puede pertenecer a UNA categoría.
"""



"""
Muchos a Uno (Many to One):
    Un profesor trabaja en UN departamento. Y ese departamento puede tener MUCHOS profesores.
"""



"""
Muchos a muchos (Many to Many):
    Un estudiante pueden tener MUCHAS asignaturas. Cada asignatura puede tener MUCHOS estudiantes.
"""


