import logging

from config.logging import setup_logging
from extract.carts import extract_carts
from validate.carts import validate_carts
from transform.carts import transform_carts
from load.postgres import load_carts

logger = logging.getLogger(__name__)

def run_pipeline():
    setup_logging()
    stage = "inicialização"

    try:
        logger.info("Pipeline iniciada.")

        stage = "extração"
        carts = extract_carts()
        logger.info("Extração concluída: %d carrinhos.", len(carts))

        stage = "validação"
        validated_carts = validate_carts(carts)
        logger.info(
            "Validação concluída: %d carrinhos validados.",
            len(validated_carts),
        )

        stage = "transformação"
        carts_df, products_df = transform_carts(validated_carts)

        logger.info("Transformação concluída.")
        logger.info("Carrinhos: %d", len(carts_df))
        logger.info("Produtos: %d", len(products_df))

        stage = "carga"
        carts_loaded, products_loaded = load_carts(carts_df, products_df)

        logger.info("Carga concluída.")
        logger.info("Carrinhos carregados: %d", carts_loaded)
        logger.info("Produtos carregados: %d", products_loaded)

        logger.info("Pipeline finalizada com sucesso.")

    except Exception:
        logger.exception("Falha durante a etapa de %s.", stage)
        raise
