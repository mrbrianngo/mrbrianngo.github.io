import mss, PIL.Image

class Capture:
    def __init__(self, region):
        self.region = region
        self.sct = mss.mss()

    def grab(self):
        raw = self.sct.grab(self.region)
        return PIL.Image.frombytes("RGB", raw.size, raw.rgb)