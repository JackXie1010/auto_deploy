import model
from playhouse.shortcuts import model_to_dict


class BaseControl(object):
    def __init__(self, *args, **kwargs):
        super(BaseControl, self).__init__(*args, **kwargs)
        self.serv_model = model.index.Server()
        self.user_model = model.index.User()

    # -----------------------------------------------------------------------------------------------CURD start
    async def table_add(self, model, table, arg):
        try:
            obj = await model.objs.create(table, **arg)
        except:
            print('excep: table_add error')
            obj = 0
        return obj

    async def table_delete(self, model, sql):
        try:
            num = await model.objs.execute(sql)
        except:
            print('excep: table_delete error')
            num = 0
        return num

    async def table_update(self, model, sql):
        try:  # success: num=1
            num = await model.objs.execute(sql)
        except:
            print('excep: table_update error')
            num = 0
        return num

    async def table_get(self, model, sql):
        try:
            obj = await model.objs.get(sql)
            obj = model_to_dict(obj)
        except:
            print('excep: table_get error')
            obj = 0
        return obj

    async def table_find(self, model, sql):
        try:
            data = await model.objs.execute(sql)
            lst = []
            for v in data:
                v = model_to_dict(v)
                lst.append(v)
        except:
            print('excep: table_find error')
            lst = []
        return lst
    # ----------------------------------------------------------------------------------------------- CURD end

    def res_ok(self, code=200, data=1, msg='请求成功！'):
        return dict(code=code, data=data, msg=msg)

    def res_err(self, code=204, data=0, msg='请求失败！'):
        return dict(code=code, data=data, msg=msg)


