import random

class Pykemon ():
    
    def __init__ (self, name, element, health, speed):
        self.name = name.title()
        self.element = element
        self.currentHealth = health
        self.maxHealth = health
        self.speed = speed
        self.alive = True
    
    def lightAttack (self, enemy):
        damage = random.randint (15,25)
        print (f"Pykemon {self.name} used {self.moves[0]}")
        print (f"It dealt {damage} damage.")
        enemy.currentHealth -= damage
        
    def massiveAttack (self, enemy):
        damage = random.randint (0,50)
        print (f"Pykemon {self.name} used {self.moves[1]}")
        if damage < 10:
            print (f"The attack missed.")
        else:
            print (f"It dealt {damage} damage.")
            enemy.currentHealth -= damage
    
    def restore (self):
        heal = random.randint(15,25)
        print (f"Pykemon {self.name} used {self.moves[2]}")
        print (f"It healed {heal} health points.")
        self.currentHealth += heal
        if self.currentHealth > self.maxHealth:
            self.currentHealth = self.maxHealth
    
    def faint (self):
        if self.currentHealth <= 0:
            self.alive = False
            print (f"Pykemon {self.name} has fainted!")
            input ("Press 'Enter' to continue.")
        
    def showStats (self):
        print (f"\nName: {self.name}")
        print (f"Element Type: {self.element}")
        print (f"Health: {self.currentHealth}/{self.maxHealth}")
        print (f"Speed: {self.speed}")