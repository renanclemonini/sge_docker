from django import forms
from . import models


class InflowForm(forms.ModelForm):

    class Meta:
        model = models.Inflow
        fields = ['supplier', 'product', 'quantity', 'description']
        widgets = {
            'supplier': forms.Select(attrs={'class': 'form-control mt-1'}),
            'product': forms.Select(attrs={'class': 'form-control mt-1'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control mt-1', 'value': 1}),
            'description': forms.Textarea(attrs={'class': 'form-control mt-1', 'rows': 3}),
        }
        labels = {
            'supplier': 'Fornecedor',
            'product': 'Produto',
            'quantity': 'Quantidade',
            'description': 'Descrição',
        }

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity <= 0:
            raise forms.ValidationError(
                'Quantidade não pode ser menor ou igual a zero'
            )

        return quantity
