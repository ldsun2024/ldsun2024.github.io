# -*- coding: utf-8 -*-
import io, sys, json
import pdfplumber

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

ROOT = "D:/github_project/ldsun2024.github.io"
SRC = ROOT + "/8861-全订本-第一版 - 副本.pdf"
OUT = ROOT + "/_struct.json"

print("pdfplumber", pdfplumber.__version__)
result = []
TOL = 4.5


def join_words(ws):
    out = ""
    for w in ws:
        t = w["text"]
        if not out:
            out = t
            continue
        pc = out[-1]
        fc = t[0]
        if ("一" <= pc <= "鿿") and ("一" <= fc <= "鿿"):
            out += t
        else:
            out += " " + t
    return out


def is_pua(s):
    for ch in s:
        if 0xE000 <= ord(ch) <= 0xF8FF:
            return True
    return False

with pdfplumber.open(SRC) as pdf:
    npages = len(pdf.pages)
    for i, pg in enumerate(pdf.pages):
        rows = {}
        try:
            words = pg.extract_words(extra_attrs=["size"])
        except Exception:
            words = []
        words = [w for w in words if not is_pua(w["text"])]
        words.sort(key=lambda w: (round(w["top"], 1), w["x0"]))
        cur = []
        cur_top = None
        lines = []
        for w in words:
            if cur_top is None or (w["top"] - cur_top) <= TOL:
                cur.append(w)
                cur_top = w["top"] if cur_top is None else cur_top
            else:
                lines.append(cur)
                cur = [w]
                cur_top = w["top"]
        if cur:
            lines.append(cur)
        out2 = []
        for ws in lines:
            ws.sort(key=lambda x: x["x0"])
            txt = join_words(ws)
            sz = max(float(w["size"]) for w in ws)
            out2.append({"t": txt, "s": round(sz, 1),
                         "y": round(min(w["top"] for w in ws), 1)})
        lines = out2
        result.append(lines)
        if (i + 1) % 100 == 0:
            print("scanned", i + 1, "/", npages)

with open(OUT, "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False)
print("saved", OUT)

big = []
mid = []
for i, lines in enumerate(result):
    for ln in lines:
        if ln["s"] >= 20:
            big.append((i + 1, ln["s"], ln["t"][:60]))
        elif 14 <= ln["s"] < 20:
            mid.append((i + 1, ln["s"], ln["t"][:50]))
print("")
print("22pt+ lines:", len(big))
for b in big[:15]:
    print("  ", b)
print("")
print("16pt lines:", len(mid))
for b in mid[:10]:
    print("  ", b)