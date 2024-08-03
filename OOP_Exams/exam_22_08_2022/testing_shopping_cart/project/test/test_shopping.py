from unittest import TestCase, main
from project.shopping_cart import ShoppingCart


class TestShoppingCart(TestCase):
    def setUp(self):
        self.cart = ShoppingCart("Metro", 250)
        self.cart.products = {"Cheese": 12.00}

        self.cart2 = ShoppingCart("Lidl", 100)
        self.cart2.products = {"Icecream": 5}

    def test_correct_init(self):
        self.assertEqual("Metro", self.cart.shop_name)
        self.assertEqual(250, self.cart.budget)
        self.assertEqual({"Cheese": 12.00}, self.cart.products)

    def test_shop_name_setter_raises_value_error(self):
        expected = "Shop must contain only letters and must start with capital letter!"

        with self.assertRaises(ValueError) as ve:
            self.cart.shop_name = "Metro1"
        self.assertEqual(expected, str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.cart.shop_name = "metro"
        self.assertEqual(expected, str(ve.exception))

    def test_add_to_cart_with_too_high_price_raises_value_error(self):
        expected = "Product TV cost too much!"
        with self.assertRaises(ValueError) as ve:
            self.cart.add_to_cart("TV", 400)
        self.assertEqual(expected, str(ve.exception))

    def test_add_to_cart_successfully(self):
        expected = f"Eggs product was successfully added to the cart!"
        self.assertEqual(expected, self.cart.add_to_cart("Eggs", 12))
        self.assertEqual({"Cheese": 12.00, "Eggs": 12.00}, self.cart.products)

    def test_remove_from_cart_successfully(self):
        expected = f"Product Cheese was successfully removed from the cart!"
        self.assertEqual(expected, self.cart.remove_from_cart("Cheese"))
        self.assertEqual({}, self.cart.products)

    def test_remove_from_cart_wih_non_existing_name_in_the_cart(self):
        expected = f"No product with name TV in the cart!"
        with self.assertRaises(ValueError) as ve:
            self.cart.remove_from_cart("TV")

        self.assertEqual(expected, str(ve.exception))

    def test__add__combines_with_other_shopping_cart(self):
        expected = ShoppingCart("MetroLidl", 350)
        expected.products = {"Cheese": 12.00, "Icecream": 5}

        result = self.cart.__add__(self.cart2)
        self.assertEqual(expected.shop_name, result.shop_name)
        self.assertEqual(expected.budget, result.budget)
        self.assertEqual(expected.products, result.products)

    def test_buy_products_with_not_enough_budget_raises_value_error(self):
        total_sum = sum(self.cart.products.values())
        self.cart.budget = 5
        expected = (f"Not enough money to buy the products! "
                    f"Over budget with {total_sum - self.cart.budget:.2f}lv!")

        with self.assertRaises(ValueError) as ve:
            self.cart.buy_products()
        self.assertEqual(expected, str(ve.exception))

    def test_buy_products_successfully(self):
        total_sum = sum(self.cart.products.values())
        expected = f'Products were successfully bought! Total cost: {total_sum:.2f}lv.'
        self.assertEqual(expected, self.cart.buy_products())


if __name__ == "__main__":
    main()
