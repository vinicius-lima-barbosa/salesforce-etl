def validate_carts(carts: list[dict]) -> list[dict]:
    if not isinstance(carts, list):
        raise ValueError("Os dados extraídos precisam ser uma lista.")

    required_cart_fields = {
        "id",
        "products",
        "total",
        "discountedTotal",
        "userId",
        "totalProducts",
        "totalQuantity",
    }

    required_product_fields = {
        "id",
        "title",
        "price",
        "quantity",
        "total",
        "discountPercentage",
        "discountedTotal",
    }

    for cart in carts:
        if not isinstance(cart, dict):
            raise ValueError("Foi encontrado um carrinho com estrutura inválida.")

        missing_fields = required_cart_fields - cart.keys()

        if missing_fields:
            raise ValueError(
                f"Carrinho {cart.get('id', 'desconhecido')}: "
                f"campos ausentes: {missing_fields}"
            )

        if not isinstance(cart["products"], list):
            raise ValueError(
                f"Carrinho {cart.get('id', 'desconhecido')}: "
                f"'products' não é uma lista."
            )

        for product in cart["products"]:
            if not isinstance(product, dict):
                raise ValueError(
                    f"Carrinho {cart['id']}: produto com estrutura inválida."
                )

            missing_fields = required_product_fields - product.keys()

            if missing_fields:
                raise ValueError(
                    f"Carrinho {cart['id']}: campos ausentes no produto: "
                    f"{missing_fields}"
                )

    return carts