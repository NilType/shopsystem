# -*- coding:utf-8 -*-
from shopsystem.apps.catalog.models import User
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
import urllib.parse
import urllib
import datetime
from shopsystem.apps.catalog.viewsdir.messageviews import Message
from shopsystem.apps.catalog.viewsdir.userSession import UserSession

def showregis(request):
    c = {}
    t = "regist.html"
    return render_to_response(t, c, context_instance=RequestContext(request))

def register(request):
    userName = urllib.parse.unquote(request.POST.get("userName"))

    password = urllib.parse.unquote(request.POST.get("password"))
    #checkCode = urllib.unquote(request.Post.get("checkCode"))


    try:
        newuser = User(userName=userName, password=password)
        newuser.save()

        user = User.objects.get(userName=userName)
        myUser = UserSession(user.userid, user.userName)
        request.session['user'] = myUser
    except:
        return HttpResponse(Message(-1, '注册失败').getJson())
    return HttpResponse(Message(0, "注册成功").getJson())

def showlogin(request):
    c = {}
    t = "login.html"
    return render_to_response(t, c, context_instance=RequestContext(request))

def login(request):

    userName = urllib.parse.unquote(request.POST.get("userName"))#从页面上得到userName的值并且解码
    password = urllib.parse.unquote(request.POST.get("password"))
    checkCode = urllib.parse.unquote(request.POST.get("checkCode"))
    ifsave = urllib.parse.unquote(request.POST.get("ifSave"))

    user = None
    print(userName)
    try:
        user = User.objects.get(userName=userName)
    except Exception as ex:
        print(ex)

    if (user == None):
        msg = Message(1, "用户名不存在")
        return HttpResponse(msg.getJson())

    if (user.password != password):
        return HttpResponse(Message(2, "密码错误").getJson())

    if(checkCode != ""):
        # return HttpResponse(Message(3, "验证码错误").getJson())
        pass


    myUser = UserSession(user.userid, user.userName)

    request.session['user'] = myUser.toDict()

    if ifsave == "true":
        dt = datetime.datetime.now() + datetime.timedelta(hours=5)
        response = HttpResponse()
        response.set_cookie("userName", user.userName, expires=dt)
        response.set_cookie("password", user.password, expires=dt)

    return HttpResponse(Message(0, "登陆成功").getJson())


def logout(request):
    if request.session["user"] != None:
        del request.session["user"]
        response = HttpResponse()
        response.delete_cookie("userName")
        response.delete_cookie("password")
    return HttpResponseRedirect("/index/")



