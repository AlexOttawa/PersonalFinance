import GeneralExpense
import Recurring



RecurringRent = Recurring.RecurringExpense('Rent',1100,"09/01/2014", 'credit card',1)
RecurringRent.get_annual_total
print RecurringRent.frequency
RecurringRent.show_info()
