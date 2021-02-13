from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired


class MainForm(FlaskForm):
    city = StringField(
        label=('City:'),
        validators=[DataRequired()]
        )
    submit = SubmitField(label=('Submit'))