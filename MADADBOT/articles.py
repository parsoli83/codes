import random
def Article():
    Link= random.choice((
        "https://sookhtejet.com/%d8%a8%db%8c-%d8%a7%d9%86%da%af%db%8c%d8%b2%da%af%db%8c/",
        "https://sookhtejet.com/%d8%a8%d8%b2%d8%b1%da%af-%d9%81%da%a9%d8%b1-%da%a9%d9%86%db%8c%d8%af-1/",
        "https://sookhtejet.com/%d8%a8%d8%b1%da%af%d9%87-%d8%aa%d9%82%d9%84%d8%a8-%d8%a7%d8%b9%d8%aa%d9%85%d8%a7%d8%af-%d8%a8%d9%87-%d9%86%d9%81%d8%b3/",
        "https://sookhtejet.com/%d9%86%d8%ac%d9%88%d8%a7%db%8c-%d8%b0%d9%87%d9%86%db%8c/",
        "https://sookhtejet.com/%d8%a7%d9%86%da%af%db%8c%d8%b2%d9%87-%da%a9%d8%a7%d8%b1%d8%a2%d9%81%d8%b1%db%8c%d9%86%db%8c/"
    ))
    
    return "href,{},{}".format("برای مطلب انگیزشی کلیک کن",Link)
print (Article())