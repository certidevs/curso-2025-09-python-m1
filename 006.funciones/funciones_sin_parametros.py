
"""

Las funciones son una forma de crear bloques de código reutilizables
varias veces en un programa.

Se usa la palabra "def"

pass indica que no hay código todavía, se suele escribir cuando estamos
diseñando al principio qué código habrá sin crearlo del todo todavía.

Sin pass me obliga a escribir código ya que no puede estar vacía.

Intentar que el nombre sea descriptivo y revele lo que hace la función


Convenciones de nomenclaturas para funciones:

is_x() si  devuelve boolean
calculate_x() si  procesa o calcula
find()
insert()
save()
remove()
get()
set()

usar nombres descriptivos como verbos que definan la accion

https://github.com/alansastre/java-clean-code?tab=readme-ov-file#3-funciones
"""

def is_adult():
    edad = int(input("Introduce tu edad: "))
    if edad >= 18:
        return True
    else:
        return False


print(is_adult())
print(is_adult())
