from handler.base import BaseHandler
import hashlib


def get_md5(arg):   # md5 加密
    m = hashlib.md5()
    arg = arg + arg[-3:]
    m.update(arg.encode('utf-8'))
    ret_str = m.hexdigest()
    return ret_str.lower()


class head(BaseHandler):
    async def get(self):
        self.finish_err()

    async def post(self):
        self.finish_err()


class hello(BaseHandler):
    async def get(self):
        ret = self.finish_ok()
        self.write(self.to_json(ret))


class login(BaseHandler):
    async def post(self):
        arg = self.to_dict(self.request.body)
        arg['password'] = get_md5(arg['password'])

        @self.validate_arg(['username', 'password'], arg)
        def handler(): return 1
        result = handler()
        result = await self.ctrl_index.login(arg) if 200 == result['code'] else result
        self.finish_err(**result)


class getConf(BaseHandler):
    async def get(self):
        token = self.get_argument('token', '')
        arg = dict(token=token)

        @self.validate_arg(['token'], arg, is_valid_tonken=1)
        def handler(): return 1
        result = handler()
        result = await self.ctrl_index.getConf(arg) if 200 == result['code'] else result
        self.finish_ok(**result)


class addConf(BaseHandler):
    async def post(self):
        arg = self.to_dict(self.request.body)

        @self.validate_arg(['token', 'name', 'host', 'password', 'projectDir', 'isOnline', 'status'], arg, is_valid_tonken=1)
        def handler(): return 1
        result = handler()
        result = await self.ctrl_index.addConf(arg) if 200 == result['code'] else result
        self.finish_ok(**result)


class delConf(BaseHandler):
    async def post(self):
        arg = self.to_dict(self.request.body)

        @self.validate_arg(['token', 'id'], arg, is_valid_tonken=1)
        def handler(): return 1
        result = handler()
        result = await self.ctrl_index.delConf(arg) if 200 == result['code'] else result
        self.finish_ok(**result)


class updateConf(BaseHandler):
    async def post(self):
        arg = self.to_dict(self.request.body)

        @self.validate_arg(['token', 'name', 'host', 'password', 'projectDir', 'isOnline', 'status', 'id'], arg, is_valid_tonken=1)
        def handler(): return 1
        result = handler()
        result = await self.ctrl_index.updateConf(arg) if 200 == result['code'] else result
        self.finish_ok(**result)


class deploy(BaseHandler):
    async def post(self):
        arg = self.to_dict(self.request.body)

        @self.validate_arg(['id', 'name'], arg, is_valid_tonken=1)
        def handler(): return 1
        result = handler()
        result = await self.ctrl_index.deploy(arg) if 200 == result['code'] else result
        self.finish_ok(**result)




