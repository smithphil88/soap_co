# Generated by Django 5.1.6 on 2025-02-26 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_product_weight'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='ingredients/')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='ingredients',
            field=models.ManyToManyField(blank=True, related_name='products', to='products.ingredient'),
        ),
    ]
