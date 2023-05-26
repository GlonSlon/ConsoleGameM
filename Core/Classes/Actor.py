import sys, os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(os.path.split(SCRIPT_DIR)[0]))

import Race
import Core.Constants.Race

class Actor:
    def __init__(
            self,
            name: str,
            race: Race.Race,
            ):
        self.name = name
        self.race = race

if __name__ == "__main__":
    player = Actor("Rance", Core.Constants.Race.Elf)
    print(player.__dict__)

