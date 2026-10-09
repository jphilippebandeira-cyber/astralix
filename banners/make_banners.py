import math, os
from PIL import Image, ImageDraw, ImageFont

OUT = os.path.dirname(os.path.abspath(__file__))
B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
R = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

NAVY = (7, 19, 27)
TEAL = (14, 122, 95)
EMER = (31, 176, 130)
WHITE = (255, 255, 255)
GOLD = (212, 162, 74)
MUTE = (168, 190, 198)


def f(path, size):
    return ImageFont.truetype(path, size)


def bg(w, h, cx=0.42, cy=0.55, spread=0.95):
    """Navy ground with a soft teal glow, like the brand cover."""
    img = Image.new("RGB", (w, h), NAVY)
    px = img.load()
    mx, my = w * cx, h * cy
    maxd = math.hypot(max(mx, w - mx), max(my, h - my)) * spread
    for y in range(h):
        for x in range(w):
            d = math.hypot(x - mx, y - my) / maxd
            t = max(0.0, 1.0 - d) ** 2.1
            px[x, y] = (
                int(NAVY[0] + (TEAL[0] - NAVY[0]) * t),
                int(NAVY[1] + (TEAL[1] - NAVY[1]) * t),
                int(NAVY[2] + (TEAL[2] - NAVY[2]) * t),
            )
    return img


def wordmark(d, x, y, size, anchor="ls"):
    """are (white) + IA (emerald), drawn as one lockup. Returns total width."""
    fb = f(B, size)
    w_are = d.textlength("are", font=fb)
    d.text((x, y), "are", font=fb, fill=WHITE, anchor=anchor)
    d.text((x + w_are, y), "IA", font=fb, fill=EMER, anchor=anchor)
    return w_are + d.textlength("IA", font=fb)


def pill(d, box, label, size):
    x0, y0, x1, y1 = box
    d.rounded_rectangle(box, radius=(y1 - y0) // 2, fill=EMER)
    d.text(((x0 + x1) / 2, (y0 + y1) / 2), label, font=f(B, size), fill=(5, 20, 16), anchor="mm")


def rule(d, x0, y, x1, color=GOLD, w=2):
    d.line([(x0, y), (x1, y)], fill=color, width=w)


def fit(d, text, path, start, maxw):
    """Largest font size at or below `start` whose text fits in maxw."""
    s = start
    while s > 7 and d.textlength(text, font=f(path, s)) > maxw:
        s -= 1
    return f(path, s)


def save(img, name):
    p = os.path.join(OUT, name)
    img.save(p, "PNG", optimize=True)
    print(name, img.size, os.path.getsize(p) // 1024, "KB")


# ---------- 250x250 ----------
img = bg(250, 250, 0.5, 0.42); d = ImageDraw.Draw(img)
wordmark(d, 24, 46, 30)
rule(d, 24, 62, 96)
d.text((24, 80), "Só 26,5%", font=f(B, 27), fill=WHITE)
d.text((24, 110), "foram treinados", font=f(B, 17), fill=WHITE)
d.text((24, 131), "pela empresa para", font=f(R, 13), fill=MUTE)
d.text((24, 148), "usar IA. E você?", font=f(R, 13), fill=MUTE)
pill(d, (24, 178, 160, 210), "Amostra grátis", 13)
d.text((24, 222), "are-ia.com", font=f(R, 11), fill=MUTE)
save(img, "areia_250x250.png")

# ---------- 300x250 ----------
img = bg(300, 250, 0.52, 0.4); d = ImageDraw.Draw(img)
wordmark(d, 26, 44, 31)
rule(d, 26, 60, 100)
d.text((26, 78), "IA no trabalho,", font=f(B, 24), fill=WHITE)
d.text((26, 104), "em português claro", font=f(B, 24), fill=EMER)
d.text((26, 138), "Prompts prontos por profissão", font=f(R, 13), fill=MUTE)
d.text((26, 156), "e o que nunca colar numa IA.", font=f(R, 13), fill=MUTE)
pill(d, (26, 184, 172, 216), "Amostra grátis", 13)
d.text((184, 196), "are-ia.com", font=f(R, 11), fill=MUTE)
save(img, "areia_300x250.png")

# ---------- 336x280 ----------
img = bg(336, 280, 0.5, 0.38); d = ImageDraw.Draw(img)
wordmark(d, 28, 48, 34)
rule(d, 28, 66, 110)
d.text((28, 86), "O manual de IA", font=f(B, 26), fill=WHITE)
d.text((28, 114), "que sua empresa", font=f(B, 26), fill=WHITE)
d.text((28, 142), "não te deu", font=f(B, 26), fill=EMER)
d.text((28, 180), "Prompts por profissão · LGPD · anti-golpes", font=f(R, 12), fill=MUTE)
pill(d, (28, 206, 180, 240), "Amostra grátis", 14)
d.text((28, 252), "are-ia.com", font=f(R, 11), fill=MUTE)
save(img, "areia_336x280.png")

# ---------- 468x60 ----------
img = bg(468, 60, 0.18, 0.5, 1.25); d = ImageDraw.Draw(img)
wordmark(d, 18, 38, 24)
d.line([(96, 14), (96, 46)], fill=(40, 66, 74), width=1)
t1, t2 = "IA no trabalho, sem jargão", "Prompts por profissão e anti-golpes"
d.text((112, 14), t1, font=fit(d, t1, B, 15, 212), fill=WHITE)
d.text((112, 34), t2, font=fit(d, t2, R, 11, 212), fill=MUTE)
pill(d, (338, 16, 452, 44), "Amostra grátis", 12)
save(img, "areia_468x60.png")

# ---------- 728x90 ----------
img = bg(728, 90, 0.16, 0.5, 1.2); d = ImageDraw.Draw(img)
wordmark(d, 26, 58, 34)
d.line([(150, 20), (150, 70)], fill=(40, 66, 74), width=1)
t1 = "Só 26,5% de quem usa IA foi treinado pela empresa"
t2 = "Guia prático em português claro: prompts por profissão e anti-golpes"
d.text((172, 21), t1, font=fit(d, t1, B, 18, 370), fill=WHITE)
d.text((172, 48), t2, font=fit(d, t2, R, 13, 370), fill=MUTE)
pill(d, (560, 28, 702, 62), "Amostra grátis", 14)
save(img, "areia_728x90.png")

# ---------- 160x600 ----------
img = bg(160, 600, 0.5, 0.3); d = ImageDraw.Draw(img)
wordmark(d, 18, 54, 26)
rule(d, 18, 70, 86)
d.text((18, 92), "O manual", font=f(B, 22), fill=WHITE)
d.text((18, 116), "de IA que", font=f(B, 22), fill=WHITE)
d.text((18, 140), "sua empresa", font=f(B, 19), fill=WHITE)
d.text((18, 163), "não te deu", font=f(B, 19), fill=EMER)
for i, line in enumerate(["Prompts prontos", "por profissão", "", "O que nunca", "colar numa IA", "", "Golpe de Pix,", "SMS e voz", "clonada"]):
    d.text((18, 212 + i * 20), line, font=f(R, 12), fill=MUTE)
pill(d, (18, 420, 142, 452), "Amostra grátis", 12)
d.text((18, 470), "are-ia.com", font=f(R, 11), fill=MUTE)
d.text((18, 560), "Conteúdo", font=f(R, 10), fill=(110, 134, 142))
d.text((18, 574), "educativo", font=f(R, 10), fill=(110, 134, 142))
save(img, "areia_160x600.png")

print("ok")
