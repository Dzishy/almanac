import random
from Person import Person


class Population ():
    
    def __init__ (self, simulation):
        
        self.population = []
        for i in range (simulation.gridSize):
            row = []
            for j in range (simulation.gridSize):
                person = Person()
                row.append (person)
            self.population.append(row)
        
    def initialInfection (self, simulation):
                        # only integers can be used in FOR loops !!!
        infectedCount = int (round (simulation.infectionPercent * simulation.populationSize,0))
        
        infections = 0
        
        while infections < infectedCount:
            #x is a random row in the population, y is a random person in the random row
            #self.population[x][y] represents a random person in the population list
            x = random.randint(0, simulation.gridSize - 1)
            y = random.randint(0, simulation.gridSize - 1)
            
            if not self.population[x][y].infected:
                self.population[x][y].infected = True
                self.population[x][y].daysInfected = 1
                infections += 1
        
    def spreadInfection (self, simulation):
        
        for i in range (simulation.gridSize):
            for j in range (simulation.gridSize):
                if self.population[i][j].dead == False:
                    #we are in the first row                
                    if i == 0:
                        if j == 0:
                            if self.population[i][j+1].infected or self.population[i+1][j].infected:
                                self.population[i][j].infect(simulation)
                        elif j == simulation.gridSize - 1:
                            if self.population[i][j-1].infected or self.population[i+1][j].infected:
                                self.population[i][j].infect(simulation)
                        else:
                            if self.population[i][j-1].infected or self.population[i][j+1].infected or self.population[i+1][j].infected:
                                self.population[i][j].infect(simulation)
                    #We are in the last row
                    elif i == simulation.gridSize - 1:
                        if j == 0:
                            if self.population[i][j+1].infected or self.population[i-1][j].infected:
                                self.population[i][j].infect(simulation)
                        elif j == simulation.gridSize - 1:
                            if self.population[i][j-1].infected or self.population[i-1][j].infected:
                                self.population[i][j].infect(simulation)
                        else:
                            if self.population[i][j-1].infected or self.population[i][j+1].infected or self.population[i-1][j].infected:
                                self.population[i][j].infect(simulation)     
                    #We are in a row inbetween
                    else: 
                        if j == 0:
                            if self.population[i][j+1].infected or self.population[i+1][j].infected or self.population[i-1][j].infected:
                                self.population[i][j].infect(simulation)
                        elif j == simulation.gridSize - 1:
                            if self.population[i][j-1].infected or self.population[i+1][j].infected or self.population[i-1][j].infected:
                                self.population[i][j].infect(simulation)
                        else:
                            if self.population[i][j-1].infected or self.population[i][j+1].infected or self.population[i+1][j].infected or self.population[i-1][j].infected:
                                self.population[i][j].infect(simulation)     
        
    def update (self,simulation):
        
        simulation.dayNum += 1
        
        for row in self.population:
            for person in row:
                person.update (simulation)
        
    def displayStats (self, simulation):
        
        totalInfectedCount = 0
        totalDeadCount = 0
        
        for row in self.population:
            for person in row:
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
        
