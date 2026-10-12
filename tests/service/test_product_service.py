from joi_delivery.domain.grocery_product import GroceryProduct
from joi_delivery.domain.grocery_store import GroceryStore
from joi_delivery.service.product_service import ProductService

def test_should_return_product_for_requested_store():
    store101=GroceryStore(
        name="Fresh Picks",
        outlet_id="store101"
    )

    store102=GroceryStore(
        name="Natural Choice",
        outlet_id="store102",
    )

    product101=GroceryProduct(
            product_id="product101",
            product_name= "chocos",
            mrp= 100.5,
            weight=200,
            threshold= 10,
            available_stock= 45,
            store=store101,
            
        
    )
    product102=GroceryProduct(
                product_id="product102",
                product_name= "sweet",
                mrp= 200.1,
                weight=200,
                threshold= 5,
                available_stock= 45,
                store=store101,
                
            
    )
    product103=GroceryProduct(
                product_id="product103",
                product_name= "bottle",
                mrp= 300.5,
                weight=200,
                threshold= 10,
                available_stock= 45,
                store=store102,
                
            
    )


    products_service=ProductService(
    products=[product101,product102,product103]
    )

    products=products_service.get_products_for_store("store101")

    assert len(products)==2
    assert product101 in products
    assert product102 in products
    assert product103 not in products


