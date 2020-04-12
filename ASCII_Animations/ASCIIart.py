import os
import time
os.system('cls')

filenames = ["img/1.txt", 'img/2.txt']


def animate(filenames, delay=0.5, repeat=10):
    frames = []

    for name in filenames:
        with open(name, "r", encoding="utf8") as f:
            frames.append(f.readlines())
    for _ in range(repeat):
        for frame in frames:
            print("".join(frame))
            time.sleep(delay)
            os.system('cls')


animate(filenames, 0.2, 10)
