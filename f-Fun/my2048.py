import os
import random

class Table:

    def __init__(self):
        self.row = 4
        self.col = 4
        self.content = [\
                        [0, 0, 0, 0],\
                        [0, 0, 0, 0],\
                        [0, 0, 0, 0],\
                        [0, 0, 0, 0]\
                       ]

    def printTable(self):
        for i in range(4):
            for j in range(4):
                print("%-4d " % self.content[i][j], end='')
            print("\n")

class gameRun:

    def randomGen(self, gameTable):
        zeroPos = []
        nowTable = gameTable.content
        for i in range(4):
            for j in range(4):
                if nowTable[i][j] == 0:
                    zeroPos.append((i, j))
        if len(zeroPos) == 0:
            return False

        which = random.randint(0, len(zeroPos)-1)
        x = zeroPos[which][0]
        y = zeroPos[which][1]
        gameTable.content[x][y] = 2
        return True

    def shift(self, gameTable, direction):
        for __ in range(2):
            for _ in range(4):
                for i in range(4):
                    for j in range(4):
                        suci = i + direction[0]
                        sucj = j + direction[1]
                        prei = i - direction[0]
                        prej = j - direction[1]
                        if suci>=0 and suci<=3 and \
                           sucj>=0 and sucj<=3 and __ == 0 and\
                           gameTable.content[i][j]==gameTable.content[suci][sucj]:
                            gameTable.content[suci][sucj] += gameTable.content[i][j]
                            gameTable.content[i][j] = 0
                        if prei>=0 and prei<=3 and \
                           prej>=0 and prej<=3 and __ == 1 and\
                           gameTable.content[i][j] == 0:
                            gameTable.content[i][j] = gameTable.content[prei][prej]
                            gameTable.content[prei][prej] = 0

    def getKey(self, key):
        if key == 'w':
            return (-1, 0)
        if key == 'a':
            return (0, -1)
        if key == 's':
            return (1, 0)
        if key == 'd':
            return (0, 1)

    def gameLoop(self, gameTable, gameEnding):
        while gameEnding:
            os.system("clear")
            gameEnding = self.randomGen(gameTable)
            gameTable.printTable()
            direction = self.getKey(input())
            self.shift(gameTable, direction)

def main():
    gameEnding = False
    controller = gameRun()
    controller.gameLoop(Table(), True)
    print("Game Over!")


if __name__ == "__main__":
    main()
