from extract.carts import extract_carts
from validate.carts import validate_carts

def run_pipeline():
    carts = extract_carts()
    print(f"Extração concluída: {len(carts)} carrinhos.")

    validated_carts = validate_carts(carts)
    print(f"Validação concluída: {len(validated_carts)} carrinhos validados.")

    return validated_carts