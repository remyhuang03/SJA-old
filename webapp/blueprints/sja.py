"""
视图模块
"""

import secrets
import os
from random import randint

from pyscratch.loader import load_from_bytes, load_from_kada
from pyscratch.reporter.highcharts import pie, needs
from pyscratch import __version__

from webapp.models import DataDict
from webapp.forms import LoadFromKadaForm

from flask import render_template, request, redirect, flash, url_for, session, Blueprint

from markdown import markdown

dd = DataDict()

sjaweb_bp = Blueprint(
    "sjaweb",
    __name__,
)

help_html = markdown(
    open(
        os.path.join(
            os.path.dirname(
                sjaweb_bp.root_path
            ),
            "../help_web.md"
        ),
        mode="r",
        encoding="utf-8"
    ).read()
)

tips = [
    "扩展名为.sb3的文件也不一定是scratch3文件哟",
    "只有scratch2文件？可以使用scratch3在线编辑器转换：上传scratch2文件->保存为scratch3文件！",
    "这个分析器只能分析scratch3文件！",
]


@sjaweb_bp.route('/', methods=["GET", "POST"])
def index():
    if 'tips' not in session:
        session['tips'] = randint(0, (len(tips)) * 3 - 1)
    session['tips'] = session['tips'] + randint(1, 3)
    if session['tips'] > len(tips) * 3 - 1:
        session['tips'] = 1

    random_name = secrets.token_hex(6)
    if request.method == 'POST':
        if "file" in request.files:
            f = request.files["file"]
            session['name'] = random_name
            scratch = load_from_bytes(f)
            scratch.filename = request.files["file"].filename
            dd[session['name']] = scratch

    return render_template(
        "index.html",
        core_version=__version__,
        tip=tips[session['tips'] // 3],
    )


@sjaweb_bp.route('/load_url', methods=['GET', 'POST'])
def load_url():
    if "pythonanywhere.com" in request.host:
        flash("抱歉，因为这个网站以免费账户身份部署在pythonanywhere上，所以访问不了kada，你可以下载离线版本。",
              category="danger")
        return redirect(url_for('sjaweb.index'))

    form = LoadFromKadaForm()

    if request.method == 'POST' and form.validate():
        if "pythonanywhere.com" in request.host:
            flash("无法访问kada网站", category="danger")
            return redirect(url_for("sjaweb.index"))
        url = form.url.data
        random_name = secrets.token_hex(6)
        session['name'] = random_name
        dd[session['name']] = load_from_kada(url)

        return redirect(url_for('sjaweb.report'))
    else:
        if request.method == 'POST':
            flash("提交的网址不正确！", category="warning")
        else:
            flash("虽然这个程序可以分析闭源项目，但这并不代表你就可以这么做，后果自负。", category="warning")

    return render_template("load_url.html", form=form)


@sjaweb_bp.route('/report')
def report():
    if 'name' in session:
        file_name = session['name']
        if file_name in dd.dict:
            print(dd[file_name].statistic.blocks_count)
            return render_template(
                'report.html',
                report=dd[file_name],
                sorted=sorted,
                round=round,
                sort_key=lambda k: k[1],
                charts=pie(dd[file_name]),
                needs=needs
            )

    flash("请先上传一个scratch文件！", category="warning")
    return redirect(url_for('sjaweb.index'))


@sjaweb_bp.route("/help")
def help_page():
    return render_template("help.html", help_html=help_html)


@sjaweb_bp.route("/about")
def about():
    return render_template("about.html")
