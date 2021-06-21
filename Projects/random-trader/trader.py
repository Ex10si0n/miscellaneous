import random
import os

# set MARKET > 0.5 means bull market, < 0.5 means bear market
MARKET = 0.55 
INIT_ASSETS = 10000
INIT_STOCK_PRICE = 30


HELP_TEXT ='''
b <numbers>      Buy <numbers> shares
s <numbers>      Sell <numbers> shares
q                Quit and summary
'''

def main():
    price = INIT_STOCK_PRICE
    assets = INIT_ASSETS
    amount = 0

    while True:
        os.system("clear")
        random_bias = 1 - MARKET
        var = random.random() - random_bias
        var /= 5
        if var < 0:
            rate = str(var * 100)[:5] + "%"
        else:
            rate = str(var * 100)[:4] + "%"
        var += 1
        price *= var
        price = int(price * 100) / 100

        earns = int((amount * price + assets - INIT_ASSETS) * 100) / 100
        print("price:", price, "   rate:", rate)
        print("assets:", assets)
        print("amount:", amount)
        print("earns:", earns)
        operation = input(">>>")
        if operation.split(' ')[0] == 'b':
            bAmount = int(operation.split(' ')[1])
            if bAmount * price > assets:
                print("Buy Failed")
                continue
            else:
                assets -= bAmount * price
                amount += bAmount
                print("Buy: ", bAmount)

        if operation.split(' ')[0] == 's':
            sAmount = int(operation.split(' ')[1])
            if sAmount > amount:
                print("Sell Failed")
                continue
            else:
                assets += sAmount * price
                amount -= sAmount
                print("Sell: ", bAmount)

        if operation == 'help':
            print(HELP_TEXT)
            input()
        elif operation == 'q':
            print("SUMMARY")
            print("assets:", assets)
            print("earns:", earns)
            break




if __name__ == '__main__':
    main()
