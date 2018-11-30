import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')




EVIDENCE_NUM = 13
STR_MAP = """
Garbage Room#####   #####    ######
            #   #   #        #    #
            #   # H #        #    # pharmacologist's lab
            #   # A #        #    #
            ##### L ##########    #######
workshop    #   # L #	                #
            #   # W #                   # Classroom
            #   # A #                   #
            ##### Y #####################
            #   #   #
            #   #   #
            #####   #
                #   #
                #   #
                #   #
            #####   #####
            #           #
            #           #
            #           #
            ############# Entrance Hall
"""

def showMap():
    clear()
    print(STR_MAP)
    print()
    print('You are now in ' + player.room.name)

def showHelp():
    clear()
    print()
    print("input <the number label of statment> to refute a statement.")
    print("input me to show your current credibility")
    print("input <the number labeled on the evidence> to present evidence if your are asked to present evidence.")
    print()
    input("press enter to continue...")


class Trial:
    def __init__(self, player):
        self.debates = []
        self.answers = None
        self.evidences = None
        self.player = player

    def addDebate(self, deb):
        self.debates.append(deb)
    def startTrial(self, read):
        if read:
            SAVE = self.readArchive('save.txt')
        i = 0
        pos = SAVE if read else 0
        with open("text.txt") as f:
            while i < pos: # scan through the script until the checkpoint
                l = f.readline()
                if l == '&\n':
                    i += 1
            is_reading = True
            while is_reading and i <= 11:
                clear()
                curr_debate = Debate(self.evidences[i], self.answers[i], self.player, i)
                curr_line = f.readline()
                while curr_line != "" and curr_line != "&\n":
                    if curr_line[0] == "[":
                        print(curr_line[1:], end='')
                    else:
                        curr_debate.addStatement(curr_line)
                    curr_line = f.readline()
                input("\npress enter to continue...")
                if curr_line == "":
                    is_reading = False
                    break
                else:
                    curr_debate.debate()
                    self.debates.append(curr_debate)
                    i += 1
    def readArchive(self, name):
        f = open(name)
        pos = f.readline()
        cred = f.readline()
        f.close()
        if cred == '':
            return 0
        elif int(cred) <= 0 or int(cred) > 100:
            self.player.credibility = 60
        else:
            self.player.credibility = int(cred)
            return int(pos)

class Debate:
    def __init__(self, evids, ans, player, pos):
        self.statements = []
        self.evidences = evids
        self.answers = ans
        self.player = player
        self.position = pos

    def saveArchive(self, n):
        f = open('save.txt', 'w')
        f.write(str(n) + '\n')
        f.write(str(self.player.credibility))
        f.close()

    def addStatement(self, state):
        self.statements.append(state)

    def debatePrompt(self):
        clear()
        print("Your evidence for this set:")
        n = 1
        for e in self.evidences:
            name = e.name
            print(str(n) + ". " + name)
            n += 1
        print()
        n = 1
        for x in self.statements:
            print(str(n) + ". " + x)
            n += 1

    def debate(self):
        i = self.position
        self.debatePrompt()
        result = False
        #Whether you're refuting or agreeing. False is refute.
        side = False
        while not result and int(self.player.credibility) > 0:
            refute = ""
            while not refute.isnumeric():
                refute = input("What do you want to do? ")
                if refute == "me":
                    self.print_my_status()
                elif refute == "help":
                    showHelp()
                elif refute == "exit":
                    self.saveArchive(i)
                    exit()
                elif refute == "refute":
                    refute = input("Which statement is suspicious? ")
                elif refute == "agree":
                    refute = input("Which statement is supported? ")
                    side = True
                elif refute == "inventory":
                    self.player.showInventory()
                elif refute == "inspect":
                    refute = input("Which piece of evidence to inspect? ")
                    if(refute >= 1 and refute <= len(self.evidences)):
                        self.evidences[refute-1].describe()
                elif refute == 'heal':
                    if len(self.player.props):
                        self.player.consume(1)
                        self.player.props.pop(0)
                    else:
                        print("No such prop!")
                        input('press enter to continue...')
                else:
                    print("invalid command!")
                self.debatePrompt()
            evid = ""
            while not evid.isnumeric():
                evid = input("What evidence relates to this? ")
                if evid == "me":
                    self.print_my_status()
                elif evid == "help":
                    showHelp()
                elif  evid == "exit":
                    self.saveArchive(i+1)
                    exit()
                else:
                    print("invalid command!")
                self.debatePrompt()
            if [int(refute), int(evid), side] == self.answers:
                result = True
                self.player.credibility = min(100, self.player.credibility + 4)
                clear()
                print("Your refute is convincing! Proceeding to the next round.")
                input("press enter to continue...")
            else:
                print("\nYour refute did not convince the crowd! Credibility lost!\n")
                result = False
                self.player.credibility += self.player.penalty
                self.player.penalty = max(min(self.player.penalty-1, -10), -40)
        if(int(self.player.credibility) <= 0):
            print("Your wild guesses have destroyed your credibility, and you are deemed completely incompetent. YOU FAIL.")
            self.saveArchive(i+1)
            input("press enter to exit.")
            exit()

    def print_my_status(self):
        clear()
        print("Your current credibility is " + str(self.player.credibility) + "%.")
        print("You are missing " + str(EVIDENCE_NUM - len(self.player.evidences)) + " pieces of evidence.\n")
        input("press enter to continue...")
