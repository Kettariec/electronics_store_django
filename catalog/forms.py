from django import forms
from catalog.models import Product, Version


class StyleFormMixin:
    """Миксин для стилизации форм"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        # fields = ('', '',)
        # exclude = ('', '',) - исключить поля

    def clean_product_name(self):
        """Валидация поля name по запрещенным словам"""
        cleaned_data = self.cleaned_data.get('product_name')
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа',
                           'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in forbidden_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError(f'Вы используете запрещённое слово {word}')

        return cleaned_data

    def clean_product_description(self):
        """Валидация поля description по запрещенным словам"""
        cleaned_data = self.cleaned_data.get('product_description')
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа',
                           'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in forbidden_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError(f'Вы используете запрещённое слово {word}')

        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
