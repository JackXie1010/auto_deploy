import peewee_async
from peewee import *
from conf.op_conf import get_conf
import model

db = peewee_async.PooledMySQLDatabase(
    database=get_conf()['db'],
    user=get_conf()['username'],
    password=get_conf()['password'],
    host=get_conf()['host'],
    port=get_conf()['port']
)

objs = peewee_async.Manager(db)
db.set_allow_sync(True)


class BaseModel(Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.trans = db.atomic_async           # 将事务改成atomic_async
        self.objs = peewee_async.Manager(db)   # 添加一个Manager类
    # add_time = DateTimeField(null=True, verbose_name="添加时间")

    class Meta:
        database = db


def create_table():
    db.create_tables([model.index.Server, model.index.User])


if __name__ == '__main__':
    create_table()