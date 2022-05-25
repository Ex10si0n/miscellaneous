class color:
    
    def __init__(self):
        pass


    def print(text, color='red', bg='default', weight='normal', end='\n'):
        try:
            palette = { 'red': 31, 'green': 32, 'yellow': 33, 'blue': 34, 'magenta': 35, 'cyan': 36, 'r': 31, 'g': 32, 'y': 33, 'b': 34, 'm': 35, 'c': 36 }
            color = palette[color]
            cstr = ''

            if bg == 'default':
                if weight == 'normal':
                    cstr = '\033[%dm%s\033[0m' % (color, text)
                if weight == 'bold':
                    cstr = '\u001b[%d;1m%s\033[0m' % (color, text)
            else:
                try:
                    bg_color = { 'black': 40, 'red': 41, 'green': 42, 'yellow': 43, 'blue': 44, 'magenta': 45, 'cyan': 46, 'white': 47, '1': 40, 'r': 41, 'g': 42, 'y': 43, 'b': 44, 'm': 45, 'c': 46, '0': 47 }
                    bg = bg_color[bg]
                    if weight == 'normal':
                        cstr = '\033[%d;%dm%s\033[0m' % (bg, color, text)
                    if weight == 'bold':
                        cstr = '\033[%d;%d;1m%s\033[0m' % (bg, color, text)
                except:
                    pass
            
            print(cstr, end=end)
            return

        except:
            cstr = ''
            if bg == 'default':
                if weight == 'normal':
                    cstr = u"\u001b[38;5;%dm%s\u001b[0m" % (color, text)
                if weight == 'bold':
                    cstr = u"\u001b[38;5;%d;1m%s\u001b[0m" % (color, text)
            else:
                try:
                    bg_color = { 'black': 40, 'red': 41, 'green': 42, 'yellow': 43, 'blue': 44, 'magenta': 45, 'cyan': 46, 'white': 47, '1': 40, 'r': 41, 'g': 42, 'y': 43, 'b': 44, 'm': 45, 'c': 46, '0': 47 }
                    bg = bg_color[bg]
                    if weight == 'normal':
                        cstr = u"\u001b[%d;38;5;%dm%s\u001b[0m" % (bg, color, text)
                    if weight == 'bold':
                        cstr = u"\u001b[%d;38;5;%d;1m%s\u001b[0m" % (bg, color, text)
                except:
                    pass

            print(cstr, end=end)


    def test():
        print('[Color Test]\n')
        for i in range(0, 16):
            for j in range(0, 16):
                code = str(i * 16 + j)
                print(u"\u001b[38;5;" + code + "m " + code.ljust(4), end='')
            print(u"\u001b[0m", end='')
            

