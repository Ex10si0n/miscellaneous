import random

class Characters:
    def __init__(self, player):
        self.needle = 0
        self.isDeath = False
        self.isBanned = False
        self.playerName = player
        self.asked = "Civil"
        self.identity = "Civil"

    def die(self):
        self.isDeath = True

    def getInject(self):
        self.needle += 1
        if self.needle >= 2:
            self.die()

    def getKilled(self):
        if self.needle == 0:
            self.die()
        else:
            self.needle = 0

    def getAsked(self):
        return self.asked

    def getBanned(self):
        self.isBanned = True

    def unBanned(self):
        self.isBanned = False

class Killer(Characters):
    def __init__(self, name):
        Characters.__init__(self, name)
        self.asked = "Killer"
        self.title = 'Killer'
        self.identity = "Killer"

class Spy(Characters):
    def __init__(self, name):
        Characters.__init__(self, name)
        self.asked = "Civil"
        self.title = 'Spy'
        self.identity = 'Killer'

class Doctor(Characters):
    def __init__(self, name):
        Characters.__init__(self, name)
        self.title = 'Doctor'

class Police(Characters):
    def __init__(self, name):
        Characters.__init__(self, name)
        self.title = 'Police'

class Baner(Characters):
    def __init__(self, name):
        Characters.__init__(self, name)
        self.asked = 'Killer'
        self.title = 'Banner'

class Player:
    def __init__(self, name, id):
        self.actAs = None
        self.name = name
        self.id = id
        if id == 0:
            self.actAs = Baner(name)
        elif id == 1:
            self.actAs = Doctor(name)
        elif id == 2:
            self.actAs = Police(name)
        elif id == 3:
            self.actAs = Killer(name)
        elif id == 4:
            self.actAs = Spy(name)

    def __str__(self):
        return '[%d] %s (%s)' % (self.id, self.name, self.actAs.title)


if __name__ == '__main__':
    player_name = ['Steve', 'Alston', 'King', 'Jane', 'Stephen']
    random.shuffle(player_name)
    player_list = []
    for i in range(len(player_name)): # Player List must length 5
        player_list.append(Player(player_name[i], i))
    for i in player_list:
        i.actAs.getInject()
        i.actAs.getKilled()
        i.actAs.getInject()
        print(i, i.actAs.isDeath, i.actAs.needle)
