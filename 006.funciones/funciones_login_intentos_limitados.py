
# LOGIN CON NÚMERO MÁXIMO DE INTENTOS

# Aquí podemos crear una aplicación de consola
# que pida al usuario email y password,
# si falla tres veces detiene el programa y no deja continuar
# si acierta le deja usar la aplicación
# KeePass para generar contraseñas seguras
import sys

VALID_EMAIL = "admin@empresa.com"
VALID_PASSWORD = "admin"
MAX_INTENTOS = 3

def login_1():
    # bucle for para máximo 3 intentos fallidos de verificar email y contraseña
    # leer por input el email y password       
    for intento in range(1, MAX_INTENTOS + 1): # 1, 2, 3
        email = input("Introduce email: ").strip()
        password = input("Introduce password: ").strip()
        
        if email == VALID_EMAIL and password == VALID_PASSWORD:
            return True
        
        intentos_restantes = MAX_INTENTOS - intento # 3 - 1 = 2, 3 - 2 = 1, 3 - 3 = 0
        if intentos_restantes > 0:
            print(f"Credenciales incorrectas, te quedan {intentos_restantes} intentos")
        else:
            print("Has agotado todos los intentos, adiós.")
            sys.exit(1) # para salir del programa
    
# Versión alternativa, más simplificado al no tener que restar intentos
def login_2():
    for intento in range(1,4):
        user_email = input("Introduce tu mail: ")
        user_pass = input("Introduce tu contraseña: ")

        if user_email == VALID_EMAIL and user_pass == VALID_PASSWORD:
            return True
        else:
            print(f"Datos incorrectos llevas {intento} /3 ")

    print("Has excedido los intentos, saliedo...")
    sys.exit(1) # para salir del     


if login_1():
    while True:
        print("Bienvenido/a a la aplicación. Opciones disponibles: 1 - ver productos, 2 - crear producto, 3 - terminar el programa.")
        opcion = input("Introduce una opción: ")
        print(f"Has elegido la opcion {opcion}")
        
        if opcion == "1":
            print("1")
        elif opcion == "2":
            print("2")
        elif opcion == "3" or opcion == "salir":
            print("saliendo...")
            break
        else:
            print("opción incorrecta.")