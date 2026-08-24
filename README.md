# AI Job Analyzer

A Python-based application for analyzing job advertisements and identifying relevant technical skills.

This project is being developed as part of my practical learning journey in Python and AI Engineering.
## Current Features
The current version can:
- Read a job advertisement from a text file
- Count the number of characters
- Count the number of words
- Count words longer than seven characters
- Identify predefined technical skills mentioned in the advertisement
- Save the analysis as a JSON file
## Project Structure

```text
ai-job-analyzer/
│
├── src/
│   └── analyzer.py
│
├── data/
│   └── jobannonce.txt
│
├── output/
│   └── analyse.json
│
├── .gitignore
└── README.md
```
## Technologies
The project currently uses:
- Python 3.12
- JSON
- Git
- GitHub
- Visual Studio Code
## Running the Application
From the project directory, run:

```Bash
python src/analyzer.py
```
The application reads the job advertisement from: `data/jobannonce.txt`

and writes the result to: `output/analyse.json`

## Example Output
```json
{
    "characters": 151,
    "words": 25,
    "long_words": 7,
    "found_skills": [
        "Python",
        "SQL",
        "PostgreSQL",
        "Docker"
    ]
}
```
## Roadmap
Planned improvements include:
- Compare job requirements with candidate skills
- Identify matching and missing skills
- Calculate a job match score
- Move candidate information to structured JSON
- Improve text and skill detection
- Integrate an LLM for intelligent job analysis
- Add structured AI output
- Add automated tests
## Purpose
The long-term goal is to develop the project from a simple Python text analyzer into an AI-powered job analysis application.

The project will be expanded step by step as new Python, software engineering, and AI Engineering concepts are introduced.