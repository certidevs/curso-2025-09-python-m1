"""
- "Vehiculo" es la clase padre que define atributos y comportamientos comunes a todos los vehículos.

- "Automovil" es la clase hija que hereda de Vehiculo y añade características específicas (número de puertas).

- La clase hija puede acceder a todos los atributos y métodos de la clase padre.

"""

class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.encendido = False
        
    def encender(self):
        self.encendido = True
        return f"{self.marca} {self.modelo} encendido"
    
    def apagar(self):
        self.encendido = False
        return f"{self.marca} {self.modelo} apagado"
    
    def describir(self):
        return f"Vehículo: {self.marca} {self.modelo} del año {self.año}"

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, año, puertas):
        # super().__init__(self, marca, modelo, año)
        Vehiculo.__init__(self, marca, modelo, año)
        self.puertas = puertas
        
    def describir(self):
        return f"Automóvil: {self.marca} {self.modelo} del año {self.año} con {self.puertas} puertas"
    
mi_auto = Automovil("Toyota", "Corolla", 2023, 4)

# Verificamos instancias
print(isinstance(mi_auto, Automovil))  # True
print(isinstance(mi_auto, Vehiculo))   # True - también es instancia de la clase padre

# Verificamos relaciones de clases
print(issubclass(Automovil, Vehiculo))  # True
print(issubclass(Vehiculo, Automovil))  # False - la relación es unidireccional

print(Automovil.__mro__)
# Muestra el orden en que Python busca métodos: primero en Automovil, luego en Vehiculo, y finalmente en object