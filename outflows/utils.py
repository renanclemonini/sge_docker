from . import models


def product_decrease(outflow: models.Outflow):
    product = outflow.product
    if product.quantity > outflow.quantity:
        product.quantity -= outflow.quantity
        product.save()
        return True

    return False
