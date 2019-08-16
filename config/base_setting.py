SQLALCHEMY_DATABASE_URI = 'mysql://root:xxxxx@127.0.0.1/jfbz'
DEBUG = False
SQLACHEMY_ECHO = False
SERVER_PORT = 9000
JSON_AS_ASCII = False#使用返回的json数据可以用中文显示
SQLALCHEMY_TRACK_MODIFICATIONS = False
#RELEASE_VERSION = '1.0'

AUTH_COOKIE_NAME = "jf_member"

IGNORE_URLS = [
    "^/user/login",
    #"^/api"

]

IGNORE_CHECK_LOGIN_URLS = [
    "^/static",
    "^/favicon.ico"
]

"""
分页参数
"""
PAGE_SIZE = 50
PAGE_DISPLAY = 10

#统一生成的密钥长度
KEY_LENGTH = 16


APP = {
    'domain':'http://192.168.199.224:9000'
}

#报障的各种状态
STATUS_MAPPING = {
    '1':'处理完成',
    '0':'无法处理',
    '-9':'延期处理',
    '-8':'待处理',
    '-7':'处理中'
}

ATTRIBUTE_MAPPING = {
    '1':'老师',
    '0':'学生'
}

MINA_APP = {
    'appid':'wx323469d8c2921db3',
    'appkey':'d861f7f3a525cecfbb37fe816ed24c52'
}

API_IGNORE_URLS = [
    "^/api"
]
UPLOAD = {
    'ext':['jpg','gif','bmp','jpeg','png'],
    'prefix_path':'/static/upload/',
    'prefix_url':'/static/upload/'
}


