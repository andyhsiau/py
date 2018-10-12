# coding:utf-8
from flask import Flask
from flask_restful import Resource, Api
from IP import getAPInfo
from asset_soup import get_CI_info
from asset_db import get_CI_from_DB
from asset_db import get_CI_from_DB_user



app = Flask(__name__)
api = Api(app)


class cpi(Resource):
    def get(self, ip):
        
        return getAPInfo(ip)
class asset(Resource):
    def get(self, hostname):
        
        return get_CI_info(hostname)

class assetdb(Resource):
    def get(self, hostname):
        
        return get_CI_from_DB(hostname)

class assetdb_user(Resource):
    def get(self, username):
        
        return get_CI_from_DB_user(username)


api.add_resource(cpi, '/ip=<ip>')
api.add_resource(asset, '/ci=<hostname>')
api.add_resource(assetdb, '/device=<hostname>')
api.add_resource(assetdb_user, '/username=<username>')


if __name__ == '__main__':
    app.run(host='0.0.0.0')

