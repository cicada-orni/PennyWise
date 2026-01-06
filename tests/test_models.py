import unittest
from datetime import datetime
from src.models import Transaction,Income, Expense

class TestModels(unittest.TestCase):
    def setUp(self):
        self.trans_1 = Transaction(40, 'Food', 'Dineout')
        self.trans_2 = Transaction(60, 'Football', 'Play in the field')
        self.income_1 = Income(3000, 'Salary', 'Monthly Salary', datetime(2026, 1, 1))
        self.expense_1 = Expense(500, 'Rent', 'Monthly Rent', datetime(2025,12,23))

        

    def test_transaction_ids(self):
        """Testing multiple transaction ids are different"""
        self.assertNotEqual(self.trans_1.id, self.trans_2.id)

    def test_income_year(self):
        """Testing income year is the same"""
        self.assertEqual(self.income_1.date.year, 2026)

    def test_income_negative_amount(self):
        """Testing negative amount raises error"""
        
        with self.assertRaises(ValueError):
            Income(-5000, 'Investment', 'Monthly Investment Coming from stocks')

    def test_expense_date_istance(self):
        """Testing datetime instance"""
        self.assertIsInstance(self.expense_1.date, datetime)

    def test_to_dict(self):
        """Test the objects covert to dictionary correctly"""
        data = self.income_1.to_dict()
        self.assertEqual(data['amount'], 3000)
        self.assertEqual(data['type'], 'income')
        # single transaction dict
        data_raw = self.trans_1.to_dict()
        self.assertEqual(data_raw['type'], 'transaction')

    def test_from_dict(self):
        """Test the object created"""
        income_obj = Income(500, 'Travel', 'Dine out')
        income_id = income_obj.id

        saved_data = income_obj.to_dict()
        loaded_data = Transaction.from_dict(saved_data)

        self.assertIsInstance(loaded_data, Income)
        self.assertEqual(loaded_data.id, income_id)
        self.assertEqual(loaded_data.amount, income_obj.amount)


