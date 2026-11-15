def comprobar_longitud(contrasena):
    return len(contrasena) >= 8


contrasena = "Hola1234"
print(contrasena)
print("Longitud correcta:", comprobar_longitud(contrasena))
