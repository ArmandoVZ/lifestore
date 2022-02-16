from re import A
import time 

accesoUsuario = False
intentos = 0

#usuarios administradores
usuariosAdmin = [
    [1,"avegaz","passw0rd"]]
#usuarios no administradores
usuariosnoAdmin = [
    [1,"jvegaz","pass"]]


# Bienvenida!
mensaje_bienvenida = 'Bienvenido \n Ingresa tus credenciales de acceso \n'
print(mensaje_bienvenida)

# Recibo constantemente sus intentos
while not accesoUsuario:
    # Primero ingresa Credenciales
    usuario = input('Usuario: ')
    password = input('Contraseña: ')
    intentos += 1
    # Reviso si el par coincide
    if usuario == 'avegaz' and password == 'passw0rd':
        accesoUsuario = True
        print('Bienvenido de vuelta')
        time.sleep(2)
    else:
        # print('Tienes', 3 - intentos, 'intentos restantes')
        print(f'Tienes {3 - intentos} intentos restantes')
        if usuario == 'avegaz':
            print('La Contraseña ingresada es incorrecta')
        else:
            print(f'El usuario: "{usuario}" no esta registrado')
            
    if intentos == 3:
        exit()

print('Acceso al sistema exitoso')
time.sleep(1)