# coding=utf-8
# 导入Flask类
from flask import Flask,jsonify
import pymssql
import configparser
cf=configparser.ConfigParser()
cf.read('config.ini')


# Flask 接收一个参数__name__，当前模块的文件名
# Flask 在查找静态文件，或者模板时候默认以当前文件所在的目录去查找
# 如果传一个不存在的模块名，将默认使用当前文件
app = Flask(__name__)


# 装饰器将路由映射到视图index
@app.route('/hello')
def index():
    return "hello world"

@app.route('/data')
def print_data():

	conn = pymssql.connect(host=cf.get("SqlServer-Database", "host"), user=cf.get("SqlServer-Database","user"), password=cf.get("SqlServer-Database","password"), database='LearnDb',autocommit=True)
	cursor=conn.cursor()
	sql="""select TOP 3 [Id],[url] FROM [LearnDb].[dbo].[pic]"""
	try:
		cursor.execute(sql)
		data = cursor.fetchall()
		cursor.close()
		conn.close()
		return jsonify({"urllist":data})
	except Exception as e :
		print(e)
		cursor.close()
		conn.close()
		return e
		
	
		
		
if __name__ == '__main__':
	# Flask 应用程序实例的方法run启动web服务器
    app.run(host='0.0.0.0',debug=True)