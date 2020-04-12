import os
import time
import requests
from bs4 import BeautifulSoup

os.system("cls")

print("WORLDWIDE CASES\n")

def loading():
    for x in range(0, 5):
        b = "Loading" + "." * x
        print(b, end="\r")
        time.sleep(0.5)


url = "https://www.worldometers.info/coronavirus/"
loading()
r = requests.get(url)
s = BeautifulSoup(r.text, 'html.parser')


data = s.find_all('div', class_='maincounter-number')


print("\u001b[37mTotal Cases :", "\u001b[33;1m" +
      data[0].text.strip() + "\u001b[0m")
print("\u001b[37mTotal Deaths :", "\u001b[31;1m" +
      data[1].text.strip() + "\u001b[0m")
print("\u001b[37mTotal Recovered :", "\u001b[32;1m" +
      data[2].text.strip() + "\u001b[0m")
