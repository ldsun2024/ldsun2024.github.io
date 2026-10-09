# -*- coding: utf-8 -*-
import io, sys, re, json, os, shutil, unicodedata
from collections import defaultdict
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
ROOT = "D:/github_project/ldsun2024.github.io"
struct = json.load(open(ROOT + "/_struct.json", encoding="utf-8"))
chapters = json.load(open(ROOT + "/_chapters.json", encoding="utf-8"))
HEAD_SZ = 20.0
NP = len(struct)
DASH = chr(0x2d) + chr(0x2014) + chr(0xff0d) + chr(0xb7) + "_"


def norm(s):
    s = unicodedata.normalize("NFKC", s).replace(chr(0x3000), " ")
    for d in DASH:
        s = s.replace(d, "")
    return re.sub(r"\s+", "", s).lower()


heads = []
for i, lines in enumerate(struct):
    for ln in lines:
        if ln["s"] >= HEAD_SZ:
            heads.append({"page": i + 1, "norm": norm(ln["t"])})
cursor = 0
matched = []
unmatched = []
for c in chapters:
    key = norm(c["title"])
    hit = None
    for j in range(cursor, len(heads)):
        if heads[j]["norm"] == key:
            hit = j
            break
    if hit is None:
        for j in range(cursor, len(heads)):
            if key and (key in heads[j]["norm"] or heads[j]["norm"] in key):
                hit = j
                break
    if hit is None:
        unmatched.append(c["title"])
        matched.append({"title": c["title"], "head": None, "page": c["page"]})
    else:
        matched.append({"title": c["title"], "head": hit, "page": heads[hit]["page"]})
        cursor = hit + 1
print("matched:", sum(1 for m in matched if m["head"] is not None), "/", len(matched))
for u in unmatched[:25]:
    print("  MISS -", u)
prev = 0
for m in matched:
    if m["head"] is not None and m["page"] < prev:
        m["head"] = None
    if m["head"] is not None:
        prev = m["page"]
json.dump(matched, open(ROOT + "/_matched.json", "w", encoding="utf-8"), ensure_ascii=False)
print("saved")
TAIL = ["交易总结", "中级课", "高级课", "研修班", "第六买点",
        "大盘分析班", "期权班", "经典语录"]
for m in matched:
    if m["head"] is None and m["title"] in TAIL:
        m["merge"] = True
    if m["head"] is None and "23-26" in m["title"]:
        m["page"] = 673
GAP = 22
PAGE_NO = 9.5
CJK_R = re.compile("[\u4e00-\u9fff\u3000-\u303f\uff00-\uffef]$")
CJK_L = re.compile("^[\u4e00-\u9fff\u3000-\u303f\uff00-\uffef]")


def page_blocks(pno):
    lines = struct[pno - 1]
    out = []
    buf = ""
    prev = None
    for ln in lines:
        t = ln["t"].strip()
        if not t:
            continue
        if ln["s"] <= PAGE_NO and re.fullmatch(r"\d{1,4}", t):
            continue
        if re.search(r"\.{6,}", t):
            continue
        if ln["s"] >= HEAD_SZ:
            if buf:
                out.append(buf)
                buf = ""
            out.append("H|" + t)
            prev = None
            continue
        gap = (ln["y"] - prev) if prev is not None else GAP
        if gap >= GAP:
            if buf:
                out.append(buf)
            buf = t
        elif not buf:
            buf = t
        elif CJK_R.search(buf) and CJK_L.match(t):
            buf += t
        else:
            buf += " " + t
        prev = ln["y"]
    if buf:
        out.append(buf)
    return out


ORDER = ["中级课", "高级课", "研修课", "研修班", "大盘多空分析", "期权课",
         "火箭课", "黄金课", "总结与语录", "个人笔记与案例"]


def cat(t):
    for k in ORDER[:-1]:
        if k in t:
            return k
    return "个人笔记与案例"


def safe(s):
    s = re.sub(r'[\\/:*?"<>|]', "", s).strip().rstrip(".")
    return s[:70] or "untitled"


# 合并尾部附录章节
final = []
bufmerge = None
for m in matched:
    if m.get("merge"):
        if bufmerge is None:
            bufmerge = {"title": "总结与语录", "page": m["page"], "head": -1}
            final.append(bufmerge)
    else:
        bufmerge = None
        final.append(m)
matched = final

DST = ROOT + "/pdf-md"
if os.path.isdir(DST):
    shutil.rmtree(DST)
os.makedirs(DST, exist_ok=True)
groups = defaultdict(list)
for m in matched:
    groups[cat(m["title"])].append(m)
present = [k for k in ORDER if k in groups]
cat_no = dict((k, "%02d" % (i + 1)) for i, k in enumerate(present))
rows = []

for gname in present:
    gdir = os.path.join(DST, cat_no[gname] + "-" + gname)
    os.makedirs(gdir, exist_ok=True)
    items = groups[gname]
    for idx, m in enumerate(items):
        start = m["page"]
        nxt = None
        for k in range(idx + 1, len(items)):
            if items[k]["head"] is not None:
                nxt = items[k]["page"]
                break
        end = (nxt - 1) if nxt else NP
        if end < start:
            end = start
        parts = []
        for pno in range(start, end + 1):
            parts.extend(page_blocks(pno))
        nchar = 0
        for b in parts:
            nchar += len(re.sub(r"\s", "", b))
        if nchar < 10:
            continue
        md = ["---",
              'title: "' + m["title"] + '"',
              'series: "' + gname + '"',
              "source: 8861-全订本-第一版",
              "pdf_page: " + str(start),
              "pdf_page_end: " + str(end),
              "---", "",
              "# " + m["title"], "",
              "> " + gname + " ｜ PDF p" + str(start) + "-" + str(end), ""]
        for b in parts:
            if b.startswith("H|"):
                t = b[2:].strip()
                if t and t != m["title"]:
                    md += ["## " + t, ""]
            else:
                md += [b, ""]
        fname = "%03d-%s.md" % (idx + 1, safe(m["title"]))
        f = open(os.path.join(gdir, fname), "w", encoding="utf-8")
        f.write("\n".join(md))
        f.close()
        rows.append((gname, fname[:-3], m["title"], start, end, nchar))

print("chapters written:", len(rows))
print("total chars: {:,}".format(sum(x[5] for x in rows)))

gstat = defaultdict(lambda: [0, 0])
for g, a, b, c, d, e in rows:
    gstat[g][0] += 1
    gstat[g][1] += e
L = ["# 8861 全订本 第一版 · 内容索引", ""]
L.append("- 源文件：`8861-全订本-第一版 - 副本.pdf`（" + str(NP) + " 页）")
L.append("- 章节数：**" + str(len(rows)) + "**")
L.append("- 正文字数：约 **{:,}**".format(sum(x[5] for x in rows)))
L.append("- 说明：按原文章节边界还原，**仅文字，不含图片**")
L += ["", "## 分类统计", "", "| 分类 | 章节 | 字数 |", "|------|-----:|-----:|"]
for g in present:
    n, c = gstat[g]
    L.append("| " + g + " | " + str(n) + " | {:,} |".format(c))
L.append("")
for g in present:
    L += ["## " + g, "", "| # | 章节 | PDF | 字数 |", "|--:|------|----:|-----:|"]
    sub = [x for x in rows if x[0] == g]
    for i, x in enumerate(sub, 1):
        L.append("| " + str(i) + " | [" + x[2] + "](" + cat_no[g] + "-" + g
                 + "/" + x[1] + ".md) | " + str(x[3]) + "-" + str(x[4])
                 + " | {:,} |".format(x[5]))
    L.append("")
f = open(os.path.join(DST, "README.md"), "w", encoding="utf-8")
f.write("\n".join(L))
f.close()
print("README ->", DST)