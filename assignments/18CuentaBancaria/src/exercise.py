def main():
    # escribe tu código abajo de esta línea
    anterior = float(input("Dame el saldo del mes anterior: "))
    ingresos = float(input("Dame los ingresos: "))
    egresos = float(input("Dame los egresos: "))
    cheques = int(input("Dame el numero de cheques: "))

    total = (anterior + ingresos - egresos - (cheques*13)) *0.925

    print("El saldo final de la cuenta es:", total)

if __name__ == '__main__':
    main()
