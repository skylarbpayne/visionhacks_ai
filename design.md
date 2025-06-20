Perfect — thanks for the correction. Let's update everything accordingly with proper `mirascope` usage and a `uv`-first workflow. Here's the revised coding workshop plan:

---

## 🧠 Workshop: **"Build an AI Article Summarizer with Python, Gemini, and Mirascope"**

### 🔧 What You'll Build

A real, working CLI tool that takes a `.txt` article and outputs a clear, bullet-point summary using Gemini and Python — all in under 60 minutes.

---

## 🛠 Tools You’ll Use

* `uv` – fast Python package & venv manager
* `mirascope` – for defining LLM-backed functions
* `google.generativeai` – to access Gemini

---

## 🕒 Agenda (60 Minutes)

| Time  | Activity                              |
| ----- | ------------------------------------- |
| 0–10  | Setup + Intro to LLM functions        |
| 10–20 | Live coding walkthrough               |
| 20–40 | Students implement & test             |
| 40–50 | Customize: tone, TLDR, Q\&A, CLI args |
| 50–60 | Share + Wrap-up                       |

---

## 🧰 Part 1: Setup Instructions (copy-paste for students)

```bash
uv venv
uv pip install mirascope google-generativeai
```

Create a file named `.env` and add:

```
GOOGLE_API_KEY=your-api-key-here
```

---

## 🧩 Part 2: Base Code – `summarize.py`

```python
from mirascope import llm
import os
from dotenv import load_dotenv

load_dotenv()

@llm.call(provider="gemini", model="models/gemini-pro", api_key=os.getenv("GOOGLE_API_KEY"))
def summarize_article(article: str) -> str:
    return f"""
    Summarize the following article in 5 bullet points using plain language.

    Article:
    {article}
    """

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python summarize.py <path-to-article.txt>")
        exit(1)

    with open(sys.argv[1], "r") as file:
        text = file.read()

    response = summarize_article(text)
    print(response.content)
```

---

## 🎯 Extension Challenges (Pick 1–2 per student)

Let students pick one:

* Add `argparse` for CLI options like `--format plain|tldr|qa`
* Change the prompt to include:

  * A TL;DR line
  * 3 discussion questions
  * A summary for a younger audience
* Add input sanitization or handle large files

---

## 📘 What They’ll Learn

* How to call an LLM from Python
* How to structure a prompt
* How to build real tools with AI
* How to safely manage secrets (API keys)

---

Would you like:

1. A GitHub starter repo or ZIP for this?
2. A printable handout?
3. A slide deck to intro LLMs + guide the coding?

Happy to prep any of those next.
