# Visuals for this course: extra cartoons and three animations (the reporting pipe, the balance scale, the users around the company).
from lib import _st
# Drawn here as inline SVG, no outside images.

_face = lambda cx, cy, r, mood='smile': (f'<circle cx="{cx - r * .32:.1f}" cy="{cy - r * .12:.1f}" r="{r * .11:.1f}" fill="#111"/><circle cx="{cx + r * .32:.1f}" cy="{cy - r * .12:.1f}" r="{r * .11:.1f}" fill="#111"/>'
    + {'smile': f'<path d="M{cx - r * .36:.1f} {cy + r * .22:.1f}q{r * .36:.1f} {r * .3:.1f} {r * .72:.1f} 0" fill="none" stroke="#111" stroke-width="2.6" stroke-linecap="round"/>',
       'sad': f'<path d="M{cx - r * .34:.1f} {cy + r * .4:.1f}q{r * .34:.1f} {-r * .26:.1f} {r * .68:.1f} 0" fill="none" stroke="#111" stroke-width="2.6" stroke-linecap="round"/>',
       'flat': f'<path d="M{cx - r * .3:.1f} {cy + r * .3:.1f}h{r * .6:.1f}" stroke="#111" stroke-width="2.6" stroke-linecap="round"/>',
       'wow': f'<ellipse cx="{cx:.1f}" cy="{cy + r * .32:.1f}" rx="{r * .14:.1f}" ry="{r * .18:.1f}" fill="#111"/>'}[mood])

TOONS.update({
 'cup': '<path d="M26 44h58v34q0 26-29 26t-29-26z" fill="#fff" stroke="#1b2d55" stroke-width="4"/><path d="M84 54q20 0 20 14t-20 14" fill="none" stroke="#1b2d55" stroke-width="4"/>'
        + '<path d="M40 20q6 8 0 14M56 14q6 8 0 16M72 20q6 8 0 14" fill="none" stroke="#8a93aa" stroke-width="3" stroke-linecap="round"/>' + _face(55, 72, 20),
 'cupsad': '<path d="M26 44h58v34q0 26-29 26t-29-26z" fill="#fff" stroke="#1b2d55" stroke-width="4"/><path d="M84 54q20 0 20 14t-20 14" fill="none" stroke="#1b2d55" stroke-width="4"/>' + _face(55, 72, 20, 'sad')
        + '<text x="100" y="34" text-anchor="middle" font-size="26" font-weight="800" fill="#e0454f">?</text>',
 'bank': '<path d="M10 40l50-26 50 26z" fill="#27447f"/><rect x="14" y="40" width="92" height="8" fill="#1b2d55"/><g fill="#e8eefb" stroke="#1b2d55" stroke-width="2"><rect x="20" y="50" width="12" height="40"/><rect x="44" y="50" width="12" height="40"/><rect x="66" y="50" width="12" height="40"/><rect x="88" y="50" width="12" height="40"/></g>'
         + '<rect x="10" y="90" width="100" height="12" fill="#1b2d55"/><circle cx="60" cy="27" r="10" fill="#ffd37a"/><text x="60" y="33" text-anchor="middle" font-size="16" font-weight="800" fill="#a86703">₪</text>',
 'mag': '<rect x="16" y="14" width="58" height="76" rx="6" fill="#fff" stroke="#1b2d55" stroke-width="3"/><path d="M26 30h38M26 42h38M26 54h26M26 66h32" stroke="#8a93aa" stroke-width="3"/>'
        + '<circle cx="74" cy="70" r="20" fill="#dff5f2" fill-opacity=".7" stroke="#0f9d90" stroke-width="5"/><path d="M88 84l18 18" stroke="#0f9d90" stroke-width="8" stroke-linecap="round"/>',
 'report': '<rect x="20" y="10" width="72" height="96" rx="6" fill="#fff" stroke="#1b2d55" stroke-width="3"/><rect x="30" y="20" width="52" height="8" rx="2" fill="#27447f"/>'
           + '<rect x="32" y="70" width="9" height="24" fill="#8a93aa"/><rect x="46" y="58" width="9" height="36" fill="#0f9d90"/><rect x="60" y="46" width="9" height="48" fill="#25a65f"/><rect x="74" y="36" width="9" height="58" fill="#ff6a4d"/>' + _face(56, 40, 0.001, 'flat')[:0],
 'gavel': '<rect x="14" y="92" width="70" height="12" rx="3" fill="#8a5a2b"/><rect x="30" y="20" width="44" height="24" rx="6" fill="#8a5a2b" transform="rotate(-30 52 32)"/><path d="M58 44l36 40" stroke="#5b3a1a" stroke-width="8" stroke-linecap="round"/>'
          + '<text x="100" y="30" text-anchor="middle" font-size="20" font-weight="800" fill="#1b2d55">§</text>',
 'mask': '<circle cx="60" cy="58" r="40" fill="#ffd37a"/><path d="M22 50q38-22 76 0v10q-38-14-76 0z" fill="#1b2d55"/><circle cx="44" cy="54" r="5" fill="#fff"/><circle cx="76" cy="54" r="5" fill="#fff"/>'
         + '<path d="M44 80q16 10 32 0" fill="none" stroke="#111" stroke-width="3" stroke-linecap="round"/><text x="102" y="24" text-anchor="middle" font-size="22" font-weight="800" fill="#e0454f">+</text>',
 'taxman': '<circle cx="60" cy="40" r="24" fill="#ffd37a"/>' + _face(60, 40, 24, 'flat') + '<rect x="40" y="10" width="40" height="10" rx="2" fill="#1b2d55"/><rect x="48" y="2" width="24" height="12" rx="2" fill="#1b2d55"/>'
           + '<path d="M28 112q0-44 32-44t32 44z" fill="#5d6a86"/><rect x="66" y="74" width="40" height="30" rx="4" fill="#fff" stroke="#1b2d55" stroke-width="2.5"/><text x="86" y="95" text-anchor="middle" font-size="15" font-weight="800" fill="#e0454f">23%</text>',
 'worker': '<circle cx="60" cy="40" r="24" fill="#ffd37a"/>' + _face(60, 40, 24) + '<path d="M36 34q24-26 48 0z" fill="#e8960c"/><path d="M28 112q0-44 32-44t32 44z" fill="#27447f"/>',
 'investor': '<circle cx="60" cy="40" r="24" fill="#ffd37a"/>' + _face(60, 40, 24) + '<path d="M28 112q0-44 32-44t32 44z" fill="#1b2d55"/><path d="M60 68l-6 14 6 30 6-30z" fill="#ff6a4d"/>'
             + '<rect x="84" y="80" width="30" height="22" rx="3" fill="#8a5a2b"/><path d="M92 80v-6h14v6" fill="none" stroke="#5b3a1a" stroke-width="3"/>',
 'truck': '<rect x="8" y="40" width="64" height="44" rx="4" fill="#0f9d90"/><path d="M72 52h22l14 16v16H72z" fill="#27447f"/><circle cx="28" cy="90" r="10" fill="#1b2d55"/><circle cx="90" cy="90" r="10" fill="#1b2d55"/>'
          + '<text x="40" y="70" text-anchor="middle" font-size="16" font-weight="800" fill="#fff">☕</text>',
 'scales2': '<path d="M60 16v80M34 104h52" stroke="#1b2d55" stroke-width="5" stroke-linecap="round"/><path d="M14 36h92" stroke="#8a5a2b" stroke-width="5" stroke-linecap="round"/>'
            + '<path d="M14 36l-10 26h20zM106 36l-10 26h20z" fill="#ffd37a" stroke="#a86703" stroke-width="2"/><text x="14" y="82" text-anchor="middle" font-size="18" font-weight="800" fill="#1b2d55">A</text><text x="106" y="82" text-anchor="middle" font-size="18" font-weight="800" fill="#1b2d55">L+E</text>',
})


def PIPE(n=0):
    """The reporting pipe, right to left as Hebrew reads: events come in from the right, the four steps light up in turn, four statements leave on the left."""
    if MODE == 'pdf':
        return ''
    rec = lambda i: (f'<g class="pp-ev e{i}"><rect x="-17" y="-21" width="34" height="42" rx="4" fill="#fff" stroke="#1b2d55" stroke-width="2.2"/>'
                     f'<path d="M-10 -10h20M-10 -2h20M-10 6h12" stroke="#8a93aa" stroke-width="2.4"/><text x="0" y="17" font-size="10" text-anchor="middle" font-weight="800" fill="#c4421f">₪</text></g>')
    steps = ['רישום', 'מיון', 'סיכום', 'דיווח']
    box = ''.join(f'<g class="pp-s s{i}"><rect x="{306 - 62 * i}" y="70" width="56" height="34" rx="8" fill="#e8eefb" stroke="#27447f" stroke-width="2"/>'
                  f'<text x="{334 - 62 * i}" y="93" font-size="15" text-anchor="middle" font-weight="800" fill="#1b2d55" direction="rtl">{t}</text></g>' for i, t in enumerate(steps))
    docs = ''.join(f'<g class="pp-doc d{i}" transform="translate({54 - 34 * (i % 2)} {40 + 44 * (i // 2)})"><rect x="0" y="0" width="28" height="36" rx="3" fill="#fff" stroke="#0f9d90" stroke-width="2.4"/>'
                   f'<path d="M6 10h16M6 17h16M6 24h10" stroke="#0f9d90" stroke-width="2"/></g>' for i in range(4))
    g = ('<rect x="106" y="40" width="268" height="94" rx="16" fill="#fff" stroke="#1b2d55" stroke-width="3"/>'
         '<text x="240" y="62" font-size="17" text-anchor="middle" font-weight="800" fill="#1b2d55" direction="rtl">חשבונאות פיננסית</text>'
         + box + rec(0) + rec(1) + rec(2) + docs
         + '<path d="M380 87h30" stroke="#8a93aa" stroke-width="3"/><path d="M90 87h12" stroke="#8a93aa" stroke-width="3"/>'
         '<text x="480" y="150" font-size="16" text-anchor="middle" font-weight="800" fill="#5d6a86" direction="rtl">עסקאות</text>'
         '<text x="50" y="150" font-size="16" text-anchor="middle" font-weight="800" fill="#0f9d90" direction="rtl">דוחות כספיים</text>')
    inner = _svg(g, '0 0 560 160', 'pipe') + '<div class="anim-cap">' + TX('עסקאות נכנסות, עוברות רישום, מיון וסיכום, ויוצאות כדוחות כספיים לקוראים מחוץ לעסק.') + '</div>'
    return ST(n, inner, cls='card animw') if n else f'<div class="card animw">{inner}</div>'


def SCALE(n=0, left='נכסים', right='התחייבויות + הון עצמי'):
    """The balance sheet identity as a scale: every transaction adds to both pans, so the beam always comes back to level."""
    if MODE == 'pdf':
        return ''
    coin = lambda x, y, c: f'<circle cx="{x}" cy="{y}" r="10" fill="{c}" stroke="#a86703" stroke-width="2"/>'
    g = ('<path d="M240 40v120M180 170h120" stroke="#1b2d55" stroke-width="7" stroke-linecap="round"/><polygon points="240,30 228,48 252,48" fill="#1b2d55"/>'
         '<g class="sc-beam"><path d="M80 48h320" stroke="#8a5a2b" stroke-width="8" stroke-linecap="round"/>'
         '<path d="M80 48l-46 56h92zM400 48l-46 56h92z" fill="#ffd37a" stroke="#a86703" stroke-width="2.5"/>'
         + ''.join(f'<g class="sc-c l{i}">{coin(60 + 20 * i, 94, "#7fe3d6")}</g>' for i in range(3))
         + ''.join(f'<g class="sc-c r{i}">{coin(380 + 20 * i, 94, "#ffb199")}</g>' for i in range(3))
         + f'<text x="80" y="128" font-size="18" text-anchor="middle" font-weight="800" fill="#0f9d90" direction="rtl">{left}</text>'
         f'<text x="400" y="128" font-size="18" text-anchor="middle" font-weight="800" fill="#c4421f" direction="rtl">{right}</text></g>')
    inner = _svg(g, '0 0 480 178', 'scl') + '<div class="anim-cap">' + TX('כל עסקה נרשמת בשני צדדים. לכן המאזניים תמיד חוזרים לאיזון.') + '</div>'
    return ST(n, inner, cls='card animw') if n else f'<div class="card animw">{inner}</div>'


def HUB(users, center='קפה נועה בע״מ', W=760, H=316):
    """The company in the centre and its readers around it. users: (label, question, toon key, click, inside?)."""
    cx, cy = W / 2, H / 2
    import math
    p = [f'<ellipse cx="{cx}" cy="{cy}" rx="104" ry="40" fill="#1b2d55"/><text x="{cx}" y="{cy + 7}" font-size="21" text-anchor="middle" font-weight="800" fill="#fff" direction="rtl">{center}</text>']
    k = len(users)
    for i, (lab, q, tk, s, inside) in enumerate(users):
        a = math.pi * (0.5 + 2 * i / k)
        x, y = cx + 272 * math.cos(a), cy - 116 * math.sin(a)
        col = {0: '#0f9d90', 1: '#e8960c', 2: '#8a93aa'}[inside]
        art = TOONS.get(tk, '')
        g = (f'<line x1="{cx + 100 * math.cos(a):.1f}" y1="{cy - 38 * math.sin(a):.1f}" x2="{x:.1f}" y2="{y:.1f}" stroke="{col}" stroke-width="2.4" stroke-dasharray="5 5"/>'
             f'<g transform="translate({x - 104:.1f} {y - 27:.1f})"><rect x="0" y="0" width="208" height="54" rx="12" fill="#fff" stroke="{col}" stroke-width="2.6"/>'
             f'<g transform="translate(6 7) scale(.34)">{art}</g>'
             f'<text x="198" y="23" font-size="17" text-anchor="start" font-weight="800" fill="#1b2d55" direction="rtl">{lab}</text>'
             f'<text x="198" y="44" font-size="14" text-anchor="start" font-weight="600" fill="#5d6a86" direction="rtl">{q}</text></g>')
        p.append(f'<g{_st(s)}>{g}</g>')
    return f'<svg class="hub" dir="ltr" viewBox="0 0 {W} {H}" role="img" style="direction:ltr">' + ''.join(p) + '</svg>'


def LADDER(levels, W=760):
    """The sources of reporting rules, as steps from the law down to the company. levels: (title, text, click)."""
    p = []
    h = 58
    for i, (t, d, s) in enumerate(levels):
        w = W - 70 * i
        x = (W - w) / 2
        y = 6 + i * (h + 8)
        col = ['#1b2d55', '#27447f', '#0f9d90', '#e8960c', '#c4421f'][i % 5]
        g = (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{col}"/>'
             f'<text x="{x + w - 18}" y="{y + 26}" font-size="20" text-anchor="start" font-weight="800" fill="#fff" direction="rtl">{t}</text>'
             f'<text x="{x + w - 18}" y="{y + 50}" font-size="16" text-anchor="start" font-weight="600" fill="#e8eefb" direction="rtl">{d}</text>')
        p.append(f'<g{_st(s)}>{g}</g>')
    H = 6 + len(levels) * (h + 8)
    return f'<svg class="ladder" dir="ltr" viewBox="0 0 {W} {H}" role="img" style="direction:ltr">' + ''.join(p) + '</svg>'


# ---------------------------------------------------------------- meeting 2 (2026-11-12): larger illustrations for the recap, the intro and the case
TOONS.update({
 'book': '<rect x="22" y="14" width="70" height="92" rx="6" fill="#27447f"/><rect x="30" y="14" width="6" height="92" fill="#1b2d55"/><rect x="44" y="30" width="38" height="24" rx="4" fill="#ffd37a"/>'
         '<text x="63" y="49" text-anchor="middle" font-size="20" font-weight="800" fill="#1b2d55">§</text><path d="M44 66h38M44 76h30M44 86h34" stroke="#c9d6ee" stroke-width="3"/><path d="M92 20q14 4 10 22" fill="none" stroke="#ff6a4d" stroke-width="4"/>',
 'box': '<path d="M18 52h84v54H18z" fill="#c8945a" stroke="#8a5a2b" stroke-width="3"/><path d="M18 52l10-16h64l10 16z" fill="#deb07a" stroke="#8a5a2b" stroke-width="3"/>'
        '<g fill="#fff" stroke="#8a93aa" stroke-width="1.5"><rect x="30" y="20" width="20" height="34" rx="2" transform="rotate(-14 40 37)"/><rect x="50" y="12" width="20" height="40" rx="2"/><rect x="70" y="20" width="20" height="34" rx="2" transform="rotate(12 80 37)"/></g>'
        '<path d="M54 22h12M54 28h12M54 34h8" stroke="#8a93aa" stroke-width="2"/><text x="60" y="88" text-anchor="middle" font-size="20" font-weight="800" fill="#5b3a1a">?!</text>',
 'family': '<ellipse cx="60" cy="86" rx="52" ry="14" fill="#8a5a2b"/><rect x="14" y="80" width="92" height="8" fill="#a8743f"/>'
           + ''.join(f'<circle cx="{x}" cy="{y}" r="13" fill="{c}"/>' + _face(x, y, 13) for x, y, c in [(26, 58, '#ffd37a'), (60, 50, '#ffcf9e'), (94, 58, '#f5c28c')])
           + '<path d="M44 78q16-12 32 0" fill="#fff" stroke="#e8960c" stroke-width="2"/><circle cx="60" cy="74" r="5" fill="#ff6a4d"/>',
 'shop': '<rect x="10" y="30" width="100" height="76" fill="#e8eefb" stroke="#1b2d55" stroke-width="3"/><path d="M6 30h108l-8-16H14z" fill="#ff6a4d"/>'
         '<path d="M14 30q8 10 16 0q8 10 16 0q8 10 16 0q8 10 16 0q8 10 16 0q8 10 16 0" fill="#ffb199"/><rect x="20" y="46" width="80" height="44" fill="#fff" stroke="#27447f" stroke-width="3"/>'
         '<rect x="34" y="58" width="12" height="20" fill="#0f9d90"/><rect x="52" y="52" width="12" height="26" fill="#25a65f"/><rect x="70" y="62" width="12" height="16" fill="#e8960c"/>'
         + ''.join(f'<circle cx="{x}" cy="108" r="7" fill="#ffd37a" stroke="#a86703" stroke-width="1.5"/>' for x in (18, 34, 50, 66, 82, 98)),
 'barista': '<path d="M30 116q0-40 30-40t30 40z" fill="#0f9d90"/><rect x="46" y="84" width="28" height="32" rx="4" fill="#fff"/><circle cx="60" cy="48" r="24" fill="#ffcf9e"/>'
            + _face(60, 50, 24) + '<path d="M36 44q2-26 24-26t24 26q-6-14-24-14t-24 14z" fill="#5b3a1a"/><path d="M84 40q10 10 4 26" fill="none" stroke="#5b3a1a" stroke-width="7" stroke-linecap="round"/>',
 'banker': '<path d="M28 116q0-42 32-42t32 42z" fill="#1b2d55"/><path d="M60 76l-7 12 7 26 7-26z" fill="#e0454f"/><circle cx="60" cy="46" r="24" fill="#f5c28c"/>' + _face(60, 48, 24)
           + '<path d="M38 36q4-18 22-18t22 18q-10-8-22-8t-22 8z" fill="#3a3a3a"/><rect x="86" y="86" width="26" height="22" rx="3" fill="#ffd37a" stroke="#a86703" stroke-width="2"/><text x="99" y="102" text-anchor="middle" font-size="14" font-weight="800" fill="#a86703">₪</text>',
 'apt': '<rect x="22" y="18" width="76" height="92" fill="#e8eefb" stroke="#1b2d55" stroke-width="3"/><path d="M16 20h88" stroke="#1b2d55" stroke-width="5"/>'
        + ''.join(f'<rect x="{x}" y="{y}" width="14" height="12" fill="#7fe3d6" stroke="#0f9d90" stroke-width="1.5"/>' for y in (28, 48, 68) for x in (32, 53, 74))
        + '<rect x="52" y="88" width="16" height="22" fill="#8a5a2b"/><circle cx="96" cy="16" r="10" fill="#ffd37a"/>',
})
