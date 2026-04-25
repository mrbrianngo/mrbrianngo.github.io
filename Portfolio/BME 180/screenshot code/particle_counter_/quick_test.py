from analyze import ParticleAnalyzer
from PIL import Image

if __name__ == "__main__":
    model = ParticleAnalyzer("models/best306.pt")
    img   = Image.open("/Users/isaachoyt/Documents/Spring 2025/BME 180C/Training Data/TitaniumParticlesNoPolarizer/99.jpg")
    for i, box in enumerate(model.analyze(img), 1):
        print(i, {k: round(box[k], 1) for k in ("x_px","y_px","width_px","height_px","score")})

