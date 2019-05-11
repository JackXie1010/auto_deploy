# coding: utf8
from tornado import web
from handler import h_index

url_route = [
    (web.url('/*', h_index.head)),
    (web.url('/login', h_index.login)),
    (web.url('/getConf', h_index.getConf)),
    (web.url('/addConf', h_index.addConf)),
    (web.url('/delConf', h_index.delConf)),
    (web.url('/updateConf', h_index.updateConf)),
    (web.url('/deploy', h_index.deploy)),
]