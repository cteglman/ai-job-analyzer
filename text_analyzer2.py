def analyze_text(text):
    resultat = {
        "characters": len(text), 
        "words": len(text.split()),
        "word_list": text.split()
        }
    return resultat

text = "Python er et programmeringssprog, der bruges meget inden for kunstig intelligens og machine learning."

result = analyze_text(text)
print(f"Antal tegn: {result['characters']}")
print(f"Antal ord: {result['words']}")
print(f"Antal ord: {result['word_list']}")
foerste_ord = result['word_list'][0]
print(f"Første ord: {foerste_ord}")
for nummer, ord in enumerate(result['word_list'],1):
    if len(ord) < 5:
        bemaerk = "kort ord"
    elif len(ord)< 8:
        bemaerk = "mellem ord"
    else:
        bemaerk = "langt ord"
    print(f"{nummer}: {ord} ({len(ord)} tegn) {bemaerk}")
