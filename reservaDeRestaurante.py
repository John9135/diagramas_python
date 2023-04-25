buscaRestaurante = "si"

while(buscaRestaurante == "si"):
    print ("¿Cuantas estrellas tiene el restaurante?")
    estrellas = input()
    estrellas = int(estrellas)

    if(estrellas >= 3):
        print ("¿Quieres ingresar a la pagina?")
        ingresaALaPagina = input().lower()

        if (ingresaALaPagina == "si"):
            print ("¿Cuanto cuesta la reserva?")
            precioDeReserva = input()
            precioDeReserva = int(precioDeReserva)

            if (precioDeReserva <= 2000000):
                print ("¿En que ciudad se encuentra el restaurante?")
                ciudad = input()

                if (ciudad == "Pereira"):
                    print ("¿Quiere confirmar la reserva?")
                    confirmarReserva = input().lower()

                    if (confirmarReserva == "si"):
                        print ("Reserva confirmada")
                        break;
    
    print ("¿Quiere seguir buscado restaurantes?")
    buscaRestaurante = input().lower()