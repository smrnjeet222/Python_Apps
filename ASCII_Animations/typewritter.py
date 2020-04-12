import sys
import time
import os

msg = "Hello, this is Jarvis! \nNice to meet YOU :-)\n"


def typewriter(msg):
    for x in range(0, 5):
        b = "Loading" + "." * x
        print(b, end="\r")
        time.sleep(0.5)
        sys.stdout.write("\033[K")  # clear line

    for char in msg:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char != "\n":
            time.sleep(0.1)
        else:
            time.sleep(0.6)


os.system("cls")

typewriter(msg)
