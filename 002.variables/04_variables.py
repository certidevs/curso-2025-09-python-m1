print("\n")
print("=" * 20)
print("VARIABLES")
print("=" * 20)
print("\n")

edad = 25
nombre = "Ana"
altura = 1.74
es_estudiante = True

print("\n")
print("=" * 20)
print("ASIGNACIÓN MÚLTIPLE")
print("=" * 20)
print("\n")

x = y = z = 0
print(f"Variables: x={x}, y={y}, z={z}")

nombre, edad, altura = "Carlos", 30, 1.75
print(f"Nombre: {nombre}, edad: {edad}, altura: {altura}")

a = 5
b = 10
print(f"a={a}, b={b}")

a, b = b, a
print(f"a={a}, b={b}")

print("\n")
print("=" * 20)
print("ASIGNACIÓN CON OPERADORES")
print("=" * 20)
print("\n")

contador = 0
print(f"Contador: {contador}")

# contador = contador + 1
contador += 1
print(f"Contador: {contador}")

contador -= 2
print(f"Contador: {contador}")

precio = 100
precio *= 1.21
print(f"Precio: {precio}")

precio /= 2
print(f"Precio: {precio}")

edad = 10
Edad = 20
EDAD_MINIMA = 30
eDaD = 40

# cammelCase (primera en minúscula)
# PascalCase (siempre en mayúscula)

# clases
class AnimalDomestico:
    pass

print("\n")
print("=" * 20)
print("ÁMBITO LOCAL Y GLOBAL")
print("=" * 20)
print("\n")

mensaje = "Hola, mundo"

print(mensaje)

def saludar():
    nombre_funcion = "Ana"
    print(f"Mensaje: {mensaje}, nombre: {nombre_funcion}")
    
saludar() # Invocar a la función (ejecutarla)

# daría error porque nombre_funcion es una variable LOCAL
# print(nombre_funcion)

contador_global = 100  # Variable global
print(f"Contador global: {contador_global}")  # Imprime: "Contador global: 100"

def incrementar():
    global contador_global # Indicamos con la palabra clave "global"
    contador = 0  # Variable local, diferente a la global
    print(f"Contador local: {contador}")
    contador += 1
    print(f"Contador local + 1: {contador}")
    contador_global += 1

incrementar()  # Imprime: "Contador local: 1"

print(f"Contador global: {contador_global}")  # Imprime: "Contador global: 100"

def funcion_principal():
    variable = 1
    def funcion_secundaria():
        print(f"Variable: {variable}")
    funcion_secundaria()
        
funcion_principal()

if True:
    nueva_variable = "Creada en un if"

print(nueva_variable)

for i in range(3):
    ultimo_valor = i

print(ultimo_valor)


print("\n")
print("=" * 20)
print("CONSTANTES")
print("=" * 20)
print("\n")

PI = 3.141592659
VELOCIDAD_LUZ = 299792458
DIAS_SEMANA = 7
USER_DEFAULT = "Usuario"

# Constante gravitacional (m³ kg⁻¹ s⁻²)
G = 6.67430e-11