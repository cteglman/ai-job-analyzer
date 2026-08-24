import json

skills = [
    "Python",
    "SQL",
    "PostgreSQL",
    "Docker",
    "Git",
    "REST",
    "COBOL",
    "DB2"
]

candidate_skills = [
    "COBOL",
    "DB2",
    "SQL",
    "Git",
    "Python"
]


def analyze_text(text):
    long_words = 0
    ord_list = text.split()
    found_skills = []
    matched_skills = []
    missing_skills = []
    text_lower = text.lower()

    for skill in skills:
        if skill.lower() in text_lower:
            found_skills.append(skill.lower())

    for cskill in candidate_skills:
        if cskill.lower() in found_skills:
            matched_skills.append(cskill)
        else:
            missing_skills.append(cskill)

    for ord in ord_list:
        if len(ord) > 7:
            long_words += 1

    resultat = {
        "characters": len(text), 
        "words": len(ord_list),
        "long_words": long_words,
        "found_skills": found_skills,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills
        }
    return resultat

with open("jobannonce.txt", "r", encoding="utf-8") as file:
    text = file.read()

result = analyze_text(text)

with open("analyse.json", "w", encoding="utf-8") as file:
    json.dump(result, file, indent=4, ensure_ascii=False)

