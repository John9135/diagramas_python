print("Bienvenido a la isla, tú mision sera encontrar el tesoro")

print("¿Derecha o izquierda?")
derechOIzquierda = input().lower()

if derechOIzquierda == "izquierda":
    print("¿Nadar o esperar?")
    nadarOEsperar = input().lower()

    if nadarOEsperar == "nadar":
        print("¿Subir o caminar?")
        subirOcaminar = input().lower()

        if subirOcaminar == "caminar":
            print("¿Entrar o seguir?")
            entrarOSeguir = input().lower()

            if entrarOSeguir == "entrar":
                print("¿Cual puerta? la roja, amarilla, verde o azul")
                puerta = input().lower()

                if puerta == "azul":
                    print("Has ganado")

                elif puerta == "roja":
                    print("Devorado por bestias game over")

                elif puerta == "amarilla":
                    print("Game over")

                elif puerta == "verde":
                    print("eres quemado game over")
            elif entrarOSeguir == "seguir":
                print("Caes a un rio game over")

        elif subirOcaminar == "subir":
            print("Picado por abejas game over")

    elif nadarOEsperar == "esperar":
        print("Caiste en un agujero game over")

elif derechOIzquierda == "derecha":
    print("Caiste en un agujero game over")
