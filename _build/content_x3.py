# Visuals of lecture 3 (efficiency ratios), usable in later lectures too: the lecture map of five stations, pictures that replace
# each other, the journey of one shekel, the cycle on a time axis, turnover as "average shelves" sold in a year, one number per click,
# news items in our own words, a drawn report excerpt, a column chart with negative values, and the "end of month + 60" calendar.
# Inline SVG and HTML only, no outside images.
K_INV, K_AR, K_AP, K_CC, K_AS = '#0f9d90', '#e8960c', '#6d4df2', '#c4421f', '#27447f'
STATIONS = [('📦', 'מלאי', 'ימי מלאי'), ('🧾', 'לקוחות', 'ימי לקוחות'), ('🚚', 'ספקים', 'ימי ספקים'), ('🔄', 'המחזור כולו', 'מחזור המרת המזומן'), ('🏭', 'הנכסים', 'מחזור נכסים')]


def CYCMAP(cur=-1, cls=''):
    """The map of the lecture: five stations in reading order, the current one lit, the earlier ones done."""
    if MODE == 'pdf':
        return ''
    out = []
    for i, (ic, h, m) in enumerate(STATIONS):
        k = 'cur' if i == cur else ('done' if 0 <= i < cur else '')
        out.append(f'<div class="cm-s {k}"><i>{ic}</i><b>{h}</b><span>{m}</span></div>')
    return f'<div class="cmap {cls}">' + '<em>←</em>'.join(out) + '</div>'


def SWAP(frames, h=260, cls=''):
    """Pictures that replace each other. frames: (click, svg, caption); click 0 is the first picture, each later one covers it at its click."""
    if MODE == 'pdf':
        return '<ol class="pl">' + ''.join(f'<li>{TX(c)}</li>' for _, _, c in frames) + '</ol>'
    out = ''
    for n, svg, cap in frames:
        inner = f'<div class="fr-art">{svg}</div><div class="fr-cap">{TX(cap)}</div>'
        out += ST(n, inner, cls='fr') if n else f'<div class="fr base">{inner}</div>'
    return f'<div class="swap {cls}" style="height:{h}px">{out}</div>'


def _coin(cx, cy, r, mood='smile', fill='#ffd37a'):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="#a86703" stroke-width="3"/>' + _face(cx, cy + r * .08, r * .82, mood)


def _truck(x, y, lab, col='#6d4df2', flip=False, load=''):
    t = (f'<rect x="0" y="0" width="128" height="64" rx="7" fill="{col}"/>{load}<path d="M128 18h34l22 24v22H128z" fill="#1b2d55"/><rect x="136" y="25" width="24" height="16" rx="2" fill="#c8d4f2"/>'
         '<circle cx="32" cy="70" r="13" fill="#1b2d55"/><circle cx="32" cy="70" r="5" fill="#c8d4f2"/><circle cx="150" cy="70" r="13" fill="#1b2d55"/><circle cx="150" cy="70" r="5" fill="#c8d4f2"/>')
    lab_x = 64
    if flip:
        return (f'<g transform="translate({x + 184} {y}) scale(-1 1)">{t}</g>'
                f'<text x="{x + 184 - lab_x}" y="{y + 40}" text-anchor="middle" font-size="16" font-weight="800" fill="#fff" direction="rtl">{lab}</text>')
    return f'<g transform="translate({x} {y})">{t}<text x="{lab_x}" y="40" text-anchor="middle" font-size="16" font-weight="800" fill="#fff" direction="rtl">{lab}</text></g>'


def _plant(x, y, lab, inside=''):
    return (f'<path d="M{x} {y + 44}L{x + 92} {y}L{x + 184} {y + 44}Z" fill="#27447f"/><rect x="{x + 8}" y="{y + 44}" width="168" height="120" fill="#e8eefb" stroke="#1b2d55" stroke-width="3"/>'
            f'<text x="{x + 92}" y="{y + 34}" text-anchor="middle" font-size="15" font-weight="800" fill="#fff" direction="rtl">{lab}</text>{inside}')


def _coat(x, y, c='#ff6a4d'):
    return (f'<g transform="translate({x} {y})"><path d="M10 0q8 7 16 0l12 6-4 15-6-2v30H8v-30l-6 2-4-15z" fill="{c}" stroke="#7a2a12" stroke-width="2"/>'
            '<path d="M18 4v45" stroke="#7a2a12" stroke-width="1.6"/><circle cx="14" cy="18" r="1.8" fill="#7a2a12"/><circle cx="14" cy="30" r="1.8" fill="#7a2a12"/></g>')


def _rolls(x, y):
    return ''.join(f'<g transform="translate({x + 34 * i} {y})"><rect x="0" y="0" width="26" height="40" rx="4" fill="{c}" stroke="#1b2d55" stroke-width="2"/><ellipse cx="13" cy="0" rx="13" ry="5" fill="#fff" stroke="#1b2d55" stroke-width="2"/></g>'
                   for i, c in enumerate(['#7fe3d6', '#ffb199', '#c8b6ff']))


def _invoice(x, y, amt='1.30 ₪'):
    return (f'<g transform="translate({x} {y})"><rect width="76" height="96" rx="6" fill="#fff" stroke="#1b2d55" stroke-width="3"/><text x="38" y="22" text-anchor="middle" font-size="14" font-weight="800" fill="#1b2d55" direction="rtl">חשבונית</text>'
            f'<path d="M12 36h52M12 48h52M12 60h34" stroke="#8a93aa" stroke-width="3"/><text x="38" y="84" text-anchor="middle" font-size="15" font-weight="800" fill="#c4421f">{amt}</text></g>')


def _store(x, y, lab='רשת אופנה'):
    stripes = ''.join(f'<rect x="{x + 10 + 24 * i}" y="{y + 40}" width="24" height="22" fill="{"#ff6a4d" if i % 2 == 0 else "#fff"}"/>' for i in range(7))
    return (f'<rect x="{x + 10}" y="{y + 60}" width="168" height="104" fill="#fff4e8" stroke="#1b2d55" stroke-width="3"/>{stripes}<rect x="{x + 6}" y="{y + 10}" width="176" height="32" rx="6" fill="#1b2d55"/>'
            f'<text x="{x + 94}" y="{y + 32}" text-anchor="middle" font-size="16" font-weight="800" fill="#fff" direction="rtl">{lab}</text><rect x="{x + 70}" y="{y + 110}" width="44" height="54" fill="#8a5a2b"/>'
            f'<rect x="{x + 22}" y="{y + 76}" width="38" height="30" fill="#7fe3d6"/><rect x="{x + 128}" y="{y + 76}" width="38" height="30" fill="#7fe3d6"/>')


def _tag(x, y, t, col, bg, w=None, fs=15):
    w = w or (len(t) * fs * .56 + 26)
    return (f'<rect x="{x - w / 2:.0f}" y="{y - 16}" width="{w:.0f}" height="32" rx="16" fill="{bg}" stroke="{col}" stroke-width="2.5"/>'
            f'<text x="{x}" y="{y + 6}" text-anchor="middle" font-size="{fs}" font-weight="800" fill="{col}" direction="rtl">{t}</text>')


def _scene(inner, vb='0 0 560 220'):
    return f'<svg viewBox="{vb}" dir="ltr" role="img" aria-hidden="true">{inner}</svg>'


def JOURNEY_FRAMES():
    """The four pictures of the journey of one shekel through a coat maker: purchase, payment to the supplier, sale on credit, collection."""
    coats_in = ''.join(_coat(392 + 34 * i, 128) for i in range(3))
    fa = _scene(_truck(14, 108, 'ספק בדים', '#6d4df2', load=_rolls(14, -38)) + '<path d="M214 150h120" stroke="#6d4df2" stroke-width="4" stroke-dasharray="8 7"/><path d="M326 141l14 9-14 9" fill="#6d4df2"/>'
                + _plant(366, 22, 'מעילי צפון', _rolls(398, 140)) + _tag(108, 30, 'נשלם בעוד 30 יום', '#6d4df2', '#efe9ff') + _coin(458, 100, 20) + _tag(458, 54, 'השקל בקופה', '#a86703', '#fff4d6'))
    fb = _scene(_plant(366, 22, 'מעילי צפון', coats_in) + f'<g>{_coin(270, 96, 22, "flat")}</g><path d="M236 96h-120" stroke="#a86703" stroke-width="4" stroke-dasharray="8 7"/><path d="M122 87l-14 9 14 9" fill="#a86703"/>'
                + '<rect x="16" y="64" width="90" height="92" rx="10" fill="#efe9ff" stroke="#6d4df2" stroke-width="3"/><text x="61" y="104" text-anchor="middle" font-size="16" font-weight="800" fill="#6d4df2" direction="rtl">הספק</text><text x="61" y="128" text-anchor="middle" font-size="14" font-weight="700" fill="#6d4df2" direction="rtl">קיבל את כספו</text>'
                + _tag(270, 36, 'יום 30: השקל יצא', '#a86703', '#fff4d6'))
    fc = _scene(_store(6, 22) + _truck(196, 112, 'מעילים', '#0f9d90', flip=True) + _plant(366, 22, 'מעילי צפון') + _invoice(240, 6) + _tag(400, 196, 'במקום מעיל: חשבונית', '#e8960c', '#fff4d6'))
    fd = _scene(_store(6, 22) + f'<g>{_coin(300, 92, 34)}</g><text x="300" y="150" text-anchor="middle" font-size="18" font-weight="800" fill="#107c41">+0.30</text>'
                + '<path d="M210 92h44" stroke="#a86703" stroke-width="4" stroke-dasharray="8 7"/><path d="M346 92h40" stroke="#a86703" stroke-width="4" stroke-dasharray="8 7"/><path d="M380 83l14 9-14 9" fill="#a86703"/>'
                + _plant(400, 22, 'מעילי צפון') + _tag(300, 196, 'השקל חזר, עם רווח', '#107c41', '#dcf5e6'))
    return fa, fb, fc, fd


def CYCLE_TL(dio, dso, dpo, clicks=(1, 2, 3, 4, 5), names=False, W=1000, maxd=None, title_cc='הכסף שלנו תקוע'):
    """The cycle on a time axis: inventory from purchase to sale, customers from sale to collection (above), supplier credit (below),
    then the whole operating cycle and the period the company finances itself. clicks: supplier, inventory, customers, operating cycle, the gap."""
    oc = dio + dso
    cc = oc - dpo
    maxd = maxd or max(oc, dpo) * 1.1 + 6
    x0, x1, y = 46, W - 70, 120
    X = lambda d: x0 + (x1 - x0) * d / maxd
    lab = (lambda a, b: b) if names else (lambda a, b: a)
    p = [f'<line x1="{x0 - 16}" y1="{y}" x2="{x1 + 26}" y2="{y}" stroke="#1b2d55" stroke-width="5" stroke-linecap="round"/><polygon points="{x1 + 44},{y} {x1 + 24},{y - 10} {x1 + 24},{y + 10}" fill="#1b2d55"/>',
         f'<text x="{x1 + 34}" y="{y + 34}" text-anchor="middle" font-size="20" font-weight="800" fill="#5d6a86" direction="rtl">ימים</text>']
    def mark(d, t, cl):
        return (f'<g{_st(cl)}><line x1="{X(d):.1f}" y1="{y - 10}" x2="{X(d):.1f}" y2="{y + 10}" stroke="#1b2d55" stroke-width="4"/><text x="{X(d):.1f}" y="{y + 32}" text-anchor="middle" font-size="22" font-weight="800" fill="#1b2d55">{d:g}</text>'
                f'<text x="{X(d):.1f}" y="{y + 56}" text-anchor="middle" font-size="19" font-weight="700" fill="#5d6a86" direction="rtl">{t}</text></g>')
    def bar(a, b, yy, h, col, bg, t, cl):
        return (f'<g{_st(cl)}><rect x="{X(a):.1f}" y="{yy}" width="{X(b) - X(a):.1f}" height="{h}" rx="10" fill="{bg}" stroke="{col}" stroke-width="3"/>'
                f'<text x="{(X(a) + X(b)) / 2:.1f}" y="{yy + h / 2 + 8:.1f}" text-anchor="middle" font-size="22" font-weight="800" fill="{col}" direction="rtl">{t}</text></g>')
    p.append(mark(0, 'קנייה', 0))
    p.append(mark(dpo, 'תשלום לספק', clicks[0]))
    p.append(bar(0, dpo, y + 66, 42, K_AP, '#efe9ff', lab(f'אשראי מהספק: {dpo:g} יום', f'ימי ספקים: {dpo:g}'), clicks[0]))
    p.append(mark(dio, 'מכירה', clicks[1]))
    p.append(bar(0, dio, y - 56, 42, K_INV, '#d7f1ec', lab(f'במחסן: {dio:g} יום', f'ימי מלאי: {dio:g}'), clicks[1]))
    p.append(mark(oc, 'גבייה', clicks[2]))
    p.append(bar(dio, oc, y - 56, 42, K_AR, '#fff0d2', lab(f'אצל הלקוח: {dso:g} יום', f'ימי לקוחות: {dso:g}'), clicks[2]))
    p.append(f'<g{_st(clicks[3])}><path d="M{X(0):.1f} {y - 66}v-14H{X(oc):.1f}v14" fill="none" stroke="#1b2d55" stroke-width="3"/>'
             f'<text x="{X(oc / 2):.1f}" y="{y - 90}" text-anchor="middle" font-size="22" font-weight="800" fill="#1b2d55" direction="rtl">{lab(f"מקנייה ועד מזומן: {oc:g} יום", f"מחזור תפעולי: {oc:g} יום")}</text></g>')
    if cc >= 0:
        p.append(f'<g{_st(clicks[4])}><rect x="{X(dpo):.1f}" y="{y + 118}" width="{X(oc) - X(dpo):.1f}" height="46" rx="12" fill="#fde2da" stroke="{K_CC}" stroke-width="3.5"/>'
                 f'<text x="{(X(dpo) + X(oc)) / 2:.1f}" y="{y + 149}" text-anchor="middle" font-size="24" font-weight="800" fill="{K_CC}" direction="rtl">{lab(f"{cc:g} יום: {title_cc}", f"מחזור המרת המזומן: {cc:g} יום")}</text></g>')
    else:
        p.append(f'<g{_st(clicks[4])}><rect x="{X(oc):.1f}" y="{y + 118}" width="{X(dpo) - X(oc):.1f}" height="46" rx="12" fill="#dcf5e6" stroke="#107c41" stroke-width="3.5"/>'
                 f'<text x="{(X(dpo) + X(oc)) / 2:.1f}" y="{y + 149}" text-anchor="middle" font-size="22" font-weight="800" fill="#107c41" direction="rtl">{lab(f"{-cc:g} יום: הכסף של הספק אצלנו", f"מחזור המרת המזומן: {cc:g} יום")}</text></g>')
    return f'<svg class="cyctl" viewBox="0 0 {W} {y + 172}" dir="ltr" role="img" aria-label="ציר הזמן של המחזור">' + ''.join(p) + '</svg>'

def CYCLE_TLP(dio, dso, dpo, names=True):
    """The print version of the cycle: a short table."""
    oc, cc = dio + dso, dio + dso - dpo
    rows = [('ימי מלאי: מהקנייה ועד המכירה', dio), ('ימי לקוחות: מהמכירה ועד הגבייה', dso), ('מחזור תפעולי: מהקנייה ועד המזומן', oc), ('ימי ספקים: מהקנייה ועד התשלום לספק', dpo), ('מחזור המרת המזומן: מחזור תפעולי פחות ימי ספקים', cc)]
    return '<table class="tbl2"><tr><th>הקטע</th><th>ימים</th></tr>' + ''.join(f'<tr><td>{TX(a)}</td><td class="amt">{TX(f"{b:g}")}</td></tr>' for a, b in rows) + '</table>'


def TURNVIS(k, avg, cogs, days, n_boxes, n_total, n_brace=0, unit='מלאי ממוצע', col=K_INV, bg='#d7f1ec'):
    """Turnover as boxes: the year's cost of sales is k boxes the size of the average inventory; each box is sold in 365/k days.
    A click of 0 shows that piece from the start; n_brace None leaves the brace out."""
    if MODE == 'pdf':
        return ''
    W, x0, x1, y = 1000, 40, 940, 192
    w = (x1 - x0) / k
    g = lambda n: f' class="st" data-n="{n * 10}"' if n else ''
    p = [f'<line x1="{x0}" y1="{y}" x2="{x1 + 16}" y2="{y}" stroke="#1b2d55" stroke-width="5" stroke-linecap="round"/><polygon points="{x1 + 34},{y} {x1 + 14},{y - 10} {x1 + 14},{y + 10}" fill="#1b2d55"/>']
    for d, t in ((0, '1.1'), (365, '31.12')):
        xx = x0 + (x1 - x0) * d / 365
        p.append(f'<line x1="{xx}" y1="{y - 10}" x2="{xx}" y2="{y + 10}" stroke="#1b2d55" stroke-width="4"/><text x="{xx}" y="{y + 34}" text-anchor="middle" font-size="22" font-weight="800" fill="#1b2d55">{t}</text>')
    for i in range(k):
        bx = x0 + i * w + 6
        cls = f' class="st an-pop" data-n="{n_boxes * 10}" style="--d:{i * .16:.2f}s"' if n_boxes else ''
        p.append(f'<g{cls}><rect x="{bx:.1f}" y="62" width="{w - 12:.1f}" height="116" rx="14" fill="{bg}" stroke="{col}" stroke-width="3.5"/>'
                 f'<text x="{bx + (w - 12) / 2:.1f}" y="122" text-anchor="middle" font-size="38" font-weight="800" fill="{col}">{avg:,}</text>'
                 f'<text x="{bx + (w - 12) / 2:.1f}" y="156" text-anchor="middle" font-size="19" font-weight="700" fill="{col}" direction="rtl">{unit}</text></g>')
    if n_brace is not None:
        p.append(f'<g{g(n_brace)}><path d="M{x0 + 6} {y + 46}v10H{x0 + w - 6:.1f}v-10" fill="none" stroke="{K_CC}" stroke-width="4"/>'
                 f'<text x="{x0 + w / 2:.1f}" y="{y + 84}" text-anchor="middle" font-size="24" font-weight="800" fill="{K_CC}" direction="rtl">כ-{days:g} יום</text></g>')
    p.append(f'<g{g(n_total)}><text x="{(x0 + x1) / 2}" y="40" text-anchor="middle" font-size="28" font-weight="800" fill="#1b2d55" direction="rtl">{k} פעמים {avg:,}: {cogs:,}, עלות המכר של השנה</text></g>')
    H = y + (92 if n_brace is not None else 44)
    return f'<svg class="turnvis" viewBox="0 0 {W} {H}" dir="ltr" role="img" aria-label="מחזור כמספר מדפים בשנה">' + ''.join(p) + '</svg>'


def WAITBAR(days, a, b, col, bg, n=0, cap=''):
    """One wait on a time axis, from a to b: the days of one station as a large bar."""
    if MODE == 'pdf':
        return ''
    W, x0, x1, y = 520, 78, 430, 150
    mx = days * 1.12
    X = lambda d: x0 + (x1 - x0) * d / mx
    g = f' class="st an-fade" data-n="{n * 10}"' if n else ''
    return (f'<svg class="waitbar" viewBox="0 0 {W} {262 if cap else 222}" dir="ltr" role="img" aria-label="ההמתנה בימים"><g{g}>'
            f'<line x1="{x0 - 10}" y1="{y}" x2="{x1 + 18}" y2="{y}" stroke="#1b2d55" stroke-width="5" stroke-linecap="round"/><polygon points="{x1 + 36},{y} {x1 + 16},{y - 11} {x1 + 16},{y + 11}" fill="#1b2d55"/>'
            f'<rect x="{X(0):.1f}" y="{y - 104}" width="{X(days) - X(0):.1f}" height="80" rx="16" fill="{bg}" stroke="{col}" stroke-width="4"/>'
            f'<text x="{(X(0) + X(days)) / 2:.1f}" y="{y - 51}" text-anchor="middle" font-size="40" font-weight="800" fill="{col}" direction="rtl">{days:g} ימים</text>'
            f'<circle cx="{X(0):.1f}" cy="{y}" r="11" fill="{col}"/><circle cx="{X(days):.1f}" cy="{y}" r="11" fill="{col}"/>'
            f'<text x="{X(0):.1f}" y="{y + 44}" text-anchor="middle" font-size="27" font-weight="800" fill="#1b2d55" direction="rtl">{a}</text>'
            f'<text x="{X(days):.1f}" y="{y + 44}" text-anchor="middle" font-size="27" font-weight="800" fill="#1b2d55" direction="rtl">{b}</text>'
            + (f'<text x="{W / 2}" y="{y + 92}" text-anchor="middle" font-size="25" font-weight="700" fill="#5d6a86" direction="rtl">{cap}</text>' if cap else '')
            + '</g></svg>')

def NUMV(val, title, lines):
    """A number that opens its calculation."""
    if MODE == 'pdf':
        return TX(val)
    body = ''.join(f'<p>{TX(x)}</p>' for x in lines)
    return f'<span class="nv"><button class="morebtn nvb" type="button" title="איך חישבנו">{TX(val)}</button><div class="more-c" hidden><div class="more-h">{TX(title)}</div>{body}</div></span>'


def ONE(rows, cls='', h=False):
    """One number per click: (click, label, value, calc title, calc lines, meaning). Each value opens its calculation. h: cards side by side."""
    if MODE == 'pdf':
        return ('<table class="tbl2"><tr><th>מה</th><th>כמה</th><th>החישוב והמשמעות</th></tr>'
                + ''.join(f'<tr><td>{TX(l)}</td><td class="amt"><b>{TX(v)}</b></td><td>{TX(" ".join(hl))} {TX(m)}</td></tr>' for n, l, v, ht, hl, m in rows) + '</table>')
    out = ''
    for n, l, v, ht, hl, m in rows:
        out += ST(n, f'<div class="o-l">{TX(l)}</div><div class="o-v">{NUMV(v, ht, hl)}</div><div class="o-m">{TX(m)}</div>', cls='orow')
    return f'<div class="ones {cls}{" h" if h else ""}">{out}</div>'

def PRESS(n, src, date, head, body, url, so=''):
    """A news item retold in our own words, the ratio it touches, and a link to the source."""
    if MODE == 'pdf':
        return f'<div class="band note"><b>{TX(src)}, {TX(date)}: {TX(head)}.</b> {TX(body)}' + (f' <b>{TX(so)}</b>' if so else '') + f' <span class="l" dir="ltr">{url}</span></div>'
    inner = (f'<div class="pr-top"><span class="pr-src">{TX(src)}</span><span class="pr-date">{TX(date)}</span></div><b class="pr-h">{TX(head)}</b><p>{TX(body)}</p>'
             + (f'<div class="pr-so">{TX(so)}</div>' if so else '') + f'<a class="pr-a" href="{url}" target="_blank" rel="noopener">למקור ↗</a>')
    return ST(n, inner, cls='press') if n else f'<div class="press">{inner}</div>'


def COLCHART(items, n0=1, W=1000, H=330, unit='ימים', step=1, lo=None, hi=None):
    """Columns around a zero line, positive up and negative down, one column per click. items: (label, value, colour, small line)."""
    if MODE == 'pdf':
        return '<table class="tbl2"><tr><th>החברה</th><th>' + TX(unit) + '</th><th></th></tr>' + ''.join(f'<tr><td>{TX(l)}</td><td class="amt">{TX(f"{v:g}")}</td><td>{TX(s)}</td></tr>' for l, v, c, s in items) + '</table>'
    vals = [v for _, v, _, _ in items]
    lo = min(0, min(vals)) if lo is None else lo
    hi = max(0, max(vals)) if hi is None else hi
    top, bot = 46, H - 104
    Y = lambda v: top + (hi - v) * (bot - top) / (hi - lo)
    y0 = Y(0)
    n = len(items)
    cw = (W - 120) / n
    p = [f'<line x1="70" y1="{y0:.1f}" x2="{W - 20}" y2="{y0:.1f}" stroke="#1b2d55" stroke-width="3"/><text x="58" y="{y0 + 7:.1f}" text-anchor="end" font-size="20" font-weight="800" fill="#1b2d55">0</text>']
    fmt = lambda v: (f'{v:g}' if v >= 0 else '−' + f'{-v:g}')
    for i, (l, v, c, s) in enumerate(items):
        cx = 90 + cw * i + cw / 2
        bw = min(100, cw * .58)
        yt, yb = (Y(v), y0) if v >= 0 else (y0, Y(v))
        vy = (yt - 12) if v >= 0 else (yb + 30)
        p.append(f'<g class="st an-grow" data-n="{(n0 + i * step) * 10}"><rect class="bar{" neg" if v < 0 else ""}" x="{cx - bw / 2:.1f}" y="{yt:.1f}" width="{bw:.1f}" height="{max(2, yb - yt):.1f}" rx="6" fill="{c}"/>'
                 f'<text x="{cx:.1f}" y="{vy:.1f}" text-anchor="middle" font-size="25" font-weight="800" fill="{c}" direction="ltr">{fmt(v)}</text>'
                 f'<text x="{cx:.1f}" y="{H - 38}" text-anchor="middle" font-size="22" font-weight="800" fill="#1b2d55" direction="rtl">{l}</text>'
                 f'<text x="{cx:.1f}" y="{H - 12}" text-anchor="middle" font-size="18" font-weight="700" fill="#5d6a86" direction="rtl">{s}</text></g>')
    return f'<svg class="colchart" viewBox="0 0 {W} {H}" dir="ltr" role="img" aria-label="תרשים עמודות">' + ''.join(p) + '</svg>'

def CAL60(clicks=(1, 2, 3)):
    """End of month + 60: three invoices of January, all paid on the same day."""
    if MODE == 'pdf':
        return ('<table class="tbl2"><tr><th>תאריך החשבונית</th><th>סוף החודש</th><th>ועוד 60 יום: התשלום</th><th>ימים מהחשבונית</th></tr>'
                + ''.join(f'<tr><td>{a}</td><td>31.1</td><td>1.4</td><td class="amt">{d}</td></tr>' for a, d in (('1.1', 90), ('15.1', 76), ('31.1', 60))) + '</table>')
    W, x0, x1, y = 1100, 60, 1030, 150
    X = lambda d: x0 + (x1 - x0) * d / 100
    p = [f'<line x1="{x0 - 20}" y1="{y}" x2="{x1 + 20}" y2="{y}" stroke="#1b2d55" stroke-width="4" stroke-linecap="round"/>']
    for d, t in ((0, 'ינואר'), (31, 'פברואר'), (59, 'מרץ'), (90, 'אפריל')):
        p.append(f'<line x1="{X(d):.1f}" y1="{y - 12}" x2="{X(d):.1f}" y2="{y + 12}" stroke="#1b2d55" stroke-width="3"/><text x="{X(d + 15.5 if d < 90 else d + 5):.1f}" y="{y + 36}" text-anchor="middle" font-size="18" font-weight="800" fill="#5d6a86" direction="rtl">{t}</text>')
    p.append(f'<g><rect x="{X(30.4):.1f}" y="{y - 128}" width="{X(31) - X(30.4) + 4:.1f}" height="0" fill="none"/></g>')
    p.append(f'<g class="st" data-n="{clicks[0] * 10}"><line x1="{X(31):.1f}" y1="{y - 6}" x2="{X(31):.1f}" y2="{y - 130}" stroke="#8a93aa" stroke-width="2" stroke-dasharray="5 5"/>'
             f'<text x="{X(31):.1f}" y="{y - 136}" text-anchor="middle" font-size="16" font-weight="800" fill="#5d6a86" direction="rtl">סוף החודש: 31.1</text>'
             f'<line x1="{X(90):.1f}" y1="{y - 6}" x2="{X(90):.1f}" y2="{y - 130}" stroke="#107c41" stroke-width="3"/><text x="{X(90):.1f}" y="{y - 136}" text-anchor="middle" font-size="17" font-weight="800" fill="#107c41" direction="rtl">התשלום: 1.4</text></g>')
    for k, (d0, t, days, h) in enumerate(((0, '1.1', 90, 104), (14, '15.1', 76, 74), (30, '31.1', 60, 44))):
        a, b = X(d0), X(90)
        col = ['#e8960c', '#c4421f', '#6d4df2'][k]
        p.append(f'<g class="st an-draw" data-n="{clicks[k] * 10}"><circle cx="{a:.1f}" cy="{y}" r="8" fill="{col}"/><text x="{a:.1f}" y="{y + 62 + 0 * k}" text-anchor="middle" font-size="16" font-weight="800" fill="{col}">{t}</text>'
                 f'<path d="M{a:.1f} {y - 8}Q{(a + b) / 2:.1f} {y - 8 - 2 * h} {b - 4:.1f} {y - 10}" pathLength="1" fill="none" stroke="{col}" stroke-width="3.5"/>'
                 f'<text x="{(a + b) / 2:.1f}" y="{y - 8 - h - 4}" text-anchor="middle" font-size="18" font-weight="800" fill="{col}" direction="rtl">{days} יום</text></g>')
    return f'<svg class="cal60" viewBox="0 0 {W} {y + 76}" dir="ltr" role="img" aria-label="שוטף ועוד 60">' + ''.join(p) + '</svg>'


def REPMOCK(rows_bs, rows_pl, note, marks):
    """A drawn excerpt of an annual report (an illustration): balance sheet lines, income statement lines and a note.
    rows: (key, label, 2026, 2025); marks: (click, key, explanation) light a line and explain where the number goes."""
    if MODE == 'pdf':
        return '<ul class="pl">' + ''.join(f'<li>{TX(t)}</li>' for _, _, t in marks) + '</ul>'
    mk = {}
    for n, key, t in marks:
        mk.setdefault(key, n)
    def tr(key, lab, a, b):
        hl = ST(mk[key], '', cls='hlx') if key in mk else ''
        return f'<tr><td>{hl}{TX(lab)}</td><td class="amt">{hl}{TX(a)}</td><td class="amt">{hl}{TX(b)}</td></tr>'
    bs = ''.join(tr(*r) for r in rows_bs)
    pl = ''.join(tr(*r) for r in rows_pl)
    nk = [n for n, key, _ in marks if key == 'note']
    nh = ST(nk[0], '', cls='hlx') if nk else ''
    side = ''.join(ST(n, f'<i>{i + 1}</i><span>{TX(t)}</span>', cls='rmk') for i, (n, key, t) in enumerate(marks))
    return ('<div class="rep"><div class="rep-p"><div class="rep-h">' + TX('דוחות על המצב הכספי') + '<small>' + TX('אלפי ש״ח · ליום 31 בדצמבר') + '</small></div>'
            f'<table class="rept"><tr><th></th><th>2026</th><th>2025</th></tr>{bs}</table>'
            '<div class="rep-h">' + TX('דוחות רווח והפסד') + '<small>' + TX('אלפי ש״ח · לשנה שהסתיימה ביום 31 בדצמבר') + '</small></div>'
            f'<table class="rept"><tr><th></th><th>2026</th><th>2025</th></tr>{pl}</table>'
            f'<div class="rep-n">{nh}{TX(note)}</div><div class="rep-ill">' + TX('איור להמחשה. החברה והמספרים הומצאו.') + f'</div></div><div class="rep-side">{side}</div></div>')


TOONS.update({
 'coat': '<path d="M60 10v10" stroke="#5d6a86" stroke-width="4"/><path d="M42 24q18-14 36 0" fill="none" stroke="#5d6a86" stroke-width="4"/><path d="M40 26q20 14 40 0l20 10-8 26-10-4v52H38v-52l-10 4-8-26z" fill="#ff6a4d" stroke="#7a2a12" stroke-width="3"/>'
         + _face(60, 62, 16),
 'boxsad': '<path d="M20 44l40-18 40 18v52l-40 18-40-18z" fill="#c8945a" stroke="#8a5a2b" stroke-width="3"/><path d="M20 44l40 18 40-18M60 62v52" fill="none" stroke="#8a5a2b" stroke-width="3"/>' + _face(40, 78, 12, 'sad')
        + '<path d="M84 10q4 8 0 12q-4-4 0-12z" fill="#8a93aa"/><path d="M98 20q4 8 0 12q-4-4 0-12z" fill="#8a93aa"/>',
 'invoice': '<rect x="26" y="12" width="68" height="92" rx="7" fill="#fff" stroke="#1b2d55" stroke-width="3"/><path d="M36 30h48M36 44h48M36 58h30" stroke="#8a93aa" stroke-width="3"/>' + _face(60, 80, 14, 'flat')
            + '<text x="98" y="26" text-anchor="middle" font-size="22" font-weight="800" fill="#e8960c">⏳</text>',
 'shelfempty': '<rect x="14" y="20" width="92" height="86" rx="6" fill="#fff" stroke="#1b2d55" stroke-width="3"/><path d="M14 48h92M14 76h92" stroke="#1b2d55" stroke-width="3"/>'
               + '<circle cx="40" cy="96" r="3" fill="#8a93aa"/><text x="60" y="44" text-anchor="middle" font-size="24" font-weight="800" fill="#e0454f">?</text>',
 'shelffull': '<rect x="14" y="20" width="92" height="86" rx="6" fill="#fff" stroke="#1b2d55" stroke-width="3"/><path d="M14 48h92M14 76h92" stroke="#1b2d55" stroke-width="3"/>'
              + ''.join(f'<rect x="{18 + 22 * i}" y="{26 + 28 * j}" width="18" height="20" fill="#c8945a" stroke="#8a5a2b" stroke-width="1.5"/>' for i in range(4) for j in range(3))
              + '<path d="M100 8q6 10 0 15q-6-5 0-15z" fill="#58b8e0"/>',
})
