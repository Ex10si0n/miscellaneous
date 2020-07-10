import time
import time
import time
import time
import time
import time
import time
import os
import random
import os
import random
import os
import random
import os
import random
import os
import random
import os
import random
import os
import random

class Card:
    def __init__(self, color, value, real_value):
        self.color = color
        self.value = value
        self.real_value = real_value

    def __str__(self):
        return "{0}{1}".format(self.color, self.value)

class Cards:
    def __init__(self):
        self.all_cards = []

    def generate(self):
        values = list("A") + list(range(2, 11)) + list("JQK")
        for color in "♥♠♦♣":
            cnt = 1
            for i in values:
                c = Card(color, i, cnt)
                self.all_cards.append(c)
                cnt += 1

    def shuffle(self):
        random.shuffle(self.all_cards)

def get_value(cards):
    sum = 0
    for c in cards:
        sum += c.real_value
    return sum

def main():
    os.system("clear")
    is_end = False
    card = Cards()
    cash = 100000
    chip = 0
    while True:
        print("Cash: ", cash, "\nChips: ", chip)
        inst = input("Type [b] to buy chips\nType [s] to sell chip to cash\nType [Enter] to start 21 points game\nType [q] to quit\n: ")
        if inst == 'b' or inst == 'B':
            inst = int(input("Buy how many chips [1 cash for 1 chip]: "))
            if cash - inst >= 0:
                cash -= inst
                chip += inst
            else:
                print("Buy Failed, Not enough cash")
                input()

        if inst == 's' or inst == 'S':
            inst = int(input("Sell how many chips [1 chip for 1 cash]: "))
            if chip - inst >= 0:
                cash += inst
                chip -= inst
            else:
                print("Sell Failed, Not enough chip")
                input()

        if inst == '':
            print("Start Game!")
            break

        if inst == 'q' or inst == 'Q':
            is_end = True
            break

        if inst == 'yzb是大帅比':
            cash += 1000000

        os.system("clear")


    while True:
        if is_end:
            print("Cash: ", cash, "\nChips: ", chip)
            input()
            break
        card.generate()
        card.shuffle()
        banker_hand_cards = []
        player_hand_cards = []

        while True:
            base = int(input('Base chips gamble: '))
            if chip - base < 0:
                print('Chips not enough')
            else:
                chip -= base
                break

        i = 0
        while i < len(card.all_cards):
            if card.all_cards[i].real_value + get_value(banker_hand_cards) > 21:
                break
            banker_hand_cards.append(card.all_cards[i])
            i += 1

        banker_score = get_value(banker_hand_cards)

        while i < len(card.all_cards):
            os.system("clear")
            print("Cash: ", cash, "\nChips: ", chip)
            print(str(banker_hand_cards[0]), "[ ] " * (len(banker_hand_cards)-1))
            print("Your Points:", get_value(player_hand_cards))
            print("Your Cards:")
            for c in player_hand_cards:
                print(c, end=' ')
            inst = input("\nDo you want to get a card? [Y/n]: ")
            if inst == 'y' or inst == 'Y':
                player_hand_cards.append(card.all_cards[i])
                if get_value(player_hand_cards) > 21:
                    print(card.all_cards[i])
                    print("Exploded!")
                    break
                i += 1

            if inst == 'n' or inst == 'N':
                break
        print("Banker Points: ", banker_score)
        print("Banker Cards: ")
        for c in banker_hand_cards:
            print(str(c), end=' ')

        if get_value(player_hand_cards) > get_value(banker_hand_cards) and get_value(player_hand_cards) <= 21:
            chip += 2 * base
            print("You Win")
        elif get_value(player_hand_cards) == get_value(banker_hand_cards):
            chip += base
            print("Draw")
        else:
            print("You Lose")
        print('\n')

        input("Press [Enter] to call the menu")
        os.system("clear")

        while True:
            print("Cash: ", cash, "\nChips: ", chip)
            inst = input("Type [b] to buy chips\nType [s] to sell chip to cash\nType [Enter] to start 21 points game\nType [q] to quit\n: ")

            if inst == 'b' or inst == 'B':
                inst = int(input("Buy how many chips [1 cash for 1 chip]: "))
                if cash - inst >= 0:
                    cash -= inst
                    chip += inst
                else:
                    print("Buy Failed, Not enough cash")
                    input()

            if inst == 's' or inst == 'S':
                inst = int(input("Sell how many chips [1 chip for 1 cash]: "))
                if chip - inst >= 0:
                    cash += inst
                    chip -= inst
                else:
                    print("Sell Failed, Not enough chip")
                    input()

            if inst == '':
                break

            if inst == 'q' or inst == 'Q':
                is_end = True
                break
            os.system("clear")

        if is_end:
            break

if __name__ == "__main__":
    main()
