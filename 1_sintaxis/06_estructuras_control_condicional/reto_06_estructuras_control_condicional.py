# Solicitar la edad al usuario
edad_input = input("Introduce tu edad: ")

# Convertir la entrada a entero
edad = int(edad_input)

# forma concisa
# edad = int(input("Introduce tu edad: "))

# Evaluar la edad usando if-elif-else
if edad < 13:
    mensaje = "Eres un niño."
# elif edad >= 13 and edad <= 17:
elif edad <= 17:
    mensaje = "Eres un adolescente."
# elif edad >= 18 and edad <= 64:
elif edad <= 64:
    mensaje = "Eres un adulto."
else:
    mensaje = "Eres un adulto mayor."

# Mostrar el mensaje correspondiente
print(mensaje)