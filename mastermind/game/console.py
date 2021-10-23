import random

class Console:
    """A code template for a computer console. The responsibility of this 
    class of objects is to get text or numerical input and display text output.
    
    Stereotype:
        Irformation Holder
        Service Provider, Interfacer

    Attributes:
        prompt (string): The prompt to display on each line.
        text(integer): The four digits number inputed (required) for the player.
    """
     
    def read(self, prompt):
        """Gets text input from the user through the screen.

        Args: 
            self (Screen): An instance of Screen.
            prompt (string): The prompt to display to the user.
           
        Returns:
            string: The user's input as text.
        """
        return input(prompt)

    def read_number(self, prompt):
        """Gets numerical input from the user through the screen.

        Args: 
            self (Screen): An instance of Screen.
            prompt (string): The prompt to display to the user.
           

        Returns:
            integer: The user's input as an integer of four digits specifically.
        """
        return int(input(prompt))
        
    def write(self, text):
        """Displays the given text as integer on the screen. 

        Args: 
            self (Screen): An instance of Screen.
            text (integer): The four digits number(required) to display as a text.
        """
        print(text)