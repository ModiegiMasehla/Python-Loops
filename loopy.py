"""Python Repeating Instructions assessment — Version 2.
Fix the bugs and complete each function.
"""


def total_hours(hours_per_day):
    total = 0
    for hours in hours_per_day:
        total = hours
    return total


def discount_receipts(prices_list):
    receipts = []
    for price in prices_list:
        discount = price // 4
        receipts.append(f"R {discount}")
    return receipts


def verify_code(correct_code):
    while True:
        entered = input("Enter access code: ")
        if entered == correct_code:
            print("Access granted!")
            break
        # TODO: print the incorrect-code message


def longest_break(study_days):
    current = 0
    longest = 0
    for day in study_days:
        if day == "B":
            current += 1
            longest = max(longest, current)
        else:
            current = 0
    return longest


def local_minima(numbers):
    minima = []
    for index in range(1, len(numbers) - 1):
        if numbers[index] < numbers[index - 1] and numbers[index] < numbers[index + 1]:
            minima.append(index)
    return minima


def email_validator(emails):
    valid_emails = []
    invalid_emails = []
    for email in emails:
        if "@" in email and "." in email:
            valid_emails.append(email)
        else:
            invalid_emails.append(email)
    return {"valid_emails": valid_emails, "invalid_emails": invalid_emails}


def budget_tracker(budget, daily_expenses):
    balance = budget
    for day, expense in enumerate(daily_expenses):
        balance -= expense
        if balance < 0:
            return f"Budget exceeded on day {day}."
    if balance == 0 and not daily_expenses:
        return "Budget depleted."
    return f"Budget remaining after the period: {balance}"
