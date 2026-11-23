# Python quiz game

A command-line quiz that asks random multiple-choice questions, then reports your score and time.

## Run it

```bash
git clone https://github.com/Samiurr129/python-quiz-game.git
cd python-quiz-game
python quiz.py
```

No packages to install. Python 3.8 or later.

## How it works

- Questions are stored in `questions.json`. Add your own in the same format:
  `{"question": "...", "options": ["A", "B", "C", "D"], "answer": "B"}`
- The game checks that every answer is one of its options when it loads.
- Invalid input (letters, numbers out of range) is asked again instead of crashing.
- The score is based on the number of questions actually asked.

## Concepts practised

File handling with JSON, functions, input validation, `random.sample` and timing with `time`.

## Author

**Samiur Rahman** · [GitHub](https://github.com/Samiurr129)
