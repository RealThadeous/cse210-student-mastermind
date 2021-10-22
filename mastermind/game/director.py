"""This imports all codes from board.py"""

from game.board import Board  

 """This imports all console from game.console"""
from game.console import Console 

 """This imports allnumber of players from game.player"""
from game.player import Player

"""This imports all roster code from game.roster"""
from game.roster import Roster  

 """This imports check codes from game.check"""
from game.check import Check    

 """This imports  clear screen from game.clear_screen"""
from game.board import Board
from game.console import Console
from game.player import Player
from game.roster import Roster
from game.check import Check
from game.clear_screen import ClearScreen
import os


file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)


class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        _board (Board): An instance of the class of objects known as Board.
        __console (Console): An instance of the class of objects known as Console.
        __keep_playing (boolean): Whether or not the game can continue.
        __roster (Roster): An instance of the class of objects known as Roster.
        __check (Check): An instasnce of the class of objects known as Check.
        __number_of_players (int): The number of players in the game.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self._board = Board()
        self.__console = Console()
        self.__keep_playing = True
        self.__roster = Roster()
        self.__check = Check()
        self.__cls = ClearScreen()
        self.__number_of_players = 3

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        self._prepare_game()
        while self.__keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _prepare_game(self):
        """Prepares the game before it begins. In this case, that 
        means getting the player names and adding them to the roster.
        
        Args:
            self (Director): An instance of Director.
            the for loop below asks for name of player and lists them on the board.
        """
        for n in range(self.__number_of_players):
            name = self.__console.read(f"Enter a name for player {n + 1}: ")
            self._player = Player(name)
            self.__roster.add_player(name)
            self._board._prepare(name)

    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the move from the current player.

        Args:
            self (Director): An instance of Director.
        """
        # display the game board
        board = self._board.to_string()

        player = self.__roster.get_current()

        while True:
            self.__cls.clear_screen()
            self.__console.write(board)
            self.__console.write(f"{player}'s turn:")
            guess = self.__console.read("What is your guess? ")
            if self.__check._check_input(guess):
                break

        code = self._board._items[player][0]

        self._hint = self._board._create_hint(code, guess)
        self._board._items[player] = [str(code), str(guess), self._hint]

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means updating the board with the current move.

        Args:
            self (Director): An instance of Director.
        """
        self._board.apply_hint(self.__roster.get_current(), self._hint)

    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if there are stones left and declaring 
        the winner.

        Args:
            self (Director): An instance of Director.
        """
        if self.__check._compare_codes(self.__roster.get_current(), self._board):
            winner = self.__roster.get_current()
            print(f"\n{winner} won!")
            self.__keep_playing = False
        self.__roster.next_player()