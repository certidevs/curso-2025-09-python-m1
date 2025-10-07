
nombres = []

def guardar_nombre(nombre):
    nombres.append(nombre)
    print(f"Insertado {nombre} en la lista, ahora hay {len(nombres)} nombres.")
    

guardar_nombre("Patricia")
guardar_nombre("Jorge")
guardar_nombre("Pablo")

# ----- 

matriculas = ["1111AAA", "2222BBB", "3333CCC"]

def guardar_matriculas(matriculas_nuevas):
    matriculas.extend(matriculas_nuevas) # se van a fusionar las listas
    
guardar_matriculas(["4444DDD", "5555EEE"])
guardar_matriculas(["6666FFF", "7777GGG", "8888HHH"])

print(matriculas)
