# clase Cuenta bancaria
class Cuenta:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        
        # validación para que el saldo inicial sea como mínimo 0 (que no sea negativo)
        if saldo_inicial < 0:
            raise ValueError("El saldo inicial no puede ser negativo")
        
        self.saldo = saldo_inicial

# crear objetos cuenta
cuenta_ana = Cuenta("Ana", 1000)

# esto lanzará un ValueError
try:
    cuenta_problematica = Cuenta("Juan", -500)
except ValueError as e:
    print(f"ERROR: {e}")