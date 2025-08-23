from . import models


def product_increase(inflow: models.Inflow) -> bool:
    product = inflow.product
    product.quantity += inflow.quantity
    product.save()
    return True
