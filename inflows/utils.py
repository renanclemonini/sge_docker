from . import models


def product_increase(inflow: models.Inflow) -> bool:
    product = inflow.product
    product.quantity += inflow.quantity
    if product.save():
        return True

    return False
