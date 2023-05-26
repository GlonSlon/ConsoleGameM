import Functions.Printing
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
        [Printing.printf, [12, 'testtesttesttesttesttesttesttesttesttesttesttesttesttesttesttest', [1,2,3]]]
    )
    
    someEvent.start()