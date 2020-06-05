import sys
import time
import os

# Settings
'''
For different Operating System
You need to set it here.
values: ['windows', 'linux', 'unix']
'''
platform = 'unix'
# End Settings

# Shortcut
version = '(Version 0.2)'
# End Shortcut

class Table:
    '''
    Table Class
    '''

    def __init__(self):
        self.size_x = 0
        self.size_y = 0
        self.table = []
        self.f_color = '⬛️'
        self.b_color = '⬜️'

    def __str__(self):
        for i in range(1, self.size_x-1):
            for j in range(1, self.size_y-1):
                if self.table[i][j] != '0':
                    print(self.f_color, end='')
                else:
                    print(self.b_color, end='')
            print()
        return ""

    def get_surround(self, x, y):
        dirs = [
            (-1, -1), (0, -1), (1, -1),
            (-1,  0),          (1,  0),
            (-1,  1), (0,  1), (1,  1)
        ]
        surrounds = 0
        for dir_ in dirs:
            surrounds += int(self.table[x+dir_[0]][y+dir_[1]])
        return surrounds

    def toggle(self, x, y, to):
        if self.table[x][y] == to:
            return False
        self.table[x][y] = to
        return True


    def get_size(self):
        self.size_x = len(self.table)
        self.size_y = len(self.table[0])


class Algorithm:
    '''
    lgorithm Class
    '''

    def check(self, Table):
        surrounds = [[0 for i in range(Table.size_y+5)] for j in range(Table.size_x+5)]
        break_inf = True
        for i in range(1, Table.size_x-1):
            for j in range(1, Table.size_y-1):
                surrounds[i][j] = Table.get_surround(i, j)

        for i in range(1, Table.size_x-1):
            for j in range(1, Table.size_y-1):
                if surrounds[i][j] == 3:
                    suc = Table.toggle(i, j, '1')
                    if suc == True:
                        break_inf = False
                elif surrounds[i][j] == 2:
                    continue
                else:
                    suc = Table.toggle(i, j, '0')
                    if suc == True:
                        break_inf = False

        return not break_inf


class Manual:

    def man(self):
        help_txt = \
'''
        Manual Documentations
------------------------------------
Commands:
    r            run single times
    r [int]      run n times
    r inf        keep running

    n            create a life file
    q            quit

    set [parameters]
        speed    [fast/mid/slow]
        color    [r/g/b/y]

'''
        print(help_txt)


def main():
    clear = 'clear' if platform == 'unix' or platform == 'linux' else 'cls'
    table = Table()
    manual = Manual()
    algorithm = Algorithm()
    sleep_time = 0.2
    print('Game of Life Simulator', version)
    print('Type "help" to open manual, "q" to exit')
    print()
    if len(sys.argv) == 1:
        print('Usage: python3 game-of-life.py [life file name]')
        create = input('Create a new [life file]? [Y/n]: ')
        if create == 'y' or create =='Y':
            file_name = input('Filename: ')
            os.system('vim '+file_name+'.life')
        else:
            print("Farewell")
            return
    if len(sys.argv) == 1:
        sys.argv.append(file_name+'.life')
    print('Loading file:', sys.argv[1])
    file_dir = sys.argv[1]
    with open(file_dir, 'r') as f:
        line = f.readline()
        while line:
            line = line.strip('\n').split(' ')
            table.table.append(line)
            line = f.readline()

    table.get_size()
    print(table.size_x, table.size_y)
    print('File loaded success')
    print('Printing initialized pattern ...')
    print(table)
    while True:
        cmd = input("> ")
        if cmd == 'n':
            create = input('Create a new [life file]? [Y/n]: ')
            if create == 'y' or create =='Y':
                file_name = input('Filename: ')
                os.system('vim '+file_name+'.life')
                file_name+='.life'
                print('Copy this command and run again in your shell',\
                      '\n      python3 game-of-life.py', file_name,\
                      '\n Type "q" to quit')
                input('> ')
                return
            else:
                continue

        if cmd == 'q':
            print("Farewell")
            break
        if cmd == 'h' or cmd == 'help':
            manual.man()
        if cmd == '':
            continue
        args = cmd.split()
        if args[0] == 'set':
            if len(args) == 1:
                print("Usage: set [parameters]\nspeed [fast/mid/slow]\ncolor [r/g/b/y]")
            elif args[1] == 'speed':
                if args[2] == 'fast':
                    sleep_time = 0.05
                    print("Speed set: Fast")
                elif args[2] == 'mid':
                    sleep_time = 0.2
                    print("Speed set: Mid")
                elif args[2] == 'slow':
                    sleep_time = 0.35
                    print("Speed set: Slow")
            elif args[1] == 'color':
                if args[2] not in ['r', 'g', 'b', 'y']:
                    print("Parameters not valid")
                else:
                    color_pane = {'r': '🟥', 'g': '🟩', 'b': '🟦', 'y': '🟨'}
                    print('Cell color set: ', color_pane[args[2]])
                    table.f_color = color_pane[args[2]]

        if args[0] == 'r':
            if len(args) == 1:
                args.append('1')

            if args[1] == 'inf':
                runable = True
                while runable:
                    os.system(clear)
                    runable = algorithm.check(table)
                    print(table)
                    time.sleep(sleep_time)

            else:
                for _ in range(int(args[1])):
                    os.system(clear)
                    algorithm.check(table)
                    print(table)
                    time.sleep(sleep_time)

if __name__ == '__main__':
    main()
