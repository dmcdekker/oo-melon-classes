"""Classes for melon orders."""

import random
from datetime import datetime


class AbstractMelonOrder(object):
    """An abstract base class that other Melon Orders inherit from."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False

    def get_base_price(self):
        """Calculates base with Splurge pricing, rush hour, and melon type."""

        self.base_price = random.randint(5, 9)

        if self.species.lower() == "christmas melon":
            self.base_price *= 1.5

        order_timestamp = datetime.now()
        if order_timestamp.hour in range(8, 11) and \
           order_timestamp.weekday() in range(0, 5):
            self.base_price += 4

    def get_total(self):
        """Calculate price, including tax."""

        self.get_base_price()

        total = (1 + self.tax) * self.qty * self.base_price

        return total

    def mark_shipped(self):
        """Record the fact that an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    tax = 0.17

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        super(InternationalMelonOrder, self).__init__(species, qty)
        self.country_code = country_code

    def get_total(self):
        """Calculate price, including tax, and check for flat fees."""

        total = super(InternationalMelonOrder, self).get_total()

        if self.qty < 10:
            total += 3

        return total

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    """A melon order by the US government."""

    tax = 0

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        super(GovernmentMelonOrder, self).__init__(species, qty)
        self.passed_inspection = False

    def mark_inspection(self, passed):
        """Updates whether or not melon has passed inspection."""

        if type(passed) == bool:
            self.passed_inspection = passed
