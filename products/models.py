from django.db import models
from cloudinary.models import CloudinaryField


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    display_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_display_name(self):
        return self.display_name


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    image = CloudinaryField('image', null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    weight = models.IntegerField(
        default=140, help_text='weight in grams', null=True, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products")
    image = CloudinaryField('image', null=True, blank=True)
    ingredients = models.ManyToManyField(
        Ingredient, related_name="products", blank=True)

    def __str__(self):
        return self.name


class ProductGallery(models.Model):

    class Meta:
        verbose_name_plural = 'Product Galleries'
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="gallery")
    image = CloudinaryField('image', null=True, blank=True)

    def __str__(self):
        return f"Image for {self.product.name}"
