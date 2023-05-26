import time
import Core.Game.Logger

MainLogger = Core.Game.Logger.Logger(
    True, 
    open(f"Logs/{time.ctime()}.txt".replace(":", " "), "a+").write)
MainLogger("Start Logger")