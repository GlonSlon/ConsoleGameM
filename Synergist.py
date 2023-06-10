import Core.Game.SaveLoader

import Core.Game.Logger

from Core.Functions.Printing import printf

MainSaveLoader = Core.Game.SaveLoader.SaveLoader("./saves", "save", MainLogger)

data = {1:2, 3:4, "oleg": "pidor"}

MainSaveLoader.Save("test", data)

data2 = MainSaveLoader.Load("test")

print(10, 1, data2)


MainLogger = Core.Game.Logger.Logger()

MainLogger("Game Succsesfuly ended")
MainLogger("Close Logger")
MainLogger.close()








