

try:
    resultado = 10 /0
    [].pop()
except ZeroDivisionError:
    print("error al dividir")
except IndexError:
    print("Error al trabajar con la lista")

print("fin")

try:
    resultado = 10 /0
    [].pop()
except Exception: # esto captura todo
    print("error") 
    
    
    