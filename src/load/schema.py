from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    MetaData,
    Numeric,
    String,
    Table,
)

metadata = MetaData()

carts_table = Table(
    "carts",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, nullable=False),
    Column("total", Numeric(12, 2), nullable=False),
    Column("discounted_total", Numeric(12, 2), nullable=False),
    Column("total_products", Integer, nullable=False),
    Column("total_quantity", Integer, nullable=False),
)

cart_products_table = Table(
    "cart_products",
    metadata,
    Column(
        "cart_id",
        Integer,
        ForeignKey("carts.id", ondelete="CASCADE"),
        primary_key=True,
    ),
    Column("product_id", Integer, primary_key=True),
    Column("title", String(255), nullable=False),
    Column("price", Numeric(12, 2), nullable=False),
    Column("quantity", Integer, nullable=False),
    Column("total", Numeric(12, 2), nullable=False),
    Column("discount_percentage", Numeric(5, 2), nullable=False),
    Column("discounted_total", Numeric(12, 2), nullable=False),
)