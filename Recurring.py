import GeneralExpense

#module adds frequency attribute to a GeneralExpense
class RecurringExpense(GeneralExpense.Expense):
    def __init__(self, expense_title, expense_amount, expense_date, expense_MOP, expense_frequency) :
        self.frequency = expense_frequency  # That's Monthly. i.e. 1 means once a month
        GeneralExpense.Expense.__init__(self, expense_title, expense_amount, expense_date, expense_MOP)
    def get_annual_total(self):
        self.total = self.frequency * 12
        print "Annual expense is ",self.total
        

