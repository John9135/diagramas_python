noCompraLaBoleta = "No compra la boleta"

print("¿El concierto es en Pereira?")
conciertoEnPereira = input().lower()

print(conciertoEnPereira)

if (conciertoEnPereira == "si"):
    print("¿El concierto es en un viernes?")
    conciertoEnViernes = input().lower()

    if (conciertoEnViernes == "si"):
        print("¿Cual es el precio de la boleta?")
        valor = input()
        valorDelConcierto = int(valor)

        if (valorDelConcierto <= 1000000):
            print("Compra la boleta")

        else:
            print(noCompraLaBoleta)

    else:
        print(noCompraLaBoleta)

else:
    print(noCompraLaBoleta)
