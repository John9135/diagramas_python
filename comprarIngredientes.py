print ("Compra ingredientes")
listaDeCompra = []
listaDeFaltantes = []

print("Ingrese la cantidad de ingredientes")
cantidadIngredientes = input()
cantidadIngredientes = int(cantidadIngredientes)

for i in range(0, cantidadIngredientes):
    print("Ingrese un producto")
    ingredientes = input()

    if ingredientes == "":
        print("No puede queda vacio escriba por favo el ingrediente")
        ingredientes = input()

    listaDeCompra.append(ingredientes)

while len(listaDeCompra) > 0:

    for i in range(0, len(listaDeCompra)):
        print("Encontraste el " + listaDeCompra[i])
        productoEncontrado = input().lower()

        if productoEncontrado == "no":
            listaDeFaltantes.append(listaDeCompra[i])

    listaDeCompra.clear()

    if len(listaDeFaltantes) > 0:
        print("¿Desea ir a otra tienda?")
        irAOtraTienda = input().lower()

        if irAOtraTienda == "si":
            listaDeCompra = listaDeFaltantes.copy()
        else:
            break

    listaDeFaltantes.clear()
