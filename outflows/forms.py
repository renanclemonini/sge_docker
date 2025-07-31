from django import forms
from django.core.exceptions import ValidationError
from . import models


class OutflowForm(forms.ModelForm):

    class Meta:
        model = models.Outflow
        fields = ['product', 'quantity', 'description']
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control mt-1'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control mt-1'}),
            'description': forms.Textarea(attrs={'class': 'form-control mt-1', 'rows': 3}),
        }
        labels = {
            'product': 'Produto',
            'quantity': 'Quantidade',
            'description': 'Descrição',
        }

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        product = self.cleaned_data.get('product')

        if quantity > product.quantity:
            raise ValidationError(
                f'Quantidade {quantity} é maior que a quantidade disponível: {product.quantity}.'
            )

        return quantity
