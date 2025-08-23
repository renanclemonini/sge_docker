from datetime import datetime
from services.notify import Notify
from . import models


def product_decrease(outflow: models.Outflow):
    product = outflow.product
    if product.quantity > outflow.quantity:
        product.quantity -= outflow.quantity
        product.save()
        return True

    return False


def send_outflow_event(outflow: models.Outflow):
    try:
        notify = Notify()
        data = {
            'event_type': 'create_outflow',
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'product': str(outflow.product),
            'product__cost_price': float(outflow.product.cost_price),
            'product__selling_price': float(outflow.product.selling_price),
            'quantity': outflow.quantity,
            'description': outflow.description,
        }
        notify.send_order_event(data)
    except:
        pass
