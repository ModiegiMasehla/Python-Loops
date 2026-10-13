Python Repeating Instructions (Loops) — 

## Learning Outcomes assessed

- Conditional statements
- Functions
- Basic loops
- Advanced loops
- Simple algorithms (problem solving)
- Basic command-line commands

---

## Assessment Structure

This assessment has two sections:

- **Form-based assessment:** multiple-choice questions and written responses.
- **Coding assessment:** complete the functions described below and make the supplied unit tests pass.

You can answer the questions in any order.

## Scoring & Weighting

| Component | Weight |
| --- | ---: |
| Coding Section (unit tests) | **60%** |
| Form-Based Section (MCQs + written responses) | **40%** |

### Coding section

Let `T` be the total number of coding tests and `P` be the number you pass.

```text
Coding Score = (P / T) × 60%
```

### Form-based section

Let `Q` be the total number of questions and `C` be the number answered correctly.

```text
Form Score = (C / Q) × 40%
```

### Final Score & Pass Mark

```text
Final Score = Coding Score + Form Score
```

To pass, your final score must be **60% or higher**.

---

## How to run your tests

Run all tests from the project directory:

```bash
python3 -m pytest tests/test_loopy.py -v
```

Run one test:

```bash
python3 -m pytest tests/test_loopy.py::TestFunctions::test_total_hours -v
```

Useful command-line commands include `pwd`, `ls`, `cd`, `mkdir`, and `python3 -m pytest`.

---

## Project Structure

```text
fun-002-loopy-version-2/
├── loopy.py
├── tests/
│   └── test_loopy.py
└── README.md
```

---

# Python Repeating Instructions — Coding Assessment, Version 2

Each function in `loopy.py` is partially implemented. Fix the bugs and complete the missing logic. Do not change the function names or test expectations.

## Question 1 — `total_hours(hours_per_day)`

A community library records how many hours volunteers work each day. Given a list of daily hours, return the total number of hours worked.

- **Input:** A list of numbers, e.g. `[2, 4, 3, 5]`
- **Output:** A number, e.g. `14`
- An empty list should return `0`.

This assesses accumulating values in a loop.

## Question 2 — `discount_receipts(prices_list)`

A local stationery shop gives customers a 25% discount on each item. For every original whole-number price, calculate the discounted price by subtracting 25% and return a list of strings formatted as South African rand.

- **Input:** A list of integers, e.g. `[100, 200, 40]`
- **Output:** `["R 75", "R 150", "R 30"]`
- Use integer floor division for the discount amount, so a price of `99` becomes `"R 75"` (`99 - 99 // 4`).

This assesses loops, arithmetic and list construction.

## Question 3 — `verify_code(correct_code)`

Simulate a kiosk access-code prompt. Keep asking the user to enter the code until the entered value matches `correct_code`.

- Prompt with exactly `Enter access code: `
- For an incorrect entry, print `Incorrect code. Try again.`
- For a correct entry, print `Access granted!` and stop.

This assesses `while` loops, input, conditions and loop termination.

## Question 4 — `longest_break(study_days)`

A student tracks study sessions using `"S"` for a study day and `"B"` for a break day. Return the longest consecutive run of study days.

- **Input:** A list such as `["S", "B", "S", "S", "S", "B"]`
- **Output:** `3`
- An empty list or a list with no `"S"` entries should return `0`.

This assesses counters and tracking a maximum across a sequence.

## Question 5 — `local_minima(numbers)`

Find every local minimum in a list. A local minimum is a value strictly smaller than both its immediate neighbours. Return the values in the order they appear.

- **Input:** `[8, 3, 7, 2, 6, 4, 9]`
- **Output:** `[3, 2, 4]`
- The first and last elements cannot be local minima. Equal neighbouring values do not count.

This assesses index-based loops and neighbour comparisons.

## Question 6 — `email_validator(emails)`

Separate email-like strings into valid and invalid lists. For this exercise, a valid email must:
- contain exactly one `@`;
- have non-empty text before and after the `@`;
- have a dot (`.`) in the domain part;
- have no spaces.

Return a dictionary with keys `valid_emails` and `invalid_emails`, preserving the original order in each list.

- **Input:** `["ana@example.com", "not-an-email", "b c@example.org"]`
- **Output:** `{"valid_emails": ["ana@example.com"], "invalid_emails": ["not-an-email", "b c@example.org"]}`

This assesses string iteration, conditionals and categorising values.

## Question 7 — `budget_tracker(budget, daily_expenses)`

Track spending against a starting budget. Subtract each day's expense in order. If the balance becomes zero or negative on a day, return `"Budget exceeded on day N."`, where `N` is the 1-based day number. If the budget is not exceeded, return `"Budget remaining after the period: X"` with the remaining balance.

- If `daily_expenses` is empty and `budget` is `0`, return `"Budget depleted."`
- If expenses add up to exactly the budget, the budget is considered to last through the whole period, and return remaining `0`.
- If an expense would take the balance below zero before the final day, report that day.
- If the balance reaches exactly zero on the final day, return the remaining-balance message.

This assesses cumulative totals, early termination and boundary conditions.

## Your Goal

Complete each function in `loopy.py` so that the code is valid Python, each function follows its specification, and all unit tests pass.

Good luck!
