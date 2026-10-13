from io import StringIO
import sys

import loopy as lp


class TestFunctions:
    def capture_output(self, function, *args):
        original_stdout = sys.stdout
        captured = StringIO()
        try:
            sys.stdout = captured
            function(*args)
        finally:
            sys.stdout = original_stdout
        return captured.getvalue()

    def test_total_hours(self):
        cases = [
            ([], 0),
            ([6], 6),
            ([2, 4, 3, 5], 14),
            ([0, 8, 0, 2], 10),
            ([1, 2, 3, 4, 5, 6], 21),
        ]
        for values, expected in cases:
            assert lp.total_hours(values) == expected

    def test_discount_receipts(self):
        cases = [
            ([], []),
            ([100], ["R 75"]),
            ([100, 200, 40], ["R 75", "R 150", "R 30"]),
            ([99, 10, 1], ["R 75", "R 8", "R 1"]),
            ([0, 400, 12], ["R 0", "R 300", "R 9"]),
        ]
        for prices, expected in cases:
            assert lp.discount_receipts(prices) == expected

    def test_verify_code_correct_first_try(self, monkeypatch):
        monkeypatch.setattr("sys.stdin", StringIO("2468\n"))
        output = self.capture_output(lp.verify_code, "2468")
        assert output.count("Enter access code:") == 1
        assert "Access granted!" in output

    def test_verify_code_incorrect_then_correct(self, monkeypatch):
        monkeypatch.setattr("sys.stdin", StringIO("0000\n1234\n2468\n"))
        output = self.capture_output(lp.verify_code, "2468")
        assert output.count("Enter access code:") == 3
        assert output.count("Incorrect code. Try again.") == 2
        assert "Access granted!" in output

    def test_longest_break(self):
        cases = [
            ([], 0),
            (["B", "B"], 0),
            (["S", "S", "S"], 3),
            (["S", "B", "S", "S", "S", "B"], 3),
            (["B", "S", "S", "B", "S", "S", "S", "S"], 4),
            (["S", "B", "S", "B", "S"], 1),
        ]
        for days, expected in cases:
            assert lp.longest_break(days) == expected

    def test_local_minima(self):
        cases = [
            ([], []),
            ([1], []),
            ([8, 3, 7, 2, 6, 4, 9], [3, 2, 4]),
            ([1, 2, 3, 4], []),
            ([5, 1, 5, 1, 5], [1, 1]),
            ([1, 3, 3, 1], []),
            ([9, 7, 5, 3, 1], []),
        ]
        for values, expected in cases:
            assert lp.local_minima(values) == expected

    def test_email_validator(self):
        cases = [
            ([], {"valid_emails": [], "invalid_emails": []}),
            (["ana@example.com"], {"valid_emails": ["ana@example.com"], "invalid_emails": []}),
            (["ana@example.com", "not-an-email", "b c@example.org"],
             {"valid_emails": ["ana@example.com"], "invalid_emails": ["not-an-email", "b c@example.org"]}),
            (["@example.com", "ana@", "a@@b.com", "a@b", "a b@c.com"],
             {"valid_emails": [], "invalid_emails": ["@example.com", "ana@", "a@@b.com", "a@b", "a b@c.com"]}),
            (["first@site.co.za", "second.name@sub.example.org"],
             {"valid_emails": ["first@site.co.za", "second.name@sub.example.org"], "invalid_emails": []}),
        ]
        for emails, expected in cases:
            assert lp.email_validator(emails) == expected

    def test_budget_tracker(self):
        cases = [
            (0, [], "Budget depleted."),
            (100, [], "Budget remaining after the period: 100"),
            (100, [10, 20, 5], "Budget remaining after the period: 65"),
            (40, [10, 10, 25], "Budget exceeded on day 3."),
            (10, [15, 2], "Budget exceeded on day 1."),
            (30, [5, 10, 15], "Budget remaining after the period: 0"),
            (25, [0, 0, 0], "Budget remaining after the period: 25"),
        ]
        for budget, expenses, expected in cases:
            assert lp.budget_tracker(budget, expenses) == expected
