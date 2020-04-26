import time
import os
import random

'''Hackable Area'''
'''END'''

elements = ['💰', '🛍 ', '💎', '🎁', '🧧', '⚜️ ', '⛱ ', '💵']

def clear():
    os.system('clear')

def displayComponents(cash):
    print('*** CASH: ', cash, ' ***')

def main():
    cash = 1000
    eachSlotPrice = 500
    clear()
    displayComponents(cash)
    print('----------------------')
    print('|      |      |      |')
    print('----------------------')
    input("\n\n\n\n\n\n\n\n --- 按Enter键开始 ---")
    while True:
        clear()
        lucky = random.randint(20, 200)
        doublePrice = [200, 100, 1000, lucky*10, lucky, 2000, 20, 100]
        triplePrice = [500, 300, 5000, lucky*30, lucky*3, 10000, 100, 500]
        displayComponents(cash)
        cash -= eachSlotPrice
        print('- ', eachSlotPrice)
        time.sleep(0.5)
        clear()
        displayComponents(cash)
        a = random.randint(0, 7)
        b = random.randint(0, 7)
        c = random.randint(0, 7)
        print('----------------------')
        print('| ', elements[a], ' | ', elements[b], ' | ', elements[c], ' |')
        print('----------------------')
        time.sleep(0.2)
        clear()
        displayComponents(cash)
        a = random.randint(0, 7)
        b = random.randint(0, 7)
        c = random.randint(0, 7)
        print('----------------------')
        print('| ', elements[a], ' | ', elements[b], ' | ', elements[c], ' |')
        print('----------------------')
        time.sleep(0.2)
        clear()
        displayComponents(cash)
        a = random.randint(0, 7)
        b = random.randint(0, 7)
        c = random.randint(0, 7)
        print('----------------------')
        print('| ', elements[a], ' | ', elements[b], ' | ', elements[c], ' |')
        print('----------------------')
        time.sleep(0.2)
        clear()
        displayComponents(cash)
        a = random.randint(0, 7)
        b = random.randint(0, 7)
        c = random.randint(0, 7)
        print('----------------------')
        print('| ', elements[a], ' | ', elements[b], ' | ', elements[c], ' |')
        print('----------------------')
        time.sleep(0.2)
        clear()
        displayComponents(cash)
        a = random.randint(0, 7)
        b = random.randint(0, 7)
        c = random.randint(0, 7)
        print('----------------------')
        print('| ', elements[a], ' | ', elements[b], ' | ', elements[c], ' |')
        print('----------------------')
        time.sleep(0.2)
        clear()
        a = random.randint(0, 7)
        b = random.randint(0, 7)
        c = random.randint(0, 7)
        displayComponents(cash)
        print('----------------------')
        print('| ', elements[a], ' | ', elements[b], ' | ', elements[c], ' |')
        print('----------------------')
        if a == b and b == c:
            cash += triplePrice[a]
        elif a == b or b == c:
            cash += doublePrice[b]
        elif a == c or a == b:
            cash += doublePrice[a]
        else:
            print('Come on!, Next time you will win')
        clear()
        displayComponents(cash)
        print('----------------------')
        print('| ', elements[a], ' | ', elements[b], ' | ', elements[c], ' |')
        print('----------------------')
        if a == b and b == c:
            print('Triple! You win ', triplePrice[a], ' coins!')
        elif a == b or b == c:
            print('Double! You win ', doublePrice[b], ' coins!')
        elif a == c or a == b:
            print('Double! You win ', doublePrice[a], ' coins!')
        else:
            print('Come on! Next time you will win')
        cont = input("\n\n\n\n\n\n\n\n --- 按Enter键开始, Q 键结束 ---")
        if cont == 'q':
            break
        if cash < eachSlotPrice:
            break
    print('See you next time')

if __name__ == '__main__':
    main()
