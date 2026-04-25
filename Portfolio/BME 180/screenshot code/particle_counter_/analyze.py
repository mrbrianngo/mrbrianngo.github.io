from ultralytics import YOLO

class ParticleAnalyzer:
    def __init__(self, model_path, conf=0.2):
        self.model = YOLO(model_path)
        self.conf = conf

    def analyze(self, img):
        results = self.model(img, conf=self.conf, verbose=False)
        boxes = results[0].boxes
        particles = []
        for b in boxes:
            x1, y1, x2, y2 = map(float, b.xyxy[0])
            w, h = x2 - x1, y2 - y1
            particles.append({
                "x_px": x1, "y_px": y1,
                "width_px": w, "height_px": h,
                "area_px": w * h,
                "score": float(b.conf[0]),
                "class": int(b.cls[0])
            })
        return particles