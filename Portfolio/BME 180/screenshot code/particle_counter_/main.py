import csv, yaml, pathlib, time
from stage_controller import StageController
from capture import Capture
from analyze import ParticleAnalyzer

cfg = yaml.safe_load(open("config.yaml"))
outdir = pathlib.Path(cfg["output"]).absolute()
outdir.mkdir(parents=True, exist_ok=True)

stage  = StageController(cfg["serial"]["port"], cfg["serial"]["baud"])
cam    = Capture(tuple(cfg["capture"]["region"]))
anlz   = ParticleAnalyzer(cfg["model_path"])

csvfile = open(outdir / "particles.csv", "w", newline="")
writer = csv.DictWriter(csvfile,
          fieldnames=["img_id","x_px","y_px","width_px","height_px","area_px","score","class"])
writer.writeheader()

img_id = 0
for cmd, n in stage.snake_scan(**cfg["grid"]):
    stage.move(cmd, n)
    img = cam.grab()
    img.save(outdir / f"{img_id:04}.png")
    for p in anlz.analyze(img):
        p["img_id"] = img_id
        writer.writerow(p)
    img_id += 1
    time.sleep(0.1)          # allow vibrations to settle

csvfile.close()
print("Scan complete")