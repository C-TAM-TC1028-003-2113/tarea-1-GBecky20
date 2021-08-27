def main():
    # escribe tu código abajo de esta línea
    nuevos = int(input("Dame la cantidad de juegos nuevos: "))
    usados = int(input("Dame la cantidad de juegos usados: "))

    costonue = 1000*nuevos
    costousa = 350 * usados

    costototal = costonue + costousa
    print("El total de la compra es:", costototal)

if __name__ == '__main__':
    main()
