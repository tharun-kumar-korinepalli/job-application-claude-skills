# job-application-skills

One Claude skill that handles a job application from posting to send button: fit check, resume or CV, cover letter, ATS keyword audit, German Bewerbung (Lebenslauf, Anschreiben, Zeugnisse), academic CV, interview prep, follow-ups and a tracker.

It was made by merging the useful parts of the resume and job-search skills floating around GitHub, checking them against what recruiters and career services actually say, and adding the German-market rules that none of them covered. Everything is plain Markdown plus three small Python scripts with no dependencies.

## What it will and will not do

It will make an application that is clear, tailored, honest and easy to scan. That raises the odds of a reply. It will not remove rejection from a job search; nothing does, and anyone who promises that is selling something. Most rejections are about fit, timing and competition, not about the document. The skill helps with the part you control.

It will not invent experience, tools, dates, degrees or numbers. If you ask it to, it says no and offers the honest version.

## Install

### Claude.ai (web or desktop)

Download `job-application-kit.skill` from the latest release, or zip the `skills/job-application-kit` folder yourself. Then Settings, Capabilities, Skills, upload. Once added it works in every chat and project.

### Claude Code

```
git clone https://github.com/<you>/job-application-skills
cp -r job-application-skills/skills/job-application-kit ~/.claude/skills/
```

Or per project:

```
mkdir -p .claude/skills && cp -r job-application-skills/skills/job-application-kit .claude/skills/
```

The skill triggers on its own when you mention a resume, CV, cover letter, job posting, Bewerbung, Lebenslauf or Anschreiben. You can also just paste a posting and your background.

## How to use it

Give Claude three things: the posting (text or link), your current CV or a plain description of what you have done, and the country plus language. Say what you want back: text in chat, Markdown, Word, PDF, or a full German Bewerbungsmappe.

Typical prompts:

```
Here is the posting and my CV. Check the fit and tailor the CV. Germany, English posting.
Write the Anschreiben for this Stelle. My German is B2. Gehaltsvorstellung 65k.
I am switching from mechanical engineering to ML. Rewrite my resume for this role in the US.
I have an interview on Thursday for this role. Build me a prep pack.
Turn this into a Lebenslauf with a photo and the Zeugnisse in one PDF.
```

Claude will first show a fit table (what the posting wants, what you have, where the gaps are) and an honest verdict. Then the documents. Then a short list of things you must check yourself before sending.

## What is inside

```
skills/job-application-kit/
  SKILL.md                         the workflow Claude follows
  references/
    resume-format.md               layout, fonts, sections, length, contact line
    writing-bullets.md             how to write experience bullets that show results
    ats-and-tailoring.md           what ATS really does, keyword strategy, fit table, why applications get no reply
    cover-letter.md                structure, openers, tone, handling gaps and switches
    germany-dach.md                Lebenslauf, Anschreiben, Zeugnisse, Bewerbungsmappe, photo, permit line, Austria, Switzerland
    regions.md                     US, UK, AU/NZ, France, NL/Nordics, India, Middle East, Japan
    academic-cv.md                 PhD, postdoc, research lab, Professur
    special-cases.md               career change, gaps, layoffs, visa, over/under qualified, students, returners
    human-voice.md                 the check that stops letters from sounding generated
    interview-and-followup.md      outreach, referral asks, STAR prep, thank-you and status emails, negotiation
    checklists.md                  what to verify before anything goes out
  assets/
    resume-template-en.md
    lebenslauf-template-de.md
    cover-letter-template-en.md
    anschreiben-template-de.md
    fit-table-template.md
  scripts/
    keyword_audit.py               resume vs posting term overlap (EN and DE terms)
    check_pdf.py                   text extracts, page count, size, name/email present, layout traps
    job_tracker.py                 CSV tracker with next actions and a "due" view
```

## Where the content comes from

The skill merges and rewrites material from these repos and sources. Details and licences in [CREDITS.md](CREDITS.md).

- dabydat/resume-builder-skill (Harvard Career Services, r/EngineeringResumes, The Tech Resume Inside Out)
- jezweb/claude-skills, resume-cover-letter (regional formats, CAR bullets, cover letter structure)
- Faizee-Asad/job-seeker-claude-skills (truth rules, keyword audit, tracker, interview and follow-up guides)
- Paramchoudhary/ResumeSkills (job description analysis, ATS checklist, academic CV, career change)
- olegvg/resume-tailor-plugin (master profile idea, ATS rules)
- proficientlyjobs/proficiently-claude-skills (cover letter voice rules, honesty checks)
- usr1243/claude-bewerbung-skill (Swiss CV and Anschreiben templates)
- hgrosche95/job-application-skill (German Anschreiben guidance, Lebenslauf fields)
- Wikipedia, "Signs of AI writing", via the humanizer skill

## Contributing

Corrections to regional rules are the most useful thing. If something in germany-dach.md or regions.md is out of date for your country, open an issue with a source. Keep the writing plain. No new dependencies in the scripts.

## Licence

MIT. See [LICENSE](LICENSE).
