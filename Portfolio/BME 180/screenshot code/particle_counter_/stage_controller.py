import serial, time, logging

class StageController:
    def __init__(self, port, baud):
        self.ser = serial.Serial(port, baud, timeout=1)
        time.sleep(2)           # allow Arduino reset
        logging.info("Serial open")

    def _send(self, c: str):
        self.ser.reset_input_buffer()
        self.ser.write(c.encode())

    def _wait_done(self):
        while True:
            line = self.ser.readline().decode("ascii", errors="ignore").strip()
            if line.startswith("Done"):
                return line

    def move(self, cmd, n=1):
        for _ in range(n):
            self._send(cmd)
            self._wait_done()

    def snake_scan(self, rows_fwd, rows_back, columns):
        for col in range(columns):
            # choose direction by column parity
            if col % 2 == 0:
                for _ in range(rows_fwd): yield ("F", 1)
            else:
                for _ in range(rows_back): yield ("D", 1)
            yield ("L", 1)           # shift one column left
        yield ("R", 1)               # return to origin column
        yield ("X", 1)               # return to origin row