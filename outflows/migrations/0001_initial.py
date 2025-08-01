# Generated by Django 5.2.3 on 2025-06-24 19:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    # pyrefly: ignore  # bad-override
    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Outflow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='Quantidade')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descrição')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='outflows', to='products.product')),
            ],
            options={
                'verbose_name': 'Saída',
                'verbose_name_plural': 'Saídas',
                'ordering': ['-created_at'],
            },
        ),
    ]
