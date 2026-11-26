"""Tests for expense_tracker.py.  Run them with:   python -m unittest -v

Don't edit this file (except in the parts of ASSIGNMENT.md that tell you to).
"""

import os
import tempfile
import unittest

from expense_tracker import (
    make_expense,
    total,
    total_by_category,
    most_expensive,
    save_expenses,
    load_expenses,
)

SAMPLE = [
    {"description": "Coffee", "amount": 4.5, "category": "food"},
    {"description": "Bus", "amount": 2.0, "category": "transport"},
    {"description": "Bagel", "amount": 3.0, "category": "food"},
]


class TestMakeExpense(unittest.TestCase):
    def test_basic(self):
        e = make_expense("Coffee", "4.50", "Food")
        self.assertEqual(e, {"description": "Coffee", "amount": 4.5, "category": "food"})

    def test_strips_spaces(self):
        e = make_expense("  Tea  ", 3, "  DRINKS ")
        self.assertEqual(e["description"], "Tea")
        self.assertEqual(e["category"], "drinks")

    def test_empty_category_becomes_other(self):
        self.assertEqual(make_expense("Gum", 1, "   ")["category"], "other")

    def test_bad_amount(self):
        with self.assertRaises(ValueError):
            make_expense("Free stuff", 0, "misc")
        with self.assertRaises(ValueError):
            make_expense("Refund?", -5, "misc")

    def test_blank_description(self):
        with self.assertRaises(ValueError):
            make_expense("   ", 5, "misc")


class TestTotals(unittest.TestCase):
    def test_total(self):
        self.assertEqual(total(SAMPLE), 9.5)

    def test_total_empty(self):
        self.assertEqual(total([]), 0)

    def test_total_rounding(self):
        items = [{"description": "x", "amount": 0.1, "category": "a"}] * 3
        self.assertEqual(total(items), 0.3)

    def test_by_category(self):
        self.assertEqual(total_by_category(SAMPLE), {"food": 7.5, "transport": 2.0})

    def test_by_category_empty(self):
        self.assertEqual(total_by_category([]), {})


class TestMostExpensive(unittest.TestCase):
    def test_finds_biggest(self):
        self.assertEqual(most_expensive(SAMPLE)["description"], "Coffee")

    def test_empty_list_returns_none(self):
        self.assertIsNone(most_expensive([]))


class TestSaveLoad(unittest.TestCase):
    def test_round_trip(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "data.json")
            save_expenses(SAMPLE, path)
            self.assertEqual(load_expenses(path), SAMPLE)

    def test_missing_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(load_expenses(os.path.join(tmp, "nope.json")), [])


if __name__ == "__main__":
    unittest.main()
