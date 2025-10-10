
def login(email, password):
    email_valido = "admin@gmail.com"
    password_valida = "1234"
    
    # verificar si email y password coinciden
    if email == email_valido and password == password_valida:
        return True
    else:
        return False


print(login("admin@gmail.com", "abcd1234")) # falso

print(login("admin@gmail.com", "1234")) # verdadero

print(login("usuario@gmail.com", "1234")) # falso

# if login("admin@gmail.com", "1234"):
    # find_lessons_by_user()