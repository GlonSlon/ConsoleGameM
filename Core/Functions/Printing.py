import threading as th
import time
import keyboard as kb

def printf(speed:int, skip:bool, text:str, *args, **kwargs):
    is_done = False
    true_speed = 1/speed

    def printing():
        nonlocal text
        
        for symbol in text:
            nonlocal true_speed, is_done
            if true_speed:
                time.sleep(true_speed)
            print(symbol, end="", flush=True)
        print()

        is_done = True

    printing_thread = th.Thread(target=printing)

    printing_thread.start()
    while not is_done:
        kb.wait("enter")
        if skip:
            true_speed = 0


if __name__ == "__main__":
    printf(90, True, "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    printf(40, False, "-------------------------------------------------------------------")
    printf(10, True, "===================================================================")

























