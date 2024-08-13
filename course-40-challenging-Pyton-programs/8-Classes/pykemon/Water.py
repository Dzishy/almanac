import random

from Pykemon import Pykemon

class Water (Pykemon):
    def __init__ (self, name, element, health, speed):
        super().__init__ (name, element, health, speed)
        self.moves = ['Bite', 'Splash', 'Dive', 'Water Cannon']
        # соответств [lightAttack, massiveAttack, restore, specialAttack]
        
    def specialAttack (self, enemy):
        print (f"Pykemon {self.name} used {self.moves[3]}")
        if enemy.element == 'FIRE':
            print ("It is very effective!")
            damage = random.randint (35,50)
        elif enemy.element == 'GRASS':
            print ("It is not very effective...")
            damage = random.randint (5,10)
        else:
            damage = random.randint (10,30)
        print (f"It dealt {damage} damage.")
        enemy.currentHealth -= damage
        
    def moveInfo(self):    # ask about the possibility for optimization of this step to repeat the prints less.
        
        print(f"\n{self.name} Moves: ")

        print(f"-- {self.moves[0]} --")
        print("\tAn efficient attack...")
        print("\tGuaranteed to do damage within a range of 15 to 25 damage points.")
        
        print(f"-- {self.moves[1]} --")
        print("\tA risky attack...")
        print("\tCould deal damage up to 50 damage points or as little as 0 damage points.")
        
        print(f"-- {self.moves[2]} --")
        print("\tA restorative move...")
        print("\tGuaranteed to heal your Pykemon 15 to 25 damage points.")
        
        print(f"-- {self.moves[3]} --")
        print("\tA powerful WATER based attack...")
        print("\tGuaranteed to deal MASSIVE damage to FIRE type Pykemon.")
        