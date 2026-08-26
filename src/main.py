#
# A Python-based application for analyzing job advertisements and 
# identifying relevant technical skills.
#
from analyzer import analyze_job
from file_handler import read_text_file, read_json_file, write_json_file

skills_data = read_json_file("data/skills.json")

candidate_skills = read_json_file("data/candidate.json")

text = read_text_file("data/jobannonce.txt")

analysis = analyze_job(
    text, 
    candidate_skills["skills"], 
    skills_data["skills"]
    )

result = {
    "candidate":  {
        "name": candidate_skills["name"],
        "skills": candidate_skills["skills"]
    },
    "job_analysis": analysis["job_analysis"],
    "text_analysis": analysis["text_statistics"]
}

write_json_file("output/analyse.json", result)
