import time
import Core.Game.Logger



MainLogger = Core.Game.Logger.Logger(
    True, 
    open(f"Logs/{time.ctime()}.txt".replace(":", " "), "a+").write)

for _ in range(10):
    time.sleep(0.8)
    MainLogger(time.ctime(), "Start logger")
MainLogger.close()
















