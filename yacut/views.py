import random
import string

from flask import flash, redirect, render_template

from . import app, db
from .forms import URLMapForm
from .models import URLMap


def get_unique_short_id():
    letters_and_digits = string.ascii_letters + string.digits
    unique_short_id = ''.join(random.sample(letters_and_digits, 6))
    return unique_short_id


@app.route('/', methods=['GET', 'POST'])
def add_link_view():
    form = URLMapForm()
    urlmap = URLMap()
    if form.validate_on_submit():
        original = form.original_link.data
        if form.custom_id.data:
            custom_id = form.custom_id.data
        else:
            custom_id = get_unique_short_id()
        if URLMap.query.filter_by(short=custom_id).first():
            flash(f'Имя {custom_id} уже занято!')
            return render_template('index.html', form=form)
        if URLMap.query.filter_by(original=original).first():
            flash('Эта ссылка уже есть в базе данных.')
            return render_template('index.html', form=form)
        urlmap = URLMap(
            original=original,
            short=custom_id
        )
        db.session.add(urlmap)
        db.session.commit()
        return render_template('index.html', form=form, urlmap=urlmap)
    return render_template('index.html', form=form)


@app.route('/<string:short>')
def link_view(short):
    urlmap = URLMap.query.filter_by(short=short).first_or_404()
    return redirect(urlmap.original)
