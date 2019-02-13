import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'     # 设置密钥，由or连接环境变量和硬编码字符串
