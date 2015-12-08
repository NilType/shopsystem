# -*- coding:utf-8 -*-
from shopsystem.apps.catalog.models import User
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.context_processors import csrf
from shopsystem.apps.catalog.viewsdir.userSession import UserSession

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
    c = {"user": request.session.get("user", None)}
    print(c)
    t = "index.html"
    return render_to_response(t, c, context_instance=RequestContext(request))
