import Race
import Constants.Race

class Actor:
    def __init__(
            self,
            name: str,
            race: Race.Race,
            ):
        self.name = name
        self.race = race

if __name__ == "__main__":
    player = Actor("Rance", Constants.Race.Elf)
    print(player.__dict__)

