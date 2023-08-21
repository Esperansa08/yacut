from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional

from settings import MAX_LENGTH_SHORT, MAX_LENGTH_LONG, MIN_LENGTH


class URLMapForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[DataRequired(message='Обязательное поле'),
                    Length(MIN_LENGTH, MAX_LENGTH_LONG)]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[Length(MIN_LENGTH, MAX_LENGTH_SHORT), Optional()]
    )
    submit = SubmitField('Создать')