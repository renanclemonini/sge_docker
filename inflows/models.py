from django.db import models
from products.models import Product
from suppliers.models import Supplier


class Inflow(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT, related_name='inflows')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='inflows')
    quantity = models.IntegerField(verbose_name='Quantidade')
    description = models.TextField(verbose_name='Descrição', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='Criado em', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'
        ordering = ['-created_at']

    def __str__(self):
        # pyrefly: ignore  # missing-attribute
        return f'(Entrada) {str(self.product)} em {self.created_at.strftime('%d-%m-%Y %H:%M:%S')}'
