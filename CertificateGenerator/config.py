MAIL = "testyoyo222@gmail.com"
PASS = "password"

DATA_PATH = "input/test_data.csv"
CER_PATH = "input/cer.jpg"

SUBJECT = "Certificate of participation in event organised by Illuminate society."


def body(name):
    return f"Greetings,\n{name.upper()} please find your event participation certificate attached with this mail.\n\nRegards,\nIlluminate Society\n\nThis is computer generated mail, don't reply."
