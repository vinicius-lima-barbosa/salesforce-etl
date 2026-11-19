import pytest

from transform.carts import transform_carts

@pytest.fixture
def sample_carts():
    return [
        {
            "id": 1,
            "userId": 10,
            "total": 200,
            "discountedTotal": 180,
            "totalProducts": 2,
            "totalQuantity": 3,
            "products": [
                {
                    "id": 100,
                    "title": "Product A",
                    "price": 100,
                    "quantity": 2,
                    "total": 200,
                    "discountPercentage": 10,
                    "discountedTotal": 180,
                },
                {
                    "id": 101,
                    "title": "Product B",
                    "price": 50,
                    "quantity": 1,
                    "total": 50,
                    "discountPercentage": 0,
                    "discountedTotal": 50,
                },
            ],
        }
    ]

def test_transform_carts_returns_dataframes(sample_carts):
    carts_df, products_df = transform_carts(sample_carts)

    assert len(carts_df) == 1
    assert len(products_df) == 2

def test_transform_carts_preserves_cart_data(sample_carts):
    carts_df, _ = transform_carts(sample_carts)

    cart = carts_df.iloc[0]

    assert cart["id"] == 1
    assert cart["user_id"] == 10
    assert cart["discounted_total"] == 180

def test_transform_carts_preserves_product_data(sample_carts):
    _, products_df = transform_carts(sample_carts)

    product = products_df.iloc[0]

    assert product["product_id"] == 100
    assert product["title"] == "Product A"
    assert product["quantity"] == 2

def test_transform_carts_preserves_relationship(sample_carts):
    _, products_df = transform_carts(sample_carts)

    assert all(products_df["cart_id"] == 1)

def test_transform_carts_aggregates_duplicate_products():
    carts = [
        {
            "id": 1,
            "userId": 10,
            "total": 200,
            "discountedTotal": 180,
            "totalProducts": 2,
            "totalQuantity": 3,
            "products": [
                {
                    "id": 100,
                    "title": "Product A",
                    "price": 50,
                    "quantity": 1,
                    "total": 50,
                    "discountPercentage": 10,
                    "discountedTotal": 45,
                },
                {
                    "id": 100,
                    "title": "Product A",
                    "price": 50,
                    "quantity": 2,
                    "total": 100,
                    "discountPercentage": 10,
                    "discountedTotal": 90,
                },
            ],
        }
    ]

    _, products_df = transform_carts(carts)

    assert len(products_df) == 1
    assert products_df.iloc[0]["quantity"] == 3
    assert products_df.iloc[0]["total"] == 150
    assert products_df.iloc[0]["discounted_total"] == 135