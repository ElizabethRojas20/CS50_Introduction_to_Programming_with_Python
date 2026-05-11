#necesitamos preguntar un input
#verificar que ese input sea 25, 10 o 5, sino return 50
#vi es 25, 10 o 5, imprimir la diferencia
#volver a insertar moneda hasta que sea 0
coins_accepted = [25, 10, 5]

def main():
    due = 50
    get_coin(due)

def get_coin(due):
    while due > 0:
        coin = int(input("Insert Coin: "))

        if coin in coins_accepted:
            due -= coin
            if due == 0:
                print("Change Owed:",due)
                break

            elif due < 0:
                due *= (-1)
                print("Change Owed:",due)
                break

            else:
                print("Amount Due:",due)

        else:
            print("Amount Due:",due)

main()