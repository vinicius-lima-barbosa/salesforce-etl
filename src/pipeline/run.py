from extract.carts import extract_carts
from validate.carts import validate_carts
from transform.carts import transform_carts
from load.postgres import load_carts

def run_pipeline():
    carts = extract_carts()
    print(f"Extração concluída: {len(carts)} carrinhos.")

    validated_carts = validate_carts(carts)
    print(f"Validação concluída: {len(validated_carts)} carrinhos validados.")

    carts_df, products_df = transform_carts(validated_carts)
    print("Transformação concluída:")
    print(f" - Carrinhos: {len(carts_df)}")
    print(f" - Produtos: {len(products_df)}")

    carts_loaded, products_loaded = load_carts(carts_df, products_df)

    print("Carregamento concluído.")
    print(f"- Carrinhos carregados: {carts_loaded}")
    print(f"- Produtos carregados: {products_loaded}")
