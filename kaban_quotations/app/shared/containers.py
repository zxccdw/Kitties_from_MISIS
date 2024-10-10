from dataclasses import dataclass
from repository.pg_repository import PGRepository
from service.product_service import ProductService
from service.prediction_service import PredicitonService


@dataclass
class Container:
    product_service: ProductService
    prediction_service: PredicitonService


def init_combat_container() -> Container:
    pg_repository = PGRepository()
    product_service = ProductService(pg_repository=pg_repository)
    prediction_service = PredicitonService()
    return Container(
        product_service=product_service, prediction_service=prediction_service
    )
