import bs4 
import requests

def GetProductPrice(myURL):
    
    res = requests.get(myURL)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    elems = soup.select('#container > div > div.t-0M7P._3GgMx1._2doH3V > div._3e7xtJ > div._1HmYoV.hCUpcT > div._1HmYoV._35HD7C.col-8-12 > div:nth-child(2) > div > div._3iZgFn > div._2i1QSc > div > div._1vC4OE._3qQ9m1')
    return elems[0].text.strip()


pixel3a = GetProductPrice("https://www.flipkart.com/google-pixel-3a-just-black-64-gb/p/itmfgk4jfgstaack?pid=MOBFFGFP7UHHJUZU&srno=b_1_1&otracker=nmenu_sub_Electronics_0_Pixel%203a%20%7C%203a%20XL&lid=LSTMOBFFGFP7UHHJUZUW7182D&fm=organic&iid=30f28682-2983-4253-ad1e-eb4d85e32057.MOBFFGFP7UHHJUZU.SEARCH&ppt=browse&ppn=browse&ssid=fhgv0ra03k0000001563211605602")

print (f'The Price of pixel 3a is {pixel3a}')

earphones = GetProductPrice("https://www.flipkart.com/boult-audio-bassbuds-oak-pure-wood-wired-headset-mic/p/itmff6zuhs466vca?pid=ACCFF6ZUBWXXDWZK&otracker=wishlist&lid=LSTACCFF6ZUBWXXDWZKMMQTES&fm=organic&iid=1d68a7f1-be67-4e73-b6a9-d37fbe61979e.ACCFF6ZUBWXXDWZK.PRODUCTSUMMARY&ppt=hp&ppn=hp")

print (f'The price of boult earphones is {earphones}')

sdcard = GetProductPrice("https://www.flipkart.com/sandisk-ultra-32-gb-microsdhc-class-10-98-mb-s-memory-card/p/itmeweghhhsdptty?pid=ACCEWEGHFTJ3G4ZG&otracker=wishlist&lid=LSTACCEWEGHFTJ3G4ZGCDXIVY&fm=organic&iid=7c6fc72e-0b57-464b-9fa4-c2b6d896cd88.ACCEWEGHFTJ3G4ZG.PRODUCTSUMMARY&ppt=hp&ppn=hp")

print(f'The Price of sd card is {sdcard}')

UCBShoes = GetProductPrice("https://www.flipkart.com/united-colors-benetton-espadrilles-men/p/itmf3yyguydgkpqa?pid=SHOEV3TZTZXGC4SM&otracker=wishlist&lid=LSTSHOEV3TZTZXGC4SMGL7DEV&fm=organic&iid=4396fe3d-c0cd-4971-a13e-3fb36bfdb084.SHOEV3TZTZXGC4SM.PRODUCTSUMMARY&ppt=hp&ppn=hp")

print(f'The Price of UCB espadrilles is {UCBShoes}')

