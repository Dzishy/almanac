from Simulation import Simulation
from Population import Population

def main ():
    
    simulation = Simulation()
    population = Population(simulation)
    
    population.initialInfection(simulation)
    population.displayStats(simulation)
    population.graphics()
    
    input("\nPress 'Enter' to begin the simulation.")
    
    for i in range (1, simulation.simDays):
        population.spreadInfection(simulation)
        population.update(simulation)
        population.displayStats(simulation)
        population.graphics()
        
        if i != simulation.simDays - 1:
            input ("\nPress 'Enter' to advance to the next day")

main()