# -*- encoding: utf-8 -*-

from shopsystem.apps.catalog.models import Product
from django.shortcuts import get_object_or_404, render




def show_product(request, product_slug, template_name):
    p = get_object_or_404(Product, slug=product_slug)
    categories = p.categories.filter(is_active=True)
    page_title = p.name
    meta_keywords = p.meta_description
    return render(request, template_name, locals())
