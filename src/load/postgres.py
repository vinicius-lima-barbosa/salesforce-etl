from sqlalchemy.dialects.postgresql import insert

from config.database import engine
from load.schema import (
    metadata,
    carts_table,
    cart_products_table,
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

def load_carts(carts_df, products_df, connection=None):
    metadata.create_all(engine)

    def execute_load(conn):
        carts_loaded = upsert_dataframe(
            conn,
            carts_table,
            carts_df,
            ["id"],
        )

        products_loaded = upsert_dataframe(
            conn,
            cart_products_table,
            products_df,
            ["cart_id", "product_id"],
        )

        return carts_loaded, products_loaded

    if connection is not None:
        return execute_load(connection)

    with engine.begin() as connection:
        return execute_load(connection)