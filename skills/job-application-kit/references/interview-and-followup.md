# Interviews, follow-ups, outreach and negotiation

## Recruiter and hiring-manager outreach

Cold messages work when they are short, specific and easy to say yes to. LinkedIn message or email, 60 to 120 words.

```
Subject: [Role] at [Company], quick question

Hi [Name],

I saw the [role] opening on your team. I have spent the last [n] years doing [the closest thing], most recently [one concrete result]. Before I apply through the portal, is this role still open and is [specific question about scope, location, or team]?

Happy to send my CV if useful.

[Name]
[LinkedIn or phone]
```

- One question. Not "can we have a call".
- Name one result. Not a summary of the career.
- If someone referred you, that is the first line.
- Send Tuesday to Thursday, morning in their time zone.
- One follow-up after a week if no reply. Then stop.

## Referral request

To a former colleague or acquaintance at the company:

```
Hi [Name], hope [something specific] is going well. I am applying for the [role] on the [team] team at [Company]. Would you be comfortable referring me? I have attached my CV and the posting so it is easy. No problem at all if not.
```

Make it a two-minute task for them. Attach everything.

## Interview prep pack

When the user has an interview, produce this in Markdown:

1. Role summary: three lines on what the job is and what they are worried about (read the posting for the pain).
2. Positioning statement, 30 to 45 seconds, for "tell me about yourself":
   "I am a [role] with [n] years in [domain]. Most recently at [company] I [result]. I am talking to you because [specific reason tied to the role]."
3. The fit table from the application, with an honest line for each gap and how to bridge it.
4. Six to eight STAR stories drawn from the resume, each mapped to a likely competency (leadership, conflict, failure, ambiguity, technical depth, delivery under pressure, learning fast, cross-team work).
5. Likely technical questions for the role and the stack, with the two or three the person should rehearse.
6. Questions to ask them: five, specific to the posting. "What does success look like in the first six months", "what happened to the last person in this role", "how does the team decide what to build", "what is the review and deployment process", "what is the biggest risk for this team this year".
7. Logistics: format, who is interviewing (look them up), duration, what to bring (Germany: originals of Zeugnisse to a final round is still common in some firms).

STAR format for each story:
- Situation: one sentence
- Task: one sentence
- Action: three or four sentences, first person, what the person did, not the team
- Result: one sentence, with a number if true
- What changed afterwards or what was learned: one sentence

Weak-spot bridging line, when a requirement is missing:
"I have not run [tool] in production. I have done [adjacent thing] and my plan would be [concrete ramp]. The rest of the role is close to what I did at [company]."

Never coach the person to claim experience they do not have.

## German interview notes

- Formal "Sie" until offered "Du".
- Expect questions about salary expectations (gross annual, say a number), notice period, and why Germany or why this city for foreign applicants.
- "Warum wollen Sie zu uns" is asked in almost every interview and needs a company-specific answer.
- Bring the originals or clean copies of Zeugnisse if asked.
- Probezeit, Urlaubstage, Homeoffice, Gleitzeit and Weiterbildung are normal things to ask about.
- Silence after an interview for two to three weeks is common. A follow-up after two weeks is fine.

## Follow-up emails

Thank-you after an interview, sent the same day or next morning, 80 to 120 words:

```
Subject: Thank you, [Role] interview

Hi [Name],

Thank you for the conversation today. The part about [specific topic] stayed with me, and it made the role more interesting because [one sentence linking it to your experience].

If it helps, [offer one concrete thing: a code sample, a paper, a reference contact].

Looking forward to hearing about next steps.

[Name]
```

Status check when nothing has come back, two to three weeks after the last contact:

```
Subject: [Role], checking in

Hi [Name],

I wanted to check in on the [role] process. I am still very interested and my availability from [date] has not changed. Is there anything else you need from me?

Thanks,
[Name]
```

- One specific reference to the conversation.
- No pressure, no "I know you are busy".
- Do not send more than one status check. After that, move on and let them come back.

## Declining an offer or withdrawing

Short, warm, gives a reason if it is a normal one, keeps the door open.

```
Hi [Name],

Thank you for the offer and for the time your team spent with me. I have decided to accept another role that is closer to [reason]. I enjoyed the conversations with [names] and would be glad to stay in touch.

Best regards,
[Name]
```

## Salary negotiation

- Research the range first: Glassdoor, levels.fyi, Kununu (DACH), Stepstone Gehaltsreport, Gehalt.de, union or collective-agreement tables (TV-L, TVöD, IG Metall) where they apply. Say which source.
- State a number, not a range, when asked for expectations; a range gets anchored at the bottom.
- Germany: gross annual, 12 or 13 payments; ask which. Public sector and Hochschulen pay by tariff (for example TV-L E13) and the negotiation is about the Stufe (step), not the number.
- Negotiate after the offer, once, in writing or in one call, with one or two asks: base, then start date, remote days, training budget, extra leave, relocation help, title.
- Justify with market data and the fit, not with personal costs.
- Get the final offer in writing before resigning anywhere.

## Application tracker

`scripts/job_tracker.py` keeps a CSV with company, role, date applied, source, contact, status, next action, next action date, notes. Update it after every event. A person applying to more than ten roles will otherwise lose track of who they told what.
