在shopsystem中的apps中创建app的语法不再是manage.py startapp appname 了，而是django-admin startapp appname

第二次工作，连接数据库mysql。

第三次，完成用户登录注册的功能和session和cookies的功能

显示图片功能的设置
在settings.py上设置：
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
在urls.py上的urlpattern上加上  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )

现在遇到的问题是要比较product的categories的id号与categories的id号一样的时候，那个product的categories的id号提取不出来
        categories = models.ManyToManyField(Category)#在models中与category是多对多关系
        products_list = Product.objects.all() #取到所有的product

        for p in products_list:
            print(p.categories.all())#p.categories.all()取到对应的所有的分类的集合，记住是集合

    在前端中就是
    {% for pro in products_list %}
        {% for p in pro.categories.all %}<!-- pro.categories.all就是相当于p.categories.all() -->
             {% if p.name == category.name  %} <!-- 一开始不知道要p.name来判断，直接就是p，-->
                                               <!-- 因为p是一个集合，不可能用来比较 -->
               <dt><a href="">{{ pro.name }}</a></dt>
             {% endif %}
        {% endfor %}
    {% endfor %}