import os

from flask import render_template, redirect, url_for

from manzai import app
from manzai.forms import ManzaiForm
from manzai.models import ManzaiMeta

@app.route('/', methods=['GET', 'POST'])
def index():
    form = ManzaiForm()

    if form.validate_on_submit():
        meta = ManzaiMeta(manzai_id=form.manzai_id.data, player_id=form.player_id.data)
        meta.add(file_path=os.path.join(app.config["DATA_DIR"], "manzai_meta.tsv"))

        return redirect(url_for('index'))

    return render_template('index.html', methods=['GET','POST'], form=form)
