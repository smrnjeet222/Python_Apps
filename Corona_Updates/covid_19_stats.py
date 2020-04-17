import requests
import re
import os
import ctypes

kernel32 = ctypes.WinDLL('kernel32')
user32 = ctypes.WinDLL('user32')

SW_MAXIMIZE = 3

hWnd = kernel32.GetConsoleWindow()
user32.ShowWindow(hWnd, SW_MAXIMIZE)

C = {
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

os.system("cls")

print(C['bright-cyan'] + r'''
           ________   ________   ___      ___  ___   ________                  _____   ________          ________   _________   ________   _________   ________      
          |\   ____\ |\   __  \ |\  \    /  /||\  \ |\   ___ \                / __  \ |\  ___  \        |\   ____\ |\___   ___\|\   __  \ |\___   ___\|\   ____\     
          \ \  \___| \ \  \|\  \\ \  \  /  / /\ \  \\ \  \_|\ \   _________  |\/_|\  \\ \____   \       \ \  \___|_\|___ \  \_|\ \  \|\  \\|___ \  \_|\ \  \___|_    
           \ \  \     \ \  \\\  \\ \  \/  / /  \ \  \\ \  \ \\ \ |\_________\\|/ \ \  \\|____|\  \       \ \_____  \    \ \  \  \ \   __  \    \ \  \  \ \_____  \   
            \ \  \____ \ \  \\\  \\ \    / /    \ \  \\ \  \_\\ \\|_________|     \ \  \   __\_\  \       \|____|\  \    \ \  \  \ \  \ \  \    \ \  \  \|____|\  \  
             \ \_______\\ \_______\\ \__/ /      \ \__\\ \_______\                 \ \__\ |\_______\        ____\_\  \    \ \__\  \ \__\ \__\    \ \__\   ____\_\  \ 
              \|_______| \|_______| \|__|/        \|__| \|_______|                  \|__| \|_______|       |\_________\    \|__|   \|__|\|__|     \|__|  |\_________\
                                                                                                            \|_________|                                  \|_________|
                                                        Track COVID-19 stats from command line   
                                                                STAY HOME , STAY SAFE!  
                                                                                                                                                              
                                                                  -Simranjeet Singh                                                                                                                            
'''+C['reset'])


def Stats():
    url = "https://corona.lmao.ninja/v2/all"
    req = requests.get(url).json()

    print(C['bright-green']+"\t\t\t_________________WORLDWIDE CASES______________________\n")
    for k, v in req.items():
        if k != "updated":
            _key = str(k).capitalize()
            _value = str(v).capitalize()

            print('\t\t\t\t \u001b[33;1m{:<25} : \u001b[31;1m{:<10}'.format(_key, _value) + C['reset'])
    return


def Countries():
    url = 'https://corona.lmao.ninja/v2/countries'
    req = requests.get(url).json()

    print(C['bright-yellow']+C['cyan-background']+"\n\t\t| {:<34}|  {:<13}|  {:<13}|  {:<13}|  {:<13}|  {:<13}|  {:<13}| {:<20}|".format('Country', 'Cases',
                                                                                                 'TodayCases', 'Deaths', 'TodayDeaths', 'Recovered', 'Critical', 'CasesPerOneMillion') + C['reset']+ "\n")

    for col in req:
        a = str(col['country'])[:35]
        b = str(col['cases'])
        c = str(col['todayCases'])
        d = str(col['deaths'])
        e = str(col['todayDeaths'])
        f = str(col['recovered'])
        g = str(col['critical'])
        h = str(col['casesPerOneMillion'])

        print("\t\t\u001b[33;1m| \u001b[35;1m{:<34}\u001b[33;1m|\u001b[31;1m  {:<13}\u001b[33;1m|\u001b[31;1m  {:<13}\u001b[33;1m|\u001b[31;1m  {:<13}\u001b[33;1m|\u001b[31;1m  {:<13}\u001b[33;1m|\u001b[31;1m  {:<13}\u001b[33;1m|\u001b[31;1m  {:<13}\u001b[33;1m|\u001b[31;1m  {:<19}\u001b[33;1m|".format(
            a, b, c, d, e, f, g, h) + C['reset'])


def sort(x):
    url = (f"https://corona.lmao.ninja/v2/countries?sort={x}")
    req = requests.get(url).json()

    print(C['bright-yellow']+C['cyan-background']+"\n\t\t| {:<34}|  {:<13}|  {:<13}|  {:<13}|  {:<13}|  {:<13}|  {:<13}| {:<20}|".format('Country', 'Cases',
                                                                                                 'TodayCases', 'Deaths', 'Active', 'Recovered', 'Critical', 'CasesPerOneMillion') + C['reset']+ "\n")
    for col in req:
        a = str(col['country'])[:35]
        b = str(col['cases'])
        c = str(col['todayCases'])
        d = str(col['deaths'])
        e = str(col['active'])
        f = str(col['recovered'])
        g = str(col['critical'])
        h = str(col['casesPerOneMillion'])

        print("\t\t\u001b[33;1m| \u001b[35;1m{:<34}\u001b[33;1m|\u001b[31;1m  {:<13}\u001b[33;1m|\u001b[31;1m  {:<13}\u001b[33;1m|\u001b[31;1m  {:<13}\u001b[33;1m|\u001b[31;1m  {:<13}\u001b[33;1m|\u001b[31;1m  {:<13}\u001b[33;1m|\u001b[31;1m  {:<13}\u001b[33;1m|\u001b[31;1m  {:<19}\u001b[33;1m|".format(
            a, b, c, d, e, f, g, h) + C['reset'])


def findCountry(x):
    url = (f"https://corona.lmao.ninja/v2/countries/{x}?strict=false")
    req = requests.get(url).content.decode('utf-8')
    if req:
        check = re.search(r'Country not found', req)
        if check:
            print("\t\t\tCountry not found")
        else:
            _p = requests.get(url).json()
            for k, v in _p.items():
                if k != 'countryInfo' and k != "updated":
                    i = str(k).capitalize()
                    print('\t\t\t\u001b[33;1m{:<25}: \u001b[31;1m{:<10}'.format(i, str(v)))
    else:
        print("ERROR")


def getCountry():
    ip = requests.get("https://ident.me/").content.decode('utf-8')
    url = (f"https://tools.keycdn.com/geo.json?host={ip}")
    result = requests.get(url).json()
    search = result['data']['geo']['country_name']
    if search:
        print(C['bright-green']+ f"\n\t\t\tIt looks like you are in {search}.")
        print('\t\t\tHere are the stats related to your country.\n\t\t\t(If this prediction is incorrect use option "3")\n' + C['reset'])
        findCountry(search)
    else:
        print(C['bright-green']+ '\n\t\t\tWe are unable to locate your country. Please use option "3" to manually search your country' + C['reset'])


Stats()
getCountry()

while True:
    try:
        print((C['bright-green']+'\n\t\t\tPress "1" to list stats related to all countries.\n\t\t\tPress "2" to sort countries list according to a given key.\n\t\t\tPress "3" to check stats realated to your country.\n\t\t\tPress any key to exit' + C['reset']))
        x = int(input(C['bright-green']+"\n\t\t\t>>>>  " + C['reset']))
        if x == 1:
            Countries()
        if x == 2:
            print(C['bright-green']+"\n\t\t\tSelect any key to sort" + C['reset'])
            print(C['bright-green']+"\n\t\t\tKeys:- Country, Cases, Active, Critical, Deaths, Recovered, TodayCases, CasesPerOneMillion\n"  + C['reset'])
            y = str(input(C['bright-green']+"\n\t\t\t>>>>  " + C['reset'])).lower()
            if y == "country":
                sort(x=y)
            if y == "cases":
                sort(x=y)
            if y == "active":
                sort(x=y)
            if y == "critical":
                sort(x=y)
            if y == "deaths":
                sort(x=y)
            if y == "recovered":
                sort(x=y)
            if y == "todaycases":
                sort(x=y)
            if y == "todaydeaths":
                sort(x=y)
            if y == "casesperonemillion":
                sort(x=y)

        if x == 3:
            t = str(input(C['bright-green']+"\n\t\t\tEnter your country name: " + C['reset']))
            print("\n", end='')
            findCountry(t)

        else:
            break

    except KeyboardInterrupt:
        print(C['bright-green']+"\n\t\t\tProgramme Interrupted" + C['reset'])
