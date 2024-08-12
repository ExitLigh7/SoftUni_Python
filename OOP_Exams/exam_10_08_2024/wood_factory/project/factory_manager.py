from typing import List
from collections import Counter
from project.products.base_product import BaseProduct
from project.products.chair import Chair
from project.products.hobby_horse import HobbyHorse
from project.stores.base_store import BaseStore
from project.stores.furniture_store import FurnitureStore
from project.stores.toy_store import ToyStore


class FactoryManager:
    VALID_PRODUCTS = {"Chair": Chair, "HobbyHorse": HobbyHorse}
    VALID_STORES = {"FurnitureStore": FurnitureStore, "ToyStore": ToyStore}

    def __init__(self, name: str):
        self.name = name
        self.income: float = 0.0
        self.products: List[BaseProduct] = []
        self.stores: List[BaseStore] = []

    def produce_item(self, product_type: str, model: str, price: float):
        if product_type not in self.VALID_PRODUCTS:
            raise Exception("Invalid product type!")

        new_product = self.VALID_PRODUCTS[product_type](model, price)
        self.products.append(new_product)
        return f"A product of sub-type {new_product.sub_type} was produced."

    def register_new_store(self, store_type: str, name: str, location: str):
        if store_type not in self.VALID_STORES:
            raise Exception(f"{store_type} is an invalid type of store!")

        new_store = self.VALID_STORES[store_type](name, location)
        self.stores.append(new_store)
        return f"A new {store_type} was successfully registered."

    def sell_products_to_store(self, store: BaseStore, *products: BaseProduct):
        if store.capacity < len(products):
            return f"Store {store.name} has no capacity for this purchase."

        sorted_products = [p for p in products if p.sub_type == store.ALLOWED_PRODUCTS]
        if not sorted_products:
            return "Products do not match in type. Nothing sold."

        store.products.extend(sorted_products)
        for product in sorted_products:
            self.products.remove(product)
        store.capacity -= len(sorted_products)
        self.income += sum(p.price for p in sorted_products)
        return f"Store {store.name} successfully purchased {len(sorted_products)} items."

    def unregister_store(self, store_name: str):
        store = next((s for s in self.stores if s.name == store_name), None)
        if store is None:
            raise Exception("No such store!")
        if store.products:
            return "The store is still having products in stock! Unregistering is inadvisable."

        self.stores.remove(store)
        return f"Successfully unregistered store {store_name}, location: {store.location}."

    def discount_products(self, product_model: str):
        products_count = 0
        for product in self.products:
            if product.model == product_model:
                product.discount()
                products_count += 1
        return f"Discount applied to {products_count} products with model: {product_model}"

    def request_store_stats(self, store_name: str):
        store = next((s for s in self.stores if s.name == store_name), None)
        if store is None:
            return "There is no store registered under this name!"

        return store.store_stats()

    def statistics(self):
        sorted_stores = sorted(self.stores, key=lambda s: s.name)
        partner_store_names = '\n'.join(s.name for s in sorted_stores)

        sorted_unsold_products = sorted(self.products, key=lambda p: p.model)
        unsold_model_counts = Counter(p.model for p in sorted_unsold_products)
        info_unsold = "\n".join(f"{model}: {count}" for model, count in unsold_model_counts.items())

        return (f"Factory: {self.name}\n"
                f"Income: {self.income:.2f}\n"
                f"***Products Statistics***\n"
                f"Unsold Products: {len(self.products)}. Total net price: {sum(p.price for p in self.products):.2f}\n"
                f"{info_unsold}\n"
                f"***Partner Stores: {len(self.stores)}***\n"
                f"{partner_store_names}")
