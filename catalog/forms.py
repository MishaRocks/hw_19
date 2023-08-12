from django import forms

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'description', 'preview', 'category', 'cost', 'add_date')

    def clean_name(self) -> str:
        cleaned_name = self.cleaned_data['name']
        exception_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in exception_list:
            if word in cleaned_name or word.title() in cleaned_name:
                raise forms.ValidationError('Вы использовали запрещенное слово')
        return cleaned_name

    def clean_description(self) -> str:
        cleaned_description = self.cleaned_data['description']
        exception_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in exception_list:
            if word in cleaned_description or word.title() in cleaned_description:
                raise forms.ValidationError('Вы использовали запрещенное слово')
        return cleaned_description


class VersionForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Version
        fields = ('number', 'name', 'sign', 'product')
