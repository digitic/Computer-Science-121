import random
import tkinter
random.seed()

def plot(xvals, yvals):
    # This is a function for creating a simple scatter plot.  You will use it,
    # but you can ignore the internal workings.
    root = tkinter.Tk()
    c = tkinter.Canvas(root, width=700, height=400, bg='white') # Was 350 x 280
    c.grid()
    # Create the x-axis.
    c.create_line(50,350,650,350, width=3)
    for i in range(5):
        x = 50 + (i * 150)
        c.create_text(x,355,anchor='n', text='%s'% (.5*(i+2) ) )
    # Create the y-axis.
    c.create_line(50,350,50,50, width=3)
    for i in range(5):
        y = 350 - (i * 75)
        c.create_text(45,y, anchor='e', text='%s'% (.25*i))
    # Plot the points.
    for i in range(len(xvals)):
        x, y = xvals[i], yvals[i]
        xpixel = int(50 + 300*(x-1))
        ypixel = int(350 - 300*y)
        c.create_oval(xpixel-3,ypixel-3,xpixel+3,ypixel+3, width=1, fill='red')
    root.mainloop()

# Constants: setting these values controls the parameters of your experiment.
injurycost     = 10  # Cost of losing a fight  
displaycost    = 1   # Cost of displaying between two passive birds  
foodbenefit    = 8   # Value of the food being fought over   
init_hawk      = 0
init_dove      = 0
init_defensive = 0
init_evolving  = 150

########
# Your code here
########
class World:
    def __init__(self):
        self.birdList = []
    def update(self):
        i = 0
        while(i < len(self.birdList)):
            self.birdList[i].update()
            i += 1
    def free_food(self, pieces):
        i = 0
        while(i < pieces):
            self.birdList[int(random.random()*len(self.birdList))].eat()
            i += 1
    def conflict(self, pieces):
        i = 0
        while(i < pieces):
            bird1 = self.birdList[int(random.random()*len(self.birdList))]
            bird2 = self.birdList[int(random.random()*len(self.birdList))]
            while(bird1 == bird2):
                bird2 = self.birdList[int(random.random()*len(self.birdList))]
            bird1.encounter(bird2)
            i += 1
    def status(self):
        doveCount = 0
        hawkCount = 0
        defensiveCount = 0 
        i = 0
        while(i < len(self.birdList)):
            if(self.birdList[i].species == "Dove"):
                doveCount += 1
            elif(self.birdList[i].species == "Hawk"):
                hawkCount += 1
            elif(self.birdList[i].species == "Defensive"):
                defensiveCount += 1
            i += 1
        print("There are currently " + str(doveCount) + " Doves and " + str(hawkCount) + " Hawks and " + str(defensiveCount) + " Defenders.")
    def evolvingPlot(self):
        self.xs = []
        self.ys = []
        for x in range (0, len(self.birdList)):
            if(self.birdList[x].species == "Evolver"):
                self.xs.append(self.birdList[x].weight)
                self.ys.append(self.birdList[x].aggro)
        plot(self.xs, self.ys)

class Bird:
    def __init__(self, world):
        world.birdList.append(self)
        self.worldIn = world
        self.health = 100
    def eat(self):
        self.health += foodbenefit
    def injured(self):
        self.health -= injurycost
    def display(self):
        self.health -= displaycost
    def die(self):
        self.worldIn.birdList.remove(self)
    def update(self):
        self.health -= 1
        if(self.health <= 0):
            self.die()

class Dove(Bird):
    def __init__(self, world):
        super().__init__(world)
        self.species = "Dove"
    def update(self):
        super().update()
        if(self.health >= 200):
            self.health -= 100
            d = Dove(self.worldIn)
            self.worldIn.birdList.append(d)
    def defend_choice(self):
        return False
    def encounter(self, bird):
        if(bird.defend_choice() == False):
            self.display()
            bird.display()
            if(random.random() >= 0.5):
                self.eat()
            else:
                bird.eat()
        else:
            bird.eat()

class Hawk(Bird):
    def __init__(self, world):
        super().__init__(world)
        self.species = "Hawk"
    def update(self):
        super().update()
        if(self.health >= 200):
            self.health -= 100
            h = Hawk(self.worldIn)
            self.worldIn.birdList.append(h)
    def defend_choice(self):
        return True
    def encounter(self, bird):
        if(bird.defend_choice() == True):
            if(random.random() >= 0.5):
                self.eat()
                bird.injured()
            else:
                bird.eat()
                self.injured()
        else:
            self.eat()

class Defensive(Bird):
    def __init__(self, world):
        super().__init__(world)
        self.species = "Defensive"
    def update(self):
        super().update()
        if(self.health >= 200):
            self.health -= 100
            #d is used for dove and def doesn't work, so f for defensive.
            f = Defensive(self.worldIn)
            self.worldIn.birdList.append(f)
    def defend_choice(self):
        return True
    def encounter(self, bird):
        if(bird.defend_choice() == False):
            self.display()
            bird.display()
            if(random.random() > 0.5):
                self.eat()
            else:
                bird.eat()
        else:
            bird.eat()

class Evolving(Bird):
    def __init__(self, world, weights, aggression):
        super().__init__(world)
        self.species = "Evolver"
        self.aggro = aggression
        self.weight = weights
        if(self.aggro == None):
            self.aggro = random.random()
        if(self.weight == None):
            self.weight = (random.random()*2) + 1
    def update(self):
        self.health -= (0.4 + (0.6 * self.weight))
        if(self.health >= 200):
            self.health -= 100
            self.weightChange = (random.random()*0.1) - 0.05
            self.aggroChange = (random.random()*0.2) - 0.1
            if(self.weight + self.weightChange < 1):
                self.weightChange = self.weight - 1
            if(self.weight + self.weightChange > 3):
                self.weightChange = 3 - self.weight
            if(self.aggro + self.aggroChange < 0):
                self.aggroChange = self.aggro
            if(self.aggro + self.aggroChange > 1):
                self.aggroChange = 1 - self.aggro
            e = Evolving(self.worldIn, self.weight + self.weightChange, self.aggro + self.aggroChange)
            self.worldIn.birdList.append(e)

    def defend_choice(self):
        willDef = random.random()
        if(willDef <= self.aggro):
            return True
        else:
            return False
    def encounter(self, bird):
        willDefend = self.defend_choice()
        if(bird.defend_choice() == willDefend):
            if(willDefend):
                if(random.random() <= self.weight/(self.weight + bird.weight)):
                    self.eat()
                    bird.injured()
                else:
                    bird.eat()
                    self.injured()
            else:
                self.display()
                bird.display()
                if(random.random() <= 0.5):
                    self.eat()
                else:
                    bird.eat()
        elif(willDefend):
            self.eat()
        else:
            bird.eat()



########
# The code below actually runs the simulation.  You shouldn't have to do anything to it.
########
w = World()
for i in range(init_dove):
    Dove(w)
for i in range(init_hawk):
    Hawk(w)
for i in range(init_defensive):
    Defensive(w)
for i in range(init_evolving):
    Evolving(w,None,None)

for t in range(10000):
    w.free_food(10)
    w.conflict(50)
    w.update()
w.status()
w.evolvingPlot()    # This line adds a plot of evolving birds. Uncomment it when needed.


