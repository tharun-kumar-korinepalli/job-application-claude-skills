#!/usr/bin/env python3
"""Compare a resume against a job posting and list matched and missing terms.

Standard library only. The output is a starting point for a human decision,
not a score to optimise. A term in the "missing" list should only be added to
the resume if the candidate actually has that experience.

Usage:
    python keyword_audit.py --resume resume.md --job posting.txt
    python keyword_audit.py --resume resume.md --job posting.txt --output audit.md
    python keyword_audit.py --resume resume.md --job posting.txt --extra "ros2,gazebo"
"""
from __future__ import annotations

import argparse
import re
from collections import Counter
from pathlib import Path

STOPWORDS = {
    # english
    "a", "an", "and", "are", "as", "at", "be", "by", "for", "from", "has", "have",
    "in", "into", "is", "it", "of", "on", "or", "our", "that", "the", "their",
    "this", "to", "we", "with", "you", "your", "will", "work", "working", "role",
    "team", "teams", "candidate", "candidates", "experience", "skills", "ability",
    "strong", "using", "use", "used", "responsibilities", "requirements",
    "preferred", "must", "nice", "plus", "including", "across", "within", "about",
    "help", "support", "years", "year", "who", "what", "how", "also", "other",
    "such", "like", "new", "well", "good", "great", "join", "looking", "ideally",
    "etc", "all", "any", "can", "more", "than", "not", "but", "they", "them",
    "company", "job", "position", "offer", "benefits", "apply", "application",
    # german
    "und", "oder", "der", "die", "das", "ein", "eine", "einen", "einer", "mit",
    "für", "von", "bei", "im", "in", "zu", "zur", "zum", "auf", "aus", "wir",
    "sie", "ihre", "ihr", "uns", "unser", "unsere", "sowie", "als", "auch",
    "sind", "ist", "haben", "hast", "bringst", "bringen", "bieten", "suchen",
    "aufgaben", "profil", "anforderungen", "wünschenswert", "vorteil",
    "kenntnisse", "erfahrung", "jahre", "gute", "sehr", "idealerweise",
    "sowohl", "über", "nach", "durch", "werden", "wird", "dich", "dein", "deine",
}

# Terms that matter and that plain tokenising would miss or split.
KNOWN_TERMS = {
    # languages
    "python", "java", "c++", "c#", "go", "golang", "rust", "typescript",
    "javascript", "sql", "r", "scala", "kotlin", "swift", "matlab", "bash",
    # ml / ai
    "machine learning", "deep learning", "pytorch", "tensorflow", "keras",
    "scikit-learn", "sklearn", "hugging face", "transformers", "llm", "llms",
    "large language models", "rag", "retrieval-augmented generation", "nlp",
    "natural language processing", "computer vision", "opencv", "yolo",
    "reinforcement learning", "mlops", "mlflow", "langchain", "llamaindex",
    "vector database", "embeddings", "fine-tuning", "lora", "qlora",
    "prompt engineering", "xgboost", "lightgbm", "onnx", "tensorrt", "cuda",
    "diffusion", "gans", "bayesian optimization", "gaussian process",
    # data
    "spark", "pyspark", "airflow", "dbt", "kafka", "hadoop", "snowflake",
    "bigquery", "redshift", "databricks", "pandas", "numpy", "postgresql",
    "postgres", "mysql", "mongodb", "redis", "elasticsearch", "etl", "elt",
    "data pipeline", "data pipelines", "data warehouse", "tableau", "power bi",
    "looker", "excel", "a/b testing", "statistics", "forecasting",
    # infra
    "docker", "kubernetes", "k8s", "terraform", "ansible", "helm", "aws",
    "azure", "gcp", "google cloud", "linux", "ci/cd", "github actions",
    "gitlab", "jenkins", "git", "proxmox", "vmware", "grafana", "prometheus",
    "rest", "rest api", "graphql", "grpc", "fastapi", "flask", "django",
    "spring boot", "react", "node", "node.js", "microservices",
    # robotics / embedded
    "ros", "ros2", "gazebo", "slam", "lidar", "embedded", "plc", "can bus",
    "simulink", "robotics", "autonomous driving", "sensor fusion",
    # methods / roles
    "agile", "scrum", "kanban", "jira", "confluence", "tdd", "code review",
    "system design", "architecture", "stakeholder management",
    "project management", "product management", "leadership", "mentoring",
    "cross-functional", "communication", "presentation", "documentation",
    "publications", "peer-reviewed", "phd", "master", "bachelor",
    # certs
    "pmp", "aws certified", "cka", "ckad", "itil", "six sigma",
    # languages (spoken)
    "german", "english", "deutsch", "englisch", "french", "spanish",
    "b1", "b2", "c1", "c2", "verhandlungssicher", "fließend",
}


def normalize(text: str) -> str:
    text = text.lower().replace("&", " and ")
    text = re.sub(r"[^a-z0-9äöüß+#./\-\s]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def contains_term(text_norm: str, term: str) -> bool:
    term_norm = normalize(term)
    if not term_norm:
        return False
    if any(ch in term_norm for ch in "+#/.-"):
        return term_norm in text_norm
    return re.search(rf"(?<![a-z0-9äöüß]){re.escape(term_norm)}(?![a-z0-9äöüß])", text_norm) is not None


def tokens(text: str) -> list[str]:
    out = []
    for tok in normalize(text).split():
        tok = tok.strip(".,;:()[]{}")
        if len(tok) >= 3 and tok not in STOPWORDS and not tok.isdigit():
            out.append(tok)
    return out


def bigrams(words: list[str]) -> list[str]:
    return [f"{a} {b}" for a, b in zip(words, words[1:])]


def extract_terms(job_text: str, extra: set[str], max_terms: int = 60) -> list[tuple[str, int]]:
    job_norm = normalize(job_text)
    found: Counter[str] = Counter()

    for term in KNOWN_TERMS | extra:
        if contains_term(job_norm, term):
            found[term] += job_norm.count(normalize(term))

    words = tokens(job_text)
    for w, n in Counter(words).most_common():
        if n >= 2 and len(w) > 3 and w not in found:
            found[w] = n
    for bg, n in Counter(bigrams(words)).most_common():
        if n >= 2 and bg not in found:
            found[bg] = n

    return found.most_common(max_terms)


def audit(resume_text: str, job_text: str, extra: set[str]) -> dict[str, list]:
    resume_norm = normalize(resume_text)
    terms = extract_terms(job_text, extra)
    matched, missing = [], []
    for term, n in terms:
        (matched if contains_term(resume_norm, term) else missing).append((term, n))
    return {"matched": matched, "missing": missing}


def render(result: dict[str, list], resume_path: str, job_path: str) -> str:
    matched, missing = result["matched"], result["missing"]
    total = len(matched) + len(missing)
    pct = round(100 * len(matched) / total) if total else 0
    lines = [
        "# Keyword audit",
        "",
        f"Resume: {resume_path}",
        f"Posting: {job_path}",
        f"Terms found in posting: {total}. Present in resume: {len(matched)} ({pct} percent).",
        "",
        "This is a word overlap, not a fit score. Add a missing term only if it is true.",
        "",
        "## Matched",
        "",
    ]
    lines += [f"- {t} (x{n} in posting)" for t, n in matched] or ["- none"]
    lines += ["", "## Missing from resume", ""]
    lines += [f"- {t} (x{n} in posting)" for t, n in missing] or ["- none"]
    lines += [
        "",
        "## Next step",
        "",
        "Sort the missing list into: true but forgotten (add with context), true but",
        "worded differently (reword), not true (leave out, address in the letter if it matters).",
    ]
    return "\n".join(lines) + "\n"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--resume", required=True)
    ap.add_argument("--job", required=True)
    ap.add_argument("--output", help="write Markdown report here instead of stdout")
    ap.add_argument("--extra", default="", help="comma-separated extra terms to look for")
    args = ap.parse_args()

    resume_text = Path(args.resume).read_text(encoding="utf-8", errors="ignore")
    job_text = Path(args.job).read_text(encoding="utf-8", errors="ignore")
    extra = {t.strip().lower() for t in args.extra.split(",") if t.strip()}

    report = render(audit(resume_text, job_text, extra), args.resume, args.job)
    if args.output:
        Path(args.output).write_text(report, encoding="utf-8")
        print(f"wrote {args.output}")
    else:
        print(report)


if __name__ == "__main__":
    main()
