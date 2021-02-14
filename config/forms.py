from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField

from wtforms.fields.html5 import DateField

from wtforms.validators import DataRequired

from config.funcs import get_date_field_data


class MainForm(FlaskForm):
    min_date, max_date = get_date_field_data()

    date = DateField(
        label='Date:',
        render_kw={'min': min_date, 'max': max_date},
        validators=[DataRequired()]
    )

    city = StringField(
        label='City:',
        validators=[DataRequired()]
        )

    submit = SubmitField(label=('Submit'))
