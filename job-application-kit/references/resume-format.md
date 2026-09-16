# Resume and CV format

Sources merged: Harvard Career Services resume guide, r/EngineeringResumes wiki, The Tech Resume Inside Out (Gergely Orosz), MIT CAPD, recruiter write-ups from Amazon and Google, Wirtschaftswoche / Stepstone / Karrierebibel guidance for the German market.

## Page

- US, Canada, India: US Letter. Everywhere else: A4. Ask if unsure; a Letter document printed on A4 in Europe looks wrong.
- Margins 1.9 to 2.5 cm (0.75 to 1 inch). Below 1.5 cm looks crammed. Above 2.5 cm looks empty.
- Length by experience: 0 to 5 years one page, 5 to 15 years two pages, 15+ years still two pages. Only academic CVs and some UK, AU and German CVs go longer.
- If page two is less than half full, cut to one page.
- Nothing in headers or footers. Several ATS parsers skip them and so do skim-readers.

## Fonts and sizes

| Element | Size | Style |
|---|---|---|
| Name | 15 to 18 pt | Bold |
| Section headings | 11 to 12 pt | Bold, small caps allowed, thin bottom rule allowed |
| Body and bullets | 10.5 to 11 pt | Regular |
| Tech line under a role | 9.5 to 10 pt | Italic or grey |

Calibri, Arial, Helvetica, Georgia, Garamond or Lato. Nothing decorative. One font family for the whole document. Black text. One accent colour for headings is fine; more looks like a template.

Line spacing 1.0 to 1.15. About 10 pt of space before a section heading, about 6 pt between roles, 1 to 2 pt between bullets.

## Layout rules that protect the document

- Single column. Sidebars and two-column layouts get parsed out of order by older ATS and scanned out of order by humans.
- No tables for layout. A simple two-column table for a skills list is acceptable if the content reads correctly row by row, but tab stops are safer.
- No text boxes, icons, skill bars, star ratings, charts, logos or progress circles. They carry no information and some parsers drop them.
- No photo outside DACH, parts of continental Europe, and some Asian and Middle Eastern markets. See regions reference.
- Bullets: the standard round bullet. No arrows, checkmarks or emoji.
- Dates right-aligned with a tab stop. Bullets must not run past the date column.
- Links as plain black text, still clickable: `github.com/name`, `linkedin.com/in/name`. No "https://www.", no underline, no "Email:" prefix.

## Section names

Use the plain ones. ATS parsers and humans both look for them.

| Use | Avoid |
|---|---|
| Experience or Work Experience | Career Journey, Professional History, Where I've Been |
| Education | Academic Background |
| Skills or Technical Skills | Toolbox, Core Competencies, What I Bring |
| Projects | Things I Built |
| Publications | Research Output |
| Certifications | Credentials |

## Section order

Tech or engineering, 3+ years:
1. Name and contact line
2. Skills
3. Experience
4. Projects (optional)
5. Education

Student, graduate, or under 3 years:
1. Name and contact line
2. Education (with grade if good, relevant coursework, thesis topic)
3. Skills
4. Experience (internships, working student, part-time, teaching, research assistant)
5. Projects

Non-technical mid-career:
1. Name and contact line
2. Summary (3 lines)
3. Experience
4. Skills
5. Education and certifications

Senior or executive:
1. Name and contact line
2. Summary
3. Selected achievements (optional, 3 to 4 lines)
4. Experience
5. Board, advisory, speaking (if any)
6. Education

Career changer: summary first, then whichever of skills, projects or experience best proves the new direction.

## Contact line

One line, centred or left, pipes between items:

`Berlin, Germany | name@gmail.com | +49 170 000 0000 | linkedin.com/in/name | github.com/name`

Include city and country. Recruiters filter by location and a missing location reads as "will need relocation". Do not include a street address outside DACH. Use a plain email address. Add a work permit line if it removes a question the recruiter would otherwise have to ask, for example "EU Blue Card holder, no sponsorship needed" or "Eligible to work in the UK".

Never include: date of birth, age, marital status, religion, nationality (outside DACH), photo (outside DACH), social security or ID numbers, a second phone number.

## Summary or positioning statement

Skip it for juniors. For everyone else, three lines:

[Role identity] with [years] in [domain]. [One signature result or strength]. [What you are looking for, in the posting's language].

> Machine learning engineer with 6 years in fraud detection for payments. Shipped models that cut chargeback losses 23 percent at two fintechs. Looking to lead applied ML for a risk team.

Not a personality description. No "motivated", "passionate", "dynamic", "results-driven".

## Experience entry

```
Job Title, Company Name, City (Remote)                         Mar 2022 – Present
One line on what the company does and what you owned, if it is not obvious
• bullet
• bullet
• bullet
Stack: Python, PyTorch, Airflow, GCP (BigQuery, Vertex), dbt
```

- Title first, company second, unless the company is the famous part.
- Add a one-line context line when the company is unknown. "Series B logistics startup, 80 people, freight matching for European hauliers."
- Multiple roles at one company: company once, then each title with its own dates underneath. It shows promotion.
- Dates: "Jan 2023 – Present". En dash with spaces. Month and year only. "Present", never "current", "now" or "today". No seasons.
- Older than ten years: one or two lines or fold into an "Earlier experience" line.

## Skills section

Group by category. Order categories by what the posting wants first.

```
Languages:      Python, SQL, Go, Bash
ML:             PyTorch, scikit-learn, Hugging Face, XGBoost, MLflow
Data:           Spark, Airflow, dbt, PostgreSQL, BigQuery
Infra:          Docker, Kubernetes, Terraform, GitHub Actions, GCP, AWS
Languages:      English (C1), German (B2), Tamil (native)
```

List only what the person could be interviewed on. No ratings, no percentages, no "beginner/expert" labels. Spoken languages get CEFR levels. Certifications go in Education or their own short section.

## Education

```
M.Sc. Artificial Intelligence, Technical University of X, City            2023
Thesis: title (grade 1.3)  ·  Relevant: NLP, Reinforcement Learning, Optimisation
```

Graduation year only, not a date range. Grade only if it helps (top third). Thesis title if relevant to the target. No high school once there is a degree, except in DACH where Abitur or equivalent is often listed in one line.

## Projects

Only projects that prove something the posting asks for. Each one: name, one line of what it does and for whom, one line of your part and result, stack, link if public. Two to four projects at most.

## Publications, talks, patents

Standard citation format, most recent first, own name in bold. On a normal resume keep to the three or four most relevant; the full list goes on an academic CV or a linked page.

## Delivering the file

- Build the .docx clean and single-column. If the docx skill is available, use it.
- Convert to PDF (LibreOffice headless). Send PDF unless the posting asks for Word.
- Check the PDF: text extracts, page count matches, name and email appear in extracted text, file under 1 MB. `scripts/check_pdf.py` does this.
- File name `Firstname_Lastname_Resume.pdf`. Never `resume_final_v3.pdf`.
- Keep the .docx for the next tailoring pass.
