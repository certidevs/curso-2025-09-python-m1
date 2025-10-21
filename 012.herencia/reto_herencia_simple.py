print("=== PROGRAMA: JERARQUÍA DE PRODUCTOS ===\n")

# Clase base Producto
class Producto:
    def __init__(self, nombre, precio, stock):
        # Inicializar atributos básicos
        self.nombre = nombre
        self.precio = precio
        self.stock = stock        
    
    def mostrar_info(self):
        # Devolver información básica del producto
        return f"Producto: {self.nombre} | Precio: {self.precio} € | Stock: {self.stock} unidades"
    
    def hay_stock(self):
        # Verificar si hay unidades disponibles
        return self.stock > 0

# Clase Alimento que hereda de Producto
class Alimento(Producto):
    def __init__(self, nombre, precio, stock, fecha_caducidad):
        # Llamar al constructor de la clase padre
        super().__init__(nombre, precio, stock)
        
        # Inicializar atributo específico de Alimento
        self.fecha_caducidad = fecha_caducidad
        
    def mostrar_info(self):
        # Sobreescribir el método para incluir fecha de caducidad
        # Escribe aquí tu código (puedes usar super() o reimplementar)
        # return f"Producto: {self.nombre} | Precio: {self.precio} € | Stock: {self.stock} unidades | Fecha de caducidad: {self.fecha_caducidad}"
        info_base = super().mostrar_info()
        return f"{info_base} | Fecha de caducidad: {self.fecha_caducidad}"
        

# Clase Electronico que hereda de Producto
class Electronico(Producto):
    def __init__(self, nombre, precio, stock, garantia):
        # Llamar al constructor de la clase padre
        super().__init__(nombre, precio, stock)
        
        # Inicializar atributo específico de Electronico
        self.garantia = garantia
        
    
    def mostrar_info(self):
        # Sobreescribir el método para incluir información de garantía
        # Escribe aquí tu código (puedes usar super() o reimplementar)
        # return f"Producto: {self.nombre} | Precio: {self.precio} € | Stock: {self.stock} unidades | Garantía: {self.garantia} meses"
        info_base = super().mostrar_info()
        return f"{info_base} | Garantía: {self.garantia} meses"
        

# === CREACIÓN Y PRUEBA DE INSTANCIAS ===
print("=== CREANDO PRODUCTOS ===")

# Crear una instancia de Producto genérico
producto_generico = Producto("Producto aleatorio", 9.99, 100)

# Crear una instancia de Alimento
alimento = Alimento("Leche", 2.50, 50, "2025-12-30")

# Crear una instancia de Electronico
electronico = Electronico("Portátil", 599.99, 0, 24)

print("\n=== INFORMACIÓN DE PRODUCTOS ===")

# Mostrar información del producto genérico
print(producto_generico.mostrar_info())

# Mostrar información del alimento
print(alimento.mostrar_info())

# Mostrar información del electrónico
print(electronico.mostrar_info())

print("\n=== VERIFICANDO STOCK ===")

# Verificar stock de cada producto

# forma fácil

productos = [producto_generico, alimento, electronico]

for item in productos:
    stock_disponible = "Sí" if item.hay_stock() else "No"
    print(f"{item.nombre} - ¿Hay stock? {stock_disponible}")

print("\n")
# forma elegante (mostrando el tipo de producto)

# lista de tuplas
productos = [
    ("Producto genérico", producto_generico),
    ("Alimento", alimento),
    ("Producto electrónico", electronico)
]

for nombre_tipo, producto in productos:
    stock_disponible = "Sí" if producto.hay_stock() else "No"
    print(f"{nombre_tipo} ({producto.nombre}): ¿Hay stock? {stock_disponible}")