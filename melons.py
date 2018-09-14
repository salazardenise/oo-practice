"""Classes for melon orders."""

from random import randint
from datetime import *

class TooManyMelonsError(ValueError):
    pass


class AbstractMelonOrder():

    def __init__(self, species, qty):
        self.species = species
        self.qty = qty
        if self.qty > 100:
            raise TooManyMelonsError("No more than 100 melons!")
        self.shipped = False

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    def get_base_price(self):
        dt = datetime.now()
        hour = dt.hour
        weekday = dt.weekday()
        base_price = randint(5,9)
        if hour >= 8 and hour <= 11 and weekday >= 0 and weekday <= 4:
            base_price += 4
        return base_price

    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price()
        if self.species == "Christmas melons":
            base_price = base_price * 1.5
        total = (1 + self.tax) * self.qty * base_price

        if self.order_type == "international" and self.qty < 10:
            total = total + 3

        return total


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    order_type = "international"
    tax = 0.17
    
    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty)
        self.country_code = country_code


    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    tax = 0
    order_type = "government"

    def __init__(self, species, qty):
        super().__init__(species, qty)
        self.passed_inspection = False

    def mark_inspection(self, passed):
        self.passed_inspection = passed