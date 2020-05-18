import os
import time
os.system('cls')

filenames = ["img/img1.txt", 'img/img2.txt',"img/img3.txt","img/img4.txt","img/img5.txt","img/img6.txt","img/img7.txt","img/img8.txt"]


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


animate(filenames, 0, 10)
