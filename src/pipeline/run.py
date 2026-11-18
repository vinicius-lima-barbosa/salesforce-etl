from extract.carts import extract_carts

def run_pipeline():
    carts = extract_carts()

    print(f"Extração concluída: {len(carts)} carrinhos.")

    return carts