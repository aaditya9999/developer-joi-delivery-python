from typing import List, Optional

from ..domain.grocery_product import GroceryProduct


class ProductService:
    def __init__(self, products: List[GroceryProduct]):
        self.products = products

    def get_product(self, product_id: str, outlet_id: str) -> Optional[GroceryProduct]:
        for product in self.products:
            if product.product_id == product_id and product.store and product.store.outlet_id == outlet_id:
                return product
        return None

    def get_products_for_store(self,store_id:str)->List[GroceryProduct]:
        return [
            product 
            for product in self.products
            if product.store and product.store.outlet_id==store_id
        ]
