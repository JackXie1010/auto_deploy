from controller.base import BaseControl
from model.index import Server, User
from conf.jwt_token import gen_token
from datetime import datetime
from fabric import Connection


class IndexControl(BaseControl):
    async def deploy(self, arg):
        try:
            sql = Server.select().where(Server.name == arg['name'], Server.id == arg['id'])
            obj = await self.table_get(self.serv_model, sql)
            if not obj['isOnline']:
                password = dict(password=obj['password'])
                conn = Connection(obj['host'], connect_kwargs=password)
                with conn.cd(obj['projectDir']):  # 进入项目目录
                    conn.run('git pull')
                ret = self.res_ok(msg='更新成功')
            else:
                ret = self.res_err(msg='该服务已经上线，如需更新服务，请联系管理员')
        except:
            ret = self.res_err(msg='更新失败！')
        return ret

    async def login(self, arg):
        sql = User.select().where(User.username == arg['username'], User.password == arg['password'])
        obj = await self.table_get(self.user_model, sql)
        token = gen_token(obj['id'], obj['username']) if obj else 0
        ret = self.res_ok(data=token, msg='登陆成功！') if token else self.res_err(msg='登陆失败！', code=204)
        return ret

    async def getConf(self, arg):
        sql = Server.select()
        confs = await self.table_find(self.serv_model, sql)
        ret = self.res_ok(data=confs)
        return ret

    async def addConf(self, arg):
        arg['addTime'] = datetime.now()
        obj = await self.table_add(self.serv_model, Server, arg)
        ret = self.res_ok(msg='添加成功！') if obj else self.res_err(msg='添加失败！')
        return ret

    async def delConf(self, arg):
        sql = Server.delete().where(Server.id == arg['id'])
        num = await self.table_delete(self.serv_model, sql)
        ret = self.res_ok(msg='删除成功') if num else self.res_err(msg='删除失败')
        return ret

    async def updateConf(self, arg):
        sql = Server.update(name=arg['name'], host=arg['host'], password=arg['password'], projectDir=arg['projectDir'], isOnline=arg['isOnline'], status=arg['status']).where(Server.id==arg['id'])
        num = await self.table_update(self.serv_model, sql)
        ret = self.res_ok(msg='修改成功') if num else self.res_err(msg='修改失败')
        return ret

