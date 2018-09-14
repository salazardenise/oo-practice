"""A hierarchy of classes for salespeople."""

class Salesperson():
    """A salesperson at Ubermelon."""

    def __init__(self, base_salary=50000, commission_rate=0.05):
        """Initialize salesperson attributes."""

        self.base_salary = base_salary
        self.commission_rate = commission_rate

    def calculate_monthly_pay(self, total_sales):
        """Calculate the person's monthly pay.

        Use the person's base salary and commissions.
        """

        commission = self.commission_rate * total_sales
        monthly_salary = self.base_salary / 12

        return monthly_salary + commission


class InternSalesperson(Salesperson):
    """A college intern at Ubermelon working in sales."""

    def __init__(self, base_salary=20000, commission_rate=0.05):
        """Initialize intern attributes."""

        self.base_salary = base_salary
        self.commission_rate = commission_rate
