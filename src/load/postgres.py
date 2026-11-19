from sqlalchemy.dialects.postgresql import insert

from config.database import engine
from load.schema import (
    metadata,
    carts_table,
    cart_products_tabel,
)

def upsert_dataframe(connection, table, dataframe, conflict_columns):
    if dataframe.empty:
        return 0

    records = dataframe.to_dict(orient="records")
    statement = insert(table).values(records)

    update_values = {
        column.name: getattr(statement.excluded, column.name)
        for column in table.columns
        if column.name not in conflict_columns
    }

    statement = statement.on_conflict_do_update(
        index_elements=conflict_columns,
        set_=update_values,
    )

    connection.execute(statement)

    return len(records)

def load_carts(carts_df, products_df):
    metadata.create_all(engine)

    with engine.begin() as connection:
        carts_loaded = upsert_dataframe(
            connection,
            carts_table,
            carts_df,
            ["id"],
        )

        products_loaded = upsert_dataframe(
            connection,
            cart_products_tabel,
            products_df,
            ["cart_id", "product_id"],
        )

    return carts_loaded, products_loaded