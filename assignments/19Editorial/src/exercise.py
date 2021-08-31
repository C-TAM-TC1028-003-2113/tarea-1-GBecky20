def main():
    # escribe tu código abajo de esta línea
    import math
    palabras = int(input("Dame el numero de palabras: "))
    cuartilla = int(math.ceil(palabras / 475))

    precio = (cuartilla * 60)
    preciototal = precio - (precio * 0.10)

    print("El costo de la publicacion es:", preciototal)

if __name__ == '__main__':
    main()
