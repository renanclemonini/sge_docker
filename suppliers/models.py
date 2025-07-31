from django.db import models
from django.forms import ValidationError


class Supplier(models.Model):
    name = models.CharField(verbose_name='Nome', max_length=500, unique=True)
    description = models.TextField(verbose_name='Descrição', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='Criado em', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Atualizado em', auto_now=True)

    class Meta:
        ordering = ["name"]
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'

    def clean(self):
        super().clean()
        normalized_name = self.name.title().strip()
        if Supplier.objects.exclude(pk=self.pk).filter(name__iexact=normalized_name).exists():
            raise ValidationError({"name": "Já existe um fornecedor com esse nome."})
        self.name = normalized_name

    def __str__(self):
        return self.name
