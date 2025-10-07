
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

Parámetros:
* que no tenga parámetros: mostrar_productos()
* que tenga un parámetro: es_mayor_edad(edad)
* que tenga dos parámetros: apto_para_beca(edad, nivel_ingresos)
* que tengan n parámetros: procesar_pedido(id, fecha, precio_total, ...)
* parámetros con valor por defecto

Retorno:
* puede no devolver nada
* puede devolver algo: return

"""
def imprimir_menu():
    print("Bienvenido/a a la app, estas son las opciones...")
    
# crear la función
def is_adult():
    edad = int(input("Introduce tu edad: "))
    if edad >= 18:
        return True
    else:
        return False

# invocar la función
print(is_adult())
print(is_adult())
