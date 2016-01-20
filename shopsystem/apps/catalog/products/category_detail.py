# -*- encoding: utf-8 -*-

from shopsystem.apps.catalog.models import Category
from django.shortcuts import get_object_or_404, render


def show_category(request, category_slug, template_name):
    c = get_object_or_404(Category, slug=category_slug)
    product = c.product_set.all()
    page_title = c.name
    meta_keywords = c.meta_description
    return render(request, template_name, locals())