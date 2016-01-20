# -*- coding:utf-8 -*-
import logging
from shopsystem.apps.catalog.models import User, Product, Category
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.context_processors import csrf
from shopsystem.apps.catalog.viewsdir.userSession import UserSession
logger = logging.getLogger('shopsystem.apps.catalog.index')

def index(request):
    userName = request.COOKIES.get("username", None)
    password = request.COOKIES.get("password", None)

    if userName != None and password != None:
        try:
            user = User.objects.get(userName=userName)
        except:
            pass

        if(user != None):
            if (user.password != password):
                myUser = UserSession(user.userid, user.userName)
                request.session["user"] = myUser.toDict()#加入session,注意db模式要使用字典，不能直接使用对象

    #得到所有产品分类和产品
    try:
        categories = Category.objects.all()
        products_list = Product.objects.all()

        for p in products_list:
            print(p.categories.all())

    except Exception as e:
        logger.error(e)

    c = {"user": request.session.get("user", None), 'categories': categories, 'products_list': products_list}
    print(c)
    t = "index.html"
    return render_to_response(t, c, context_instance=RequestContext(request))


























