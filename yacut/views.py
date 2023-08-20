from flask import abort, flash, redirect, render_template, url_for

from . import app, db
from .forms import URLMapForm
from .models import URLMap
from .utils import special_match, get_unique_short_id


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLMapForm()
    if form.validate_on_submit():
        original = form.original_link.data
        if URLMap.query.filter_by(original=original).first():
            flash('Такая ссылка уже занята!')
            return redirect(url_for('index_view'))
        if form.custom_id.data:
            custom_id = form.custom_id.data
            if URLMap.query.filter_by(short=custom_id).first():
                form.custom_id.errors = [f'Имя {custom_id} уже занято!']
                render_template('index.html', form=form)
            if special_match(custom_id):
                flash('Hедопустимое именя для короткой ссылки')
                render_template('index.html', form=form)
        else:
            custom_id = get_unique_short_id()
            if URLMap.query.filter_by(short=custom_id).first():
                custom_id = get_unique_short_id()
        urlmap = URLMap(
            original=original,
            short=custom_id)
        db.session.add(urlmap)
        db.session.commit()
        return render_template('index.html', short=custom_id, form=form)
    return render_template('index.html', form=form)


@app.route('/<path:short>')
def redirect_view(short):
    return redirect(
        URLMap.query.filter_by(short=short).first_or_404().original)
