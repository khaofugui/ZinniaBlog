## 本地运行

1. 尽量使用 Python3.4 以上版本以及 1.9 <= django < 1.0 

2. 创建 virtualenv

   $ virtualenv zinnia_blog_env

3. 激活虚拟环境

4. 克隆代码到本地：

   git clone https://github.com/zmrenwu/ZinniaBlog.git

5. 进入到 ZinniaBlog 目录下，安装依赖

   pip install -r requirements.txt

6. 在 ZinniaBlog/config 目录下创建 email_setting.py 文件，并写入以下代码

   ```python
   ZinniaBlog/config/email_setting.py

   EMAIL_HOST_USER = '你的邮箱用户名'
   EMAIL_HOST_PASSWORD = '邮箱密码'
   ```

   可选：为了使用评论后自动发邮件给管理员的功能，需要确保你的邮箱开启了 SMTP 服务。

7. 在 ZinniaBlog 目录下（与 manage.py 同级）建立一个 database 目录

8. 迁移数据库

   python manage.py migrate

9. 运行本地服务器

   python manage.py runserver

10. 浏览器输入 http://127.0.0.1:8000/

11. 创建后台管理员账户

   python manage.py createsuperuser

12. 浏览器输入 http://127.0.0.1:8000/admin 登录后台

## 自动化部署

注：演示代码仅适合运行 ubuntu 的服务器，但稍加修改也可适用于其他 linux 系统

1. 服务器系统最好是 ubuntu 14，其他版本的 ubuntu 没有测试。

2. 注册好域名并做好域名解析。

3. 远程登录你的服务器，配置服务器，安装必要服务

   更新系统

   $ sudo apt-get update

   $ sudo apt-get upgrade

   安装和开启 Nginx

   $ sudo apt-get install nginx

   $ sudo service nginx start

   安装 git、python3、pip、virtualenv

   $ sudo apt-get install git python3 python3-pip

   $ sudo pip3 install virtualenv

   安装 fabric

   $ sudo pip install fabric

   安装 pillow 所需依赖

   $ sudo apt-get install libjpeg-dev
   $ sudo apt-get install zlib1g-dev

4. 创建非 root 用户

5. 进入 ZinniaBlog/deploy_tools 目录下，运行部署脚本

   $ fab deploy:host=you_user_name@you_web_site_domain_name

   you_user_name 为你 linux 系统用户名（即 home 目录下用户文件夹名）

   you_web_site_domain_name 为你的部署网站的域名

6. 远程登录你的服务器，进入到 ZinniaBlog/deploy_tools 目录下，运行命令

   $ sed "s/SITENAME/you_web_site_domain_name/g" \
   deploy_tools/nginx.template.conf | sudo tee \
   /etc/nginx/sites-available/you_web_site_domain_name

   $ sudo ln -s /etc/nginx/sites-available/you_web_site_domain_name \
   /etc/nginx/sites-enabled/you_web_site_domain_name

   $ sed "s/SITENAME/you_web_site_domain_name/g" \
   deploy_tools/gunicorn-upstart.template.conf | sudo tee \
   /etc/init/gunicorn-you_web_site_domain_name.conf

7. 启动服务

   $ sudo service nginx reload

   $ sudo start gunicorn-you_web_site_domain_name