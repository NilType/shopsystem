# -*- encoding: utf-8 -*-

from django.conf.urls import url
from shopsystem.apps.catalog import index
from shopsystem.apps.catalog.viewsdir import messageviews, registerView,userSession
from shopsystem.apps.catalog.products import goods_detail,category_detail

urlpatterns = [

    url(r"^$", "shopsystem.apps.catalog.index.index"),
    url(r"^index/$", "shopsystem.apps.catalog.index.index"),
    url(r"showlogin/", "shopsystem.apps.catalog.viewsdir.registerView.showlogin"),
    url(r"^loginIn/$",  registerView.login),
    url(r"showregist/", "shopsystem.apps.catalog.viewsdir.registerView.showregis"),
    url(r"logout/", "shopsystem.apps.catalog.viewsdir.registerView.logout"),
    url(r"regist/$", "shopsystem.apps.catalog.viewsdir.registerView.register"),
    #url(r'^$', goods_detail.index, {'template_name': 'product/category.html'},
     #   'catalog_home'),
    url(r'^category/(?P<category_slug>[-\w]+)/$', category_detail.show_category,
        {'template_name': 'category.html'}, 'catalog_category'),
    url(r'^product/(?P<product_slug>[-\w]+)/$', goods_detail.show_product,
        {'template_name': 'product.html'}, 'catalog_product'),
]