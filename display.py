from smbus import SMBus
import math
import time
import backlight
import screen

class Display(object):
    backlight = None
    screen = None

    def __init__(self, bus):
        self.backlight = backlight.Backlight(bus, 0x62)
        self.screen    = screen.Screen(bus, 0x3e)

    def write(self, text):
        self.screen.write(text)

    def color(self, r, g, b):
        self.backlight.set_color(r, g, b)

    def move(self, col, row):
        self.screen.setCursor(col, row)

if __name__ == "__main__":
    cnt = 0

    d = Display(SMBus(1))
    d.move(0, 0)
    d.write("Yeah.      Nice.")

    while True:
        r = int((math.sin(cnt) + 1) * 128)
        g = int((math.sin(cnt + 0.75 * math.pi) + 1) * 128)
        b = int((math.sin(cnt + 1.5 * math.pi) + 1) * 128)

        d.color(r, g, b)

        # d.move(0, 1)
        # d.write("{:>3} {:>3} {:>3}".format(r, g, b))

        cnt += 0.01
        time.sleep(0.00001)
