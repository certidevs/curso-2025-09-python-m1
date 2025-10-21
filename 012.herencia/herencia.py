"""
La herencia permite que una clase (llamada clase hija o subclase) adquiera los atributos y métodos de otra clase (llamada clase padre o superclase).
"""

# clase padre o superclase
class Animal:
    def __init__(self, edad):
        self.edad = edad

# clase hija (subclase) de Animal y es también la clase padre (superclase) de Mirlo
class Ave(Animal):
    def __init__(self, edad, plumas):
        pass

# clase hija (subclase) de Animal y es también la clase padre (superclase) de Gato y Tigre
class Felino(Animal):
    def __init__(self, edad, ronrroneo):
        pass

# clase hija (subclase) de Ave
class Mirlo(Ave):
    def __init__(self, edad, plumas, canto):
        pass

# clase hija (subclase) de Felino
class Gato(Felino):
    def __init__(self, edad, ronrroneo, nombre):
        pass

# clase hija (subclase) de Felino
class Tigre(Felino):
    def __init__(self, edad, ronrroneo, rayas):
        pass