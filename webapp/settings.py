"""
配置文件
"""

from secrets import token_hex


class BaseConfig(object):
    SECRET_KEY = token_hex()

    DEBUG_TB_INTER_CEPT_REDIRECTS = False

    # 文件上传设置
    DROPZONE_MAX_FILES = 1
    DROPZONE_MAX_FILE_SIZE = 20
    MAX_CONTENT_LENGTH = 20 * 1024 * 1024
    DROPZONE_ALLOWED_FILE_CUSTOM = True
    DROPZONE_ALLOWED_FILE_TYPE = '.sb3'
    DROPZONE_ENABLE_CSRF = True  # csrf保护

    WTF_CSRF_ENABLED = True

    # Dropzone的中文提示
    DROPZONE_DEFAULT_MESSAGE = "把 scratch3 文件拖动到这里或点击这里进行上传(目前只能上传一个)"
    DROPZONE_INVALID_FILE_TYPE = "你不能上传这种类型的文件"
    DROPZONE_FILE_TOO_BIG = "你最大可以上传{{ maxFilesize }}MB，上传的文件超出了限制：{{ filesize }}MB"
    DROPZONE_MAX_FILE_EXCEED = "你不能再上传更多文件了"

    DEBUG_TB_INTERCEPT_REDIRECTS = False

    # 资源加载位置
    DROPZONE_SERVE_LOCAL = True
    BOOTSTRAP_SERVE_LOCAL = True

    CACHE_TYPE = "simple"


class DevConfig(BaseConfig):
    CACHE_TYPE = "null"
    FLASK_DEBUG = True

class ProConfig(BaseConfig):
    FLASK_DEBUG = False
    DROPZONE_SERVE_LOCAL = False
    BOOTSTRAP_SERVE_LOCAL = False


class TestConfig(BaseConfig):
    DROPZONE_ENABLE_CSRF = False
    WTF_CSRF_ENABLED = False
    TESTING = True


config = {
    'development': DevConfig,
    'testing': TestConfig,
    'production': ProConfig
}
