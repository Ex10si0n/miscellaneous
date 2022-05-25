import random

class Mahjong:
    def __init__(self, suit, num):
        '''
        suit = [dot, character, bamboo, honor]  饼 万 条 役

        num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

            役牌编号:
                1: 东
                2: 南
                3: 西
                4: 北
                5: 中 
                6: 发 
                7: 白
        '''
        self.suit = suit 
        self.num = num

    def __str__(self):
        if self.suit == 'H':
            _map = {1: 'EA', 2: 'SO', 3: 'WE', 4: 'NO', 5: 'RE', 6: 'GR', 7: 'WD'}
            return '[%s]' % _map[self.num]
        return '[%s%d]' % (self.suit, self.num)

    def __le__(self, other):
        return self.suit <= other.suit and self.num <= other.num

    def __ge__(self, other):
        return self.suit >= other.suit and self.num >= other.num


class Game:

    def __init__(self):
        '''
        game class:

        '''
        self.ground = []  # mahjong on the ground
        self.head = 0     # tile head pointer
        self.mahjong = [] # all tiles
        self.p1 = []      # banker player
        self.p2 = []
        self.p3 = []
        self.p4 = []

        for suit in ['D', 'C', 'B']:
            for num in range(1, 9+1):
                for i in range(4):
                    m = Mahjong(suit, num)
                    self.mahjong.append(m)

        for num in range(1, 7+1):
            for i in range(4):
                m = Mahjong('H', num)
                self.mahjong.append(m)

    def __str__(self):
        ret = ''
        for tile in self.mahjong:
            ret += str(tile) + ' '
        return ret
    
    def print(self):
        for elm in self.p1:
            print(elm, end=' ')
        print()
        for elm in self.p2:
            print(elm, end=' ')
        print()
        for elm in self.p3:
            print(elm, end=' ')
        print()
        for elm in self.p4:
            print(elm, end=' ')
        print()


    def shuffle(self):
        random.shuffle(self.mahjong)

    def sorted(self, _list):
        return sorted(_list)
    '''
        for i in range(len(_list)):
            for j in range(len(_list)-i-1):
                if _list[j] > _list[j+1]:
                    t = _list[j]
                    _list[j] = _list[j+1]
                    _list[j+1] = t
        return _list
    '''


    def draw(self):
        pass

    def discard(self):
        pass

    def start(self):
        self.shuffle()
        for i in range(self.head, self.head+14):
            self.p1.append(self.mahjong[i])
        self.head += 14
        for i in range(self.head, self.head+13):
            self.p2.append(self.mahjong[i])
        self.head += 13
        for i in range(self.head, self.head+13):
            self.p3.append(self.mahjong[i])
        self.head += 13
        for i in range(self.head, self.head+13):
            self.p4.append(self.mahjong[i])
        self.head += 13
        self.p1 = self.sorted(self.p1)
        self.p2 = self.sorted(self.p2)
        self.p3 = self.sorted(self.p3)
        self.p4 = self.sorted(self.p4)
        self.print()




if __name__ == '__main__':
    game = Game()
    game.start()

