# Initialize the app
from flask import Flask, Config
from os import environ as env
from dotenv import find_dotenv, load_dotenv


print("--------------------------------------init----------api-----")
ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

# static_folder 和 template_folder都是执行文件路径，如果app初始化在根目录下，这个/static没有问题，但是现在
# api目录下，这个时候要往上一层路径
app = Flask(__name__,
            static_url_path='/',  # 配置静态文件的访问 url 前缀)
            static_folder='../static',  # 配置静态文件的文件夹
            template_folder='../templates'  # 配置模板文件的文件夹
            )
app.secret_key = env.get("APP_SECRET_KEY")

DEV_DB_URL = env.get("DEV_DB_URL")

app.config['SQLALCHEMY_DATABASE_URI'] = DEV_DB_URL
# 动态追踪修改设置，如未设置只会提示警告，此字段会增加了大量的开销,建议设置为False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# 若要查看映射的sql语句,需要如下配置，此功能对调试有用，正式环境建议设置为False
app.config['SQLALCHEMY_ECHO'] = True


DEBUG = env.get("DEBUG")


def get_app():
    return app
