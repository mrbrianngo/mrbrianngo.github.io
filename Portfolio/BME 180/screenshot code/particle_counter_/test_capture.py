from capture import Capture

if __name__ == "__main__":
    cap = Capture((100, 120, 800, 600))
    cap.grab().save("test.png")
    print("screenshot saved")