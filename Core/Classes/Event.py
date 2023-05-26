import sys, os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(os.path.split(SCRIPT_DIR)[0]))

from Core.Functions.Printing import printf
class Event:
    def __init__(self, *comands):
        self.comands = comands
        for comand in self.comands:
            if len(comand) == 2:
                comand.append({})

    def start(self):
        for comand in self.comands:
            comand[0](*comand[1], **comand[2])



if __name__ == "__main__":

    someEvent = Event(
        [print, ["test", 23, [1,2,3]], {}],
        [printf, [12, 'testtesttesttesttesttesttesttesttesttesttesttesttesttesttesttest', [1,2,3]]]
    )
    
    someEvent.start()


    