import Classes
import Functions.Printing as Printing

winning = Classes.Event.Event(
    [print, "\n"*40],
    [Printing.printf, [25, "You are lose."]],
    [Printing.printf, [25, "Your team is dead."]],
    [Printing.printf, [1, "..."]],
    [Printing.printf, [25, "But you can turn back time."]]
)



stalemate = None



lose = None


if __name__ == "__main__":
    winning.start()
