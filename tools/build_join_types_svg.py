#!/usr/bin/env python3
"""Draw images/join_types.svg: one-to-one, many-to-one, many-to-many, using a
grades table joined to three other tables.  Run from textbook_261/."""
PRAIRIE, INK, MUTED, LINE, HILITE = "#4A7C59", "#24302A", "#5C6B62", "#7A8F82", "#C96A2B"
RH, FS = 22, 13                       # row height, font size
grades = [("Ana","AREC 261","82"),("Ana","AREC 262","78"),("Ben","AREC 261","71"),("Chen","AREC 262","90")]
panels = [
 ("One-to-one (1:1)", "key: student + class", ("student","class","classes_attended"),
  [("Ana","AREC 261","11"),("Ana","AREC 262","9"),("Ben","AREC 261","12"),("Chen","AREC 262","10")],
  [(0,0),(1,1),(2,2),(3,3)], "4 rows join 4 rows: 4 rows"),
 ("Many-to-one (n:1)", "key: class", ("class","professor"),
  [("AREC 261","Slade"),("AREC 262","Gray")],
  [(0,0),(1,1),(2,0),(3,1)], "4 rows join 2 rows: 4 rows"),
 ("Many-to-many (n:n)", "key: class", ("class","teaching_assistant"),
  [("AREC 261","Priya"),("AREC 261","Tom"),("AREC 262","Lee"),("AREC 262","Maria")],
  [(0,0),(0,1),(1,2),(1,3),(2,0),(2,1),(3,2),(3,3)], "4 rows join 4 rows: 8 rows"),
]
W = 720; PH = 190; H = PH*len(panels) + 10
out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="Arial, Helvetica, sans-serif" font-size="{FS}">',
       f'<rect width="{W}" height="{H}" fill="white"/>']
def table(x, y, hdr, rows, widths):
    s = []; cx = x
    for h, w in zip(hdr, widths):
        s.append(f'<rect x="{cx}" y="{y}" width="{w}" height="{RH}" fill="{PRAIRIE}"/>')
        s.append(f'<text x="{cx+6}" y="{y+15}" fill="white" font-weight="bold">{h}</text>'); cx += w
    for i, r in enumerate(rows):
        cx = x; yy = y + RH*(i+1)
        for v, w in zip(r, widths):
            s.append(f'<rect x="{cx}" y="{yy}" width="{w}" height="{RH}" fill="none" stroke="{LINE}" stroke-width="0.8"/>')
            s.append(f'<text x="{cx+6}" y="{yy+15}" fill="{INK}">{v}</text>'); cx += w
    return s, sum(widths)
for p, (title, keynote, hdr, rows, links, result) in enumerate(panels):
    top = 10 + p*PH
    out.append(f'<text x="10" y="{top+14}" fill="{INK}" font-weight="bold" font-size="15">{title}</text>')
    out.append(f'<text x="{W-10}" y="{top+14}" fill="{MUTED}" text-anchor="end">{keynote}</text>')
    ty = top + 26
    lw = (60, 80, 50); s, lwid = table(10, ty, ("student","class","grade"), grades, lw); out += s
    rw = (60, 80, 120) if len(hdr) == 3 else (80, 130)
    rx = W - 10 - sum(rw); s, _ = table(rx, ty, hdr, rows, rw); out += s
    x1 = 10 + lwid; x2 = rx
    for a, b in links:
        y1 = ty + RH*(a+1) + RH/2; y2 = ty + RH*(b+1) + RH/2
        col = HILITE if p == 2 else PRAIRIE
        out.append(f'<path d="M{x1},{y1} C{x1+60},{y1} {x2-60},{y2} {x2},{y2}" fill="none" stroke="{col}" stroke-width="1.4" opacity="0.85"/>')
    out.append(f'<text x="10" y="{ty + RH*5 + 18}" fill="{MUTED}">{result}</text>')
out.append('</svg>')
open("images/join_types.svg","w").write("\n".join(out)); print("ok")
