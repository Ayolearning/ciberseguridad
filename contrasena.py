from utilidades import comprobar_numero


def comprobar_longitud(contrasena):
    return len(contrasena) >= 8


contrasena = "Hola1234"
print(contrasena)
print("Longitud correcta:", comprobar_longitud(contrasena))
print("Tiene número:", comprobar_numero(contrasena))
