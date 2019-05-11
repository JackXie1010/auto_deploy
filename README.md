# 服务自动部署
主要功能：通过frabric远程拉取git的代码，服务管理人员可以通过前端配置控制服务是否上线
 接口：  
 1. /login:登陆接口，通过该接口进入配置管理界面  
 2. /getConf: 获取服务配置信息  
 3. /addConf: 添加服务配置
 4. /delConf: 删除配置
 5. /updteConf: 修改配置
 6. /deploy：提供给开发人员远程拉取更新代码

 页面效果:
![Image text](https://github.com/JackXie1010/auto_deploy/blob/master/static/img/a.PNG)
![Image text](https://github.com/JackXie1010/auto_deploy/blob/master/static/img/b.PNG)
![Image text](https://github.com/JackXie1010/auto_deploy/blob/master/static/img/c.PNG)

 启动：运行python server.py --port=8880，浏览器输入http://localhost:8080/static/login.html 进入登陆页

前端：
Vue + ElementUI中的分页组件，模态框组件 + 表单组件 + fly进行接口HTTP请求

后端：
python Tornado 框架，数据库使用的是MySQL

注意：不需要将server.sql 的文件导入数据库，服务运行时会自动生成数据表，只需要在conf/setting.conf 配置正确的数据库信息