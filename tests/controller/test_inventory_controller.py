import pytest
from fastapi.testclient import TestClient
from joi_delivery.main import app
from unittest.mock import patch

class TestInventoryController:
    @pytest.fixture
    def client(self):
        return TestClient(app)

    @patch(
            "joi_delivery.controller.inventory_controller.InventoryService.get_inventory_health"
        )
    def test_should_return_the_health_of_the_store(self,mock_get_inventory_health,client):
        mock_get_inventory_health.return_value={
            "storeid":"store101",
            "inventory":[
                {
                    "product_id":"product101",
                    "status":"HEALTHY"
                }
            ]
        }
        get_url = "/inventory/health?store_id=store101"

        # add required mocking.

        response = client.get(get_url)


        # Then: Assert the response
        assert response.status_code == 200
        data=response.json()
        assert data['storeid']=="store101"
        assert data["inventory"][0]['product_id']=="product101"
        assert data['inventory'][0]['status']=="HEALTHY"

        mock_get_inventory_health.assert_called_once_with("store101")

