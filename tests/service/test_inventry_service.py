from joi_delivery.domain.grocery_store import GroceryStore
from joi_delivery.domain.grocery_product import GroceryProduct
from joi_delivery.service.product_service import ProductService
from joi_delivery.service.inventory_service import InventoryService


def test_should_mark_product_as_healthy():
    store=GroceryStore(
        name="Fresh Picks",
        outlet_id="store12",
                       )

    product=GroceryProduct(
        product_id="product101",
        product_name="apple",
        mrp=100.6,
        weight=200,
        threshold=10,
        available_stock=30,
        store=store,
    )
    product_service=ProductService(products=[product])
    inventory_service=InventoryService(product_service)
    result=inventory_service.get_inventory_health("store12")

    assert result['storeid']=="store12"
    assert result['inventory'][0]['product_id']=="product101"
    assert result["inventory"][0]['status']=="HEALTHY"


def test_should_mark_product_as_low():
    store=GroceryStore(
          name="Fresh Limca",
          outlet_id="store101",
     )
    product=GroceryProduct(
        product_id="product101",
        product_name="apple",
        mrp=123.77,
        weight=134.6,
        threshold=15,
        available_stock=4,
        store=store,

    )
    product_service=ProductService(products=[product])
    inventory_service=InventoryService(product_service)

    result=inventory_service.get_inventory_health("store101")
    assert result['inventory'][0]['status']=="LOW_STOCK"

def test_should_mark_product_outofstock():
    store=GroceryStore(
        name="Fresh Picks",
        outlet_id="store101"
    )
    product=GroceryProduct(
        product_id="product101",
        product_name="greensand",
        mrp=55.33,
        weight=35,
        threshold=24,
        available_stock=0,
        store=store,


    )
    product_service=ProductService(products=[product])
    inventory_service=InventoryService(product_service)
    result=inventory_service.get_inventory_health("store101")
    assert result['inventory'][0]['status']=="OUT_OF_STOCK"

 
