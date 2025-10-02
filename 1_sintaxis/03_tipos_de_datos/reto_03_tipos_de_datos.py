print("=== EJERCICIO: TIPOS DE DATOS BÁSICOS ===\n")

# 1. Crear una variable 'entero' con el valor numérico 42
entero = 42

# 2. Crear una variable 'decimal' con el valor 3.14159
decimal = 3.14159

# 3. Crear una variable 'texto' con el valor "Python"
texto = "Python"

# 4. Crear una variable 'booleano' con el valor True
booleano = True

print("=== VARIABLES ORIGINALES ===")
# Aquí se imprimirán las variables originales (no borres estas líneas)
print(f"entero: {entero} - Tipo: {type(entero)}")
print(f"decimal: {decimal} - Tipo: {type(decimal)}")
print(f"texto: {texto} - Tipo: {type(texto)}")
print(f"booleano: {booleano} - Tipo: {type(booleano)}")

print("\n=== CONVERSIONES ===")

# 5. Convertir el 'entero' a texto y guardarlo en 'entero_texto'
entero_texto = str(entero)

# 6. Convertir el 'decimal' a entero y guardarlo en 'decimal_entero'
decimal_entero = int(decimal)

# 7. Convertir el 'texto' a una lista de caracteres y guardarlo en 'texto_lista'
texto_lista = list(texto)

# 8. Convertir el 'booleano' a entero y guardarlo en 'booleano_entero'
booleano_entero = int(booleano)

print("=== VARIABLES CONVERTIDAS ===")
# Aquí se imprimirán las variables convertidas (no borres estas líneas)
print(f"entero_texto: {entero_texto} - Tipo: {type(entero_texto)}")
print(f"decimal_entero: {decimal_entero} - Tipo: {type(decimal_entero)}")
print(f"texto_lista: {texto_lista} - Tipo: {type(texto_lista)}")
print(f"booleano_entero: {booleano_entero} - Tipo: {type(booleano_entero)}")

print("\n=== EJERCICIO COMPLETADO ===")