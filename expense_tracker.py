"""Expense Tracker - a tiny command-line app for logging what you spend.

Each expense is a dict that looks like this:
    {"description": "Coffee", "amount": 4.5, "category": "food"}

Your job is to fill in every function marked TODO.
Read ASSIGNMENT.md first: it tells you WHEN to work on each function
(and which git branch to be on when you do).
"""

import json
import os

DATA_FILE = "expenses.json"


def make_expense(description, amount, category):
    """Build and return one expense dict.

    Rules:
    - description: strip surrounding spaces. If it's empty after that,
      raise ValueError.
    """
    description = description.strip()
    if description == '':
        raise ValueError("description can't be empty")
    amount = float(amount)
    if amount <= 0:
        raise ValueError
    category = category.strip().lower()
    if not category:
        category = "other"
    """
    - amount: convert to float. If it's <= 0, raise ValueError.
    - category: strip spaces and make it lowercase ("  Food " -> "food").
      If it's empty, use "other".
    """
    # TODO (Part 3)
    return {"description": description, "amount": amount, "category": category}


def total(expenses):
    """Return the sum of all amounts, rounded to 2 decimals. Empty list -> 0."""
    if expenses == []:
        return 0
    total = sum(x['amount'] for x in expenses)
    return round(total, 2)


def total_by_category(expenses):
    """Return a dict mapping category -> total spent in that category.

    Example:
        [{"description": "Coffee", "amount": 4.5, "category": "food"},
         {"description": "Bus", "amount": 2.0, "category": "transport"},
         {"description": "Bagel", "amount": 3.0, "category": "food"}]
        -> {"food": 7.5, "transport": 2.0}

    Round each total to 2 decimals.
    """
    # TODO (Part 3)
    raise NotImplementedError


def most_expensive(expenses):
    """Return the expense dict with the biggest amount.

    NOTE: this one is already written... but it has a bug.
    You'll deal with it in Part 4. Don't fix it early!
    """
    return max(expenses, key=lambda e: e["amount"])


def save_expenses(expenses, path=DATA_FILE):
    """Write the list of expenses to `path` as JSON."""
    # TODO (Part 5)
    raise NotImplementedError


def load_expenses(path=DATA_FILE):
    """Read expenses from `path` and return them as a list.

    If the file doesn't exist yet, return an empty list.
    """
    # TODO (Part 5)
    raise NotImplementedError


def print_expenses(expenses):
    if not expenses:
        print("No expenses yet.")
        return
    for i, e in enumerate(expenses, start=1):
        print(f"{i}. {e['description']:<20} ${e['amount']:>8.2f}  [{e['category']}]")


def main():
    expenses = load_expenses()
    while True:
        print()
        print("=== Expense Tracker ===")
        print("1) Add expense")
        print("2) List expenses")
        print("3) Show totals")
        print("4) Show most expensive")
        print("5) Save and quit")
        choice = input("> ").strip()

        if choice == "1":
            desc = input("Description: ")
            amount = input("Amount: ")
            category = input("Category: ")
            try:
                expenses.append(make_expense(desc, amount, category))
                print("Added!")
            except ValueError as err:
                print(f"Could not add expense: {err}")
        elif choice == "2":
            print_expenses(expenses)
        elif choice == "3":
            print(f"Total: ${total(expenses):.2f}")
            for cat, amt in total_by_category(expenses).items():
                print(f"  {cat}: ${amt:.2f}")
        elif choice == "4":
            top = most_expensive(expenses)
            if top is None:
                print("No expenses yet.")
            else:
                print(f"Biggest: {top['description']} (${top['amount']:.2f})")
        elif choice == "5":
            save_expenses(expenses)
            print("Saved. Bye!")
            break
        else:
            print("Pick 1-5.")


if __name__ == "__main__":
    main()
