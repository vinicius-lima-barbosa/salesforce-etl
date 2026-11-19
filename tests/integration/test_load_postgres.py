
import pandas as pd
import pytest

from config.database import engine
from load.postgres import load_carts
from load.schema import carts_table, cart_products_table

@pytest.fixture
def db_connection():
    connection = engine.connect()
    transaction = connection.begin()

    yield connection

    transaction.rollback()
    connection.close()

def test_load_carts_inserts_records(db_connection):
    carts_df = pd.DataFrame([
        {
            "id": 999001,
            "user_id": 10,
            "total": 100.00,
            "discounted_total": 90.00,
            "total_products": 1,
            "total_quantity": 2,
        }
    ])

    products_df = pd.DataFrame([
        {
            "cart_id": 999001,
            "product_id": 888001,
            "title": "Test Product",
            "price": 50.00,
            "quantity": 2,
            "total": 100.00,
            "discount_percentage": 10.00,
            "discounted_total": 90.00,
        }
    ])

    result = load_carts(carts_df, products_df, db_connection)

    assert result == (1, 1)

    cart = db_connection.execute(
        carts_table.select().where(carts_table.c.id == 999001)
    ).mappings().one()

    assert cart["user_id"] == 10

    product = db_connection.execute(
        cart_products_table.select().where(
            cart_products_table.c.cart_id == 999001
        )
    ).mappings().one()

    assert product["product_id"] == 888001

def test_load_carts_updates_existing_records(db_connection):
    carts_df = pd.DataFrame([
        {
            "id": 999002,
            "user_id": 10,
            "total": 100.00,
            "discounted_total": 90.00,
            "total_products": 1,
            "total_quantity": 2,
        }
    ])

    products_df = pd.DataFrame([
        {
            "cart_id": 999002,
            "product_id": 888002,
            "title": "Test Product",
            "price": 50.00,
            "quantity": 2,
            "total": 100.00,
            "discount_percentage": 10.00,
            "discounted_total": 90.00,
        }
    ])

    load_carts(carts_df, products_df, db_connection)

    carts_df.loc[0, "total"] = 200.00
    products_df.loc[0, "quantity"] = 4
    products_df.loc[0, "total"] = 200.00

    load_carts(carts_df, products_df, db_connection)

    cart_count = db_connection.execute(
        carts_table.select().where(carts_table.c.id == 999002)
    ).all()

    product_count = db_connection.execute(
        cart_products_table.select().where(
            cart_products_table.c.cart_id == 999002
        )
    ).all()

    assert len(cart_count) == 1
    assert len(product_count) == 1
    assert float(cart_count[0].total) == 200.00
    assert product_count[0].quantity == 4
