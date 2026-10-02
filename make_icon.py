"""Draws the 1024x1024 app icon (icon.png) used for the developer apps."""
from PIL import Image, ImageDraw, ImageFont

S = 1024
img = Image.new("RGB", (S, S), "#141312")
d = ImageDraw.Draw(img)
font = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 300)
text = "NOM"
box = d.textbbox((0, 0), text, font=font)
w, h = box[2] - box[0], box[3] - box[1]
d.text(((S - w) / 2 - box[0], (S - h) / 2 - box[1] - 40), text, font=font, fill="#ece8e0")
# level-meter bars under the name
x0, bar, gap = (S - (9 * 44 + 8 * 20)) / 2, 44, 20
for i, lvl in enumerate([0.35, 0.6, 0.85, 1.0, 0.7, 0.9, 0.5, 0.75, 0.4]):
    x = x0 + i * (bar + gap)
    top = 800 - 110 * lvl
    d.rounded_rectangle([x, top, x + bar, 800], radius=10, fill="#f0a63a")
img.save("icon.png")
