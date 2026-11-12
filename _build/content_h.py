# Helpers shared by every lesson: statements revealed line by line, and the statement-format sheets.
def PAREN(x):
    return f'<span class="n">({x})</span>'


def STEPROWS(rows, start=1, why=True):
    """A statement revealed line by line: (label, amount, why, total?)."""
    out, n = '', start
    for lab, amt, w, tot in rows:
        out += ST(n, f'<td>{TX(lab)}</td><td class="amt">{amt if amt.startswith("<") else TX(amt)}</td>' + (f'<td class="why">{TX(w)}</td>' if why else ''), 'tr', 'tot' if tot else '')
        n += 1
    return out, n



def ISQ(sid, tag, title, stem, v, note=None, done='', xtitle='', build=None, more=''):
    """An income statement in its own format: the lines in the order of the statement, amounts typed in, every profit a formula."""
    d = {'A1': 'סעיף', 'B1': 'ש״ח', 'A2': 'הכנסות ממכירות', 'A3': 'עלות המכירות', 'A4': 'רווח גולמי', 'A5': 'הוצאות מכירה ושיווק', 'A6': 'הוצאות הנהלה וכלליות', 'A7': 'רווח תפעולי',
         'A8': 'הוצאות מימון', 'A9': 'רווח לפני מסים על ההכנסה', 'A10': 'מסים על ההכנסה', 'A11': 'רווח נקי', 'A13': 'שיעור מס',
         'B2': v['rev'], 'B3': v['cogs'], 'B5': v['sm'], 'B6': v['ga'], 'B8': v['fin'], 'B13': v['tax']}
    sol = {'B4': '=B2-B3', 'B7': '=B4-B5-B6', 'B9': '=B7-B8', 'B10': '=B9*B13', 'B11': '=B9-B10'}
    QX(sid, tag, title, stem, 'הקלידו כל סכום בשורה שלו בדוח, ואת שיעור המס ב-B13. השורות הלבנות של הרווחים הן נוסחאות: השורה שמעל, פחות הקטגוריה הבאה.',
       d, sol, [230, 110], [1], fmt={**{f'B{i}': 'num0' for i in range(2, 12)}, 'B13': 'pct0'},
       hints=['רווח גולמי: =B2-B3. רווח תפעולי: =B4-B5-B6.', 'המס מחושב על הרווח לפני מס: =B9*B13. רווח נקי: =B9-B10.'], remind='=B4-B5-B6', partial=['B4'],
       traps={'B10': [('=B7*B13', 'המס מחושב על הרווח <b>לפני מס</b>, אחרי הוצאות המימון: =B9*B13.')], 'B7': [('=B4-B5', 'שכחתם את הוצאות ההנהלה והכלליות.')]},
       steps=[dict(cells={'B4': '=B2-B3'}, note='רווח גולמי: =B2-B3.'), dict(cells={'B7': '=B4-B5-B6'}, note='רווח תפעולי: =B4-B5-B6.'),
              dict(cells={'B9': '=B7-B8'}, note='רווח לפני מס: =B7-B8.'), dict(cells={'B10': '=B9*B13', 'B11': '=B9-B10'}, note='מס: =B9*B13. רווח נקי: =B9-B10.')],
       note=note or [], done=done, xtitle=xtitle, build=build, qmc=more)


def BSQ(sid, tag, title, stem, ca, nca, cl, ncl, sc, re_, note=None, done='', xtitle='', more=''):
    """A balance sheet in its own format: assets on one side, liabilities and equity on the other, each group with its total.
    ca: three (label, amount); nca, ncl: one (label, amount); cl: two (label, amount)."""
    d = {'A1': 'נכסים', 'B1': 'ש״ח', 'C1': 'התחייבויות והון עצמי', 'D1': 'ש״ח',
         'A2': 'נכסים שוטפים', 'A6': 'סך נכסים שוטפים', 'A7': 'נכסים לא שוטפים', 'A11': 'סך הנכסים',
         'C2': 'התחייבויות שוטפות', 'C5': 'סך התחייבויות שוטפות', 'C6': 'התחייבויות לא שוטפות', 'C8': 'הון מניות', 'C9': 'עודפים', 'C10': 'סך הון עצמי', 'C11': 'סך התחייבויות והון'}
    for i, (lab, x) in enumerate(ca): d[f'A{3 + i}'] = lab; d[f'B{3 + i}'] = x
    d['A8'] = nca[0]; d['B8'] = nca[1]
    for i, (lab, x) in enumerate(cl): d[f'C{3 + i}'] = lab; d[f'D{3 + i}'] = x
    d['C7'] = ncl[0]; d['D7'] = ncl[1]; d['D8'] = sc; d['D9'] = re_
    sol = {'B6': '=SUM(B3:B5)', 'B11': '=B6+B8', 'D5': '=D3+D4', 'D10': '=D8+D9', 'D11': '=D5+D7+D10'}
    QX(sid, tag, title, stem, 'הקלידו כל סכום ליד הפריט שלו. שורות הסיכום הן נוסחאות.',
       d, sol, [165, 90, 180, 90], [1], fmt={f'{c}{r}': 'num0' for c in 'BD' for r in range(2, 12)},
       hints=['נכסים שוטפים: =SUM(B3:B5). סך הנכסים: ועוד הנכס הלא שוטף, =B6+B8.', 'בצד השני: שוטפות =D3+D4, הון =D8+D9, והכול יחד =D5+D7+D10.'], remind='=D5+D7+D10', partial=['B6'],
       traps={'D11': [('=D5+D10', 'שכחתם את ההתחייבות הלא שוטפת בשורה 7.')], 'B11': [('=B6', 'שכחתם את הנכס הלא שוטף בשורה 8.')]},
       steps=[dict(cells={'B6': '=SUM(B3:B5)', 'B11': '=B6+B8'}, note='צד הנכסים: סך נכסים שוטפים, ואז סך הנכסים.'),
              dict(cells={'D5': '=D3+D4', 'D10': '=D8+D9', 'D11': '=D5+D7+D10'}, note='הצד השני: שוטפות, הון עצמי, ובסוף הכול יחד. שני הסכומים בשורה 11 שווים.', sel='D5', sel2='D11')],
       note=note or [], done=done, xtitle=xtitle, qmc=more)



# ---------------------------------------------------------------- meeting 2, rebuilt 2026-11-12
# Shay: one question per slide, large; the accounting identity as a table with a column for every account (as in his Coursebook
# 10280, lecture 1): assets, liabilities, equity (share capital, premium, revenues, expenses with a minus) and a control column.
def POP(n, html, cls=''):
    return ST(n, html, cls='pop ' + cls)


def MC1(sid, title, q, opts, a, why, art=None, story=None):
    """One multiple choice question on its own slide, in large type, with an illustration beside it."""
    item = mc(sid + '-q', q, opts, a, why)
    if MODE == 'pdf':
        S(sid, title, title, (f'<p>{TX(story)}</p>' if story else '') + item); return
    side = f'<div class="mc1art">{_svg(TOONS.get(art, art))}</div>' if art else ''
    st = f'<div class="card qstem mc1s"><p>{TX(story)}</p></div>' if story else ''
    S(sid, title, title, f'<div class="mc1">{side}<div class="mc1q">{st}{item}</div></div>', kick=f'חלק {CUR[0]} · שאלה אחת')


GFILL = {'a': '#d7f1ec', 'l': '#fde2da', 'e': '#e1e7f8', 'pl': '#fff0c2', 'c': '#ececec', 't': '#f3f2f1'}
GNAME = {'a': 'נכסים', 'l': 'התחייבויות', 'e': 'הון עצמי', 'pl': 'עודפים: הכנסות והוצאות'}


def _amt(v):
    return v if isinstance(v, (int, float)) else v[0]


def _fmt_s(x):
    return f'({abs(x):,})' if x < 0 else f'{x:,}'


def IDSHEET(accts, rows, cur, total=None, profit=False, lab_w=150, w=80, given_total=False, date='31.12.2026'):
    """The accounting identity as a table.
    accts: [(key, name, group)] in column order from B; group in a (assets), l (liabilities), e (equity), pl (revenues and expenses).
    rows: [(label, {key: amount or (amount, why)})]; rows whose index is in cur are the student's, the rest are given.
    total: also a totals row (its formulas are the student's unless given_total); profit: a net profit row under it."""
    L = {k: chr(66 + i) for i, (k, _, _) in enumerate(accts)}
    ctl = chr(66 + len(accts))
    grp = {k: g for k, _, g in accts}
    first = lambda g: next(L[k] for k, _, gg in accts if gg == g)
    last = lambda g: [L[k] for k, _, gg in accts if gg == g][-1]
    la, ll = last('a'), last('pl' if any(g == 'pl' for *_, g in accts) else 'e')
    data, given, sol, sty, steps, zone = {'A1': '', 'A2': 'עסקה', f'{ctl}2': 'בקרה'}, {}, {}, {}, [], []
    seen = set()
    for k, name, g in accts:
        data[f'{L[k]}2'] = name
        if g not in seen:
            seen.add(g); data[f'{L[k]}1'] = GNAME[g]
        sty[f'{L[k]}1'] = {'fill': GFILL[g], 'b': True}; sty[f'{L[k]}2'] = {'fill': GFILL[g], 'b': True}
    sty['A2'] = sty['A1'] = {'fill': GFILL['t'], 'b': True}; sty[f'{ctl}1'] = sty[f'{ctl}2'] = {'fill': GFILL['c'], 'b': True}
    data[f'{ctl}1'] = 'מאוזן?'
    fmt = {}
    for i, (lab, eff) in enumerate(rows):
        r = 3 + i
        data[f'A{r}'] = lab
        given[f'{ctl}{r}'] = f'=SUM(B{r}:{la}{r})-SUM({chr(ord(la) + 1)}{r}:{ll}{r})'
        sty[f'{ctl}{r}'] = {'fill': GFILL['c']}
        for k in L:
            fmt[f'{L[k]}{r}'] = 'acc0'
        fmt[f'{ctl}{r}'] = 'acc0'
        for k, v in eff.items():
            a = f'{L[k]}{r}'
            if i in cur:
                sol[a] = str(_amt(v))
                why = v[1] if isinstance(v, tuple) else ''
                name = next(n for kk, n, _ in accts if kk == k)
                steps.append(dict(cells={a: str(_amt(v))}, note=f'<b>{name}:</b> {_fmt_s(_amt(v))}. {why}'.strip(), sel=a))
            else:
                given[a] = _amt(v)
        if i in cur:
            zone += [f'{L[k]}{r}' for k in L]
    tr = None
    if total:
        tr = 3 + len(rows)
        data[f'A{tr}'] = f'סה״כ: יתרה ליום {date}'
        sty[f'A{tr}'] = {'fill': GFILL['t'], 'b': True}
        for k in list(L) + ['_c']:
            col = ctl if k == '_c' else L[k]
            f = f'=SUM({col}3:{col}{tr - 1})' if k != '_c' else f'=SUM(B{tr}:{la}{tr})-SUM({chr(ord(la) + 1)}{tr}:{ll}{tr})'
            fmt[f'{col}{tr}'] = 'acc0'
            sty[f'{col}{tr}'] = {'fill': GFILL[grp.get(k, 'c')], 'b': True}
            if given_total:
                given[f'{col}{tr}'] = f
            else:
                sol[f'{col}{tr}'] = f
                nm = 'הבקרה' if k == '_c' else next(n for kk, n, _ in accts if kk == k)
                steps.append(dict(cells={f'{col}{tr}': f}, note=f'<b>{nm}:</b> ' + (f'סכום העמודה, {XL(f)}. זו היתרה של החשבון ליום {date}.' if k != '_c' else f'{XL(f)}: גם בסיכום, הנכסים פחות כל השאר נותנים 0.'), sel=f'{col}{tr}'))
        if profit:
            pr = tr + 1
            kr = next(L[k] for k, _, g in accts if g == 'pl')
            ke = [L[k] for k, _, g in accts if g == 'pl'][-1]
            data[f'A{pr}'] = 'רווח נקי: הכנסות ועוד הוצאות'
            sty[f'A{pr}'] = {'fill': GFILL['pl'], 'b': True}
            f = f'={kr}{tr}+{ke}{tr}'
            fmt[f'{kr}{pr}'] = 'acc0'
            sty[f'{kr}{pr}'] = {'fill': GFILL['pl'], 'b': True}
            if given_total: given[f'{kr}{pr}'] = f
            else:
                sol[f'{kr}{pr}'] = f
                steps.append(dict(cells={f'{kr}{pr}': f}, note=f'<b>רווח נקי:</b> {XL(f)}. ההוצאות כבר במינוס, ולכן מחברים.', sel=f'{kr}{pr}'))
    widths = [lab_w] + [w] * len(accts) + [72]
    start = (min(sol, key=lambda a: (int(a[1:]), a[0])) if sol else 'A1')
    return dict(data=data, given=given, sol=sol, sty=sty, steps=steps, zone=zone or None, fmt=fmt, widths=widths, head=[1, 2], start=start, L=L, ctl=ctl, tr=tr)


def QT(sid, tag, title, stem, task, sp, chips=None, note=None, done='', xtitle='', hints=None, remind=None, more='', **kw):
    """A transaction (or a stage of an exercise) above a full width identity table: the story, then the effect on each part of the
    identity revealed click by click, then the sheet where the row is written."""
    head_t = f'{tag}: {title}' if tag else title
    stem_html = ''.join(f'<p>{TX(x)}</p>' for x in stem)
    chip = lambda i, k, h, t: ST(i + 1, f'<b>{TX(h)}</b> {TX(t)}', cls=f'fxc {k}') if MODE == 'deck' else f'<div class="fxc {k}"><b>{TX(h)}</b> {TX(t)}</div>'
    chip_html = ''.join(chip(i, k, h, t) for i, (k, h, t) in enumerate(chips or []))
    nb = len(chips or [])
    notes = ''.join(BAND(x[0], x[1], (x[2] if len(x) > 2 else nb + 1 + i)) if MODE == 'deck' else BAND(x[0], x[1]) for i, x in enumerate(note or []))
    _rows = sorted({int(re.sub('[A-Z]', '', a)) for a in sp['sol']} | set(sp['head']))
    r = _xsheet(sid, task, sp['data'], sp['sol'], sp['widths'], sp['head'], side=True, area=1130, title=head_t, pdf_rows=(_rows if 'L' in sp and sp.get('tr') is None else None), qtext=' '.join(re.sub('<[^>]+>', '', x) for x in stem),
                fmt=sp['fmt'], zone=sp['zone'], given=sp['given'], sty=sp['sty'], start=sp['start'], steps=sp['steps'] or None, values=True,
                hints=hints or ['לכל חשבון שמשתנה כותבים את השינוי בעמודה שלו: מספר חיובי כשהוא גדל, ומינוס כשהוא קטן.', 'הבקרה בעמודה האחרונה צריכה להראות 0 (מקף). אם לא, משהו חסר או בצד הלא נכון.'],
                remind=remind or 'נכסים = התחייבויות + הון עצמי', partial=list(sp['sol'])[:1], done=done, xtitle=xtitle or head_t, **kw)
    if MODE == 'pdf':
        S(sid, head_t, head_t, f'<div class="qstem">{stem_html}</div>{chip_html}{notes}{more}{r}', kind='q'); return
    cfgd, inner = r
    multi = ' multi' if len(stem) > 2 else ''
    S(sid, head_t, head_t, f'<div class="act xlq qt{multi}" id="{sid}-x" data-cfg="{_cfg(cfgd)}"><div class="qtop"><div class="card qstem">{stem_html}{more}</div><div class="qnotes">{chip_html}{notes}</div></div><div class="xw">{inner}<div class="xfb"></div></div></div>',
      kick=f'חלק {CUR[0]} · {tag.split(":")[0] if tag else "טבלת הזהות"}', cls='qslide qtslide')
