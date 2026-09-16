# ATS, keywords and tailoring

## What an ATS actually does

Greenhouse, Lever, Workday, SmartRecruiters, Personio, SAP SuccessFactors, iCIMS, Taleo. All of them are databases with a workflow on top. They store the application, parse the resume into fields, let recruiters search and filter, and move candidates through stages. Some rank by keyword overlap or ask knockout questions.

What they mostly do not do: auto-reject a resume because of a score. The "75 percent of resumes are rejected by robots" line comes from companies selling resume services. Rejection happens when a recruiter scans a list of two hundred candidates and your line does not show the fit.

What can still hurt you in the parser:
- Multi-column layout read out of order
- Contact details in a header the parser skipped
- Skills in an image or a text box
- A scanned PDF with no text layer
- Creative section names the parser cannot map to Experience or Education
- Dates in odd formats

What can hurt you in the workflow:
- Knockout questions answered wrong (work authorisation, minimum years, willingness to relocate, language level)
- Applying to five roles at the same company at once
- Missing a required attachment (Germany: Zeugnisse)

## The two readers

Write for both:

1. The parser. Standard headings, single column, plain text, real words for skills.
2. The human at 5 to 10 seconds. Title, company, dates, skills line, first bullet of each role. Those elements must show the fit alone.

Recruiters use the search box. If the posting says "Kubernetes" and the resume says "container orchestration", the search misses. Use their word when it is true.

## Keyword strategy that is not stuffing

1. Pull every hard skill, tool, method, certification and domain term from the posting. `scripts/keyword_audit.py` does a first pass.
2. Sort into four buckets:
   - Matched: already on the resume in the same words
   - Rephrase: on the resume in different words (fix the wording)
   - Missing but true: the person has it, the resume forgot it (add it, in a bullet with context)
   - Missing and unsupported: the person does not have it (leave it out, mention in the letter if it is a planned gap)
3. Place the must-have terms where the eye and the parser both land: skills section, the summary if there is one, and the first bullets of the most recent role.
4. Each important term appears once or twice with context. Not five times. A skills line with "Python, Python development, Python programming, Python engineer" is a flag.
5. Spell out acronyms once, then use the acronym: "natural language processing (NLP)". Both forms get searched.

Soft skills do not go in a skills list. They get shown in bullets: "coordinated three vendor teams across two time zones" says more than "communication".

## Reading the posting

Most postings have four layers:

- Must-have: usually the first bullet block, phrases like "required", "you have", "minimum", "Sie bringen mit", "Voraussetzung". Missing several of these means a low fit.
- Nice-to-have: "bonus", "ideally", "plus", "wünschenswert", "von Vorteil". Good to match, not fatal to miss.
- Responsibilities: what the day looks like. Mirror these in bullet phrasing. If they say "own the data pipeline end to end", a bullet that says "owned the ingestion pipeline end to end" lands.
- Culture and noise: "fast-paced", "rockstar", "family". Ignore for the resume, use lightly in the letter.

Seniority signals: "mentor", "define architecture", "cross-team", "stakeholder", "own the roadmap" mean they want someone who has done those things. Show one or two if true.

## Fit table

Produce this before tailoring and show it to the user:

```
Requirement                     Evidence                               Status
------------------------------  -------------------------------------  --------
5+ yrs Python                   6 yrs across 3 roles                   strong
LLM / RAG in production         built RAG platform, 2 deployments      strong
Kubernetes                      Docker + Compose only                  adjacent
German C1                       B1, improving                          gap
Team lead experience            led 2 interns, no formal reports           partial
```

Verdict: strong, apply. Or: 60 percent, apply with a letter that addresses k8s and German. Or: under 50 percent of must-haves, better to skip.

Be honest in this table. It is the one place the user should hear "this posting is a stretch" before spending two hours.

## Tailoring in practice

Tailoring is reordering and rewording. It is not rewriting the whole document each time.

1. Keep a master resume with everything. Tailored versions are cut from it.
2. Change the summary line to speak the posting's language.
3. Reorder skill categories so the posting's must-haves lead.
4. Within each role, move the two most relevant bullets to the top.
5. Swap wording to match the posting's terms where it is true.
6. Drop bullets that do not serve this application. Shorter and relevant beats long and complete.
7. If a project proves something the experience section does not, add or promote it.
8. Do not change the title of a past job. If the internal title was odd ("Technology Associate II"), add the plain equivalent in brackets: "Technology Associate II (Software Engineer)".

Ten minutes of tailoring per application is the right amount. If it takes an hour, the master resume is weak.

## Why applications get no reply, in order of frequency

1. Fit is not visible in the top third of page one
2. The person is not a fit and the letter did not address it
3. Wrong location or work authorisation answer in the form
4. Same generic letter as everyone else
5. Applied late (postings fill in the first two weeks; apply early)
6. Company is not really hiring (evergreen posting, hiring freeze, internal candidate)
7. Resume formatting hid the content
8. No referral, in a company where referrals fill most roles

Notice that only number 7 is about the ATS.

## Match score

Do not present a made-up percentage as science. If the user wants a number, count must-haves matched over must-haves total, say how it was counted, and say that it is a rough signal.
