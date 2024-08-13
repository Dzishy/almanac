import random
from Pykemon import Pykemon
from Game import Game


def main ():
    
    print ("Welcome to Pykemon!")
    print ("We will gift you your first Pykemon.")
    print ("Here are three potencial Pykemon partners.")
    input ("Press 'Enter' to choose your first Pykemon!")
    playing = True
    while playing:
        
        game = Game ()        
        player = game.choosePykemon ()
        print (f"Congratulations! You have chosen {player.name}")
        input (f"Your journey with {player.name} starts now... Press 'Enter'.")
        
        while player.alive:
            
            computer = game.createPykemon()
            print (f"Oh, no!!! Wild {computer.name} has approached.")
            computer.showStats()
            
            while player.alive and computer.alive:
                game.battle(player,computer)
                
                if player.alive and computer.alive:
                    player.showStats()
                    computer.showStats()
                    print("\n-----------------------------------------------------------------------------")
                
            if player.alive:
                game.battlesWon += 1

        print (f"\nPoor {player.name} has fainted...")
        print (f"\nBut it won {game.battlesWon} battle(s).")
        
        choice = input ("Do you want to play again (y/n): ")
        if choice != 'y':
            playing = False
    
    
main()