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





***三.创建myBlog项目***

1.空文件夹下，执行`django-admin startproject myBlog;`

2.给myBlog创建虚拟环境，使用：`python -m venv env`

3.进入到虚拟环境，windows下：`.\\env\\Scrtipst\\activate`

4.推出虚拟环境，windows下：'deactivate':


