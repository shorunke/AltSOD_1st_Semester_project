import uuid
from datetime import datetime, timezone


class Expenses:
    def __init__(self, id, title, amount, created_at, update_at):
        self.id = uuid.UUID(id)
        self.title = title
        self.amount = amount
        self.created_at = created_at
        self.update_at = update_at

    def update(self, title=None, amount=None):
        self.title = title
        self.amount = amount
        self.update_at = datetime.utcnow()

    def dict_to(self):
        return {'id': self.id, 'title': self.title, 'amount': self.amount, 'created_at': self.created_at,
                'update_at': self.update_at}


class ExpenseDB:
    def __init__(self):
        self.expense = ['id', 'title', 'amount', 'created_at', 'update_at']

    def add_expense(self, expense):
        assert isinstance(expense, object)
        return self.expense.append(expense)

    def remove_expense(self, expense):
        return self.expense.remove(expense)

    def get_expense_by_id(self, expense):
        return self.expense['id']

    def get_expense_by_title(self, expense):
        return self.expense['title']

    @property
    def to_dict(self):
        return self.expense.__dict__
