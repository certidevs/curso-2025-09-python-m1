import datetime


# date para fechas sin tiempo:
fecha_actual = datetime.date.today()
print(f'fecha_actual {fecha_actual}')

# datetime fecha con tiempo:
ahora = datetime.datetime.now()
print(f'ahora {ahora}')

# time solo tiempo:
tiempo = datetime.time(10, 30)
print(f'tiempo {tiempo}')