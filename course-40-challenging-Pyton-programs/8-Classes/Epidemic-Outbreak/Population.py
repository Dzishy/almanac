import random
from Person import Person


class Population ():
    
    def __init__ (self, simulation):
        
        self.population = []
        for i in range (simulation.populationSize):
            person = Person()
            self.population.append (person)
        
    def initialInfection (self, simulation):
        
        infectedCount = int (round (simulation.infectionPercent * simulation.populationSize,0))
        
        for i in range (infectedCount):
            self.population[i].infected = True
            self.population[i].daysInfected = 1
        
        random.shuffle(self.population)
        
    def spreadInfection (self, simulation):
        
        for i in range (len (self.population)):
            if self.population[i].dead == False:
                #i is the first person in the list, can only check to the right [i+1].                
                if i == 0:
                    if self.population[i+1].infected:
                        self.population[i].infect(simulation)
                #i is in the middle of the list, can check to the left [i-1] and right [i+1].
                elif i < len (self.population) -1:
                    if self.population[i+1].infected or self.population[i-1].infected:
                        self.population[i].infect(simulation)
                #i is the last person in the list, can only check to the left [i-1].
                elif i == len (self.population) -1:
                    if self.population[i-1].infected:
                        self.population[i].infect(simulation)
        
    def update (self,simulation):
        
        simulation.dayNum += 1
        
        for person in self.population:
            person.update (simulation)
        
    def displayStats (self, simulation):
        
        totalInfectedCount = 0
        totalDeadCount = 0
        
        for person in self.population:
            if person.infected:
                totalInfectedCount += 1
                if person.dead:
                    totalDeadCount += 1
                    
        infectedPercent = round((totalInfectedCount/simulation.populationSize)*100, 4)
        deadPercent = round((totalDeadCount/simulation.populationSize)*100, 4)
        
        print (f"\n Day # {simulation.dayNum}")
        print (f"Percentage of population infected: {infectedPercent}")
        print (f"Percentage of population dead: {deadPercent}")
        print (f"Total people infected: {totalInfectedCount} / {simulation.populationSize}")
        print (f"Total deaths: {totalDeadCount} / {simulation.populationSize}")
        

    def graphics (self):
        
        status = []
        
        for person in self.population:
            if person.dead:
                char = 'X'
            else:
                if person.infected:
                    char = 'I'
                else:
                    char = 'O'
            
            status.append(char)
        
        for letter in status:
            print (letter, end='-')