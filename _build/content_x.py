# Visuals and sheet helpers of the course סוגיות בחשבונאות (statement analysis and valuation). Inline SVG and HTML only, no outside images.
TOONS.update({
 'sofa': '<rect x="14" y="52" width="92" height="34" rx="10" fill="#0f9d90"/><rect x="8" y="60" width="18" height="34" rx="8" fill="#087469"/><rect x="94" y="60" width="18" height="34" rx="8" fill="#087469"/>'
         '<rect x="22" y="34" width="76" height="30" rx="12" fill="#58e0cf"/><path d="M24 94v10M96 94v10" stroke="#5b3a1a" stroke-width="6" stroke-linecap="round"/>' + _face(60, 50, 16),
 'thermo': '<rect x="50" y="10" width="20" height="74" rx="10" fill="#fff" stroke="#1b2d55" stroke-width="4"/><circle cx="60" cy="94" r="18" fill="#e0454f" stroke="#1b2d55" stroke-width="4"/>'
           '<rect x="56" y="38" width="8" height="52" fill="#e0454f"/><path d="M74 24h10M74 38h10M74 52h10M74 66h10" stroke="#1b2d55" stroke-width="3" stroke-linecap="round"/><text x="100" y="30" font-size="15" font-weight="800" fill="#e0454f" text-anchor="middle">38.5</text>',
 'dress': '<path d="M46 14h28l-4 18 22 66H28l22-66z" fill="#ff8fa6" stroke="#7a2a3a" stroke-width="3"/><path d="M46 14q14 12 28 0" fill="none" stroke="#7a2a3a" stroke-width="3"/><path d="M50 32h20" stroke="#7a2a3a" stroke-width="3"/>'
          '<path d="M40 104l-6 10M80 104l6 10" stroke="#7a2a3a" stroke-width="3" stroke-linecap="round"/><text x="100" y="30" font-size="15" font-weight="800" fill="#e0454f" text-anchor="middle">70%−</text>',
 'chip': '<rect x="30" y="30" width="60" height="60" rx="8" fill="#1b2d55"/><rect x="42" y="42" width="36" height="36" rx="4" fill="#25a65f"/>'
         + ''.join(f'<path d="M{38 + 11 * i} 30v-12M{38 + 11 * i} 90v12M30 {38 + 11 * i}h-12M90 {38 + 11 * i}h12" stroke="#8a93aa" stroke-width="4" stroke-linecap="round"/>' for i in range(5)) + _face(60, 60, 16),
 'cart': '<path d="M10 24h16l14 50h50l10-36H32" fill="none" stroke="#1b2d55" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/><circle cx="46" cy="92" r="8" fill="#1b2d55"/><circle cx="84" cy="92" r="8" fill="#1b2d55"/>'
         '<rect x="42" y="44" width="14" height="22" fill="#ff6a4d"/><rect x="60" y="40" width="14" height="26" fill="#0f9d90"/><rect x="78" y="46" width="12" height="20" fill="#e8960c"/>',
 'light': '<rect x="38" y="8" width="44" height="100" rx="14" fill="#1b2d55"/><circle cx="60" cy="30" r="12" fill="#e0454f"/><circle cx="60" cy="58" r="12" fill="#f0b429"/><circle cx="60" cy="86" r="12" fill="#25a65f"/>',
 'safe': '<rect x="16" y="18" width="88" height="80" rx="8" fill="#5d6a86" stroke="#1b2d55" stroke-width="4"/><rect x="26" y="28" width="68" height="60" rx="5" fill="#8a93aa"/><circle cx="60" cy="58" r="16" fill="#e8eefb" stroke="#1b2d55" stroke-width="3"/>'
         '<path d="M60 44v28M46 58h28" stroke="#1b2d55" stroke-width="3"/><path d="M26 98v10M94 98v10" stroke="#1b2d55" stroke-width="6" stroke-linecap="round"/><text x="60" y="16" font-size="13" font-weight="800" fill="#a86703" text-anchor="middle">₪ ₪ ₪</text>',
 'detective': '<circle cx="54" cy="52" r="26" fill="#ffcf9e"/>' + _face(54, 54, 26) + '<path d="M24 40q30-34 60 0z" fill="#8a5a2b"/><rect x="18" y="38" width="72" height="7" rx="3" fill="#5b3a1a"/>'
              '<path d="M22 116q0-36 32-36t32 36z" fill="#27447f"/><circle cx="96" cy="82" r="14" fill="#dff5f2" fill-opacity=".8" stroke="#0f9d90" stroke-width="5"/><path d="M106 92l10 12" stroke="#0f9d90" stroke-width="7" stroke-linecap="round"/>',
 'builder': '<circle cx="60" cy="42" r="22" fill="#ffd37a"/>' + _face(60, 44, 22) + '<path d="M38 36q22-26 44 0z" fill="#e8960c"/><rect x="34" y="34" width="52" height="6" rx="3" fill="#a86703"/><path d="M28 114q0-44 32-44t32 44z" fill="#ff6a4d"/>'
            '<rect x="84" y="78" width="26" height="12" fill="#c8945a" stroke="#8a5a2b" stroke-width="2"/><rect x="88" y="92" width="26" height="12" fill="#c8945a" stroke="#8a5a2b" stroke-width="2"/>',
})

_tw = lambda head, blocks: '<div class="tower"><div class="tw-h">' + head + '</div><div class="tw-b">' + ''.join(blocks) + '</div></div>'


def BK(n, lab, amt, cls, flex, veil=0, vt='לא נספר'):
    """One block of a tower. veil: the click at which the block is struck out of the ratio."""
    if MODE == 'pdf': return f'<span class="pblk">{TX(lab)} <span class="n">{amt}</span></span>'
    v = ST(veil, TX(vt), cls='veil') if veil else ''
    inner = f'<b>{TX(lab)}</b><span class="n">{amt}</span>{v}'
    if not n: return f'<div class="blk {cls} show" style="flex:{flex} 1 0">{inner}</div>'
    return ST(n, inner, cls=f'blk {cls}" style="flex:{flex} 1 0')


def RES(n, name, val, sub='', k=''):
    if MODE == 'pdf': return f'<span class="pres"><b>{TX(name)}:</b> <span class="n">{val}</span>' + (f' ({TX(sub)})' if sub else '') + '</span>'
    return POP(n, f'<span>{TX(name)}</span><b class="n">{val}</b>' + (f'<em>{TX(sub)}</em>' if sub else ''), 'rres ' + k)


def RT(top, bottom, results, th='נכסים שוטפים', bh='התחייבויות שוטפות', op='÷', n_op=0, cls=''):
    """A ratio as two towers: the numerator, the operator, the denominator, and the results that appear click by click."""
    if MODE == 'pdf':
        return (f'<table class="tbl2 prt"><tr><th>{th}</th><th>{bh}</th><th>התוצאה</th></tr><tr><td>' + '<br>'.join(top) + '</td><td>' + '<br>'.join(bottom) + '</td><td>' + '<br>'.join(results) + '</td></tr></table>')
    o = POP(n_op, f'<div class="rt-op">{op}</div>', 'eqw') if n_op else f'<div class="eqw"><div class="rt-op">{op}</div></div>'
    return f'<div class="rt {cls}">' + _tw(th, top) + o + _tw(bh, bottom) + '<div class="rt-res">' + ''.join(results) + '</div></div>'


def RDEF(n, he, en, num, den, key=None, pct=False, op='÷'):
    """The definition of a ratio in words: numerator over denominator, with its English name. A definition, not a solution: solutions are Excel formulas."""
    nm = f'[[{key}|{he}]]' if key else he
    if MODE == 'pdf':
        return f'<div class="band prdef"><b>{TX(nm)}</b> <bdi dir="ltr">({en})</bdi> = {TX(num)} <b>{"חלקי" if op == "÷" else op}</b> {TX(den)}</div>'
    inner = (f'<div class="rd-n"><b>{TX(nm)}</b><bdi dir="ltr">{en}</bdi></div><div class="rd-eq">=</div>'
             f'<div class="rd-f"><span>{TX(num)}</span><i></i><span>{TX(den)}</span></div>') if op == '÷' else \
            (f'<div class="rd-n"><b>{TX(nm)}</b><bdi dir="ltr">{en}</bdi></div><div class="rd-eq">=</div><div class="rd-l"><span>{TX(num)}</span><u>{op}</u><span>{TX(den)}</span></div>')
    return ST(n, inner, cls='rdef pop') if n else f'<div class="rdef">{inner}</div>'


def GAUGE(val, n=0, lo=0.0, hi=3.0, cap='', zones=((0, .8, '#e0454f'), (.8, 1.0, '#f0b429'), (1.0, 3.0, '#25a65f')), ticks=(0, 1, 2, 3)):
    """A half-circle gauge. The needle swings to the value when the step is revealed."""
    import math
    if MODE == 'pdf': return ''
    cx, cy, r = 160, 150, 120
    P = lambda v, rr=r: (cx - rr * math.cos(math.pi * (v - lo) / (hi - lo)), cy - rr * math.sin(math.pi * (v - lo) / (hi - lo)))
    arcs = ''
    for a, b, c in zones:
        (x1, y1), (x2, y2) = P(a), P(b)
        arcs += f'<path d="M{x1:.1f} {y1:.1f} A{r} {r} 0 0 1 {x2:.1f} {y2:.1f}" fill="none" stroke="{c}" stroke-width="26"/>'
    tk = ''.join(f'<text x="{P(t, r - 34)[0]:.1f}" y="{P(t, r - 34)[1] + 6:.1f}" font-size="18" font-weight="800" text-anchor="middle" fill="#1b2d55">{t}</text>' for t in ticks)
    ang = 180 * (min(max(val, lo), hi) - lo) / (hi - lo)
    ndl = f'<g class="ndl{" st" if n else ""}"{f" data-n={chr(34)}{n * 10}{chr(34)}" if n else ""} style="--a:{ang:.1f}deg"><path d="M{cx - 96} {cy}L{cx} {cy - 7}L{cx} {cy + 7}z" fill="#1b2d55"/></g>'
    v = ''
    _unused = f'<text x="{cx}" y="{cy - 28}" font-size="34" font-weight="800" text-anchor="middle" fill="#1b2d55"{f" class={chr(34)}st{chr(34)} data-n={chr(34)}{n * 10}{chr(34)}" if n else ""}>{val:g}</text>'
    svg = f'<svg viewBox="0 0 320 170" dir="ltr" class="gauge" role="img">{arcs}{tk}{ndl}<circle cx="{cx}" cy="{cy}" r="11" fill="#1b2d55"/>{v}</svg>'
    return f'<div class="gaugew">{svg}' + (f'<div class="g-cap">{TX(cap)}</div>' if cap else '') + '</div>'


def YEAR12(items_up, items_dn):
    """The coming year as an axis from the balance sheet date to twelve months later. Resources above it, obligations under it; each item is (click, label, month)."""
    if MODE == 'pdf':
        return ('<table class="tbl2 prt"><tr><th>מה צריך לשלם בשנה הקרובה</th><th>מה יהפוך למזומן בשנה הקרובה</th></tr><tr><td>' + '<br>'.join(TX(l) for _, l, _ in items_dn) + '</td><td>' + '<br>'.join(TX(l) for _, l, _ in items_up) + '</td></tr></table>')
    W, H, x0, x1, y = 1100, 290, 70, 880, 140
    X = lambda m: x0 + (x1 - x0) * m / 12
    p = [f'<line x1="{x0 - 30}" y1="{y}" x2="{x1 + 40}" y2="{y}" stroke="#1b2d55" stroke-width="5" stroke-linecap="round"/><polygon points="{x1 + 54},{y} {x1 + 36},{y - 9} {x1 + 36},{y + 9}" fill="#1b2d55"/>']
    for m in range(0, 13, 3):
        p.append(f'<line x1="{X(m)}" y1="{y - 9}" x2="{X(m)}" y2="{y + 9}" stroke="#1b2d55" stroke-width="3"/>')
    for m, d, c in ((0, '31.12.2026', 'תאריך המאזן'), (12, '31.12.2027', 'שנה אחר כך')):
        p.append(f'<rect x="{X(m) - 62}" y="{y + 110}" width="124" height="54" rx="12" fill="#1b2d55"/><text x="{X(m)}" y="{y + 132}" font-size="18" font-weight="800" text-anchor="middle" fill="#fff">{d}</text>'
                 f'<text x="{X(m)}" y="{y + 154}" font-size="16" font-weight="700" text-anchor="middle" fill="#c8d4f2" direction="rtl">{c}</text><line x1="{X(m)}" y1="{y + 12}" x2="{X(m)}" y2="{y + 110}" stroke="#1b2d55" stroke-width="2" stroke-dasharray="3 5"/>')
    def chip(s, lab, m, up, k):
        w = 34 + len(lab) * 10.5
        yy = (y - 50 - 46 * (k % 2)) if up else (y + 46 + 0 * (k % 2))
        cx = min(max(X(m) + (0 if up else 70), w / 2 + 4), W - w / 2 - 4)
        col, bg = ('#087469', '#d7f1ec') if up else ('#b8391f', '#fde2da')
        return (f'<g{_st(s)}><line x1="{X(m)}" y1="{y}" x2="{X(m)}" y2="{yy + (18 if up else -18)}" stroke="{col}" stroke-width="2.5" stroke-dasharray="4 4"/><circle cx="{X(m)}" cy="{y}" r="7" fill="{col}"/>'
                f'<rect x="{cx - w / 2}" y="{yy - 18}" width="{w}" height="36" rx="18" fill="{bg}" stroke="{col}" stroke-width="2.5"/>'
                f'<text x="{cx}" y="{yy + 6}" font-size="18" font-weight="800" text-anchor="middle" fill="{col}" direction="rtl">{lab}</text></g>')
    for k, (s, lab, m) in enumerate(items_up): p.append(chip(s, lab, m, True, k))
    for k, (s, lab, m) in enumerate(items_dn): p.append(chip(s, lab, m, False, k))
    for yy, lab, col, bg in ((y - 62, 'מה יהפוך למזומן', '#087469', '#d7f1ec'), (y + 46, 'מה צריך לשלם', '#b8391f', '#fde2da')):
        p.append(f'<rect x="{W - 172}" y="{yy - 22}" width="168" height="44" rx="10" fill="{col}"/><text x="{W - 88}" y="{yy + 7}" font-size="19" font-weight="800" text-anchor="middle" fill="#fff" direction="rtl">{lab}</text>')
    return f'<svg class="year12" dir="ltr" viewBox="0 0 {W} {H + 10}" role="img">' + ''.join(p) + '</svg>'


def LANE(n, who, a, b, art, k=''):
    if MODE == 'pdf': return f'<p><b>{TX(who)}:</b> {TX("מתחילים מ" + a + ", ומגיעים אל " + b + ".")}</p>'
    return POP(n, f'<div class="ln-art">{_svg(TOONS[art])}</div><div class="ln-who">{TX(who)}</div><div class="ln-flow"><span>{TX(a)}</span><i>←</i><span class="hot">{TX(b)}</span></div>', 'lane ' + k)


def GRP6(items, cur=0):
    """The six groups of ratios, one card per click: (icon, name, English, the question it answers, lecture)."""
    if MODE == 'pdf':
        return '<table class="tbl2"><tr><th>קבוצת היחסים</th><th>באנגלית</th><th>השאלה שהיא שואלת</th><th>מתי</th></tr>' + ''.join(f'<tr><td><b>{TX(he)}</b></td><td><bdi dir="ltr">{en}</bdi></td><td>{TX(q)}</td><td>{TX(lec)}</td></tr>' for ic, he, en, q, lec in items) + '</table>'
    out = ''
    for i, (ic, he, en, q, lec) in enumerate(items):
        out += POP(i + 1, f'<div class="g6-i">{ic}</div><b>{TX(he)}</b><bdi dir="ltr">{en}</bdi><p>{TX(q)}</p><em>{TX(lec)}</em>', 'g6c' + (' cur' if i == cur else ''))
    return '<div class="grp6">' + out + '</div>'


def STEPS4(items):
    """How near each current asset is to cash: (click, name, amount, steps text, class)."""
    if MODE == 'pdf':
        return '<table class="tbl2"><tr><th>הנכס השוטף</th><th>אלפי ש״ח</th><th>המרחק מהמזומן</th></tr>' + ''.join(f'<tr><td><b>{TX(name)}</b></td><td><span class="n">{amt}</span></td><td>{TX(steps)}</td></tr>' for n, name, amt, steps, k in items) + '</table>'
    out = ''
    for n, name, amt, steps, k in items:
        out += POP(n, f'<b>{TX(name)}</b><span class="n">{amt}</span><p>{TX(steps)}</p>', 'liqs ' + k)
    return '<div class="liqrow">' + out + '</div>'


# ---------------------------------------------------------------- liquidity sheets
CA_L = ['מזומנים ושווי מזומנים', 'לקוחות', 'מלאי', 'הוצאות מראש']
CL_L = ['ספקים', 'הלוואות לזמן קצר', 'הוצאות לשלם']


def LIQD(ca, cl, totals=True, unit='אלפי ש״ח'):
    """A short balance sheet as on an exam sheet: current assets in A:B (rows 2-5, total in row 6), current liabilities in C:D (rows 2-4, total in row 6).
    Returns (labels, given numbers, formats, totals as formulas, styles). The amounts are given; the student writes only formulas, from row 8 down."""
    lab = {'A1': 'נכסים שוטפים', 'B1': unit, 'C1': 'התחייבויות שוטפות', 'D1': unit, 'A6': 'סך הנכסים השוטפים', 'C6': 'סך ההתחייבויות השוטפות'}
    giv = {}
    for i, (l, v) in enumerate(zip(CA_L, ca)): lab[f'A{2 + i}'] = l; giv[f'B{2 + i}'] = v
    for i, (l, v) in enumerate(zip(CL_L, cl)): lab[f'C{2 + i}'] = l; giv[f'D{2 + i}'] = v
    tot = {'B6': '=SUM(B2:B5)', 'D6': '=SUM(D2:D4)'}
    if totals: giv.update({'B6': sum(ca), 'D6': sum(cl)})
    fmt = {f'{c}{r}': 'num0' for c in 'BD' for r in range(2, 7)}
    sty = {**{f'{c}6': {'b': True} for c in 'ABCD'}, **{f'{c}1': {'b': True, 'fill': '#e1e7f8'} for c in 'ABCD'}}
    return lab, giv, fmt, tot, sty


LW = [190, 72, 172, 72]
