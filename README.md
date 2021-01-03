**一、环境配置**

1.VSCode 下载，安装python,chinese,,path intellisence,npm,npm intillisence  ,Vetur, Vue3

Snippets ,vscode-icons, live serve这些文件

2.配置终端

切换到cmd

3.安装全段开发工具HbuilderX ：https://developers.weixin.qq.com/miniprogram/dev/devtools/download.html

4.安小程序开发工具：https://www.dcloud.io/hbuilderx.html



***二.安装git***

1.安装git：

2.创建远程仓库myBlog

3.初始化本地仓库，也就是在本地的myBLOG文件夹下执行：git init，执行完后会创建一个.git的隐藏文件

4.远程仓库和本地仓库进行关联：git remote add origin"你的远程仓库地址"

5.如果出现错误，ssh没有创建

6.先去创建密钥：ssh-keygen，一路ENTER，生成密钥

7.查看生成密钥 cat-/.ssh/id_rsa.pub,将密钥写入github上的settings下的SSH and GPG keys下

8.推送四步骤：

​    git status   查看发生变化的文件
​    git add .  追踪所有发生变化的文件
​    git  commit -m "备注"
​    git push -u origin master   第一次提交
​    git push





***三.创建myBlog虚拟环境***

1.空文件夹下，执行`django-admin startproject myBlog;`

2.给myBlog创建虚拟环境，使用：`python -m venv env`

3.进入到虚拟环境，windows下：`.\\env\\Scrtipst\\activate`

4.退出虚拟环境，windows下：'deactivate’：exit

5.创建app：`python manage.py startapp (app名字)`

***四.代码并执行***`

1.models.py:

`from django.db import models`

`from django.contrib.auth.models import User`



`\# Create your models here.`

`class Articles(models.Model):`

​    `title=models.CharField(max_length=128,verbose_name="文章标题")`

​    `author=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="作者")`

​    `img = models.ImageField(upload_to="",blank=True,null=True,verbose_name="文章配图")`

​    `abstract=models.TextField(verbose_name="文章摘要")`

​    `content = models.TextField(verbose_name="文章内容")`

​    `visited = models.IntegerField(default=0, verbose_name="文章访问量")`

​    `created_at = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")`

​    `modified_at = models.DateTimeField(auto_now=True,verbose_name="修改时间")`





​        `verbose_name="文章"`

​        `verbose_name_plural = verbose_name`

​        `ordering = ('created_at',)`

​    `def __str__(self):`

​        `return self.title`

2.项目myBlog中的settings.py配置：

`INSTALLED_APPS = [`

​    `'django.contrib.admin',`

​    `'django.contrib.auth',`

​    `'django.contrib.contenttypes',`

​    `'django.contrib.sessions',`

​    `'django.contrib.messages',`

​    `'django.contrib.staticfiles',`

​    `'articles',`

   `'cousers',`

​    `'users',`

`]`

3.迁移数据库：python manage.py makemigrations

4.执行迁移文件：`python manage.py migrate`

5.admin.py:

`from django.contrib import admin`

`from .models import Articles`

`\# Register your models here.`



`class ArticlesAdmin(admin.ModelAdmin):`

​    `\# 表头`

​    `list_display = ("title","author","img","abstract","created_at")`

​    `\# 搜索`

​    `search_fields = ("title","author","abstract","content")`

​    `list_filter = list_display`



`admin.site.register(Articles)`

6.执行命令：`python manage.py runserver`



