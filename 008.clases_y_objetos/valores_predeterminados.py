"""
Al definir valores predeterminados para los parámetros del constructor los convertimos en opcionales.
"""

# crear la clase Producto
class Producto:
    def __init__(self, nombre, precio, stock=0):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

# crear objetos Producto
laptop = Producto("Portátil baratucho", 350) # el stock será 0 (porque el valor por defecto es 0)
teclado = Producto("Teclado mecánico", 80, 15) # el stock será 15 (porque lo he especificado)