import random

class Person():
    
    def __init__ (self):
        
        self.infected = False
        self.dead = False
        self.daysInfected = 0
        
    def infect (self, simulation):
        
        if random.randint(0,100) < simulation.infectionProbability:
            self.infected = True
        
    def heal (self):
        
        self.infected = False
        self.daysInfected = 0
        
    def die (self):
        
        self.dead = True
        
    def update (self, simulation):
        
        if not self.dead:
            if self.infected:
                self.daysInfected += 1
                if random.randint(0,100) < simulation.mortalityRate:
                    self.die()
                elif self.daysInfected == simulation.infectionDuration:
                    self.heal()