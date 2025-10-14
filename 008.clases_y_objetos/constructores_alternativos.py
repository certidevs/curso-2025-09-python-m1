class Fecha:
    def __init__(self, dia, mes, año): # (23, 07, 1998)
        self.dia = dia
        self.mes = mes
        self.año = año
    
    @classmethod # ("23-07-1998")
    def desde_texto(cls, texto):
        """Constructor alternativo que crea una Fecha desde un texto con formato DD-MM-AAAA"""
        dia, mes, año = map(int, texto.split('-'))
        return cls(dia, mes, año)
    
    @classmethod
    def hoy(cls):
        """Constructor alternativo que crea una Fecha con la fecha actual"""
        import datetime
        fecha_actual = datetime.date.today()
        return cls(fecha_actual.day, fecha_actual.month, fecha_actual.year)

# Diferentes formas de crear objetos Fecha
fecha1 = Fecha(15, 3, 2023)  # Constructor normal
fecha2 = Fecha.desde_texto("25-12-2023")  # Constructor alternativo
fecha3 = Fecha.hoy()  # Constructor alternativo que usa la fecha actual

print(f"{fecha1.dia}/{fecha1.mes}/{fecha1.año}")  # Imprime: 15/3/2023
print(f"{fecha2.dia}/{fecha2.mes}/{fecha2.año}")  # Imprime: 25/12/2023