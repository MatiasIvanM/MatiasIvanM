from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

F = "node_modules/@fontsource/"
slab = TTFont(F + "alfa-slab-one/files/alfa-slab-one-latin-400-normal.woff2")
osw  = TTFont(F + "oswald/files/oswald-latin-500-normal.woff2")

def text_path(font, text, size, x, y, tracking=0, anchor="start"):
    gs = font.getGlyphSet(); cmap = font.getBestCmap()
    upm = font["head"].unitsPerEm; s = size / upm
    names = [cmap[ord(c)] for c in text]
    adv = [font["hmtx"][n][0] * s + tracking for n in names]
    total = sum(adv) - tracking
    cx = x - total / 2 if anchor == "middle" else x
    pen = SVGPathPen(gs); 
    for n, a in zip(names, adv):
        tp = TransformPen(pen, (s, 0, 0, -s, cx, y))
        gs[n].draw(tp); cx += a
    return pen.getCommands(), total

W, H = 1200, 390
name, nw = text_path(slab, "MATÍAS", 150, W/2, 255, tracking=14, anchor="middle")
sub1, _ = text_path(osw, "FULL STACK  /  QA  /  PRODUCT", 26, W/2, 330, tracking=7, anchor="middle")
sub2, _ = text_path(osw, "OUTCOMES OVER OUTPUT", 20, W/2, 92, tracking=9, anchor="middle")

rivets = "".join(f'<circle cx="{x}" cy="{y}" r="6" fill="#2b241b" stroke="#b08d57" stroke-width="1.5"/>'
                 for x in (46, W-46) for y in (46, H-46))

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Matías, Full Stack, QA, Product. Outcomes over output.">
  <title>Matías · Full Stack / QA / Product</title>
  <rect width="{W}" height="{H}" rx="18" fill="#17130e"/>
  <rect x="14" y="14" width="{W-28}" height="{H-28}" rx="10" fill="none" stroke="#b08d57" stroke-width="3"/>
  <rect x="24" y="24" width="{W-48}" height="{H-48}" rx="5" fill="none" stroke="#c8681e" stroke-width="1.5"/>
  {rivets}
  <path d="{sub2}" fill="#b08d57"/>
  <path d="{name}" fill="#c8681e" transform="translate(5 5)"/>
  <path d="{name}" fill="#efe4cc"/>
  <rect x="{W/2-300}" y="282" width="600" height="3" fill="#c8681e"/>
  <path d="{sub1}" fill="#efe4cc"/>
</svg>
'''
open("assets/banner.svg", "w").write(svg)
print(len(svg), "bytes")
