# Syllabus PDF. Run: python3 build_syllabus.py  ->  ../materials/syllabus.pdf
import html, os, shutil, subprocess, tempfile
H = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(H, '..', '..', 'iit-build', 'fonts')
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
SITE = 'https://shaytsaban.github.io/issues-in-accounting-clb/'
NOTE = 'ייתכנו שינויים בסדר הנושאים ובקצב ההתקדמות במהלך הסמסטר. עדכונים יפורסמו באתר הקורס.'
n = lambda s: f'<span class="n">{s}</span>'
en = lambda s: f'<span class="en2">{s}</span>'
# the 13 lectures, planned from the course notes of the previous year (11 meetings) and the summary exercises
L = [('1', 'מבוא לניתוח דוחות כספיים, ויחסי נזילות', 'ההבדל בין עריכת דוחות לניתוחם; יחס פיננסי כאינדיקציה; שש קבוצות היחסים; יחס שוטף, יחס מהיר, יחס מזומן, הון חוזר, ויחס התזרים מפעילות שוטפת להתחייבויות השוטפות.'),
     ('2', 'השפעת עסקאות על היחס השוטף, ויחסי איתנות פיננסית', 'מה קורה ליחס השוטף כשנוטלים הלוואה או פורעים חוב; התחייבויות להון עצמי, התחייבויות לנכסים, הון עצמי לנכסים, יחס כיסוי ריבית ויחס שירות חוב.'),
     ('3', 'יחסי יעילות', 'מחזור מלאי וימי מלאי; מחזור לקוחות וימי לקוחות; מחזור ספקים וימי ספקים; מחזור נכסים; מחזור המרת המזומן.'),
     ('4', 'יחסי רווחיות', 'שיעור רווח גולמי, תפעולי ונקי; הפערים ביניהם ומה מסביר אותם; כוח מיקוח, מודל עסקי ומבנה ההוצאות.'),
     ('5', 'יחסי תשואה ויחסי שוק', 'תשואה על ההון העצמי ועל הנכסים; רווח למניה, מכפיל רווח, תשואת דיבידנד, שיעור חלוקת הדיבידנד, שווי שוק מול שווי בספרים.'),
     ('6', 'שאלת ניתוח מלאה ברמת בחינה', 'ניתוח משולב של חברה אחת בכל קבוצות היחסים, לאורך שנים ומול ממוצעי הענף: נקודות חוזק, נקודות חולשה והסברים חלופיים.'),
     ('7', 'הערכת שווי: הבסיס', 'מהו שווי חברה; גישת השווי הנכסי; גישת המכפיל; מבוא לגישת היוון תזרימי המזומנים ' + en('(DCF, Discounted Cash Flow)') + '.'),
     ('8', 'היוון תזרימי מזומנים: דוגמה מלאה', 'מהרווח התפעולי לתזרים המזומנים החופשי: מס, פחת, השקעות והון חוזר; תקופת התחזית והערך הטרמינלי; מחיר ההון הממוצע המשוקלל ' + en('(WACC, Weighted Average Cost of Capital)') + '.'),
     ('9', 'מחיר ההון לעומק', 'התשואה הנדרשת על המניות לפי מודל תמחור נכסי הון ' + en('(CAPM, Capital Asset Pricing Model)') + '; ביטא וחישובה ב-Excel; חילוץ מחיר החוב מנתוני אגרת חוב.'),
     ('10', 'הערכת שווי מלאה, ושיפוט איכותני', 'שאלת הערכת שווי ברמת בחינה; תיקון נתונים והנחות; איך שינויים בסיכון ובסביבה הכלכלית משנים את השווי.'),
     ('11', 'שאלות קצרות בכל נושאי הקורס', 'שאלות הבנה ותיאוריה בנושאי ניתוח הדוחות והערכת השווי.'),
     ('12', 'בחינה לדוגמה', 'פתרון מלא של בחינה לדוגמה, במבנה הבחינה.'),
     ('13', 'חזרה מסכמת', 'חזרה על נושאי הקורס המרכזיים, ומענה לשאלות לקראת הבחינה.')]
rows = ''.join(f'<tr{" class=hi" if i == 0 else ""}><td class="c">{n(k)}</td><td><b>{t}</b></td><td class="rd"><div>{w}</div></td></tr>' for i, (k, t, w) in enumerate(L))
OUT = ['חישוב יחסי נזילות, איתנות, יעילות, רווחיות, תשואה ושוק מתוך דוחות כספיים, ופרשנות התוצאה.',
       'ניתוח מגמות לאורך שנים, והשוואה לממוצעי ענף ולמדיניות המוצהרת של החברה.',
       'ניסוח מסקנה מנומקת על מצב החברה: נקודות חוזק, נקודות חולשה, והסברים חלופיים לממצאים.',
       'הערכת שווי חברה בגישת השווי הנכסי ובגישת המכפיל.',
       'בניית תזרים מזומנים חופשי, חישוב ערך טרמינלי, והערכת שווי בגישת היוון תזרימי המזומנים.',
       'חישוב מחיר ההון: התשואה הנדרשת על המניות, מחיר החוב, ומחיר ההון הממוצע המשוקלל.',
       'ביצוע כל החישובים ב-Excel.']
body = f"""
<div class="hd"><div class="k">המרכז האקדמי למשפט ולעסקים, רמת גן · החוג לחשבונאות · סמסטר א׳ תשפ״ז</div><h1 class="t">סוגיות בחשבונאות</h1><div class="s">ניתוח דוחות כספיים והערכת שווי חברות · סילבוס הקורס · <span class="en2">Financial Reports Analysis &amp; Corporate Valuation</span></div></div>
<table class="meta"><tr><td>היקף</td><td>{n('13')} הרצאות</td></tr>
<tr><td>קהל היעד</td><td>סטודנטים במסלול ראיית חשבון</td></tr>
<tr><td>מרצה</td><td>ד״ר שי צבאן, {n('shay.tsaban@gmail.com')}</td></tr>
<tr><td>אתר הקורס</td><td><span class="url">{SITE}</span></td></tr></table>
<h3>תיאור הקורס ומטרותיו</h3>
<p>בקורסי החשבונאות הפיננסית לומדים איך עורכים דוחות כספיים: איך מודדים ומציגים כל פריט. נקודת המוצא של הקורס הזה שונה: הדוחות כבר מוכנים, והמטרה היא להבין מה הם מספרים על החברה.</p>
<p><b>החצי הראשון: ניתוח דוחות כספיים.</b> נלמד שש קבוצות של יחסים פיננסיים: נזילות, איתנות פיננסית, יעילות, רווחיות, תשואה ושוק. לכל יחס: איך מחשבים אותו, מה משמעותו, ואיך מפרשים אותו מול שנים קודמות ומול הענף. יחס פיננסי הוא אינדיקציה, ולא פסק דין, ולכן הדגש הוא על מסקנה מנומקת.</p>
<p><b>החצי השני: הערכת שווי חברות.</b> נכיר שלוש גישות להערכת שווי: השווי הנכסי, המכפיל, והיוון תזרימי המזומנים, שהיא הגישה המרכזית בקורס. נבנה תזרים מזומנים חופשי, נחשב ערך טרמינלי, ונאמוד את מחיר ההון של החברה.</p>
<h3>שיטת ההוראה</h3>
<p>הרצאות שבהן שזורים תרגילים. לכל הרצאה באתר הקורס: מצגת אינטראקטיבית עם גיליונות Excel חיים, סיכום כתוב להדפסה וקובץ תרגול. חוברת התרגילים מסודרת לפי הרצאות, ופרק חדש נוסף לה אחרי כל הרצאה.</p>
<h3>תוצרי למידה: בסוף הקורס הסטודנטים ידעו</h3>
<ol>{''.join(f'<li>{x}</li>' for x in OUT)}</ol>
<h3>תוכנית הקורס</h3>
<table class="plan"><thead><tr><th>הרצאה</th><th>הנושא</th><th>התוכן</th></tr></thead><tbody>{rows}</tbody></table>
<div class="note">{NOTE}</div>
<h3>מרכיבי הציון</h3>
<table class="meta"><tr><td>בחינה מסכמת</td><td>{n('100%')} מהציון הסופי. הבחינה מקיפה את כל נושאי הקורס. מבנה הבחינה יפורסם במהלך הסמסטר.</td></tr></table>
<h3>קריאת רשות</h3>
<p>חומרי האתר מכסים את כל תוכן הקורס. למי שמבקש להרחיב:</p>
<ul><li>עדן, י׳ ושוב, ש׳. <i>ניתוח דוחות כספיים והערכות שווי</i>.</li></ul>
<ul class="enl"><li>Palepu, K. G., Healy, P. M., &amp; Peek, E. Business Analysis and Valuation: IFRS Edition.</li>
<li>Damodaran, A. Investment Valuation: Tools and Techniques for Determining the Value of Any Asset.</li></ul>
<h3>יצירת קשר</h3>
<p>פניות לד״ר שי צבאן במייל: {n('shay.tsaban@gmail.com')}. חובה לרשום בכל פנייה את שם המוסד ואת שם הקורס.</p>"""
CSS = '''
@font-face{font-family:"David";src:url("david.ttf");font-weight:400}
@font-face{font-family:"David";src:url("davidbd.ttf");font-weight:700}
@page{size:A4;margin:16mm;@bottom-center{content:counter(page);font-family:"David";font-size:10pt;color:#5d6a86}}
:root{--ink:#16213a;--navy:#1b2d55;--coral:#ff6a4d;--mut:#5d6a86;--line:#d9d2c3}
*{box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact}
html{direction:rtl}body{font-family:"David";font-size:11.8pt;line-height:1.34;color:var(--ink);margin:0}
.n{direction:ltr;unicode-bidi:isolate}
.hd{background:linear-gradient(160deg,#0f1b33 0%,#1b2d55 60%,#27447f 100%);color:#fff;border-radius:3mm;padding:6mm 8mm;margin-bottom:4mm}
.hd .k{color:#7fe3d6;font-weight:700;font-size:12pt}.hd h1.t{color:#fff;margin:1.5mm 0 1mm;font-size:24pt}.hd .s{color:#d6e0f7;font-size:13.5pt}
h3{font-size:13.4pt;color:var(--navy);margin:4mm 0 1.2mm;break-after:avoid;border-bottom:.5mm solid var(--coral);padding-bottom:.6mm}
p{margin:0 0 1.6mm}ul{margin:0 0 1.6mm;padding-right:6mm}li{margin-bottom:.5mm}
table{width:100%;border-collapse:collapse;font-size:10.8pt;margin:1.2mm 0 2mm}th{background:var(--navy);color:#fff;text-align:right;padding:1mm 2mm}td{padding:1mm 2mm;border-bottom:.25mm solid var(--line);vertical-align:top}tr{break-inside:avoid}
table.meta td:first-child{font-weight:700;width:30mm;color:var(--navy)}td.c{text-align:center;font-weight:700}td.r{white-space:nowrap}
tr.hi td{background:#fff0d2}.note{background:#eef2ff;border-right:1.2mm solid var(--navy);border-radius:1mm;padding:1.2mm 2.6mm;font-size:10.8pt}
.url{direction:ltr;unicode-bidi:isolate;font-family:Arial,sans-serif;font-size:10pt;color:var(--navy)}
.tbd{background:#fff0d2;border:.3mm dashed #a86703;border-radius:1mm;padding:0 2mm;font-weight:700;color:#7a4a00}
.lit{list-style:none;padding:0}.lit .n{display:block;text-align:left}
.w{font-size:10.4pt;color:#2a3858;margin-top:.4mm}td.rd{font-size:10pt;width:62mm}li.en,div.en{direction:ltr;text-align:left;unicode-bidi:isolate}.en2{direction:ltr;unicode-bidi:isolate}ul.enl{direction:ltr;text-align:left;padding-left:6mm;padding-right:0;font-size:10.4pt}ol{margin:0 0 1.6mm;padding-right:6mm}
'''
page = f'<!doctype html><html lang="he" dir="rtl"><head><meta charset="utf-8"><title>סוגיות בחשבונאות | סילבוס</title><style>{CSS}.plan td.rd{{width:56%}}</style></head><body>{body}</body></html>'
assert '—' not in page and '־' not in page
d = tempfile.mkdtemp(dir=os.environ.get('TMPDIR'))
for f in ('david.ttf', 'davidbd.ttf'): shutil.copy(os.path.join(FONTS, f), d)
open(os.path.join(d, 's.html'), 'w', encoding='utf8').write(page)
out = os.path.abspath(os.path.join(H, '..', 'materials', 'syllabus.pdf'))
subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--no-sandbox', f'--user-data-dir={d}/p', '--no-pdf-header-footer', '--virtual-time-budget=6000', f'--print-to-pdf={out}', 'file://' + d + '/s.html'], capture_output=True, timeout=120)
shutil.rmtree(d, True)
import fitz
D = fitz.open(out); print('pages', len(D), 'bytes', os.path.getsize(out), sorted({f[3].split('+')[-1] for p in D for f in p.get_fonts()}))
