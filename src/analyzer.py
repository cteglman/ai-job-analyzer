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

with open("data/candidate.json", "r", encoding="utf-8") as file:
    candidate = json.load(file)
       
def analyze_job(text, candidate_skills):
    long_words = 0
    ord_list = text.split()
    found_skills = []
    matched_skills = []
    missing_skills = []
    text_lower = text.lower()
    candidate_skills_lower = [skill.lower() for skill in candidate_skills]

    for skill in skills:
        if skill.lower() in text_lower:
            found_skills.append(skill)

    for skill in found_skills:
        if skill.lower() in candidate_skills_lower:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    for ord in ord_list:
        if len(ord) > 7:
            long_words += 1

    if len(found_skills) > 0:
        match_percentage = round(len(matched_skills) / len(found_skills) * 100, 1)
    else:
        match_percentage = 0

    resultat = {
        "characters": len(text), 
        "words": len(ord_list),
        "long_words": long_words,
        "match_percentage": match_percentage,
        "found_skills": found_skills,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills
        }
    return resultat

with open("data/jobannonce.txt", "r", encoding="utf-8") as file:
    text = file.read()

result = analyze_job(text, candidate["skills"])

with open("output/analyse.json", "w", encoding="utf-8") as file:
    json.dump(result, file, indent=4, ensure_ascii=False)

