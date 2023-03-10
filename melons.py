"""Classes for melon orders."""
import random
import datetime
class AbstractMelonOrder:
    order_type = None
    tax = 0
    
    def __init__(self, species, qty):
        self.species = species
        self.qty = qty
        self.shipped = False

    def get_base_price(self):
        base_price = random.randint(5,9)

        time = datetime.datetime.now()
        day = time.weekday()
        hour_of_day = time.hour

        if day <= 4 and hour_of_day >= 8 and hour_of_day <= 11:
            base_price += 4

        return base_price

    def get_total(self):
        """Calculate price, including tax."""
        base_price = self.get_base_price()
        if self.species == "christmas melon":
            base_price *= 1.5
            
        total = (1 + self.tax) * self.qty * base_price

        if self.order_type == "international" and self.qty < 10:
            total += 3

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    order_type =  "domestic"
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
    tax = 0.00
    order_type = "government"

    def __init__(self, species, qty):
        super().__init__(species, qty)
        self.passed_inspection = False

    def mark_inspection(self, passed):
        if passed == "passed":

            self.passed_inspection = True
 