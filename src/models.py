import uuid
from datetime import datetime

# Transaction Class

class Transaction:
    def __init__(self, amount: float, category: str, description: str, date: datetime | None = None) -> None:
        # Validation
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        
        if not description:
            raise ValueError(f"Description cannot be blank.")
        
        if not category:
            raise ValueError(f"Category cannot be empty.")

        self.id = str(uuid.uuid4())
        self.amount = float(amount)
        self.category = category
        self.description = description
        # Date Logic
        if date is None:
            self.date = datetime.now()
        else:
            self.date = date

    def __repr__(self) -> str:
        return f"<Transaction: {self.amount:.2f} | {self.category} | {self.date.date()}>"
    
    # SERIALIZATION
    def to_dict(self) -> dict:
        dict_transaction: dict = {
            'id': self.id,
            'amount': self.amount,
            'category': self.category,
            'description': self.description,
            'date': self.date.isoformat(),
            'type': getattr(self, 'type', 'transaction')
        }
        return dict_transaction

    # DESERIALIZATION
    @classmethod
    def from_dict(cls, data: dict):
        target_class_name = data.get('type', 'transaction').capitalize()
        target_class = globals().get(target_class_name, Transaction)
        obj = target_class(
            amount=float(data['amount']),
            category=data['category'],
            description=data['description'],
            date=datetime.fromisoformat(data['date'])
        )
        obj.id = data['id']
        return obj
# Income Class Inheriting Transaction

class Income(Transaction):
    def __init__(self, amount: float, category: str, description: str, date: datetime | None = None) -> None:
        super().__init__(amount, category, description, date)
        self.type = "income"

# Expense Class Inheriting Transaction

class Expense(Transaction):
    def __init__(self, amount: float, category: str, description: str, date: datetime | None = None):
        super().__init__(amount, category, description, date)
        self.type = "expense"

