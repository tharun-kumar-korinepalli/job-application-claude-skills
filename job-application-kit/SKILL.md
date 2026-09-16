---
name: job-application-kit
description: "Build, tailor, review and package job applications: resumes, CVs, Lebensläufe, cover letters, Anschreiben, motivation letters, ATS keyword audits, job description fit checks, interview prep, follow-up emails and an application tracker. Use this skill whenever the user mentions a resume, CV, cover letter, job posting, job description, applying for a job, ATS, 'not getting interviews', 'help me get hired', LinkedIn-to-resume, or wants documents tailored to one role. Also use it for German-speaking markets (Germany, Austria, Switzerland): Bewerbung, Lebenslauf, Anschreiben, Motivationsschreiben, Arbeitszeugnis, Bewerbungsmappe. Use it even when the user only pastes a job ad and their background with no explicit request. Do not use for LinkedIn profile copy, portfolio websites or general document formatting unrelated to job hunting."
---

# Job application kit

One skill for the whole application. It turns a job posting plus a person's real background into documents a recruiter reads in the first ten seconds and keeps reading.

The skill is built around three ideas that every serious source agrees on (Harvard Career Services, r/EngineeringResumes, The Tech Resume Inside Out, ex-FAANG recruiters, German HR practice):

1. Humans reject resumes, not robots. The ATS is a database. A resume gets skipped because a tired recruiter could not see the fit in five seconds. Write for that recruiter.
2. Tailored beats polished. A document that could be sent to fifty companies gets treated like it was.
3. Never invent anything. Every claim will be tested in an interview. Truth is the whole strategy.

## What to read, and when

Read `SKILL.md` fully. Then load only the references the task needs:

| Task | Read |
|---|---|
| Any resume or CV work | `references/resume-format.md`, `references/writing-bullets.md` |
| Tailoring to a posting, keyword audit, "why no replies" | `references/ats-and-tailoring.md` |
| Cover letter, motivation letter, application email | `references/cover-letter.md` |
| Germany, Austria, Switzerland, any German-language application | `references/germany-dach.md` |
| US, UK, Ireland, Australia, NZ, India, EU outside DACH | `references/regions.md` |
| Academic, research, PhD, postdoc, professor track | `references/academic-cv.md` |
| Career change, gaps, visa, over/under qualified, layoffs, returning parents | `references/special-cases.md` |
| Any prose the user will send (letter, email, summary) | `references/human-voice.md` |
| Interview prep, follow-ups, recruiter messages, negotiation | `references/interview-and-followup.md` |
| Final check before delivery | `references/checklists.md` |

Templates live in `assets/`. Scripts live in `scripts/` and need only the Python standard library.

## Step 0: Find out what you are working with

Before writing anything, establish these. Ask only for what is missing; do not run a questionnaire if the answers are already in the chat or in uploaded files.

- Target: job title, company, and the full posting text (or URL). Without a posting, work generically and say so.
- Market and language: which country, and does the posting want English or German (or both)?
- What exists already: current resume, LinkedIn export, old cover letters, references, Zeugnisse.
- Background: every role with dates, what the company does, what the person actually built or did, numbers where they exist.
- Constraints: page limit, deadline, salary expectation or start date if the posting asks, visa or work permit status if it matters for the market.
- Deliverable: chat text, Markdown, .docx, PDF, or a full application folder.

Ask about domain context for every role. "Built web apps" is nothing. "Built the credit-limit engine for a fintech lending app used by 40k SMEs" is a candidate. The single biggest upgrade to any resume is domain context, so dig for it: what industry, what data, who were the users, what changed because of the work.

If the person cannot give numbers, ask for estimates and label them `[confirm]`. If they still cannot, use scale words (thousands of users, daily releases, team of six).

## Step 1: Decode the posting

Do this before touching the resume. Produce a short fit table in chat:

```
Requirement (from posting)      | Evidence (from candidate)          | Status
Python, production ML           | 3 yrs at X, shipped Y              | strong
Kubernetes                      | used Docker, no k8s                | adjacent
German C1                       | B1                                 | gap
```

Rules for the table:
- Split must-have from nice-to-have. Postings put must-haves in the first block and in phrases like "required", "you have", "Sie bringen mit".
- Note the exact vocabulary the posting uses. Mirror it where it is true.
- Mark red flags plainly (unpaid trial work, ten roles in one, salary far below market). The user decides.
- Give a rough fit: apply now, apply with a strong letter that addresses the gap, or skip. Below about 60 percent of must-haves the time is usually better spent elsewhere.

`scripts/keyword_audit.py --resume r.md --job jd.md` gives a deterministic keyword diff to start from. It is a helper, not a verdict.

## Step 2: Write or rewrite the resume

Full detail in `references/resume-format.md` and `references/writing-bullets.md`. The rules that matter most:

Layout
- Single column, no tables for layout, no text boxes, no icons, no photo (except DACH, see the Germany reference), nothing in headers or footers.
- Calibri or Arial, 10.5 to 11 pt body, name 16 pt, margins about 2 cm. Black text, one accent colour at most.
- Standard headings only: Experience, Education, Skills, Projects, Publications. Nothing creative.
- Reverse chronological. Dates right-aligned, "Mar 2022 – Present", never "current".
- Length: one page under about five years of experience, two pages otherwise. Never three, except academic CVs.

Content
- No summary for juniors. A three-line positioning statement for mid and senior people, and for career changers.
- Skills section near the top for technical roles, grouped by category, only things the person can talk about for ten minutes.
- Every bullet: strong verb, what was done, in what context, with what result. "Cut checkout latency 38 percent by moving image processing to a background queue (Python, Redis)". Aim for measurable results in more than half the bullets.
- 4 to 6 bullets for the current role, 2 to 3 for roles older than five years. Old or irrelevant jobs get one line.
- Cut: objectives, "references on request", hobbies (unless they are relevant), Microsoft Office, high school once there is a degree, pronouns, "responsible for", "helped", adjectives about oneself.

Tailoring
- Move the most relevant bullets to the top of each role.
- Reorder skill categories so the posting's must-haves are first.
- Use the posting's own terms where they are true. "CI/CD" if they say CI/CD.
- Never add a tool, title, date, metric or degree the person does not have. If a keyword is missing and unsupported, it stays missing. Say so in the fit table.

## Step 3: Write the cover letter

Full detail in `references/cover-letter.md`. Short version:

- Under one page, 200 to 350 words, three or four paragraphs, same header font as the resume.
- Address a named person if it can be found. Otherwise "Dear Hiring Team" (or "Sehr geehrte Damen und Herren" only as a last resort).
- Paragraph 1: a specific hook tied to this company or this role. Never "I am writing to express my interest".
- Paragraph 2: the two or three strongest proofs, with results, mapped to what the posting asks for. Not a rerun of the resume.
- Paragraph 3: why this company. Something concrete: their product, a recent launch, a team, a paper, a problem they publicly have.
- Paragraph 4: a plain close. Availability, start date and salary expectation if the posting asked. No begging, no "perfect candidate".
- Address the obvious question head-on if there is one (gap, relocation, career switch, overqualified). One or two sentences, no apology.
- Read it aloud. Every sentence that would fit any other company gets cut.

Then run the letter against `references/human-voice.md`. Recruiters in 2026 read hundreds of AI-written letters a week. The ones that get replies sound like a specific person.

## Step 4: Region and language

Germany, Austria and Switzerland have their own conventions and they are where most foreign applicants get filtered out. Read `references/germany-dach.md` for anything DACH: tabular Lebenslauf, whether to include a photo, personal data lines, Zeugnisse, Bewerbungsmappe as one PDF, Anschreiben letter layout, Gehaltsvorstellung, Eintrittstermin, language levels, and how to present a foreign degree.

For everywhere else read `references/regions.md`.

## Step 5: Build the file, check it, deliver it

- Deliver text in chat first so the user can react. Only then build files.
- For .docx use the docx skill if available. Build from a clean single-column structure. Convert to PDF and check the PDF with `scripts/check_pdf.py`: text must extract, page count must match, name and email must be present, no layout tables.
- File name: `Firstname_Lastname_Resume.pdf`, `Firstname_Lastname_Cover_Letter.pdf`. German: `Lebenslauf_Vorname_Nachname.pdf`, `Anschreiben_Vorname_Nachname.pdf`, `Bewerbung_Vorname_Nachname_Firma.pdf` for a merged Mappe.
- Run `references/checklists.md` before handing anything over. It is short and it catches the mistakes that get applications binned.
- End with a short list of things the user must verify (numbers marked `[confirm]`, dates, spelling of the company and contact name).

## Step 6: Optional extras

Only when asked or clearly useful:
- Interview prep pack and STAR story bank: `references/interview-and-followup.md`
- Follow-up and thank-you emails: same file
- Recruiter or hiring-manager outreach message: same file
- Application tracker: `scripts/job_tracker.py`

## Rules that never bend

- Do not invent employers, titles, dates, degrees, certifications, tools, metrics, publications, awards, citizenship, visa status, language levels or references.
- Do not hide gaps with fake dates. Handle them in the letter or with an honest line on the resume.
- Do not stuff keywords, hide white text, or pad the skills list. It is detectable and recruiters treat it as lying.
- Do not recommend removing or changing information about protected characteristics to game a process. Do help remove personal data that is simply irrelevant for the target market.
- Do not promise outcomes. A better application raises the odds. Nothing removes rejection from a job search, and saying otherwise to the user is a disservice.
- Keep the person's voice. A polished letter that sounds like a chatbot is worse than a slightly plain one that sounds like them.

## Output style

Give the finished draft first, then a few lines on what changed and what needs verifying. Plain English. Short sentences. No bold labels inside the documents, no em dashes, no headings inside a cover letter.
