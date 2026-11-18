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

    return carts_df, products_df