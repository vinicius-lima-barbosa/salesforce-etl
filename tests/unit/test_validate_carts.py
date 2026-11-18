import pytest

from validate.carts import validate_carts

@pytest.fixture
def valid_carts():
    return [
        {
            "id": 1,
            "products": [
                {
                    "id": 10,
                    "title": "Product A",
                    "price": 100,
                    "quantity": 2,
                    "total": 200,
                    "discountPercentage": 10,
                    "discountedTotal": 180,
                }
            ],
            "total": 200,
            "discountedTotal": 180,
            "userId": 1,
            "totalProducts": 1,
            "totalQuantity": 2,
        }
    ]

def test_validate_carts_with_valid_data(valid_carts):
    result = validate_carts(valid_carts)

    assert result == valid_carts

def test_validate_carts_rejects_non_list():
    with pytest.raises(ValueError):
        validate_carts({})

def test_validate_carts_rejects_missing_cart_field(valid_carts):
    del valid_carts[0]["userId"]

    with pytest.raises(ValueError, match="campos ausentes"):
        validate_carts(valid_carts)

def test_validate_carts_rejects_invalid_products_structure(valid_carts):
    valid_carts[0]["products"] = {}

    with pytest.raises(ValueError, match="products"):
        validate_carts(valid_carts)

def test_validate_carts_rejects_missing_product_field(valid_carts):
    del valid_carts[0]["products"][0]["price"]

    with pytest.raises(ValueError, match="campos ausentes"):
        validate_carts(valid_carts)

def test_validate_carts_rejects_invalid_cart_structure():
    with pytest.raises(ValueError, match="estrutura inválida"):
        validate_carts(["invalid"])