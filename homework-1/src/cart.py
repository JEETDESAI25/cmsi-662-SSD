import uuid
import re
from copy import deepcopy


class ShoppingCartError(Exception):
    pass


class ItemNotFoundInCatalogError(ShoppingCartError):
    pass


class InvalidCustomerIDError(ShoppingCartError):
    pass


class InvalidQuantityError(ShoppingCartError):
    pass


class ShoppingCart:
    """
    A shopping cart for managing purchases in an e-commerce platform.

    Attributes:
        _id (uuid.UUID): The unique identifier for the shopping cart.
        _customer_id (str): The ID of the customer owning the cart.
        _items (dict): The items in the cart along with their quantities.
    """

    def __init__(self, customer_id: str, catalog: dict):
        self._validate_customer_id(customer_id)
        self._id = uuid.uuid4()
        self._customer_id = customer_id
        self._items = {}
        self._catalog = catalog

    @property
    def id(self):
        return str(self._id)

    @property
    def customer_id(self):
        return self._customer_id

    @property
    def items(self):
        return deepcopy(self._items)

    def add_item(self, item_name: str, quantity: int):
        self._validate_item_name(item_name)
        self._validate_quantity(quantity)
        self._items[item_name] = self._items.get(item_name, 0) + quantity

    def update_item(self, item_name: str, quantity: int):
        self._validate_item_in_cart(item_name)
        self._validate_quantity(quantity)
        if quantity == 0:
            del self._items[item_name]
        else:
            self._items[item_name] = quantity

    def remove_item(self, item_name: str):
        self._validate_item_in_cart(item_name)
        del self._items[item_name]

    def get_total_cost(self) -> float:
        return sum(self._catalog[item] * qty for item, qty in self._items.items())

    @staticmethod
    def _validate_customer_id(customer_id: str):
        pattern = re.compile(r"^[A-Za-z]{3}\d{5}[A-Za-z]{2}-[Aa]$")
        if not pattern.match(customer_id):
            raise InvalidCustomerIDError("Invalid customer ID format.")

    def _validate_item_name(self, item_name: str):
        if item_name not in self._catalog or len(item_name) > 100:
            raise ItemNotFoundInCatalogError(
                "Item not found in catalog or name too long."
            )

    def _validate_quantity(self, quantity: int):
        if not 0 <= quantity <= 100:
            raise InvalidQuantityError("Quantity must be between 0 and 100.")

    def _validate_item_in_cart(self, item_name: str):
        if item_name not in self._items:
            raise ItemNotFoundInCatalogError("Item not found in cart.")


# Usage example (to be placed outside the class definition)
# catalog = {'apple': 0.5, 'banana': 0.3, 'orange': 0.7}
# cart = ShoppingCart('ABC12345DE-A', catalog)
# cart.add_item('apple', 2)
# cart.add_item('banana', 3)
# print(cart.id, cart.customer_id, cart.items)
# print(f"Total cost: ${cart.get_total_cost()}")
