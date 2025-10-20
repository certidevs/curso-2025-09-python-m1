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

# crear las clases
class Categoria:
    def __init__(self, id, nombre, descripcion):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.productos = []

class Producto:
    def __init__(self, id, nombre, precio):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        
# crear los objetos
categoria1 = Categoria(1, "Lácteos", "Productos derivados de la leche")
categoria2 = Categoria(2, "Frutas", "Productos frescos")
producto1 = Producto(1, "Leche", 1.0)
producto2 = Producto(2, "Queso", 4.5)
producto3 = Producto(3, "Yogur", 1.25)
producto4 = Producto(4, "Naranja", 0.75)

# asignar la referencia
categoria1.productos.append(producto1)
categoria1.productos.append(producto2)
categoria1.productos.append(producto3)
categoria2.productos.append(producto4)


# relación BIDIRECCIONAL (ambas conocen de la otra)

# crear las clases
class Categoria:
    def __init__(self, id, nombre, descripcion):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.productos = [] # lista de productos

class Producto:
    def __init__(self, id, nombre, precio, categoria):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria # agregamos referencia

categoria1 = Categoria(1, "Electrónica", "Dispositivos electrónicos")
producto1 = Producto(1, "Portátil", 799.99, categoria1)
producto2 = Producto(2, "Teclado mecánico", 150.0, categoria1)

"""
Muchos a Uno (Many to One):
    Un profesor trabaja en UN departamento. Y ese departamento puede tener MUCHOS profesores.
"""

# crear las clases
class Departamento:
    def __init__(self, id, nombre, ubicacion):
        self.id = id
        self.nombre = nombre
        self.ubicacion = ubicacion

class Profesor:
    def __init__(self, id, nombre, especialidad, departamento):
        self.id = id
        self.nombre = nombre
        self.especialidad = especialidad
        self.departamento = departamento

# crear los objetos
dpto1 = Departamento(1, "Matemáticas", "Edificio A1")

# asignar la referencia
profesor1 = Profesor(1, "Tornasol", "Topología", dpto1)
profesor2 = Profesor(2, "Bacterio", "Cálculo", dpto1)


"""
Muchos a muchos (Many to Many):
    Un estudiante pueden tener MUCHAS asignaturas. Cada asignatura puede tener MUCHOS estudiantes.
"""


