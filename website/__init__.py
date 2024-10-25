from flask import Flask
from flask_mysqldb import MySQL

def create_app():
    app = Flask(__name__)
    
    app.secret_key = 'joshua'
    app.config['MYSQL_HOST'] = 'ant-hill-systemproject.e.aivencloud.com'
    app.config['MYSQL_USER'] = 'avnadmin'
    app.config['MYSQL_PASSWORD'] = 'AVNS_GqaCqy7Ur5_hs6iLcyk'
    app.config['MYSQL_DB'] = 'ant_hill'
    
    from .main_route import views
    app.register_blueprint(views)
    
    return app