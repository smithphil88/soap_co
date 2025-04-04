from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):
    """ Form to add/edit products """
    image = forms.ImageField(
        required=True,
        error_messages={'required': 'An image is required to add a product.'}
    )

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        display_names = [(c.id, c.get_display_name()) for c in categories]

        self.fields['category'].choices = display_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
