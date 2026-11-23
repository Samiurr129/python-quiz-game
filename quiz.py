"""Random quiz game: asks random multiple-choice questions and reports score and time.

Run:  python quiz.py
Questions live in questions.json next to this file.
"""
import json
import random
import time
from pathlib import Path

QUESTIONS_FILE = Path(__file__).with_name("questions.json")


def load_questions(path=QUESTIONS_FILE):
    with open(path, encoding="utf-8") as f:
        questions = json.load(f)["questions"]
    for q in questions:
        if q["answer"] not in q["options"]:
            raise ValueError(f"Answer not in options for question: {q['question']}")
    return questions


def ask_int(prompt, low, high):
    """Keep asking until the user enters a whole number between low and high."""
    while True:
        raw = input(prompt).strip()
        if raw.isdigit() and low <= int(raw) <= high:
            return int(raw)
        print(f"Please enter a number from {low} to {high}.")


def ask_question(question):
    print(question["question"])
    for i, option in enumerate(question["options"], start=1):
        print(f"{i}. {option}")
    choice = ask_int("Select the correct number: ", 1, len(question["options"]))
    correct = question["options"][choice - 1] == question["answer"]
    print("Correct!" if correct else f"Wrong. The answer is: {question['answer']}")
    return correct


def main():
    questions = load_questions()
    total = ask_int(f"How many questions? (1 to {len(questions)}): ", 1, len(questions))
    chosen = random.sample(questions, total)
    correct = 0
    start = time.time()
    for question in chosen:
        if ask_question(question):
            correct += 1
        print("-----------------")
    elapsed = time.time() - start
    print("Summary")
    print("Total questions:", total)
    print("Correct answers:", correct)
    print(f"Score: {correct / total * 100:.2f}%")
    print(f"Time: {elapsed:.2f} seconds")


if __name__ == "__main__":
    main()
