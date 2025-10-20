print("=== EJERCICIO: RELACIÓN HABITACIONES-HOTEL ===\n")

# 1. Crear la clase Hotel con los atributos: id, nombre, direccion, estrellas
class Hotel:
    def __init__(self, id, nombre, direccion, estrellas):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.estrellas = estrellas

# 2. Crear la clase Habitacion con los atributos: id, numero, tipo, precio, hotel
class Habitacion:
    def __init__(self, id, numero, tipo, precio, hotel):
        self.id = id
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.hotel = hotel

print("=== CREANDO OBJETOS ===")

# 3. Crear un hotel con id: 1, nombre: Hotel Carbonero, dirección: Plaza Parus Mayor 123, estrellas: 4
hotel1 = Hotel(1, "Hotel Carbonero", "Plaza Parus Mayor 123", 4)

# 4. Crear tres habitaciones:
# - id: 1, número: 101, tipo: Individual, precio: 80, hotel: Hotel Carbonero
# - id: 2, número: 102, tipo: Doble, precio: 120, hotel: Hotel Carbonero
# - id: 3, número: 103, tipo: Suite, precio: 200, hotel: Hotel Carbonero
habitacion1 = Habitacion(1, 101, "Individual", 80, hotel1)
habitacion2 = Habitacion(2, 102, "Doble", 120, hotel1)
habitacion3 = Habitacion(3, 103, "Suite", 200, hotel1)

print("=== VERIFICANDO RELACIÓN ===")

# 5. Imprimir información del hotel y sus habitaciones
# Hay que mostrar:
# - Nombre del hotel y sus estrellas
print(f"Nombre: {hotel1.nombre}, Estrellas: {hotel1.estrellas}")
print(f"Nombre: {habitacion1.hotel.nombre}, Estrellas: {habitacion1.hotel.estrellas}")

print("\n=== RESULTADO FINAL ===")
# 7. Mostrar un mensaje confirmando la relación many-to-one
print(f"La habitación {habitacion1.numero} pertenece al hotel {habitacion1.hotel.nombre}")