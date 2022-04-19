import Characters
import random
DEBUG = True

class Game:
    def __init__(self, player_name):
        random.shuffle(player_name)
        self.player_name = player_name
        self.name2id = {}
        self.killer = 2
        self.civil = 3
        for i in range(len(player_name)):
            self.name2id[player_name[i]] = i

        self.player_list = []
        for i in range(len(player_name)): # Player List must length 5
            self.player_list.append(Characters.Player(player_name[i], i))

        self.gameEnd = False
        self.log = ''

    def playerStatus(self):
        res = ''
        for player in self.player_list:
            res += '[%d] %s (%s) { Death: %s, Needles: %d }\n' % (player.id, player.name, player.actAs.title, str(player.actAs.isDeath), player.actAs.needle)
        return res

    def playerAnonymousStatus(self):
        res = []
        for player in self.player_list:
            res.append([player.name, "Died" if player.actAs.isDeath else "Alive"])
        return sorted(res)

    def getPlayerStatus(self, name):
        dic = {}
        id = self.name2id[name]
        dic['title'] = self.player_list[id].actAs.title
        dic['death'] = self.player_list[id].actAs.isDeath
        dic['needle'] = self.player_list[id].actAs.needle
        return dic

    def updatePlayer(self):
        k = 0
        c = 0
        for player in self.player_list:
            if player.actAs.identity == 'Killer' and not player.actAs.isDeath:
                k += 1
            elif player.actAs.identity == 'Civil' and not player.actAs.isDeath:
                c += 1
        self.killer = k
        self.civil = c

    def getPlayer(self, name):
        id = self.name2id[name]
        return self.player_list[id]

    def whichEnd(self):
        if DEBUG: print("Civil: %d, Killer: %d" % (self.civil, self.killer))
        if self.civil == 0 and self.killer >= 1:
            self.gameEnd = True
            return "Killer Win"
        if self.civil >= 1 and self.killer == 0:
            self.gameEnd = True
            return "Civil Win"
        else:
            return "Game Continue"

    def elect(self):
        input('Discussing ... (Anykeys Continue)')
        dic = {}
        vote = {}
        for player in sorted(player_name):
            vote[player] = 0
        vote['pass'] = 0
        for player in sorted(player_name):
            if not wereWolves.getPlayer(player).actAs.isDeath:
                election = input("%s ➜ " % player)
                if election not in player_name:
                    dic[player] = ''
                    vote['pass'] += 1
                    continue
                else:
                    dic[player] = election
                    vote[election] += 1
        _max = -1
        who = ''
        for key in vote:
            if vote[key] >= _max:
                _max = vote[key]
                who = key
        if who == 'pass':
            return dic, 'Skipped, No one'
        tie = 0
        for key in vote:
            if vote[key] == _max:
                tie += 1
        if tie > 1:
            return dic, 'Tie, No one'
        else:
            wereWolves.getPlayer(who).actAs.die()
            return dic, '%s' % who


        return dic

    def printElection(self, dic):
        print('==== Election ====')
        for key in dic:
            print("%s ➜ %s" % (key, dic[key]))
        print('==================')




    def loop(self):
        while not self.gameEnd:

            for player in self.player_list:
                if player.actAs.isBanned:
                    player.actAs.unBanned()

            for player in self.player_list:
                title = player.actAs.title
                prompt = ''
                if player.actAs.isDeath:
                    print("[%s - %s] Died" % (
                        player.name,
                        player.actAs.title,
                    ))
                    continue
                if not player.actAs.isBanned:
                    prompt = input("[%s - %s] Operation on whom? >>> " % (
                        player.name,
                        title,
                    ))
                    if prompt in self.player_name:
                        dic = {'Banner': 'bans', 'Doctor': 'injects', 'Police': 'asks', 'Killer': 'kills', 'Spy': 'kills'}
                        self.log += '%s (%s) %s %s (%s)' % (player.name, player.actAs.title, dic[player.actAs.title], prompt, wereWolves.getPlayer(prompt).actAs.title)
                        if player.actAs.title == 'Police':
                            self.log += ' as a ' + self.getPlayer(prompt).actAs.getAsked()
                        self.log += '\n'
                if player.actAs.isBanned:
                    input("[%s - %s] (Banned) Operation on whom? >>> " % (
                        player.name,
                        title,
                    ))
                if prompt not in self.player_name:
                    continue
                if title == 'Banner':
                    self.getPlayer(prompt).actAs.getBanned()
                if title == 'Doctor':
                    self.getPlayer(prompt).actAs.getInject()
                if title == 'Police':
                    identity = self.getPlayer(prompt).actAs.getAsked()
                    print(identity)
                if title == 'Killer' or title == 'Spy':
                    self.getPlayer(prompt).actAs.getKilled()



            # Print Player Status
            print(self.playerAnonymousStatus())

            # Count Player Nums
            self.updatePlayer()
            # Print Result
            end = self.whichEnd()
            print(end)
            if self.gameEnd:
                break

            # Election
            dic, who = self.elect()
            self.printElection(dic)
            print(who + " was voted as a Killer.")

            # Count Player Nums
            self.updatePlayer()
            # Print Result
            print(self.whichEnd())




if __name__ == '__main__':
    player_name = []
    for i in range(5):
        name = input("Enter P%d's Name: " % (i+1))
        player_name.append(name)
    # FOR DEBUG PURPOSE
    # player_name = ['Steve', 'Alston', 'King', 'Jane', 'Stephen']
    wereWolves = Game(player_name=player_name)
    wereWolves.loop()
    print(wereWolves.log)

