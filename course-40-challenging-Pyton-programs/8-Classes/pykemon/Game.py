import random
#from Pykemon import Pykemon
from Fire import Fire
from Water import Water
from Grass import Grass

class Game ():
    
    def __init__ (self):
        self.pElements = ['FIRE', 'WATER', 'GRASS']
        self.pNames = ['Chewdie', 'Spatol', 'Burnmander', 'Pykachu', 'Pyonx', 'Abbacab',
                       'Sweetil', 'Jampot', 'Hownstooth', 'Swagilybo', 'Muttle', 'Zantbat',
                       'Wiggly Poof', 'Rubblesaur']
        self.battlesWon = 0
        
    def createPykemon (self):
        name = self.pNames[random.randint(0, len(self.pNames)-1)]
        element = self.pElements[random.randint(0, len(self.pElements)-1)]
        health = random.randint(70, 100)
        speed = random.randint(1, 10)
        
        if element == 'FIRE':
            pykemon = Fire (name, element, health, speed)
        elif element == 'WATER':
            pykemon = Water (name, element, health, speed)
        else:
            pykemon = Grass (name, element, health, speed)
        
        return pykemon
    
    def choosePykemon (self):
        startPykemons = []
        while len(startPykemons) < 3:
            pykemon = self.createPykemon()
            valid = True
            for startPykemon in startPykemons:
                if startPykemon.name == pykemon.name or startPykemon.element == pykemon.element:
                    valid = False
            if valid:
                startPykemons.append (pykemon)
            
        for startPykemon in startPykemons:
            startPykemon.showStats ()
            startPykemon.moveInfo () 
            
        print ("Presenting you three Pykemon:")
        print (f"1. {startPykemons[0].name}")
        print (f"2. {startPykemons[1].name}")
        print (f"3. {startPykemons[2].name}")
        
        choice = int (input ("Which one you choose (1,2,3): "))
        pykemon = startPykemons[choice-1]
        return pykemon
    
    def chooseAttack (self, pykemon):
        print("\nWhat would you like to do...")
        print(f"- 1 - {pykemon.moves[0]}")
        print(f"- 2 - {pykemon.moves[1]}")
        print(f"- 3 - {pykemon.moves[2]}")
        print(f"- 4 - {pykemon.moves[3]}")
        
        choice = int (input("Please enter your move choice: "))
        print("\n-----------------------------------------------------------------------------")
        return choice
    
    def playerAttack (self, move, player, computer):
        if move == 1:
            player.lightAttack (computer)
        elif move == 2:
            player.massiveAttack (computer)
        elif move == 3:
            player.restore ()
        elif move == 4:
            player.specialAttack (computer)
            
        computer.faint()
    
    def compAttack(self, player, computer):
        move = random.randint(1,4)
        if move == 1:
            computer.lightAttack (player)
        elif move == 2:
            computer.massiveAttack (player)
        elif move == 3:
            computer.restore ()
        elif move == 4:
            computer.specialAttack (player)
            
        player.faint()
        
    def battle (self, player, computer):
        move = self.chooseAttack(player)
        
        if player.speed >= computer.speed:
            self.playerAttack(move, player, computer)
            if computer.alive:
                self.compAttack(player, computer)
        else:
            self.compAttack(player, computer)
            if player.alive:
                self.playerAttack(move, player, computer)