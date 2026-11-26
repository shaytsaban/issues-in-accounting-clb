# Visuals of lecture 4 (profitability): the income statement as a staircase per 100 shekels of sales, and two staircases side by side.
K_GP, K_OP, K_NP, K_DED = '#0f9d90', '#27447f', '#25a65f', '#e0454f'


def PLSTAIRS(rows, n0=1, title='', W=680, rowh=44, lw=210):
    """The income statement per 100 shekels of sales, one line per click. rows: (label, value, kind) where kind is
    'top' (sales, a full bar), 'ded' (a deduction, a red piece hanging from the previous total) or 'tot' (a profit line, a bar from 0)."""
    if MODE == 'pdf':
        return ('<table class="tbl2"><tr><th>' + TX(title or 'לכל 100 ש״ח של מכירות') + '</th><th>ש״ח</th></tr>'
                + ''.join(f'<tr{" class=tot" if k != "ded" else ""}><td>{TX(l)}</td><td class="amt">{TX(("(" + f"{v:g}" + ")") if k == "ded" else f"{v:g}")}</td></tr>' for l, v, k in rows) + '</table>')
    x0, x1 = 20, W - lw - 20
    X = lambda v: x0 + (x1 - x0) * v / 100
    p, cur, y = [], 100, 12
    for i, (l, v, k) in enumerate(rows):
        n = n0 + i
        if k == 'ded':
            a, b, col, bg = cur - v, cur, K_DED, '#fde2da'
            cur -= v
            txt = f'({v:g})'
        else:
            a, b = 0, v
            col, bg = {'top': ('#1b2d55', '#e1e7f8'), 'tot': (K_GP, '#d7f1ec')}[k]
            cur = v
            txt = f'{v:g}'
        lab_x = W - 12
        p.append(f'<g class="st an-fade" data-n="{n * 10}"><rect x="{X(a):.1f}" y="{y}" width="{max(3, X(b) - X(a)):.1f}" height="{rowh - 10}" rx="6" fill="{bg}" stroke="{col}" stroke-width="2.5"/>'
                 f'<text x="{(X(b) + 8) if X(b) - X(a) < 70 else (X(a) + X(b)) / 2:.1f}" y="{y + rowh / 2 + 2:.1f}" text-anchor="{"start" if X(b) - X(a) < 70 else "middle"}" font-size="23" font-weight="800" fill="{col}" direction="ltr">{txt}</text>'
                 f'<text x="{lab_x}" y="{y + rowh / 2 + 2:.1f}" text-anchor="start" font-size="22" font-weight="{800 if k != "ded" else 600}" fill="#1b2d55" direction="rtl">{l}</text></g>')
        y += rowh
    return f'<svg class="plst" viewBox="0 0 {W} {y + 6}" dir="ltr" role="img" aria-label="דוח רווח והפסד לכל 100 ש״ח">' + ''.join(p) + '</svg>'
