# -*- encoding:utf-8 -*-
from django import forms
from shopsystem.apps.catalog.models import Product

class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = [] #必须有这个exclude，不然会报错

    def clean_price(self):
        if self.cleaned_data['price'] <= 0:
            raise forms.ValidationError('价格必须大于0')
        return self.cleaned_data['price']

