from utilidades import comprobar_numero


def comprobar_longitud(contrasena):
    return len(contrasena) >= 8


def comprobar_mayuscula(contrasena):
    for caracter in contrasena:
        if caracter.isupper():
            return True
    return False


contrasena = "Hola1234"
print(contrasena)
print("Tiene mayúscula:", comprobar_mayuscula(contrasena))
print("Longitud correcta:", comprobar_longitud(contrasena))
print("Tiene número:", comprobar_numero(contrasena))
