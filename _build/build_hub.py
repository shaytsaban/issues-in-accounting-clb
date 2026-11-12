# Course hub. Run: python3 build_hub.py  ->  ../index.html
# No recording boxes yet (Shay: add them when the first recording exists). Solutions are published and linked (Shay approved 2026-11-12).
import os, re
H = os.path.dirname(os.path.abspath(__file__))
n = lambda s: f'<span class="n">{s}</span>'
D = open(os.path.join(H, '..', 'lectures', 'lecture-1', 'presentation.html'), encoding='utf8').read()
NS, NX, NM = D.count('<section class="slide'), D.count('act xlq'), D.count('class="mc"')
_ns = {}
exec(open(os.path.join(H, '..', '_private', 'booklet.py'), encoding='utf8').read(), _ns)   # gitignored: holds the answer key
NB = len(_ns['EX'])
PLAN = [(1, 'מבוא לניתוח דוחות כספיים, ויחסי נזילות', 'יחס שוטף, יחס מהיר, יחס מזומן, הון חוזר ויחס התזרים', 'a'),
        (2, 'השפעת עסקאות על היחס השוטף, ויחסי איתנות פיננסית', 'התחייבויות להון עצמי, כיסוי ריבית, שירות חוב', 'a'),
        (3, 'יחסי יעילות', 'מלאי, לקוחות, ספקים ומחזור המרת המזומן', 'a'),
        (4, 'יחסי רווחיות', 'רווח גולמי, תפעולי ונקי, והמודל העסקי', 'a'),
        (5, 'יחסי תשואה ויחסי שוק', 'תשואה על ההון, מכפיל רווח, תשואת דיבידנד', 'a'),
        (6, 'שאלת ניתוח מלאה ברמת בחינה', 'כל קבוצות היחסים על חברה אחת', 'a'),
        (7, 'הערכת שווי: הבסיס', 'שווי נכסי, מכפילים, ומבוא להיוון תזרימי מזומנים', 'b'),
        (8, 'היוון תזרימי מזומנים: דוגמה מלאה', 'תזרים חופשי, ערך טרמינלי ומחיר ההון', 'b'),
        (9, 'מחיר ההון לעומק', 'ביטא, התשואה הנדרשת על המניות ומחיר החוב', 'b'),
        (10, 'הערכת שווי מלאה, ושיפוט איכותני', 'שאלה ברמת בחינה, ומה משנה את השווי', 'b'),
        (11, 'שאלות קצרות בכל נושאי הקורס', 'הבנה ותיאוריה', 'c'),
        (12, 'בחינה לדוגמה', 'פתרון מלא, במבנה הבחינה', 'c'),
        (13, 'חזרה מסכמת', 'לקראת הבחינה', 'c')]
plan = ''.join((f'<a class="pc {k} on" href="#lesson-1">' if i == 1 else f'<div class="pc {k}">') + f'<span class="pn">{n(i)}</span><b>{t}</b><span class="pd">{d}</span><em>{"באתר" if i == 1 else "בקרוב"}</em>' + ('</a>' if i == 1 else '</div>') for i, t, d, k in PLAN)
css = open(os.path.join(H, 'shell', 'hub.css'), encoding='utf8').read()
css += '''
.hero h1{font-size:64px}.hero .h1s{font-size:30px;font-weight:700;color:#7fe3d6;margin-top:6px;line-height:1.25}
.facts{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:-34px;position:relative;z-index:2}
.fact{background:#fff;border-radius:18px;padding:16px 20px;box-shadow:0 2px 0 var(--line),0 14px 34px rgba(22,33,58,.1);border-top:6px solid var(--coral)}
.fact:nth-child(2){border-top-color:#0f9d90}.fact:nth-child(3){border-top-color:#e8960c}.fact:nth-child(4){border-top-color:#27447f}
.fact .fi{font-size:28px;line-height:1}.fact b{display:block;font-size:19px;font-weight:800;color:var(--navy2);margin-top:6px}.fact>span{display:block;font-size:15.5px;color:var(--ink2);line-height:1.4;margin-top:2px}
.fact a{direction:ltr;unicode-bidi:isolate;display:inline-block;text-decoration:underline;overflow-wrap:anywhere}
.halves{display:flex;gap:10px;margin-top:16px;font-weight:800;font-size:15.5px;flex-wrap:wrap}
.halves>span{border-radius:99px;padding:5px 16px}.halves .a{background:#dff5f2;color:#087469}.halves .b{background:#ece8ff;color:#4f33c9}.halves .c{background:#fff0d2;color:#a86703}
.plan{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-top:14px}
.pc{position:relative;background:#fff;border-radius:16px;padding:14px 16px 34px;box-shadow:0 2px 0 var(--line);border-right:7px solid #0f9d90;display:block;color:inherit;text-decoration:none;min-height:132px;opacity:.78}
.pc.b{border-right-color:#6d4df2}.pc.c{border-right-color:#e8960c}
.pc.on{opacity:1;box-shadow:0 0 0 3px var(--coral),0 14px 30px rgba(255,106,77,.22);transition:transform .15s}.pc.on:hover{transform:translateY(-3px)}
.pc .pn{display:inline-grid;place-items:center;min-width:32px;height:32px;border-radius:10px;background:var(--navy2);color:#fff;font-weight:800;font-size:17px;margin-bottom:6px}
.pc b{display:block;font-size:17px;line-height:1.3;font-weight:800;color:var(--navy2)}.pc .pd{display:block;font-size:14.5px;color:var(--mut);line-height:1.35;margin-top:3px}
.pc em{position:absolute;bottom:10px;right:16px;font-style:normal;font-size:13px;font-weight:800;color:var(--mut);background:#eef0f6;border-radius:99px;padding:1px 12px}
.pc.on em{background:var(--coral);color:#fff}
.cgrid{display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px;margin-top:12px}.cnote{font-size:15px;color:var(--mut);margin-top:8px}
.grp{margin-bottom:14px}.grp h5{font-size:15.5px;font-weight:800;color:var(--navy2);margin:0 0 8px}
@media (max-width:900px){.plan{grid-template-columns:repeat(2,1fr)}.facts{grid-template-columns:repeat(2,1fr)}.cgrid{grid-template-columns:1fr}}
@media (max-width:560px){.plan{grid-template-columns:1fr}.pc{min-height:0}.facts{grid-template-columns:1fr;margin-top:-22px}.hero h1{font-size:42px}.hero .h1s{font-size:22px}}
'''
lk = lambda k, href, e, b, d, dl=False: f'<a class="lk {k}" href="{href}"' + (' download' if dl else ' target="_blank" rel="noopener"') + f'><span class="e">{e}</span><span><b>{b}</b><span class="d">{d}</span></span></a>'
html = f'''<!doctype html>
<html lang="he" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>סוגיות בחשבונאות | אתר הקורס</title>
<meta name="description" content="אתר הקורס סוגיות בחשבונאות, ניתוח דוחות כספיים והערכת שווי חברות, המרכז האקדמי למשפט ולעסקים ברמת גן: מצגות אינטראקטיביות עם גיליונות Excel חיים, סיכומים, חוברת תרגילים וקובצי תרגול.">
<link rel="stylesheet" href="assets/fonts.css">
<style>{css}</style>
</head>
<body>
<header class="hero"><div class="wrap">
<div class="kick"><span>המרכז האקדמי למשפט ולעסקים, רמת גן · החוג לחשבונאות · סמסטר א׳ תשפ״ז</span></div>
<h1>סוגיות בחשבונאות</h1>
<div class="h1s">ניתוח דוחות כספיים והערכת שווי חברות</div>
<p class="lead">בקורסי החשבונאות הפיננסית לומדים לערוך דוחות כספיים. כאן הדוחות כבר מוכנים, ולומדים לקרוא אותם: בחצי הראשון מנתחים חברה באמצעות יחסים פיננסיים, ובחצי השני מעריכים כמה היא שווה. לכל הרצאה באתר: מצגת אינטראקטיבית עם גיליונות Excel חיים שבודקים את הנוסחה שלכם, סיכום כתוב להדפסה וקובץ תרגול.</p>
<p class="meta">ד״ר שי צבאן · {n(13)} הרצאות</p>
</div></header>
<main class="wrap">
<section class="facts">
<div class="fact"><div class="fi">🎓</div><b>הציון</b><span>בחינה מסכמת: {n('100%')} מהציון. אין עבודות להגשה.</span></div>
<div class="fact"><div class="fi">🗓️</div><b>{n(13)} הרצאות</b><span>שש על ניתוח דוחות, ארבע על הערכת שווי, שלוש של תרגול וחזרה.</span></div>
<div class="fact"><div class="fi">📊</div><b>פותרים ב-Excel</b><span>כל שאלה במצגת נפתרת בגיליון חי, עם רמזים ופתרון צעד אחר צעד.</span></div>
<div class="fact"><div class="fi">✉️</div><b>פניות למרצה</b><span><a href="mailto:shay.tsaban@gmail.com">shay.tsaban@gmail.com</a><br>יש לציין את שם המוסד ואת שם הקורס.</span></div>
</section>
<section class="block" id="course-files">
<h2 class="sec">קובצי הקורס</h2>
<div class="cgrid">
{lk('s', 'materials/syllabus.pdf', '📋', 'סילבוס הקורס (PDF)', f'תיאור הקורס, תוצרי הלמידה, תוכנית {n(13)} ההרצאות והרכב הציון.')}
{lk('s', 'materials/booklet.pdf', '📘', 'חוברת תרגילים (PDF)', f'שאלות ברמת בחינה, לפי הרצאות. כרגע: {n(NB)} תרגילים להרצאה {n(1)}. פרק חדש נוסף אחרי כל הרצאה.')}
{lk('x', 'materials/booklet-practice.xlsx', '📊', 'קובץ התרגול של החוברת (Excel)', 'גיליון לכל תרגיל: הנתונים בתאים כחולים, ותאים צהובים ריקים לנוסחאות שלכם.', True)}
{lk('r', 'materials/booklet-solutions.pdf', '✅', 'פתרונות החוברת (PDF)', 'לכל תרגיל: הנוסחה בכל תא, התוצאה והמסקנה. פותחים רק אחרי שפותרים.')}
{lk('r', 'materials/booklet-solutions.xlsx', '✅', 'קובץ הפתרונות של החוברת (Excel)', 'אותם גיליונות, עם נוסחאות חיות.', True)}
</div>
</section>
<section class="block" id="plan">
<h2 class="sec">תוכנית הקורס: {n(13)} הרצאות</h2>
<div class="halves"><span class="a">הרצאות {n(1)} עד {n(6)}: ניתוח דוחות כספיים</span><span class="b">הרצאות {n(7)} עד {n(10)}: הערכת שווי חברות</span><span class="c">הרצאות {n(11)} עד {n(13)}: תרגול וחזרה</span></div>
<div class="plan">{plan}</div>
<p class="cnote">ייתכנו שינויים בסדר הנושאים ובקצב ההתקדמות במהלך הסמסטר. החומרים של כל הרצאה עולים לאתר כשהיא נלמדת.</p>
</section>
<section class="block">
<h2 class="sec">ההרצאות</h2>
<article class="lec" id="lesson-1">
<div class="lec-head"><div class="lec-n">1</div><div><h3>מבוא לניתוח דוחות כספיים, ויחסי נזילות</h3><div class="sub">הרצאה {n(1)}</div></div></div>
<div class="lec-body">
<div><h4>מה לומדים בהרצאה</h4><ul class="learn">
<li>ההבדל בין עריכת דוחות לניתוח דוחות, ומהו יחס פיננסי</li>
<li>יחס הוא אינדיקציה: השוואה לשנים קודמות, לענף ולהקשר</li>
<li>שש קבוצות היחסים של הקורס</li>
<li>נכסים שוטפים והתחייבויות שוטפות, כולל חלויות שוטפות</li>
<li>יחס שוטף, יחס מהיר ויחס מזומן: חישוב, פרשנות, יתרונות וחסרונות</li>
<li>הון חוזר, ויחס התזרים מפעילות שוטפת להתחייבויות השוטפות</li>
<li>ניתוח נזילות מלא: שנתיים, ממוצע ענפי ומסקנה מנומקת</li>
<li>תרגול עצמי: שישה תרגילים, כל אחד עם גיליון, רמזים, פתרון צעד אחר צעד וכפתור ״הסבר נוסף״</li>
</ul></div>
<div><h4>חומרי ההרצאה</h4>
<div class="grp"><h5>1. בהרצאה</h5><div class="links">
<a class="lk p" href="lectures/lecture-1/presentation.html"><span class="e">🖥️</span><span><b>מצגת ההרצאה</b><span class="d">{n(NS)} שקפים, וגיליון Excel חי ליד כל שאלה ({n(NX)} גיליונות), עם בדיקה, רמזים ופתרון צעד אחר צעד.</span></span></a>
</div></div>
<div class="grp"><h5>2. אחרי ההרצאה, לחזרה</h5><div class="links">
<a class="lk s" href="lectures/lecture-1/summary.pdf"><span class="e">📄</span><span><b>סיכום ההרצאה (PDF)</b><span class="d">כל תוכן המצגת במסמך אחד: הגדרות, השאלות והפתרון שלהן בגיליון, ומילון מושגים.</span></span></a>
</div></div>
<div class="grp"><h5>3. תרגול</h5><div class="links">
<a class="lk x" href="materials/practice-1.xlsx" download><span class="e">📊</span><span><b>קובץ התרגול של הרצאה 1 (Excel)</b><span class="d">כל {n(NX)} השאלות של המצגת, באותן כתובות תאים. התאים הצהובים ריקים: כותבים בהם את הנוסחאות.</span></span></a>
<a class="lk s" href="materials/booklet.pdf" target="_blank" rel="noopener"><span class="e">📘</span><span><b>חוברת התרגילים: הרצאה 1</b><span class="d">תרגילים {n('1-1')} עד {n(f'1-{NB}')}: שאלות ברמת בחינה, עם סעיף פרשנות.</span></span></a>
<a class="lk r" href="materials/practice-1-solutions.xlsx" download><span class="e">✅</span><span><b>קובץ הפתרונות של הרצאה 1 (Excel)</b><span class="d">גיליונות המצגת עם נוסחאות חיות. פותחים רק אחרי שפותרים.</span></span></a>
<a class="lk r" href="materials/booklet-solutions.pdf" target="_blank" rel="noopener"><span class="e">✅</span><span><b>פתרונות החוברת (PDF)</b><span class="d">הנוסחה בכל תא, התוצאה והמסקנה.</span></span></a>
</div></div>
</div>
</div>
<div class="todo"><h4>📝 מה עושים בהרצאה {n(1)}</h4><ol>
<li><b>בהרצאה:</b> עובדים במצגת, בגיליונות שבתוך השקפים.</li>
<li><b>אחרי ההרצאה:</b> קוראים את הסיכום, ופותרים בקובץ התרגול את השאלות של המצגת. בכל שאלה במצגת, ״צעד אחר צעד״ מראה את הפתרון.</li>
<li><b>מהחוברת:</b> תרגילים {n('1-1')} עד {n(f'1-{NB}')}, בקובץ התרגול של החוברת. את סעיפי הפרשנות כותבים במילים, ורק אחר כך בודקים מול הפתרונות.</li>
</ol></div>
</article>
</section>
<footer>ד״ר שי צבאן · פניות במייל: <a href="mailto:shay.tsaban@gmail.com">shay.tsaban@gmail.com</a>, עם שם המוסד ושם הקורס</footer>
</main>
</body>
</html>
'''
for bad in ('—', '־', '–'):
    assert bad not in html, bad
open(os.path.join(H, '..', 'index.html'), 'w', encoding='utf8').write(html)
print('hub', len(html), 'slides', NS, 'sheets', NX, 'booklet', NB)
