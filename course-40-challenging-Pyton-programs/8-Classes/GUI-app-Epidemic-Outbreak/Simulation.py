import math


class Simulation ():
    
    def __init__ (self):
        
        self.dayNum = 1
        
        print ("To simulate the epidemic outbreak we need to know the population size")
        self.populationSize = int (input("Enter the population size: "))
        root = math.sqrt(self.populationSize)
        if int (root + .5)**2 != self.populationSize:
            root = round (root,0)
            self.gridSize = int (root)
            self.populationSize = self.gridSize**2
            print (f"Rounding population size to {self.populationSize} for visual purposes.")
        else:
             self.gridSize = int (math.sqrt(self.populationSize))
        
        print ("\nWe must first start by infecting a portion of the population")
        self.infectionPercent = float (input ("Enter the percentage (0-100) of the population to initially infect: "))
        self.infectionPercent /= 100
        
        print ("\nWe must know the risk person has to contract the desease when exposed")
        self.infectionProbability = float (input ("Enter the probability (0-100) that a person gets infected when exposed to the desease: "))
        
        print ("\nWe must know how long the infection will last when exposed.")
        self.infectionDuration = int (input ("Enter the duration (in days) of the infection: "))
        
        print ("\nWe must know the mortality rate of those infected.")
        self.mortalityRate = float (input ("Enter the mortality rate (0-100) of the infection: "))
        
        print ("\n We must know how long to run the simulation.")
        self.simDays = int (input ("Enter the number of days to simulate: "))