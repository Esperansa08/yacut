from flask import flash, redirect, render_template

from . import app, db
from .forms import URLMapForm
from .models import URLMap
from .utils import special_match, get_unique_short_id


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLMapForm()
    if form.validate_on_submit():
        original = form.original_link.data
        custom_id = form.custom_id.data
        if custom_id is None or len(custom_id) == 0:
            custom_id = get_unique_short_id()
        elif URLMap.query.filter_by(short=custom_id).first():
            flash(f'Имя {custom_id} уже занято!')
            return render_template('index.html', form=form)
        elif special_match(custom_id):
            flash('Hедопустимое именя для короткой ссылки')
            return render_template('index.html', form=form)
        urlmap = URLMap(
            original=original,
            short=custom_id)
        db.session.add(urlmap)
        db.session.commit()
        return render_template('index.html', short=custom_id, form=form)
    return render_template('index.html', form=form)


@app.route('/<string:short>', methods=['GET'])
def redirect_view(short):
    return redirect(
        URLMap.query.filter_by(short=short).first_or_404().original)
