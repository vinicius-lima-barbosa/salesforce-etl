import pandas as pd

def transform_carts(carts: list[dict]) -> tuple[pd.DataFrame, pd.DataFrame]:
    carts_data = []
    products_data = []

    for cart in carts:
        carts_data.append({
            "id": cart["id"],
            "user_id": cart["userId"],
            "total": cart["total"],
            "discounted_total": cart["discountedTotal"],
            "total_products": cart["totalProducts"],
            "total_quantity": cart["totalQuantity"],
        })

        for product in cart["products"]:
            products_data.append({
                "cart_id": cart["id"],
                "product_id": product["id"],
                "title": product["title"],
                "price": product["price"],
                "quantity": product["quantity"],
                "total": product["total"],
                "discount_percentage": product["discountPercentage"],
                "discounted_total": product["discountedTotal"], 
            })

    carts_df = pd.DataFrame(carts_data)
    products_df = pd.DataFrame(products_data)

    if not products_df.empty:
        products_df = (
            products_df
            .groupby(["cart_id", "product_id"], as_index=False)
            .agg(
                title=("title", "first"),
                quantity=("quantity", "sum"),
                total=("total", "sum"),
                discounted_total=("discounted_total", "sum"),
            )
        )

        products_df["price"] = (
            products_df["total"] / products_df["quantity"]
        ).round(2)

        products_df["discount_percentage"] = (
            (
                1 - products_df["discounted_total"] / products_df["total"]
            ) * 100
        ).round(2)

    return carts_df, products_df