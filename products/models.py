from django.db import models
from django.forms import ValidationError
from brands.models import Brand
from categories.models import Category


class Product(models.Model):
    title = models.CharField(verbose_name='Título', max_length=500, unique=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='products')
    description = models.TextField(verbose_name='Descrição', blank=True, null=True)
    serie_number = models.CharField(verbose_name='Número de Série', max_length=200, blank=True, null=True)
    cost_price = models.DecimalField(verbose_name='Preço de Custo', max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(verbose_name='Preço de Venda', max_digits=10, decimal_places=2)
    quantity = models.IntegerField(verbose_name='Quantidade', default=0)
    created_at = models.DateTimeField(verbose_name='Criado em', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['title']

    def clean(self):
        super().clean()
        title_normalized = self.title.title().strip()
        if Product.objects.exclude(pk=self.pk).filter(title__iexact=title_normalized).exists():
            raise ValidationError({"title": "Já existe um produto com esse título."})
        self.title = title_normalized

    def __str__(self):
        return self.title
