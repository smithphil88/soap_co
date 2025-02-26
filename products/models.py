from django.db import models


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
    image = models.ImageField(upload_to='ingredients/', null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    weight = models.IntegerField(default=140,
                                    help_text='weight in grams', null=True,
                                    blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                    related_name="soaps")
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    ingredients = models.ManyToManyField(Ingredient, related_name="products",
                                        blank=True)

    def __str__(self):
        return self.name
