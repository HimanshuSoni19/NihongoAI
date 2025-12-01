"""
NihongoAI – JLPT N5 Quiz Backend using Gemini 2.5

This module:

- Generates JLPT N5 style multiple-choice quizzes
- Analyzes user answers and returns a clear score + short feedback
- Generates a project report for your B.Tech submission
"""

import os
import json
import pandas as pd
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()


class NihongoCrew:
    """Gemini 2.5 based helper for NihongoAI."""

    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in .env file!")

        # Configure Gemini (same as your working test script)
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-2.5-flash")

        # Optional vocabulary (you can ignore if file missing)
        try:
            self.vocab_df = pd.read_csv("data/N5_vocabulary.csv")
            print(f"✅ Loaded {len(self.vocab_df)} vocabulary words")
        except Exception as e:
            print(f"⚠️ Could not load vocabulary CSV: {e}")
            self.vocab_df = None

    # ------------------------------------------------------------------ #
    #  QUIZ GENERATION
    # ------------------------------------------------------------------ #
    def generate_quiz(self, topic='general', difficulty='N5', num_questions=5):
        """
        Generate a JLPT-style multiple-choice quiz.

        Returns:
            quiz_text (str) – ONLY the questions + options, no answer key.
        """
        print(
            f"\n🎯 [Gemini] Generating {difficulty} quiz | "
            f"topic='{topic}' | questions={num_questions}"
        )

        topic_hint = self._topic_hint(topic)

        prompt = f"""
You are a professional Japanese teacher creating JLPT {difficulty} practice
questions for an English-speaking learner.

GOAL:
Create EXACTLY {num_questions} multiple-choice questions that look like
official JLPT N5 practice (kanji, grammar, vocabulary, reading).

TOPIC HINT:
{topic_hint}

=== STYLE TARGET (IMPORTANT) ===
The questions should look like these examples:

Example 1 – Kanji reading:
1. 来月
○ らいげつ
○ らいがつ
○ くがつ
○ くげつ

Example 2 – Grammar / particles:
1. まいにちしんぶん ______ 読みます。
○ へ
○ を
○ に
○ が

Example 3 – Vocabulary:
1. わたしはいつも ______ をききながらべんきょうします。
○ ペン
○ ラジオ
○ テーブル
○ ストーブ

If topic is "reading", first give a short passage (3–5 simple sentences),
then questions in the SAME format as above.

=== FORMAT RULES (FOLLOW EXACTLY) ===

1. Number questions like:

1. [question]
○ option1
○ option2
○ option3
○ option4

2. Put each option on its own line starting with:
   "○ " (circle + space). Do NOT put options on the same line.

3. Use ONE completely blank line between questions.

4. Use only plain text. No markdown, no headings, no extra bullets.

5. DO NOT show which option is correct.
   DO NOT write an answer key.
   DO NOT explain anything, greet the user, or add comments.

=== RANDOMIZATION OF CORRECT OPTION (VERY IMPORTANT) ===

- For each question, decide which option is correct.
- RANDOMLY place the correct option as A, B, C, or D.
- Over the whole quiz, the correct answers MUST be spread across
  A/B/C/D, not always the first option.
- It is OK if sometimes A is correct, sometimes B, sometimes C, sometimes D,
  but never always the same letter.

Now output ONLY the quiz in the exact format described.
Start directly with "1." – no title, no intro sentence.
        """

        response = self.model.generate_content(prompt)
        quiz_text = response.text.strip()
        print("✅ [Gemini] Quiz generated (questions only).")
        return quiz_text

    # ------------------------------------------------------------------ #
    #  ANSWER ANALYSIS
    # ------------------------------------------------------------------ #
    def analyze_answers(self, quiz_content: str, user_answers: dict) -> str:
        """
        Analyze user's quiz answers and provide structured feedback.

        quiz_content: text returned from generate_quiz()
        user_answers: dict like {"1": "A", "2": "C", ...}

        Returns:
            Markdown-style text like:

            Score: 3 / 5 (60%)

            Q1: Correct
            - Your answer: B
            - Correct answer (model): B
            - Reason: ...

            Q2: Incorrect
            - Your answer: A
            - Correct answer (model): C
            - Reason: ...
        """

        print(f"\n📊 [Gemini] Analyzing {len(user_answers)} answers...")

        answers_json = json.dumps(user_answers, ensure_ascii=False, indent=2)

        prompt = f"""
You are a JLPT N5 teacher checking a multiple-choice quiz.

QUIZ (questions only, no answer key):

---
{quiz_content}
---

The student's answers are given as JSON where
the key is the question number (string) and the value is a letter:

{answers_json}

YOUR TASK:

1. For EACH question:
   - Decide which option (A/B/C/D) is correct based on the quiz text.
   - Compare the student's answer to your correct answer.

2. Compute the total score X / N and percentage.

3. OUTPUT FORMAT (FOLLOW EXACTLY):

Score: X / N (Y%)

Q1: Correct/Incorrect
- Your answer: [student_letter or "—" if blank]
- Correct answer (model): [letter]
- Reason: [1–2 short lines only]

Q2: Correct/Incorrect
- Your answer: ...
- Correct answer (model): ...
- Reason: ...

[continue like this until the last question]

IMPORTANT RULES:
- Keep each Reason VERY SHORT (max 2 lines).
- Do NOT repeat the full question text.
- Do NOT add any extra sections before or after this pattern.
- If an answer is missing in the JSON, treat it as blank ("—") and mark
  it incorrect.
        """

        response = self.model.generate_content(prompt)
        result_text = response.text.strip()
        print("✅ [Gemini] Analysis generated.")
        return result_text

    # ------------------------------------------------------------------ #
    #  PROJECT REPORT
    # ------------------------------------------------------------------ #
    def generate_project_report(self, quiz_history, user_stats):
        """
        Generate a technical project report for NihongoAI.

        quiz_history: list of quiz data (can be [])
        user_stats: dict, e.g.:
            {
                "total_quizzes": 12,
                "ai_quizzes": 10,
                "classic_quizzes": 2
            }

        Returns:
            Markdown text suitable for exporting to Word/PDF.
        """

        print("\n📄 [Gemini] Generating project report...")

        stats_json = json.dumps(user_stats or {}, ensure_ascii=False, indent=2)
        num_history = len(quiz_history) if quiz_history else 0

        prompt = f"""
You are writing a professional B.Tech project report for:

"NihongoAI: Japanese Language Learning Assistant using Gemini 2.5"

The app:
- generates JLPT N5-style quizzes (kanji, grammar, vocabulary, reading),
- analyzes answers,
- gives feedback and study recommendations.

PROJECT STATISTICS (JSON):
{stats_json}

Quiz history entries available: {num_history}.

Write a well-structured report in MARKDOWN with these sections:

1. Executive Summary
   - Brief overview of the project
   - Main objectives and features
   - Technologies used (Python, Streamlit, Gemini 2.5, etc.)

2. System Architecture
   - Overall workflow of the app
   - How quizzes are generated (prompting Gemini, no answer key)
   - How answers are analyzed and scores are computed
   - How the NihongoCrew class is used by the Streamlit frontend

3. Technical Implementation
   - Important Python modules and structure
   - Prompt design for quiz generation and analysis
   - Optional use of an N5 vocabulary CSV if available
   - Any key design decisions (e.g. not using CrewAI / LiteLLM anymore)

4. Performance & Evaluation
   - Response quality and speed (qualitative, not exact benchmarks)
   - Typical quiz examples and how well they resemble JLPT style
   - Limitations of the current approach

5. Educational Impact
   - How the tool helps JLPT N5 learners (kanji, vocab, grammar, reading)
   - Advantages over static worksheets or textbooks
   - Potential use in a classroom or self-study environment

6. Future Work
   - 5–7 bullet points, e.g.:
     * support for N4–N2 levels
     * spaced repetition scheduling
     * user accounts and progress tracking
     * audio questions using TTS/STT
     * integration with mobile apps
     * better analytics dashboards

STYLE:
- Formal academic tone, but clear and readable.
- Use headings, subheadings, and bullet points where helpful.
- Do NOT invent fake numeric performance metrics; keep them qualitative.
        """

        response = self.model.generate_content(prompt)
        report_text = response.text.strip()
        print("✅ [Gemini] Project report generated.")
        return report_text


# ---------------------------------------------------------------------- #
# Simple manual test (run this file directly)
# ---------------------------------------------------------------------- #
def test_agents():
    print("🧪 Testing NihongoAI backend with Gemini 2.5...")
    try:
        crew = NihongoCrew()
        quiz = crew.generate_quiz(topic="grammar", difficulty="N5", num_questions=4)
        print("\n--- SAMPLE QUIZ ---\n")
        print(quiz)
        print("\n✅ Backend initialized and quiz generated successfully.")
        return True
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\n💡 Check:")
        print("   1. GEMINI_API_KEY in .env")
        print("   2. Packages installed: google-generativeai, python-dotenv, pandas")
        print("   3. Internet connection")
        return False


if __name__ == "__main__":
    test_agents()
