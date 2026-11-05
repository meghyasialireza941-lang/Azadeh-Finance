# Puts the logo directly into the Android launcher icon slots (full image, no margin, no zoom)
import os, shutil
from PIL import Image

res = "android/app/src/main/res"
sizes = {"mdpi": 48, "hdpi": 72, "xhdpi": 96, "xxhdpi": 144, "xxxhdpi": 192}
src = Image.open("assets/icon.png").convert("RGBA")

# remove adaptive icon definitions so the plain full-bleed image is used
shutil.rmtree(os.path.join(res, "mipmap-anydpi-v26"), ignore_errors=True)

for name, px in sizes.items():
    d = os.path.join(res, "mipmap-" + name)
    os.makedirs(d, exist_ok=True)
    img = src.resize((px, px), Image.LANCZOS)
    for f in ("ic_launcher.png", "ic_launcher_round.png", "ic_launcher_foreground.png"):
        img.save(os.path.join(d, f))
print("icons done")
