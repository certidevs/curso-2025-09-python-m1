"""

Operadores lógicos

and
or
not

Evalúan condiciones por ejemplo eres mayor de edad o tienes tutor

"""

ingresos_suficientes = True
buen_historial_crediticio = True

aprobacion_prestamo = ingresos_suficientes and buen_historial_crediticio
print(f"¿Préstamo aprobado? {aprobacion_prestamo}")

ingresos_suficientes = False
buen_historial_crediticio = True

aprobacion_prestamo = ingresos_suficientes and buen_historial_crediticio
print(f"¿Préstamo aprobado? {aprobacion_prestamo}")

es_socio = False
tiene_invitacion = True

puede_entrar = es_socio or tiene_invitacion
print(f"¿Puede entrar al evento? {puede_entrar}")

disponible = False
no_disponible = not disponible
print(f"¿El producto no está disponible?")