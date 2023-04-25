print("¿Buscar centro de adopción?")
encontroCentroDeAdapcion = input().lower()

while encontroCentroDeAdapcion == "si":
    print("¿Quieres entrar al centro de adopción?")
    entrarAlCentroDeAdopcion = input().lower()

    if entrarAlCentroDeAdopcion == "si":
        print("¿Tienen gatos?")
        tieneGatos = input().lower()

        if tieneGatos == "si":
            print("¿Cuantos meses de edad tiene el gato?")
            edad = input()
            edad = int(edad)

            if edad >= 3 and edad <= 5:
                print("¿Cúal es el color del gato?")
                color = input().lower()

                if color == "amarillo":
                    print("Adopta el gato")
                    break

    print("¿Buscar centro de adopción?")
    encontroCentroDeAdapcion = input().lower()
