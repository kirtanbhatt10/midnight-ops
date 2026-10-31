#!/usr/bin/env python3
"""Render the README demo frames: python scripts/render-demo.py <out_dir>"""
import os, sys
from PIL import Image, ImageDraw, ImageFont
OUT = sys.argv[1] if len(sys.argv) > 1 else "frames"
os.makedirs(OUT, exist_ok=True)
for f in os.listdir(OUT):
    os.remove(os.path.join(OUT, f))
W, H = 1280, 720
FPS = 30
MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
MONO_B = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
f_body = ImageFont.truetype(MONO, 21)
f_bodyb = ImageFont.truetype(MONO_B, 21)
f_title = ImageFont.truetype(MONO, 15)
f_big = ImageFont.truetype(SANS_B, 60)
f_tag = ImageFont.truetype(MONO, 22)
BG = (10, 14, 22)
PANEL = (13, 17, 25)
BAR = (22, 27, 34)
BORDER = (40, 48, 60)
FG = (220, 227, 235)
DIM = (120, 132, 148)
PURPLE = (160, 135, 235)   # Claude
GREEN = (60, 200, 150)     # ok / Codex
ORANGE = (240, 170, 70)    # warn
RED = (240, 110, 110)
CYAN = (120, 200, 230)
BLUE = (110, 160, 240)
BARH = 46
PADX = 28
TOP = BARH + 22
LH = 29
VISIBLE = (H - TOP - 24) // LH
S = []
def typ(t, c=FG):   S.append(("type", t, c))
def pr(t, c=FG):    S.append(("print", t, c))
def blank(n=1):
    for _ in range(n): S.append(("blank", "", FG))
def hold(fr):       S.append(("hold", fr, FG))
typ("$ claude --skill midnight-ops", GREEN); hold(10)
blank()
typ("> Help me plan a web pentest of our staging app.", FG); hold(8)
blank()
pr("midnight-ops  //  authorization gate", PURPLE)
pr("[!] Before anything target-specific I need, in writing:", ORANGE); hold(2)
pr("    - authorizing signatory   - signed SOW / ROE", DIM)
pr("    - explicit scope          - testing window", DIM)
pr("    - a human operator who owns every action", DIM); hold(14)
blank()
typ("> ROE #AW-2026-014 attached. Scope: app.acme.example (staging).", FG); hold(10)
blank()
pr("[OK] Authorization confirmed  -  scope locked to 1 host", GREEN); hold(10)
blank()
pr("Plan (OWASP WSTG + PTES, mapped to ATT&CK):", CYAN)
pr("  [x] WSTG-CONF   headers / TLS / exposure", FG); hold(4)
pr("  [x] WSTG-SESS   session lifecycle + CSRF", FG); hold(4)
pr("  [>] WSTG-ATHZ   object-level authorization", FG); hold(10)
blank()
pr("FINDING  FND-001  -  IDOR on order lookup (API)", RED)
pr("  severity HIGH   CVSS 7.1   ATT&CK TA0007 / TA0009", ORANGE)
pr("  low-priv user can read another tenant's orders", DIM)
pr("  fix: enforce per-object authZ server-side", DIM); hold(14)
blank()
pr("Report assembled -> exec summary + 1 High, 2 Med", BLUE)
pr("  + remediation & retest plan                 [done]", GREEN); hold(20)
def draw_base():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([16, 16, W-16, H-16], radius=14, fill=PANEL, outline=BORDER, width=2)
    d.rounded_rectangle([16, 16, W-16, 16+BARH], radius=14, fill=BAR)
    d.rectangle([16, 16+BARH-14, W-16, 16+BARH], fill=BAR)
    for i, col in enumerate([(237,106,94),(245,191,79),(98,197,84)]):
        d.ellipse([40+i*26, 16+BARH//2-7, 54+i*26, 16+BARH//2+7], fill=col)
    d.text((W//2-150, 16+BARH//2-9), "midnight-ops  -  engagement session", font=f_title, fill=DIM)
    return img, d
frame_idx = 0
printed = []  # (text, color, None=full)
cursor_line = None  # (text, color, n)
def emit():
    global frame_idx
    img, d = draw_base()
    lines = list(printed)
    if cursor_line is not None:
        lines = lines + [cursor_line]
    shown = lines[-VISIBLE:]
    y = TOP
    for text, color, typed_n in shown:
        t = text if typed_n is None else text[:typed_n]
        d.text((PADX+18, y), t, font=f_body, fill=color)
        if typed_n is not None and (frame_idx // 8) % 2 == 0:
            w = d.textlength(t, font=f_body)
            d.rectangle([PADX+18+w+1, y+3, PADX+18+w+12, y+22], fill=GREEN)
        y += LH
    img.save(os.path.join(OUT, f"f{frame_idx:05d}.png"))
    frame_idx += 1
CPF = 2  # chars per frame
for kind, text, color in S:
    if kind == "hold":
        for _ in range(int(text)): emit()
    elif kind == "blank":
        printed.append(("", FG, None)); emit()
    elif kind == "print":
        printed.append((text, color, None))
        emit(); emit()  # brief pause
    elif kind == "type":
        n = 0
        cursor_line = (text, color, 0)
        while n < len(text):
            n = min(len(text), n + CPF)
            cursor_line = (text, color, n)
            emit()
        for _ in range(6): emit()
        printed.append((text, color, None))
        cursor_line = None
def crescent(d, cx, cy, r, col):
    d.ellipse([cx-r, cy-r, cx+r, cy+r], fill=col)
    off = int(r*0.55)
    d.ellipse([cx-r+off, cy-r-int(r*0.12), cx+r+off, cy+r-int(r*0.12)], fill=PANEL)
END_FRAMES = 70
for i in range(END_FRAMES):
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([16,16,W-16,H-16], radius=14, fill=PANEL, outline=BORDER, width=2)
    a = min(1.0, i/12)
    cx, cy = W//2, H//2 - 40
    crescent(d, cx-150, cy, 46, tuple(int(c*a) for c in (210,205,245)))
    tw = d.textlength("midnight-ops", font=f_big)
    d.text((cx-70, cy-42), "midnight-ops", font=f_big, fill=tuple(int(c*a) for c in FG))
    tag = "authorization-first red-team methodology for AI agents"
    twt = d.textlength(tag, font=f_tag)
    d.text((cx - twt/2, cy+70), tag, font=f_tag, fill=tuple(int(c*a) for c in DIM))
    sub = "Claude  .  Codex"
    sw = d.textlength(sub, font=f_tag)
    d.text((cx - sw/2, cy+108), sub, font=f_tag, fill=tuple(int(c*a) for c in PURPLE))
    img.save(os.path.join(OUT, f"f{frame_idx:05d}.png"))
    frame_idx += 1
print("frames:", frame_idx, "duration s:", round(frame_idx/FPS,1))
