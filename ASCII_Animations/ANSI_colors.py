import os

os.system("cls")

COLORS = {
    "black": "\u001b[30;1m",
    "red": "\u001b[31;1m",
    "green": "\u001b[32m",
    "yellow": "\u001b[33;1m",
    "blue": "\u001b[34;1m",
    "magenta": "\u001b[35m",
    "cyan": "\u001b[36m",
    "white": "\u001b[37m",
    "yellow-background": "\u001b[43m",
    "black-background": "\u001b[40m",
    "cyan-background": "\u001b[46;1m",
    "bright-black": "\u001b[30;1m",
    "bright-red": "\u001b[31;1m",
    "bright-green": "\u001b[32;1m",
    "bright-yellow": "\u001b[33;1m",
    "bright-blue": "\u001b[34;1m",
    "bright-magenta": "\u001b[35;1m",
    "bright-cyan": "\u001b[36;1m",
    "bright-white": "\u001b[37;1m",
    "reset": "\u001b[0m",
}


def colorText(text):
    for color in COLORS:
        text = text.replace("[[" + color + "]]", COLORS[color])
    return text


f = open("img/3.txt", "r")
ascii = "".join(f.readlines())
print(colorText(ascii))

f.close()
