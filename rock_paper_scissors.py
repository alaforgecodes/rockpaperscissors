#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

"""The Player class is the parent class for all of the Players
in this game"""

import random
import time 
moves = ['rock', 'paper', 'scissors']


# class ANSI:
#     def human_player_color(self, player_name):
#         player_name = "\033[1;32m".player_name.
#         return player_name
    #Hunter = red, Amity = pink, Lux = purple, Gus = cyan, player = green


#Makes text appear at a reasonable speed and spacing between lines to make it easier to read
def text_pacing(text):
    print(text)
    print("")
    time.sleep(2)


#Function determines which move wins each round
def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


#Basic Player Class that only ever plays "Rock"
class Player:
    def __init__(self):
        self.score = 0
    
    #Method for adding to player's score
    def score(self):
        self.score += 1

    def name(self):
        return "Hunter"

    #Method determining opponent's move
    def move(self):
        return "rock"

    #Method allowing opponent to learn from previous round
    def learn(self, my_move, their_move):
        pass


#Player Subclass that randomly chooses its move each round
class RandomPlayer(Player):
    def name(self):
        return "Amity"
    #Method determining opponent's move
    def move(self):
        move = random.choice(moves)
        return move 


#Player Subclass that copies its opponent's move and plays it in the following round
class ReflectPlayer(Player):
    #Method determining opponen'ts name
    def name(self):
        return "Gus"

    #Method determining opponent's move
    def move(self):
        move = random.choice(moves)
        return move
    
    #Method allowing opponent to learn from previous round
    def learn(self, my_move, their_move):
        self.move = their_move
        return self.move


#Player Subclass that cycles through all possible move choices
class CyclePlayer(Player): 
    def name(self):
        return "Luz"

    #Method determining opponent's move
    def move(self):
        if self.my_move == "rock":
            return "paper"
        elif self.move == "paper":
            return "scissors"
        elif self.move == "scissors":
            return "rock"

    #Method allowing opponent to learn from previous round
    def learn(self, my_move, their_move):
        self.my_move = my_move


#Subclass that selects from the CPU players for the human player to play against   
class OpponentChoice(Player):
    opponents = [Player(), 
                 RandomPlayer(), 
                 ReflectPlayer(), 
                 CyclePlayer()]

    opponent = random.choice(opponents)

    #Method that applies name to CPU player
    def name(self):
        return self.opponent.name()

    #Method determining opponent's move
    def move(self):
        return self.opponent.move()
    
    #Method allowing opponent to learn from previous round
    def learn(self, my_move, their_move):
        self.opponent.learn(my_move, their_move)


#Player Subclass that allows a human to play the game
class HumanPlayer(Player):
    #Method allowing human player to enter their name
    def name(self):
        name = input("Please submit your name to enter the tournament.\n")
        return name

    #Method allowing human player to input move choice
    def move(self):
        move = input("What move will you make? (Please enter Rock, Paper, or Scissors.)\n")
        if move.lower() in ["rock", "paper", "scissors"]:
            return move
        else:
            text_pacing("I'm sorry, I don't understand that.")
            move = input("Please enter Rock, Paper, or Scissors. \n")
            return move


#Class containing all gameplay
class Game:
    #Method initializing two players for game
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    #Method containing intro text to game
    def game_intro(self, player_name, opponent_name):
        print("")
        text_pacing("Welcome to the Rock, Paper, Scissors Championship!")
        text_pacing(f"Our players for this round will be {player_name} and {opponent_name}.")
        text_pacing("Let's begin!")

    #Method that plays a round of Rock, Paper, Scissors
    def play_round(self, player_name, opponent_name):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print("")
        text_pacing(f"{player_name} chose {move1}.\n"
                    f"{opponent_name} chose {move2}.")
        if beats(move1, move2):
            Player.score(self.p1)
            text_pacing(f"{player_name} wins!")
        elif beats(move2, move1):
            Player.score(self.p2)
            text_pacing(f"{opponent_name} wins!")
        else:
            print("It's a tie!")
        text_pacing(f"{player_name}'s Score: {self.p1.score} \n"
                    f"{opponent_name}'s Score: {self.p2.score}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    #Method that tallies final scores and announces the winner of the tournament
    def end_game(self, player_name, opponent_name):
        text_pacing("Game over! Time to determine the winner.")
        print("Final Scores:")
        text_pacing(f"{player_name}: {self.p1.score} \n"
                    f"{opponent_name}: {self.p2.score}")
        if self.p1.score > self.p2.score:
            text_pacing(f"{player_name} is our champion!!!")
        elif self.p1.score < self.p2.score:
            text_pacing(f"{opponent_name} is our champion! "
                        "Better luck next time.")
        else:
            text_pacing("It's a tie! You'll have to try again if you want "
                        "to be champion.")
        text_pacing("Thank you for playing. We hope you enter the tournament again!")

    #Method that starts the Rock, Paper, Scissors tournament
    def play_game(self):
        player_name = HumanPlayer.name(self)
        opponent_name = OpponentChoice.name(self.p2)
        Game.game_intro(self, player_name, opponent_name)       
        for round in range(1, 4):
            text_pacing(f"Round {round}:")
            self.play_round(player_name, opponent_name)
        Game.end_game(self, player_name, opponent_name)

#Footer
if __name__ == '__main__':
    game = Game(HumanPlayer(), OpponentChoice())
    game.play_game()