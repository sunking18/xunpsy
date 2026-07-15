#!/Users/jinnan/.workbuddy/binaries/python/envs/default/bin/python3
"""Generate 3 logo design PNGs - high contrast, 2x supersampled."""

from PIL import Image, ImageDraw, ImageFont
from math import cos, sin, pi
import os

OUT = "/Users/jinnan/WorkBuddy/2026-06-29-22-35-51/寻心理官网"
S = 1600  # render at 2x for crisp anti-aliasing
DOWN = 2  # downsample factor

songti_path = "/System/Library/Fonts/Supplemental/Songti.ttc"
georgia_path = "/System/Library/Fonts/Georgia.ttf"

def get_font(size, font_path=songti_path):
    try:
        return ImageFont.truetype(font_path, size)
    except:
        return ImageFont.load_default()

# Fonts at 2x size
f_name = get_font(90 * DOWN)
f_name_m = get_font(68 * DOWN)
f_name_s = get_font(52 * DOWN)
f_en = get_font(38 * DOWN, georgia_path)
f_en_i = get_font(48 * DOWN, "/System/Library/Fonts/Supplemental/Georgia Italic.ttf")
f_en_bi = get_font(32 * DOWN, "/System/Library/Fonts/Supplemental/Georgia Bold Italic.ttf")
f_tag = get_font(32 * DOWN)
f_tag_sm = get_font(28 * DOWN)
f_arc = get_font(30 * DOWN)

def load_logo(dark=False):
    f = os.path.join(OUT, "logo.png" if dark else "logo-white.png")
    return Image.open(f).convert("RGBA")

def text_center(draw, text, font, y, fill):
    bbox = draw.textbbox((0, 0), text, font=font)
    w = bbox[2] - bbox[0]
    draw.text(((S - w) // 2, y), text, font=font, fill=fill)

def text_left(draw, text, font, x, y, fill):
    draw.text((x, y), text, font=font, fill=fill)

def save_down(img, name):
    if DOWN > 1:
        ow, oh = img.size
        img = img.resize((ow // DOWN, oh // DOWN), Image.LANCZOS)
    path = os.path.join(OUT, name)
    img.save(path)
    print(f"Saved: {path}")


# ==================== DESIGN 1: 经典圆章 ====================
def make_design1():
    img = Image.new("RGBA", (S, S), (255, 251, 245, 255))
    draw = ImageDraw.Draw(img)

    # Green border ring - opaque
    draw.ellipse([80, 80, S-80, S-80], fill=(74, 124, 111, 255))
    draw.ellipse([96, 96, S-96, S-96], fill=(255, 251, 245, 255))

    # Dashed decoration ring - more opaque
    r = 348 * DOWN
    cx = cy = S // 2
    for a in range(0, 360, 8):
        a1 = a * pi / 180
        a2 = (a + 4) * pi / 180
        x1 = cx + r * cos(a1)
        y1 = cy + r * sin(a1)
        x2 = cx + r * cos(a2)
        y2 = cy + r * sin(a2)
        draw.line([x1, y1, x2, y2], fill=(212, 165, 116, 220), width=6)

    # Logo
    logo = load_logo(dark=True)
    logo_sz = 180 * DOWN
    logo_rs = logo.resize((logo_sz, logo_sz), Image.LANCZOS)
    img.paste(logo_rs, ((S - logo_sz)//2, 100 * DOWN), logo_rs)

    # 寻心理 - pure black for max contrast
    text_center(draw, "寻心理", f_name, 320 * DOWN, (0, 0, 0, 255))

    # InnerSeed - deep green
    text_center(draw, "InnerSeed", f_en_i, 450 * DOWN, (74, 124, 111, 255))

    # Gold separator - full opaque
    lw = 180 * DOWN
    y1 = 520 * DOWN
    draw.line([(S - lw)//2, y1, (S + lw)//2, y1], fill=(212, 165, 116, 255), width=4)

    # Tagline - darker brown
    text_center(draw, "向内寻 · 向外生", f_tag, 572 * DOWN, (75, 60, 45, 255))

    # Dots - opaque
    dot_y = 645 * DOWN
    dot_r = 10
    for i, fill in enumerate([(212, 165, 116, 255), (74, 124, 111, 255), (212, 165, 116, 255)]):
        dx = S//2 + (i - 1) * 60
        draw.ellipse([dx - dot_r, dot_y - dot_r, dx + dot_r, dot_y + dot_r], fill=fill)

    save_down(img, "logo-design-1.png")


# ==================== DESIGN 2: 现代拼接 ====================
def make_design2():
    img = Image.new("RGBA", (S, S), (45, 74, 66, 255))
    draw = ImageDraw.Draw(img)

    # Logo
    logo = load_logo(dark=False)
    logo_sz = 280 * DOWN
    logo_rs = logo.resize((logo_sz, logo_sz), Image.LANCZOS)
    img.paste(logo_rs, (60 * DOWN, (S - logo_sz)//2), logo_rs)

    tx = 370 * DOWN
    ty = 288 * DOWN

    # 寻心理 - pure white
    text_left(draw, "寻心理", f_name, tx - 10 * DOWN, ty, (255, 255, 255, 255))

    # InnerSeed - bright gold
    text_left(draw, "InnerSeed", f_en_bi, tx, ty + 120 * DOWN, (230, 185, 130, 255))

    # Divider - opaque
    div_y = ty + 168 * DOWN
    draw.line([tx, div_y, tx + 120 * DOWN, div_y], fill=(212, 165, 116, 255), width=4)

    # Tagline - brighter grass green
    text_left(draw, "向 内 寻   ·   向 外 生", f_tag_sm, tx, div_y + 30 * DOWN, (130, 200, 90, 255))

    save_down(img, "logo-design-2.png")


# ==================== DESIGN 3: 印章风格 ====================
def make_design3():
    img = Image.new("RGBA", (S, S), (45, 74, 66, 255))
    draw = ImageDraw.Draw(img)

    # Outer ring - solid opaque
    draw.ellipse([80, 80, S-80, S-80], fill=(107, 158, 138, 220))
    draw.ellipse([94, 94, S-94, S-94], fill=(45, 74, 66, 255))

    # Inner ring - solid opaque
    draw.ellipse([120, 120, S-120, S-120], fill=(212, 165, 116, 200))
    draw.ellipse([128, 128, S-128, S-128], fill=(45, 74, 66, 255))

    # Arc text - brighter green
    text_center(draw, "向内寻 · 向外生", f_arc, 160 * DOWN, (170, 210, 100, 255))

    # Logo
    logo = load_logo(dark=False)
    logo_sz = 190 * DOWN
    logo_rs = logo.resize((logo_sz, logo_sz), Image.LANCZOS)
    img.paste(logo_rs, ((S - logo_sz)//2, 240 * DOWN), logo_rs)

    # 寻心理 - pure white
    text_center(draw, "寻心理", f_name, 440 * DOWN, (255, 255, 255, 255))

    # InnerSeed - bright gold
    text_center(draw, "InnerSeed", f_en_bi, 590 * DOWN, (230, 185, 130, 255))

    save_down(img, "logo-design-3.png")


make_design1()
make_design2()
make_design3()
print("All 3 done!")
