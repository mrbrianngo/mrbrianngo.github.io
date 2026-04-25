
from ultralytics import YOLO
from PIL import Image

model = YOLO("/Users/isaachoyt/Documents/Spring 2025/BME 180C/particle_counter:/models/best306.pt")
img_path = "/Users/isaachoyt/Documents/Spring 2025/BME 180C/Training Data/TitaniumParticlesNoPolarizer/99.jpg"

result = model(img_path, conf=0.25, verbose=False)[0]
boxed  = Image.fromarray(result.plot())   # draw boxes
boxed.save("99_annotated.png")
print("saved 99_annotated.png")
