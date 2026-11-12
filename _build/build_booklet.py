# Exercise booklet (PDF, questions only), its practice workbook (yellow answer cells left empty) and a private solutions workbook.
# Run: python3 build_booklet.py  ->  ../materials/booklet.pdf, booklet-solutions.pdf, booklet-practice.xlsx and booklet-solutions.xlsx
# Every answer is computed twice: by fin.py, and by a LibreOffice recalculation of the solutions workbook. Answer keys are never written into the repository.
import os, re, sys, shutil, subprocess, tempfile, html
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, H)
import fin
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
REPO = os.path.abspath(os.path.join(H, '..'))
# the exercises and their answer formulas live outside the repository, so the keys are never published
exec(open(os.path.join(REPO, '_private', 'booklet.py'), encoding='utf8').read())   # the exercises and their answer key live in the gitignored _private folder
FONTS = os.path.join(REPO, '..', 'iit-build', 'fonts')
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
COURSE = 'סוגיות בחשבונאות'
PRIV = os.path.join(REPO, '_private'); os.makedirs(PRIV, exist_ok=True)
os.makedirs(os.path.join(REPO, 'materials'), exist_ok=True)
NAVY, YEL, GIV = '1B2D55', 'FFF4C2', 'EEF2FF'
thin = Side(style='thin', color='D9D2C3'); BOX = Border(left=thin, right=thin, top=thin, bottom=thin)


def layout(e):
    """Cell addresses of every row, the data values and the solution formulas of one exercise."""
    cols = ['B', 'C'] if e['cols'] else ['B']
    rows, r = {}, 3
    for k, *_ in e['data']:
        rows[k] = r; r += 1
    r += 1
    for k, *_ in e['ask']:
        rows[k] = r; r += 1
    cells, labels, sol, fmt = {}, {}, {}, {}
    labels['A2'] = 'פריט'
    for i, c in enumerate(cols):
        labels[f'{c}2'] = e['cols'][i] if e['cols'] else 'ערך'
    for k, lab, v, f in e['data']:
        labels[f'A{rows[k]}'] = lab
        for i, c in enumerate(cols):
            cells[f'{c}{rows[k]}'] = v[i] if isinstance(v, tuple) else v
            fmt[f'{c}{rows[k]}'] = f
    labels[f'A{rows[e["ask"][0][0]] - 1}'] = 'החישובים'
    for k, lab, fx, f in e['ask']:
        labels[f'A{rows[k]}'] = lab
        for c in cols:
            sol[f'{c}{rows[k]}'] = re.sub(r'\{(\w+)\}', lambda m: f'{c}{rows[m.group(1)]}', fx)
            fmt[f'{c}{rows[k]}'] = f
    t = e['table']
    if t:
        th = r + 1
        L = 'ABCDEF'
        for j, h in enumerate(t['head']):
            labels[f'{L[j]}{th}'] = h
        cl = {name: L[j + 1] for j, name in enumerate(t['cols'])}
        ab = lambda k: f'$B${rows[k]}'
        for y in range(1, t['rows'] + 1):
            rr = th + y
            cells[f'A{rr}'] = y; fmt[f'A{rr}'] = 'num0'
            for name in t['cols']:
                fx = (t['first'].get(name) if y == 1 and name in t['first'] else t['each'][name])
                fx = re.sub(r'\{(\w+)@prev\}', lambda m: f'{cl[m.group(1)]}{rr - 1}', fx)
                fx = re.sub(r'\{(\w+)@\}', lambda m: f'{cl[m.group(1)]}{rr}', fx)
                fx = re.sub(r'\{(\w+)\}', lambda m: ab(m.group(1)), fx)
                sol[f'{cl[name]}{rr}'] = fx; fmt[f'{cl[name]}{rr}'] = 'num2'
        tr = th + t['rows'] + 1
        k, lab = t['total']
        labels[f'A{tr}'] = lab
        sol[f'{cl[k]}{tr}'] = f'=SUM({cl[k]}{th + 1}:{cl[k]}{tr - 1})'; fmt[f'{cl[k]}{tr}'] = 'num2'
        e['_th'] = th
    return labels, cells, sol, fmt


def xfmt(f):
    m = re.fullmatch(r'(pct|num)(\d)', f or '')
    d = int(m.group(2)); z = ('.' + '0' * d) if d else ''
    return ('0' + z + '%') if m.group(1) == 'pct' else ('#,##0' + z)


def build(path, solved, exs=None, m=None):
    exs = exs or EX
    wb = Workbook(); w0 = wb.active; w0.title = 'הוראות'; w0.sheet_view.rightToLeft = True; w0.column_dimensions['A'].width = 110
    lines = [f'{COURSE}: חוברת תרגילים' + (f', התרגילים של מפגש {m}' if m else '') + ', ' + ('קובץ פתרונות' if solved else 'קובץ תרגול'), 'המרכז האקדמי למשפט ולעסקים, רמת גן · ד״ר שי צבאן · סמסטר א׳ תשפ״ז', '',
             'כל גיליון הוא תרגיל אחד מהחוברת, לפי מספרו (למשל 1-3: הרצאה 1, תרגיל 3). השאלה המלאה כתובה בראש הגיליון.',
             'התאים הכחולים הם נתוני השאלה. ' + ('התאים הירוקים מכילים נוסחאות חיות.' if solved else 'התאים הצהובים ריקים: כתבו בהם נוסחאות עם הפניות לתאים, לא מספרים.'),
             (f'בקובץ הזה רק התרגילים שאפשר לפתור אחרי מפגש {m}: ' + ', '.join(x['id'] for x in exs) + '.' if m else 'התרגילים מסודרים לפי הרצאות. אחרי כל הרצאה נוסף לחוברת פרק חדש.'), 'כל המספרים להמחשה בלבד. החברות בתרגילים הומצאו להמחשה.']
    for i, t in enumerate(lines, 1):
        c = w0.cell(i, 1, t); c.alignment = Alignment(horizontal='right', wrap_text=True); c.font = Font(name='Arial', size=16 if i == 1 else 12, bold=i == 1, color=NAVY)
    for e in exs:
        labels, cells, sol, fmt = layout(e)
        ws = wb.create_sheet(e['id']); ws.sheet_view.rightToLeft = True
        ws.column_dimensions['A'].width = 34
        for c in 'BCDEF': ws.column_dimensions[c].width = 16
        ws.column_dimensions['H'].width = 80
        ws['A1'] = f'תרגיל {e["id"]}: {e["t"]}'; ws['A1'].font = Font(name='Arial', size=14, bold=True, color=NAVY)
        ws['H2'] = '\n\n'.join(re.sub('<[^>]+>', '', q) for q in e['q']); ws['H2'].alignment = Alignment(wrap_text=True, vertical='top', horizontal='right'); ws['H2'].font = Font(name='Arial', size=11)
        ws.merge_cells('H2:H24')
        for a, v in labels.items():
            c = ws[a]; c.value = v
            r = int(a[1:])
            if r == 2 or (e['table'] and r == e['_th']):
                c.fill = PatternFill('solid', fgColor=NAVY); c.font = Font(name='Arial', size=11, bold=True, color='FFFFFF'); c.alignment = Alignment(horizontal='center', wrap_text=True)
            else:
                c.font = Font(name='Arial', size=11, bold=True); c.alignment = Alignment(horizontal='right')
        for a, v in cells.items():
            c = ws[a]; c.value = v; c.fill = PatternFill('solid', fgColor=GIV); c.border = BOX; c.number_format = xfmt(fmt[a]); c.font = Font(name='Arial', size=11); c.alignment = Alignment(horizontal='center')
        for a, f in sol.items():
            c = ws[a]; c.fill = PatternFill('solid', fgColor='DDF5E6' if solved else YEL); c.border = BOX; c.number_format = xfmt(fmt[a]); c.font = Font(name='Arial', size=11); c.alignment = Alignment(horizontal='center')
            if solved: c.value = f
    wb.calculation.fullCalcOnLoad = True
    wb.save(path)


# ---------------------------------------------------------------- workbooks and their check
PY = {}
for e in EX:
    labels, cells, sol, fmt = layout(e)
    v, _ = fin.evaluate({**cells, **sol})
    PY[e['id']] = {a: v[a] for a in sol}


def workbooks(exs, m=None):
    """The practice workbook and the solutions workbook, recalculated by LibreOffice and checked against Python, cell by cell."""
    tag = f'-m{m}' if m else ''
    prac = os.path.join(REPO, 'materials', f'booklet{tag}-practice.xlsx'); solp = os.path.join(PRIV, f'booklet{tag}-solutions.xlsx')
    build(prac, False, exs, m); build(solp, True, exs, m)
    d = tempfile.mkdtemp(dir=os.environ.get('TMPDIR'))
    subprocess.run(['soffice', '--headless', f'-env:UserInstallation=file://{d}/lo', '--convert-to', 'xlsx:Calc MS Excel 2007 XML', '--outdir', d, solp], capture_output=True, timeout=600)
    V = load_workbook(os.path.join(d, os.path.basename(solp)), data_only=True)
    errs, n = [], 0
    for e in exs:
        for a, py in PY[e['id']].items():
            n += 1; lo = V[e['id']][a].value
            if not isinstance(lo, (int, float)) or abs(lo - py) > 1e-6 * max(1, abs(py)): errs.append((e['id'], a, py, lo))
    shutil.copy(os.path.join(d, os.path.basename(solp)), solp); shutil.rmtree(d, True)
    print(os.path.basename(solp), 'exercises', len(exs), 'answer cells', n, 'python vs LibreOffice mismatches', errs[:5])
    assert not errs
    P = load_workbook(prac)
    leak = sum(1 for e in exs for a in PY[e['id']] if P[e['id']][a].value is not None)
    print('answers leaked into the practice workbook:', leak); assert leak == 0


BYID = {e['id']: e for e in EX}
AFTER = {i: m for m, ids in MEET.items() for i in ids}
assert all(i in BYID for i in AFTER), 'MEET names an exercise that does not exist'
workbooks(EX)
for _m, _ids in {}.items():
    workbooks([BYID[i] for i in _ids], _m)
# ---------------------------------------------------------------- the PDF: questions only
def P_(s):
    # numbers and Latin runs isolated as LTR, so the Hebrew sentence keeps its order
    out = []
    for seg in re.split(r'(<[^>]+>)', s):
        if seg.startswith('<'): out.append(seg); continue
        seg = re.sub(r'(?<![\w.,])(\d{1,2}\.\d{1,2}\.\d{4}|-?\d{1,3}(?:,\d{3})+(?:\.\d+)?%?|-?\d+(?:\.\d+)?%?)(?!\w)', r'⟦\1⟧', seg)
        seg = re.sub(r'([A-Za-z][A-Za-z0-9]*(?:[ ,.&=+\-]+[A-Za-z0-9(⟦][A-Za-z0-9.⟦⟧)]*)*)', r'⟪\1⟫', seg)
        out.append(seg)
    s = ''.join(out)
    s = re.sub(r'⟪([^⟫]*)⟫', lambda m: '<span class="n">' + m.group(1).replace('⟦', '').replace('⟧', '') + '</span>', s)
    return re.sub(r'⟦([^⟧]*)⟧', r'<span class="n">\1</span>', s)


def tag(e, full):
    """In the full booklet every exercise says after which meeting it can be solved."""
    if not full: return ''
    m = AFTER.get(e['id'])
    return f'<span class="mt{" later" if not m else ""}">' + (f'אחרי הרצאה <span class="n">{m}</span>' if m else 'בהמשך הקורס') + '</span>'


def qbody(exs, full):
    body, SEEN = '', {}
    for L, lt in LESSONS.items():
        part = [x for x in exs if x['id'].startswith(f'{L}-')]
        if not part: continue
        body += f'<section><h1><span class="sn">{L}</span>הרצאה {L}: {lt}</h1>'
        for e in part:
            first = SEEN.setdefault(id(e['data']), e['id'])
            qs = ''.join(f'<p>{P_(html.escape(q, quote=False))}</p>' for q in e['q'][:-1]) if first == e['id'] else f'<p>{P_("נתוני החברה בטבלה של תרגיל " + first + ".")}</p>'
            if e['cols'] and first == e['id']:
                fm = lambda v, f: (f'{v * 100:g}%' if f.startswith('pct') else f'{v:,.2f}'.rstrip('0').rstrip('.') if v != int(v) else f'{int(v):,}')
                qs += '<table class="dt"><tr><th>פריט</th>' + ''.join(f'<th>{P_(c)}</th>' for c in e['cols']) + '</tr>' + ''.join(f'<tr><td>{lab}</td>' + ''.join(f'<td><span class="n">{fm(x, f)}</span></td>' for x in v) + '</tr>' for k, lab, v, f in e['data']) + '</table>'
            qs += f'<p>{P_(html.escape(e["q"][-1], quote=False))}</p>'
            body += f'<div class="ex"><h3>{tag(e, full)}תרגיל <span class="n">{e["id"]}</span>: {P_(html.escape(e["t"], quote=False))}</h3>{qs}<p class="sh">בקובץ התרגול: גיליון <span class="n">{e["id"]}</span>.</p></div>'
        body += '</section>'
    return body


MAP = ''
intro = ('<div class="intro"><p><b>איך עובדים עם החוברת.</b> התרגילים מסודרים לפי הרצאות: לכל הרצאה פרק, והפרק שלה נוסף לחוברת אחרי שהיא נלמדת. כרגע בחוברת: הרצאה 1. '
         'כל תרגיל נפתר ב-Excel: בקובץ התרגול יש גיליון לכל תרגיל, עם הנתונים בתאים כחולים ותאים צהובים ריקים לתשובות. כותבים נוסחאות עם הפניות לתאים, ולא מספרים.</p>'
         '<p>התרגילים בנויים כשאלות בחינה: סיפור מלא, חישוב, ואז סעיף של פרשנות. את סעיף הפרשנות כותבים במילים, בשניים או שלושה משפטים, עם נימוק מתוך הנתונים. כל המספרים להמחשה בלבד, והחברות בתרגילים הומצאו להמחשה.</p></div>')
CSS = '''
@font-face{font-family:"David";src:url("david.ttf");font-weight:400}
@font-face{font-family:"David";src:url("davidbd.ttf");font-weight:700}
@page{size:A4;margin:15mm;@bottom-center{content:counter(page);font-family:"David";font-size:10pt;color:#5d6a86}}
@page:first{margin:0;@bottom-center{content:none}}
*{box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact}
html{direction:rtl}body{font-family:"David";font-size:11.8pt;line-height:1.3;color:#16213a;margin:0}
.n{direction:ltr;unicode-bidi:isolate}
.cover{height:297mm;width:210mm;padding:42mm 24mm 24mm;background:linear-gradient(160deg,#0f1b33 0%,#1b2d55 60%,#27447f 100%);color:#fff;position:relative;break-after:page}
.c-top{font-size:16pt;color:#7fe3d6;font-weight:700}.c-title{font-size:40pt;line-height:1.15;margin:14mm 0 4mm;font-weight:700}.c-sub{font-size:18pt;color:#d6e0f7;line-height:1.35}
.c-line{width:60mm;height:3mm;background:#ff6a4d;margin:12mm 0;border-radius:2mm}.c-meta{font-size:14pt;color:#c8d4f2;line-height:1.5}
.c-author{position:absolute;right:24mm;bottom:28mm}.c-name{font-size:20pt;font-weight:700}.c-mail{font-size:14pt;color:#c8d4f2}
h1{font-size:16.5pt;color:#1b2d55;margin:5mm 0 2mm;padding-bottom:1.4mm;border-bottom:.8mm solid #ff6a4d;break-after:avoid}
h1 .sn{display:inline-block;background:#1b2d55;color:#fff;border-radius:50%;width:8.5mm;height:8.5mm;line-height:8.5mm;text-align:center;margin-left:3mm;font-size:12pt}
h3{font-size:12.4pt;color:#1b2d55;margin:0 0 .8mm;break-after:avoid}
.ex{border:.25mm solid #d9d2c3;border-radius:1.6mm;padding:1.8mm 3mm;margin:0 0 2mm;break-inside:avoid}
.ex p{margin:0 0 .8mm}.sh{color:#087469;font-size:10.4pt;font-weight:700}
.dt{border-collapse:collapse;font-size:10.6pt;margin:.6mm 0 1.2mm;width:auto;min-width:50%}.dt th{background:#1b2d55;color:#fff;padding:.4mm 2.4mm;text-align:right}.dt td{border-bottom:.25mm solid #d9d2c3;padding:.3mm 2.4mm}.dt td:not(:first-child),.dt th:not(:first-child){text-align:center}
.mt{float:left;font-size:10pt;font-weight:700;color:#fff;background:#087469;border-radius:1.4mm;padding:.2mm 2.2mm;margin-top:.4mm}.mt.later{background:#8a93a8}.mp{width:100%;margin-top:1mm}
.intro{background:#eef2ff;border-right:1.2mm solid #1b2d55;border-radius:1.2mm;padding:1.6mm 3mm;margin-bottom:2mm}.intro p{margin:0 0 1mm}
'''
def mkcover(title, sub, meta):
    return ('<div class="cover"><div class="c-top">המרכז האקדמי למשפט ולעסקים, רמת גן · החוג לחשבונאות</div>'
            f'<div class="c-title">{title}</div><div class="c-sub">{sub}</div><div class="c-line"></div>'
            f'<div class="c-meta">ניתוח דוחות כספיים והערכת שווי חברות · סמסטר א׳ תשפ״ז<br>{meta}</div>'
            '<div class="c-author"><div class="c-name">ד״ר שי צבאן</div><div class="c-mail" dir="ltr">shay.tsaban@gmail.com</div></div></div>')


HEAD = lambda t, css: f'<!doctype html><html lang="he" dir="rtl"><head><meta charset="utf-8"><title>{COURSE} | {t}</title><style>{css}</style></head><body>'
cover = mkcover('חוברת תרגילים', f'{COURSE}: תרגילים ברמת בחינה, לפי הרצאות, לפתרון ב-Excel.', f'<span class="n">{len(EX)}</span> תרגילים. קובץ התרגול באתר הקורס.')
page = HEAD('חוברת תרגילים', CSS) + cover + intro + qbody(EX, True) + '</body></html>'
MINTRO = lambda m, ids, what: (f'<div class="intro"><p><b>התרגילים של מפגש {m}: {MEET_T[m]}.</b> בקובץ הזה רק התרגילים שאפשר לפתור אחרי מפגש {m}, על החומר שנלמד בו: '
                               + ', '.join(f'<span class="n">{i}</span>' for i in ids) + f'. המספרים שלהם הם המספרים בחוברת המלאה. {what}</p></div>')
for bad in ('—', '־', '–'):
    assert bad not in page, bad


def render(page, name):
    for bad in ('—', '־', '–'):
        assert bad not in page, bad
    d = tempfile.mkdtemp(dir=os.environ.get('TMPDIR'))
    for f in ('david.ttf', 'davidbd.ttf'): shutil.copy(os.path.join(FONTS, f), d)
    open(os.path.join(d, 'b.html'), 'w', encoding='utf8').write(page)
    out = os.path.join(PRIV if 'solutions' in name else os.path.join(REPO, 'materials'), name)
    subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--no-sandbox', f'--user-data-dir={d}/p', '--no-pdf-header-footer', '--virtual-time-budget=6000', f'--print-to-pdf={out}', 'file://' + d + '/b.html'], capture_output=True, timeout=120)
    shutil.rmtree(d, True)
    import fitz
    D = fitz.open(out); print(name, 'pages', len(D), sorted({f[3].split('+')[-1] for p in D for f in p.get_fonts()}))


render(page, 'booklet.pdf')
for _m, _ids in {}.items():
    render(HEAD(f'חוברת תרגילים, מפגש {_m}', CSS) + mkcover(f'תרגילים למפגש {_m}', f'{COURSE}: {MEET_T[_m]}. התרגילים של המפגש בלבד, לפתרון ב-Excel.', f'<span class="n">{len(_ids)}</span> תרגילים מתוך חוברת התרגילים. קובץ התרגול של המפגש באתר הקורס.')
           + MINTRO(_m, _ids, 'פותרים בקובץ התרגול של המפגש, ורק אחר כך בודקים בפתרונות.') + qbody([BYID[i] for i in _ids], False) + '</body></html>', f'booklet-m{_m}.pdf')

# ---------------------------------------------------------------- the solutions book: every answer cell with its formula and value, then the conclusion
def fmtv(v, f):
    if f.startswith('pct'): t = f'{v * 100:,.{int(f[-1])}f}%'
    else: t = f'{v:,.{int(f[-1])}f}'
    return t.replace('-', '−')


def sbody_of(exs, full):
  sbody = ''
  for L, lt in LESSONS.items():
    if not [x for x in exs if x['id'].startswith(f'{L}-')]: continue
    sbody += f'<section><h1><span class="sn">{L}</span>הרצאה {L}: {lt}</h1>'
    for e in [x for x in exs if x['id'].startswith(f'{L}-')]:
        labels, cells, sol, fmt = layout(e)
        rows = ''
        for a, fx in sol.items():
            r = a[1:]
            lab = labels.get('A' + r, '')
            if e['cols']: lab += f' · {labels.get(a[0] + "2", "")}'
            if e['table'] and int(r) > e['_th'] and int(r) <= e['_th'] + e['table']['rows']:
                lab = f'שנה {int(r) - e["_th"]} · ' + labels.get(a[0] + str(e['_th']), '')
            rows += f'<tr><td>{P_(html.escape(lab, quote=False))}</td><td class="c"><span class="n">{a}</span></td><td><code class="n">{html.escape(fx)}</code></td><td class="c"><span class="n">{fmtv(PY[e["id"]][a], fmt[a])}</span></td></tr>'
        tbl = f'<table class="sol"><tr><th>מה מחשבים</th><th>תא</th><th>נוסחה</th><th>תוצאה</th></tr>{rows}</table>'
        sbody += (f'<div class="ex"><h3>{tag(e, full)}תרגיל <span class="n">{e["id"]}</span>: {P_(html.escape(e["t"], quote=False))}</h3>'
                  f'<p class="sh">הנוסחאות בכתובות התאים של גיליון <span class="n">{e["id"]}</span> בקובץ התרגול.</p>{tbl}'
                  f'<p class="cc"><b>מסקנה:</b> {P_(html.escape(C[e["id"]], quote=False))}</p></div>')
    sbody += '</section>'
  return sbody


SCSS = CSS + 'table.sol{width:100%;border-collapse:collapse;font-size:10.4pt;margin:.6mm 0 1.2mm}.sol th{background:#1b2d55;color:#fff;padding:.4mm 2mm;text-align:right}.sol td{border-bottom:.25mm solid #d9d2c3;padding:.3mm 2mm}.sol td.c{text-align:center;white-space:nowrap}.sol code{font-family:"Courier New",monospace;font-size:9.6pt;direction:ltr;unicode-bidi:isolate}.cc{background:#e3f6ea;border-right:1.2mm solid #25a65f;border-radius:1mm;padding:.8mm 2.4mm;margin-top:1mm}'
scover = mkcover('פתרונות חוברת התרגילים', f'{COURSE}: הפתרון של כל תרגיל: הנוסחה בכל תא, התוצאה, והמסקנה.', f'<span class="n">{len(EX)}</span> תרגילים. קובץ התרגול באתר הקורס.')
sintro = ('<div class="intro"><p><b>איך משתמשים בפתרונות.</b> פותרים קודם לבד, בקובץ התרגול. רק אחר כך משווים: נוסחה מול נוסחה, ותוצאה מול תוצאה. '
          'כל נוסחה נכונה מתקבלת, גם אם היא כתובה אחרת. קובץ הפתרונות ב-Excel מכיל את אותן נוסחאות, חיות.</p></div>')
spage = HEAD('פתרונות חוברת התרגילים', SCSS) + scover + sintro + sbody_of(EX, True) + '</body></html>'
render(spage, 'booklet-solutions.pdf')
for _m, _ids in {}.items():
    render(HEAD(f'פתרונות, מפגש {_m}', SCSS) + mkcover(f'פתרונות: תרגילים למפגש {_m}', f'{COURSE}: {MEET_T[_m]}. הנוסחה בכל תא, התוצאה, והמסקנה.', f'<span class="n">{len(_ids)}</span> תרגילים מתוך חוברת התרגילים.')
           + MINTRO(_m, _ids, 'קודם פותרים לבד, ורק אז משווים: כל נוסחה נכונה מתקבלת, גם אם היא כתובה אחרת.') + sbody_of([BYID[i] for i in _ids], False) + '</body></html>', f'booklet-m{_m}-solutions.pdf')
