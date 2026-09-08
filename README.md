# 🎯 GoalForge — Intelligent Goal Recommendation System

A career-guidance app that helps students figure out "what next?" after school — not with generic quizzes, but by mapping everyday interests and habits (hobbies, the videos they watch, subjects they enjoy) directly to real career paths.

`Python` `Streamlit` `Career Guidance` `Recommendation System`

**Live Demo →** *(add your Streamlit Cloud link here)*

---

## 📖 The Problem

Most students finishing school face the same question — "what should I do next?" — without a clear way to connect what they *actually enjoy* to what they could *actually become*. Career counseling is often generic, one-size-fits-all, or simply unavailable.

GoalForge solves this by asking students about their everyday interests — hobbies, favorite subjects, the type of YouTube content they watch, how they spend weekends — and mapping those answers to concrete career paths across 40+ interest categories, from Art to Quantum Science.

---

## 🔄 How It Works

20 Interest-Based Questions
(hobbies, subjects, YouTube habits, free time, etc.)
│
▼
Student Selects Closest-Matching
Interest per Question (from 40 categories)
│
▼
Interest → Career Mapping Engine
(each category maps to 2–3 real career paths)
│
▼
Aggregation & Deduplication
(combine careers across all selected interests)
│
▼
Random Sampling
(narrow down to Top 5 if more than 5 match)
│
▼
Personalized Career Suggestions


For example — a student who selects both **Art** and **Technology** across different questions ends up with overlapping suggestions like **UI/UX Designer**, alongside other matches like **Illustrator** or **AI Researcher**.

---

## 🛠️ Tech Stack

| Layer | Tools |
|---|---|
| Frontend / App | Streamlit |
| Logic | Python (dictionary-based interest → career mapping) |
| Recommendation Method | Rule-based aggregation + random sampling |
| Environment | Python 3 |

---

## ❓ The Questionnaire

Students answer **20 questions** designed to surface interests indirectly rather than asking "what career do you want" outright — things like:

- What is your favorite hobby?
- How do you usually spend your weekends?
- What subject do you enjoy the most in school?
- Which activity makes you lose track of time?
- What do your friends usually ask your help for?

Each answer is picked from **40+ interest categories** spanning the arts, sciences, tech, and beyond — Art, Business, Cooking, Design, Engineering, Fashion, Gaming, Healthcare, Law, Psychology, Quantum Science, Technology, UX/UI, Zoology, and more.

---

## 🧠 Recommendation Logic

| Step | Description |
|---|---|
| 1. Interest Extraction | Filters out blank/"None" answers to isolate genuine interests |
| 2. Career Lookup | Each selected interest maps to a predefined list of real-world careers |
| 3. Aggregation | Careers from all 20 answers are pooled together and deduplicated |
| 4. Top-5 Selection | If more than 5 careers match, 5 are randomly sampled for a focused, non-overwhelming result |

---

## 🚀 Getting Started

```bash
git clone https://github.com/Cashlin3/GoalForge-Intelligent-Goal-Recommendation-System.git
cd GoalForge-Intelligent-Goal-Recommendation-System
pip install streamlit
streamlit run app.py
```

---

## 🔮 Future Improvements

- Replace random sampling with **weighted ranking** — careers matched by multiple answers should rank higher than single-match careers
- Add a short description or "day in the life" blurb for each suggested career
- Incorporate a lightweight ML classifier (e.g. clustering or similarity scoring) instead of pure dictionary lookup, for more nuanced multi-interest matching
- Add resource links (courses, roadmaps) for each recommended career
- Save/export results as a PDF summary for students to share with parents or counselors

---

## 👤 Contributors

| Person | Role | Contributions |
|---|---|---|
| **Cashlin** ([@Cashlin3](https://github.com/Cashlin3)) | Developer | Question design, interest-to-career mapping, and full Streamlit app development |

---


Made with 🎯 curiosity + ❤️ by **Cashlin**
