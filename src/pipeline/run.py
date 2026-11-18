from extract.carts import extract_carts
from validate.carts import validate_carts
from transform.carts import transform_carts

def run_pipeline():
    carts = extract_carts()
    print(f"Extração concluída: {len(carts)} carrinhos.")

    validated_carts = validate_carts(carts)
    print(f"Validação concluída: {len(validated_carts)} carrinhos validados.")

    carts_df, products_df = transform_carts(validated_carts)
    print("Transformação concluída:")
    print(f" - Carrinhos: {len(carts_df)}")
    print(f" - Produtos: {len(products_df)}")

    return carts_df, products_df