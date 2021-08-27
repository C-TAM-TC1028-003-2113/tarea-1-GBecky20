def main():
    # escribe tu código abajo de esta línea
    mensajes = int(input("Dame el numero de mensajes: "))
    megas = float(input("Dame el numero de megas: "))
    minutos = int(input("Dame el numero de minutos: "))

    costomen = mensajes*0.80
    costomeg = megas*0.80
    costomin = minutos*0.80

    costototal = costomeg + costomeg + costomin

    print("El costo mensual es:", costototal)
if __name__ == '__main__':
    main()
