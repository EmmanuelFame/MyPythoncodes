from Item import Item
import csv

class Keyboard(Item): #Inheritance
    def __init__(self, name: str, price: float, quantity=0, broken_phone=0):
        # Call to super function to have access to all attribute/methods
        super().__init__(
            name, price, quantity
        )

        # Run validations to the received arguments
        assert price >= 0, f"price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"quantity {quantity} is not greater than or equal to zero!"
        assert broken_phone >= 0, f"broken_phone {broken_phone} is not greater than or equal to zero!"

        # Assigned to self object

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.__price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        # we will count out the floats that are point zero
        # i.e 5.0, 10.0
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"Item('{self.name}', {self.price},{self.quantity})"

