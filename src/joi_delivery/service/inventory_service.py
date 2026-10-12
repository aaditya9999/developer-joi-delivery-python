from .product_service import ProductService

class InventoryService:
    def __init__(self,product_service:ProductService):

        self.product_service=product_service

    def get_inventory_health(self,store_id:str):
        products=self.product_service.get_products_for_store(store_id)

        inventory=[]

        for product in products:
            if product.available_stock==0:
                status="OUT_OF_STOCK"
            elif product.available_stock<=product.threshold:
                status="LOW_STOCK"
            else:
                status="HEALTHY"
            inventory.append(
                {
                    'product_id':product.product_id,
                    "status":status,
                }

            )
        return {
            "storeid":store_id,
            "inventory":inventory,
        }