# from django.db.models.signals import pre_save, post_save
# from django.dispatch import receiver
# from inflows.models import Inflow


# @receiver(post_save, sender=Inflow)
# def update_product_quantity(sender, instance, created, **kwargs):
#     if created:
#         print('Passou aqui no signal')
#         # if instance.quantity > 0:
#         #     product = instance.product
#         #     product.quantity += instance.quantity
#         #     product.save()
