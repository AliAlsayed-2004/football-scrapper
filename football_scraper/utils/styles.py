from colorama import Fore, Style
import random
from typing import Optional
import pyfiglet
import os


class Colors:
    """
    A collection of color and style constants for terminal output using colorama.
    Includes bright and light variants for various colors, as well as a reset style.
    Also provides lists of all color codes and available fonts for CLI styling.
    """
    RED = Style.BRIGHT + Fore.RED
    MAG = Style.BRIGHT + Fore.MAGENTA
    BLU = Style.BRIGHT + Fore.BLUE
    CYA = Style.BRIGHT + Fore.CYAN
    GRE = Style.BRIGHT + Fore.GREEN
    YEL = Style.BRIGHT + Fore.YELLOW
    LRED = Style.BRIGHT +  Fore.LIGHTRED_EX
    LMAG = Style.BRIGHT +  Fore.LIGHTMAGENTA_EX
    LBLU = Style.BRIGHT +  Fore.LIGHTBLUE_EX
    LCYA = Style.BRIGHT +  Fore.LIGHTCYAN_EX
    LGRE = Style.BRIGHT +  Fore.LIGHTGREEN_EX
    LYEL = Style.BRIGHT +  Fore.LIGHTYELLOW_EX
    ENDC = Style.RESET_ALL

    COLORS = [RED, MAG, BLU, CYA, GRE, YEL, LRED, LMAG, LBLU, LCYA, LGRE, LYEL]
    
    FONTS = (
        "basic", "o8", "cosmic", "graffiti", "chunky", "epic",
        "poison", "doom", "avatar", "slant", "speed", "blocks",
        "big_money-ne", "big", "coinstak", "dancing_font",
        "georgia11", "roman", "slant_relief", "univers",
        "varsity", "banner3-D"
    )
    

class CliStyle:
    """
    Provides CLI styling utilities, including random color/font selection and
    methods for printing a stylized logo and GitHub contact info in the terminal.
    Uses pyfiglet for ASCII art and colorama for colored output.
    """
    def __init__(self):
        self.colors = Colors.COLORS
        self.fonts = Colors.FONTS
        self._terminal_width = os.get_terminal_size().columns  
        self.name = "Football Scraper"
        self.github = "https://github.com/AliAlsayed-2004" 

    def get_font(self):
        return random.choice(self.fonts)

    def get_color(self):
        return random.choice(self.colors)
    

    
    def print_logo(self, name: Optional[str] = None, 
                 github: Optional[str] = None) -> None:
        """
        Print a stylized logo with contact information.
        
        Args:
            name (str, optional): Override default name
            github (str, optional): Override default GitHub info
        """
        # Use provided values or fall back to defaults
        display_name = name or self.name
        display_github = github or self.github


        # Print separator
        separator = f"{random.choice(self.colors)}{('=' * (self._terminal_width)).center(self._terminal_width)}"
        print(f"{separator}\n\n", end="")

        # Generate and print logo
        logo_text = pyfiglet.figlet_format(
            display_name, 
            font=random.choice(self.fonts), 
            justify="center", 
            width=self._terminal_width
        )
        print(f"{random.choice(self.colors)}{logo_text}\n", end="")

        # Print contact info
        print(f"{random.choice(self.colors)}{('[+] GitHup =>  ' + display_github).center(self._terminal_width)}", end="")

        print(f"{separator}\n\n", end="")

