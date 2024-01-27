import unittest
import re
from src.cart import (
    ShoppingCart,
    InvalidCustomerIDError,
    ItemNotFoundInCatalogError,
    InvalidQuantityError,
)


class ShoppingCartTest(unittest.TestCase):
    def setUp(self):
        self.catalog = {"apple": 0.5, "banana": 0.3, "orange": 0.7}
        self.cart = ShoppingCart("ABC12345DE-A", self.catalog)

    def test_add_item(self):
        self.cart.add_item("apple", 2)
        self.assertEqual(self.cart.items["apple"], 2)

    def test_update_item(self):
        self.cart.add_item("apple", 2)
        self.cart.update_item("apple", 5)
        self.assertEqual(self.cart.items["apple"], 5)

    def test_remove_item(self):
        self.cart.add_item("banana", 1)
        self.cart.remove_item("banana")
        self.assertNotIn("banana", self.cart.items)

    def test_total_cost(self):
        self.cart.add_item("apple", 2)
        self.cart.add_item("banana", 3)
        self.assertEqual(self.cart.get_total_cost(), 2 * 0.5 + 3 * 0.3)

    def test_invalid_customer_id(self):
        with self.assertRaises(InvalidCustomerIDError):
            ShoppingCart("INVALID123", self.catalog)

    def test_invalid_item_name(self):
        with self.assertRaises(ItemNotFoundInCatalogError):
            self.cart.add_item("invalid_item", 1)

    def test_invalid_quantity(self):
        with self.assertRaises(InvalidQuantityError):
            self.cart.add_item("apple", -1)

    def test_quantity_upper_bound(self):
        with self.assertRaises(InvalidQuantityError):
            self.cart.add_item("apple", 101)

    def test_uuid_format_for_cart_id(self):
        uuid_regex = re.compile(
            r"^[0-9a-f]{8}-[0-9a-f]{4}-[4][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$",
            re.I,
        )
        self.assertTrue(uuid_regex.match(self.cart.id))

    def test_immutable_id_and_customer_id(self):
        with self.assertRaises(AttributeError):
            self.cart.id = "new_id"
        with self.assertRaises(AttributeError):
            self.cart.customer_id = "new_customer_id"

    def test_defensive_copying_of_items(self):
        items_copy = self.cart.items
        items_copy["apple"] = 10
        self.assertNotEqual(self.cart.items, items_copy)


# Run the tests
if __name__ == "__main__":
    unittest.main()
