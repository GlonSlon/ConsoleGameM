import sys, os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(os.path.split(SCRIPT_DIR)[0]))

from Core.Constants.Requarement_Bonuses import requarement_bonuses



class Race:
    def __init__(self, name:str, **bonuses):
        self.name = name
        self.__bonuses = {}
        if not all(map(lambda x: x in requarement_bonuses, bonuses)):
            raise ValueError("Bonuses and requarement_bonuses do not match!")
        self.__bonuses = bonuses
        
    





        
if __name__ == "__main__":
    elf = Race("Ельф",
               MP=2,
               HP=0.7,
               stamina=1.7)
    print(elf)
