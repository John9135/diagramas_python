enciendaLaTv = "tome el control y encienda el televisor"


print("¿El televisor esta conectado?")
tvConectada = input().lower()

if (tvConectada == 'si'):
    print(enciendaLaTv)

elif (tvConectada == "no"):
    print("Conencte el televisor " + enciendaLaTv)

else:
    print("La respuesta que dio no es aceptable")
