#!/usr/bin/env python

import pandas as pd
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

from sendMail import sendMail
from config import CER_PATH, DATA_PATH
import os

BASE_DIR = os.getcwd()


def createDic(df, lst):
    dic = {}
    for (n, e), rest in df.groupby(lst):
        dic[e] = n.lower().replace(' ', '_')

    return dic


def drawName(msg, fnt='bahnschrift', fnt_sz=45, show=False):
    img = Image.open(os.path.join(BASE_DIR, CER_PATH))
    img_draw = ImageDraw.Draw(img)
    W, H = img.size

    font = ImageFont.truetype(
        f"C:/Users/System-Pc/Desktop/{fnt}.ttf", fnt_sz)

    w, h = font.getsize(msg)

    img_draw.text(((W-w)/2, (H-h)/2 + 60),
                  msg.replace("_", " ").title(), fill='black', font=font)
    if show:
        img.show()
    else:
        op = os.path.join(BASE_DIR, 'output')
        os.makedirs(op, exist_ok=True)
        img.save(os.path.join(
            BASE_DIR, f'output/{msg.lower().replace(" ", "_")}.pdf'))


def run(m_data):
    for mail in m_data:
        name = m_data[mail]
        print(f"Processing...{name.upper()} : {mail}")

        drawName(name, show=False)
        sendMail(name, mail)


if __name__ == "__main__":
    try:
        df = pd.read_csv(os.path.join(os.getcwd(), DATA_PATH))
        mail_data = createDic(df, ['your-name', 'your-email'])
        run(mail_data)
    except:
        print("ERROR 404")
