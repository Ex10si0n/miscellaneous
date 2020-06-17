import pygame
import random
import pyttsx3

class WordDict:
    greeting = ['Hello', 'Hello小伙伴们', '小伙伴们']
    intro = ['这里是', '我是', '欢迎收看']
    writer_name = ['小A看世界', 'X哥讲堂']
    topic = ['大锤没拍', '莱因哈特没有大招了']

class ParaStrut:
    def getInput():
        WordDict.topic[0] = input('输入文章话题:')
        WordDict.topic[1] = input('输入文章话题的另外一种表述方式:')
    def getPara():
        a = random.randint(0, len(WordDict.greeting)-1)
        b = random.randint(0, len(WordDict.intro)-1)
        c = random.randint(0, len(WordDict.writer_name)-1)
        p = ('%s大家好，%s%s。%s是怎么回事呢?%s相信大家都很熟悉，但是%s是怎么回事呢?下面就让小编带大家一起了解吧。%s，其实就是%s，大家可能会感到很惊讶，但事实就是这样，小编也感到非常惊讶。那么这就是关于%s的事情了，大家有什么想法呢？欢迎在评论区告诉小编一起讨论哦。视频资料来自互联网，这里是%s，我们下期再见，拜拜。'\
            % (WordDict.greeting[a], WordDict.intro[b], WordDict.writer_name[c], WordDict.topic[0],\
            WordDict.topic[0], WordDict.topic[0], WordDict.topic[0], WordDict.topic[1],\
            WordDict.topic[0], WordDict.writer_name[c]))
        engine = pyttsx3.init()
        pygame.mixer.init()
        track = pygame.mixer.music.load("trip.mp3")
        pygame.mixer.music.play()
        engine.say(p)
        print(p)
        engine.runAndWait()


if __name__ == '__main__':
    ParaStrut.getInput()
    ParaStrut.getPara()

