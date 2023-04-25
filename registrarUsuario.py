print("ingresar pagina")
ingresoALaPagina = input().lower()

if (ingresoALaPagina == "si"):
    print("Número de documento: ")
    numeroDocumento = input()
    print("Ingrese su nombre: ")
    nombre = input()
    print("Ingrese sus apellidos: ")
    apellido = input()

    print("Recordar usuario")
    recordarUsuario = input().lower()

    if (recordarUsuario == "si"):
        usuario = nombre

    print("Escoger la hora y el día para la reserva")
    horaYDia = input()

    print("confimar reserva")
    confirmaReserva = input().lower()

    if (confirmaReserva == "si"):
        print("Reserva confimado")

    else:
        print("No se hace la reserva")
else:
    print("No se hace la reserva")
