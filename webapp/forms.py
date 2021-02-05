"""
表单
"""

from wtforms import StringField, SubmitField
from wtforms.validators import Length, DataRequired, URL, InputRequired, Regexp
from flask_wtf import FlaskForm


class LoadFromKadaForm(FlaskForm):
    url = StringField("kada网址：", validators=[
        Length(10, 80),
        DataRequired(),
        InputRequired(),
        URL(),
        Regexp(r"(https://){0,1}kada.163.com/project/[0-9]{5,10}-[0-9]{5,10}.htm")
    ], render_kw={"placeholder": "例如：https://kada.163.com/project/6346529-4176102.htm"})
    submit = SubmitField("确定", validators=[DataRequired()])
