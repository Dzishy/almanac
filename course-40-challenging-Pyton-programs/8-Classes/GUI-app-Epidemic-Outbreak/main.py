from Simulation import Simulation
from Population import Population
import tkinter

def graphics (simulation, population, canvas):
    #Get the dimensions of an individual square in a grid
    #Each square represents a person in the population
    #Use 600 for a GUI window that is 600x600, change if desired.
    #To get the dimensions of a square, take the dimensions of the window and divide by total number of squares in a row
    
    # / division, returns an integer
    # // - Floor division is a division operation that returns the largest integer that is less than or equal to the result of the division 
    squareDim = 600//simulation.gridSize
    for i in range (simulation.gridSize):
        #y is the starting index of where a given square should be drawn
        y = i * squareDim
        for j in range (simulation.gridSize):
            #x is the starting index of where a given square should be drawn.
            x = j * squareDim
            
            if population.population[i][j].dead:
                canvas.create_rectangle(x, y, x+squareDim, y+squareDim, fill = 'red')
            else:
                if population.population[i][j].infected:
                    canvas.create_rectangle(x, y, x+squareDim, y+squareDim, fill = 'yellow')
                else:
                    canvas.create_rectangle(x, y, x+squareDim, y+squareDim, fill = 'green')




def main ():
    
    simulation = Simulation()
    population = Population(simulation)
    
    winWidth = 600
    winHeight = 600
    
    simWindow = tkinter.Tk()
    simWindow.title("Epidemic Outbreak")
    simCanvas = tkinter.Canvas(simWindow, width=winWidth, height=winHeight, bg='lightblue')
    simCanvas.pack(side=tkinter.LEFT)
    
    
    
    population.initialInfection(simulation)
    population.displayStats(simulation)
    
    input("\nPress 'Enter' to begin the simulation.")

    for i in range (1, simulation.simDays):
        population.spreadInfection(simulation)
        population.update(simulation)
        population.displayStats(simulation)
        graphics(simulation, population, simCanvas)
        
        simWindow.update()
        
        if i != simulation.simDays-1:
            simCanvas.delete('all')

    simWindow.mainloop()
    
main()