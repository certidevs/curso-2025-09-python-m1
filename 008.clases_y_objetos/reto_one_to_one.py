print("=== EJERCICIO: RELACIÓN EMPLEADO-TARJETA CORPORATIVA ===\n")

# 1. Crear la clase Empleado con los atributos: id, nombre, cargo, salario
# El atributo 'tarjeta' debe inicializarse como None
class Empleado:
    def __init__(self, id, nombre, cargo, salario):
        self.id = id
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario
        self.tarjeta = None

# 2. Crear la clase TarjetaCorporativa con los atributos: id, numero, fecha_emision, empleado_id
class TarjetaCorporativa:
    def __init__(self, id, numero, fecha_emision, empleado_id):
        self.id = id
        self.numero = numero
        self.fecha_emision = fecha_emision
        self.empleado_id = empleado_id # FK (Clave Foránea) hacia Empleado

print("=== CREANDO OBJETOS ===")

# 3. Crear un empleado con id: 1, nombre: Alba Motacilla, cargo: Desarrolladora, salario: 45000
empleado1 = Empleado(1, "Alba Motacilla", "Desarrolladora", 45000)

# 4. Crear una tarjeta corporativa con id: 1, número: TC001, fecha de emisión: 2025-01-15, id de empleado: 1
tarjeta1 = TarjetaCorporativa(1, "TC001", "2025-01-01", 1)

print("=== ESTABLECIENDO RELACIÓN ===")

# 5. Asignar la tarjeta al empleado (relación one-to-one)
empleado1.tarjeta = tarjeta1

print("=== VERIFICANDO RELACIÓN ===")

# 6. Imprimir información del empleado y su tarjeta
# Hay para mostrar:
# - Nombre del empleado
# - Número de tarjeta
print(f"Empleado: {empleado1.nombre}")
print(f"Número de tarjeta: {empleado1.tarjeta.numero}")
print(f"Fecha de emisión: {empleado1.tarjeta.fecha_emision}")
print(f"Fecha de emisión: {tarjeta1.fecha_emision}")

print("\n=== RESULTADO FINAL ===")
# 7. Mostrar un mensaje confirmando la relación one-to-one
print(f"{empleado1.nombre} tiene la tarjeta {empleado1.tarjeta.numero}")