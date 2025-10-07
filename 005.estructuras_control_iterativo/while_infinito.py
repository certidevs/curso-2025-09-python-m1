
"""
Bucle infinito

Ideal para aplicaciones de terminal-consola (cli)

Salimos del bucle cuando el usuario escriba salir

Es indeterminado porque a priori no sabemos cuándo el usuario va a querer salir
"""

while True:
    print("""
            Welcome.
            Elige una opción:
            1 - Mostrar productos
            2 - Mostrar un producto
            salir - salir del programa
            """)

    opcion = input("Introduce una opción: ")
    print(f"Has elegido la opción: {opcion}")
    
    if opcion == "salir":
        print("Hasta la proxima")
        break
    

print("Fuera del bucle")