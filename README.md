# סוגיות בחשבונאות: ניתוח דוחות כספיים והערכת שווי חברות

אתר הקורס: https://shaytsaban.github.io/issues-in-accounting-clb/

המרכז האקדמי למשפט ולעסקים, רמת גן, החוג לחשבונאות. סמסטר א׳ תשפ״ז. ד״ר שי צבאן. 13 הרצאות, ציון: בחינה מסכמת 100%.

- `index.html`: דף הבית, עם תוכנית 13 ההרצאות.
- `lectures/lecture-1/`: מצגת הרצאה 1 (`presentation.html`) וסיכום PDF (`summary.pdf`): מבוא לניתוח דוחות כספיים ויחסי נזילות.
- `materials/`: סילבוס, חוברת תרגילים לפי הרצאות (`booklet.pdf`), קובץ התרגול שלה, וקובץ התרגול של הרצאה 1.
- `_build/`: מקורות הבנייה. התוכן כתוב פעם אחת (`content_*.py`) ומזין גם את המצגת וגם את הסיכום.
  - `python3 build_deck.py 1`: המצגת. גיליונות ה-Excel החיים רצים על `xl.js`.
  - `python3 test_deck.py`: בדיקה בדפדפן ללא ממשק: שקפים שחורגים, כיוון מספרים, וכל גיליון: דוחה תשובה שגויה ומקבל נוסחה נכונה.
  - `python3 build_summary.py 1`, `python3 build_syllabus.py`, `python3 build_hub.py`.
  - `python3 build_xlsx.py 1` ו-`python3 build_booklet.py`: קובצי התרגול. כל תשובה נבדקת מול חישוב מחדש ב-LibreOffice.
  - הפתרונות (חוברת וקובץ התרגול) נכתבים לתיקייה `_private`, שאינה חלק מהמאגר.
  - פונטי David נטענים מ-`../iit-build/fonts` ואינם נשמרים כאן.
