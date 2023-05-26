import threading as th
import time
import keyboard as kb

def printf(speed:int, text:str, *args, **kwargs):
    true_speed = 1/speed

    def printing():
        nonlocal text
        
        for symbol in text:
            nonlocal true_speed
            if true_speed:
                time.sleep(true_speed)
            print(symbol, end="", flush=True)
        print()

    printing_thread = th.Thread(target=printing)

    printing_thread.start()
    if "isSkip" in kwargs:
        if kwargs["isSkip"]:
            kb.wait("enter")
            true_speed = 0


if __name__ == "__main__":
    printf(35, "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    printf(25, "-------------------------------------------------------------------")
    printf(15, "===================================================================")











