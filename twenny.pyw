from win10toast import ToastNotifier
import time

SHOW_EVERY = 60 * 20  # 20 minutes
LOOK_AWAY_DURATION = 20
CONTINUE_DURATION = 5

starttime = time.time()
toaster = ToastNotifier()


def start():
    toaster.show_toast("twenny", "It's time, look away for 20 seconds!", duration=LOOK_AWAY_DURATION)
    toaster.show_toast("twenny", "You can continue working now!", duration=CONTINUE_DURATION)
    

while True:
    start()
    time.sleep(SHOW_EVERY - ((time.time() - starttime) % SHOW_EVERY))
    