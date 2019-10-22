import os

from flask import render_template, redirect, url_for, request
import pandas as pd

from manzai import app
from manzai.forms import ManzaiMetaForm, ManzaiLogForm
from manzai.models import ManzaiMeta, ManzaiLog

@app.route('/', methods=['GET', 'POST'])
def index():
    form = ManzaiMetaForm()
    form_data ={
            "manzai_id":form.manzai_id.data, 
            "player_id":form.player_id.data,
    }

    if form.validate_on_submit():
        print("bbb")
        meta = ManzaiMeta(data=form_data)
        meta.add(file_path=os.path.join(app.config["DATA_DIR"], "manzai_meta.tsv"))

        return redirect(url_for('annotation', manzai_id=form.manzai_id.data, player_id=form.player_id.data))

    return render_template('index.html', methods=['GET','POST'], form=form)

@app.route('/annotation', methods=('GET', 'POST'))
def annotation():
    form = ManzaiLogForm()

    # 初回はパラメータから取得し、２回目以降はフォームの内容から取得
    if request.args.get("manzai_id"):
        manzai_id=request.args.get("manzai_id")
        player_id=request.args.get("player_id")
    else:
        manzai_id=form.manzai_id.data 
        player_id=form.manzai_id.data

    file_path=os.path.join(app.config["DATA_DIR"], "tmp", manzai_id+"_log.tsv")

    # すでに記録済みのデータを読み込み
    if os.path.exists(file_path):
        talks_df=pd.read_table(file_path, sep="\t").sort_values('talk_num', ascending=False)
        talks_list= [{"num":num, "text":text} for num, text in zip(talks_df["talk_num"],talks_df["talk_text"])]
    else:
        talks_list= [{"num":None, "text":None}]

    if form.validate_on_submit():
        form_data ={
                "manzai_id":manzai_id, 
                "player_id":player_id,
                "talker":form.talker.data, 
                "talk_text":form.talk_text.data, 
                "boke_flag":form.boke_flag.data, 
                "tsukkomi_flag":form.tsukkomi_flag.data, 
                "tsukkomi_for":form.tsukkomi_for.data, 
                "act_flag":form.act_flag.data, 
                "ma":form.ma.data, 
                "move":form.move.data, 
                "position":form.position.data, 
                "voice_speed":form.voice_speed.data, 
                "voice_loudness":form.voice_loudness.data, 
                "voice_pitch":form.voice_pitch.data, 
                "laugher":form.laugher.data
        }
        log = ManzaiLog(data=form_data)
        log.add(file_path=file_path)

        return redirect(url_for(
            'annotation', manzai_id=manzai_id, player_id=player_id))

    return render_template(
        'annotation.html', methods=['GET','POST'], 
        form=form, manzai_id=manzai_id, player_id=player_id, talks=talks_list)

@app.route('/register', methods=('GET', 'POST'))
def register():
    form = ManzaiMetaForm()
    log = ManzaiLog()
    
    tmp_file_path = os.path.join(app.config["DATA_DIR"], "tmp", request.args.get("manzai_id")+"_log.tsv")
    full_file_path = os.path.join(app.config["DATA_DIR"], "manzai_log.tsv")

    # 全体のログに結合
    log.union(tmp_file_path=tmp_file_path, full_file_path=full_file_path)

    return redirect(url_for("index"))