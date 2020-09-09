import random
def anti_offence(inp):
    swears=[
            "چس",
            "گوز",
            "ان",
            "لجن",
            "کثافت",
            "بی شرف",
            "بیشعور",
            "گوه",
            "کون",
            "کیری",
            "کسکش",
            "بی ناموس",
            "سگ پدر",
            "پدرسگ",
            "شاش",
            "ریدن",
            "ریدی",
            "کونی",
            "دیوس",
            "انی",
            "گهی",
            "بی پدر",
            "مادرسگ",
            "بی ناموس",
            "جنده",
            "گایدی",
            "گایدن",
            "کیر",
            "کیروکس",
            "عمتو",
            "خفه شو",
            "خفه",
            "خفه خون",
            "مرض داری",
            "مرضداری",
            "گردن دراز",
            "خری",
            "گاوی",
            "اسبی",
            "سگی",
            "حیوانی",
            "دهنتوببند",
            "انگل",
            "آشغال",
            "خرفت",
            "پپه",
            "خنگ",
            "دکل",
            "دله",
            "قرتی",
            "گوزو",
            "کونده",
            "کون ده",
            "گاگول",
            "ابله",
            "گنده گوز",
            "کس",
            "کله کیری",
            "گشاد",
            "دخترقرتی",
            "خواهرجنده",
            "مادرجنده",
            "لخت",
            "بخورش",
            "بپرسرش",
            "بپرروش",
            "بیابخورش",
            "میخوریش",
            "بمال",
            "دیوس خان",
            "زرنزن",
            "زنشو",
            "زنتو",
            "زن جنده",
            "بکنمت",
            "بکن",
            "بکن توش",
            "بکنش",
            "لز",
            "سکس",
            "سکسی",
            "ساک",
            "ساک بزن",
            "پورن",
            "سکسیی",
            "کونن",
            "کیرر",
            "جاکش",
            "انی",
            "بدبخت",
            "خایه",
            "خایه مال",
            "خایه خور",
            "ممه",
            "ممه خور",
            "دخترجنده",
            "خارکسده",
            "کس ننت",
            "کیردوس",
            "مادرکونی",
            "خارکسده",
            "خارکس ده",
            "کیروکس",
            "کس و کیر",
            "زنا",
            "زنازاده",
            "ولدزنا",
            "ملنگ",
            "سادیسمی",
            "فاحشه",
            "خانم جنده",
            "فاحشه خانم",
            "سیکتیر",
            "سسکی",
            "کس خیس",
            "حشری",
            "گاییدن",
            "بکارت",
            "داف",
            "بچه کونی",
            "کسشعر",
            "سرکیر",
            "سوراخ کون",
            "حشری شدن",
            "کس کردن",
            "کس دادن",
            "بکن بکن",
            "شق کردن",
            "کس لیسیدن",
            "آب کیر",
            "جاکش",
            "جلق زدن",
            "جنده خانه",
            "شهوتی",
            "عن",
            "قس",
            "کردن",
            "کردنی",
            "کس لیس",
            "کس کش",
            "کوس",
            "کیرمکیدن",
            "لاکونی",
            "پستان",
            "آلت",
            "آلت تناسلی",
            "نرکده",
            "مالوندن",
            "سولاخ",
            "جنسی",
            "دوجنسه",
            "سگ تو روحت",
            "بی غیرت",
            "نعشه",
            "بی عفت",
            "مادرقهوه",
            "پلشت",
            "پریود",
            "کله کیری",
            "کیرناز",
            "پشمام",
            "لختی",
            "کسکیر",
            "دوست دختر",
            "دوست پسر",
            "کونشو",
            "دول",
            "شنگول",
            "کیردراز",
            "داف ناز",
            "سکسیم",
            "کوص",
            "ساکونی",
            "کون گنده",
            "سکسی باش",
            "کسخل",
            "صیغه ای",
            "گوش دراز",
            "درازگوش",
            "توله سگ",
            "خز",
            "ماچ",
            "ماچ کردنی",
            "اسکل",
            "هیز",
            "بیناموس",
            "اوسکل",
            "بی آبرو",
            "لاشی",
            "لاش گوشت",
            "باسن",
            "جکس",
            "سگ صفت",
            "کصکش",
            "مشروب",
            "عرق خور",
            "سکس چت",
            "جوون",
            "سرخور",
            "کلفت",
            "حشر",
            "لاس",
            "زارت",
            "رشتیf",
            "ترک",
            "فارس",
            "لر",
            "عرب",
            "خر",
            "گاو",
            "اسب",
            "گوسفند",
            "کرم",
            "الاق",
            "الاغ",
            "احمق",
            "بی شعور",
            "حرومزاده",
            "کونی",
            "گه",
            "مادر جنده",
            "کث",
            "کص",
            "پسون",
            "خارکسّه",
            "دهن گاییده",
            "دهن سرویس",
            "پدر سگ",
            "پدر سوخته",
            "پدر صلواتی",
            "لامصب",
            "زنیکه",
            "مرتیکه",
            "مردیکه",
            "بی خایه",
            "عوضی",
            "اسگل",
            "اوسکل",
            "اوسگل",
            "اوصگل",
            "اوصکل",
            "دیوث",
            "دیوص",
            "قرمصاق",
            "قرمساق",
            "غرمساق",
            "غرمصاق",
            "فیلم سوپر",
            "چاقال",
            "چاغال",
            "چس خور",
            "کس خور",
            "کس خل",
            "کوس خور",
            "کوس خل",
            "کص لیس",
            "کث لیس",
            "کس لیس",
            "کوص لیس",
            "کوث لیس",
            "کوس لیس",
            "کون سوراخ",
            "سوراخ کون",
            "کون پنیر"
    ]
    for item in swears:
        if item==inp:
            return random.choice(swears)
    return False
while True:
    print(anti_offence(input("input :")))
