"""
sja的web应用
"""

from flask import Flask, flash, redirect, make_response, request, url_for, render_template
from flask_wtf.csrf import CSRFError
from sja.errors import NotScratch3Error

import os

from flask_debugtoolbar import DebugToolbarExtension
from flask_bootstrap import Bootstrap
from flask_dropzone import Dropzone
from flask_wtf import CSRFProtect

from webapp.models import DataDict
from webapp.settings import config

from webapp.views import sjaweb_bp


# 扩展
bootstrap = Bootstrap()
dropzone = Dropzone()
dd = DataDict()
csrf = CSRFProtect()
toolbar = DebugToolbarExtension()


def make_app(config_name=None) -> Flask:
    if config_name is None:
        config_name = os.getenv('FLASK_ENV', 'development')

    app = Flask("webapp")
    app.config.from_object(config[config_name])

    # 去除jinja模板中的空白行
    app.jinja_env.trim_blocks = True
    app.jinja_env.lstrip_blocks = True

    bootstrap.init_app(app)
    dropzone.init_app(app)
    csrf.init_app(app)
    if config_name == "development":
        # toolbar.init_app(app)
        pass

    app.register_blueprint(sjaweb_bp)

    register_errors(app)

    return app


def register_errors(app: Flask):
    @app.errorhandler(404)
    def error_404(err):
        return render_template("404.html"), 404

    @app.errorhandler(NotScratch3Error)
    def error_not_scratch3(err):
        if request.path in ['/']:
            response = make_response('分析失败，这不是一个scratch3项目文件')
            response.mimetype = 'text/plain'
            return response, 400
        else:
            flash("分析失败，这不是一个scratch3项目文件", category="warning")
            return redirect(url_for("sjaweb.index")), 400

    @app.errorhandler(CSRFError)
    def error_csrf(err):
        if request.path in ['/']:
            response = make_response('会话过期，刷新重试')
            response.mimetype = 'text/plain'
            return response, 400
        else:
            flash("会话过期，请重试", category="warning")
            return redirect(url_for("sjaweb.index")), 400

    @app.errorhandler(500)
    def error_500(err):
        flash("服务器内部似乎出了一点小问题...", category="danger")
        return redirect(url_for("sjaweb.index")), 500

