from flask_wtf import FlaskForm
from wtforms import TextAreaField ,StringField, SubmitField, RadioField
from wtforms.validators import DataRequired

class ManzaiMetaForm(FlaskForm):
    # メタデータ
    manzai_id = StringField('漫才ID', validators=[DataRequired()])
    player_id = StringField('出場者ID', validators=[DataRequired()])
    submit_meta = SubmitField('スタート')

class ManzaiLogForm(FlaskForm):
    # # メタデータ
    manzai_id = StringField('漫才ID', validators=[DataRequired()])
    player_id = StringField('出場者ID', validators=[DataRequired()])

    # 漫才ログ
    talker = RadioField(
        '話者',choices=[('A', 'A(基本立ち位置左)'), ('B', 'B(基本立ち位置右)')], 
        default='A', validators=[DataRequired()])

    talk_text = TextAreaField(
        '発話内容', validators=[DataRequired()])

        
    boke_flag = RadioField(
        'ボケ',choices=[('0', 'いいえ'), ('1', 'はい')], 
        default='0', validators=[DataRequired()])

    tsukkomi_flag = RadioField(
        'ツッコミ',choices=[('0', 'いいえ'), ('1', 'はい')], 
        default='0', validators=[DataRequired()])

    tsukkomi_for = StringField(
        'ツッコミの対象発話番号（カンマ区切り）')

    act_flag = RadioField(
        '役柄を演じているか',choices=[('0', 'いいえ'), ('1', 'はい')], 
        default='0', validators=[DataRequired()])

    ma = RadioField(
        '間', choices=[('-2', '完全に重複'), ('-1', '食い気味'), ('0',"ゼロ"), ('1',"小"), ('2',"大")],
        default='0', validators=[DataRequired()])

    move = RadioField(
        '動き',choices=[('1', '小(手まで)'), ('2', '中（上半身まで）'), ('3', '大（体全体）')], 
        default='1', validators=[DataRequired()])

    position = RadioField(
        '立ち位置', choices=[('-2', '大きく左'), ('-1', '左'), ('0', '初期位置'), ('1', '右'), ('2', "大きく右")],
        default='0', validators=[DataRequired()])

    voice_speed = RadioField(
        'しゃべる速さ', choices=[('-1', '遅い'), ('0', '普通'), ('1', '速い')],
        default='0', validators=[DataRequired()])

    voice_loudness = RadioField(
        '声の大きさ', choices=[('-1', '小さい'), ('0', '普通'), ('1', '大きい')],
        default='0', validators=[DataRequired()])

    voice_pitch = RadioField(
        '声の高さ', choices=[('-1', '低い'), ('0', '普通'), ('1', "高い")],
        default='0', validators=[DataRequired()])

    laugher = RadioField(
        '会場の笑い', choices=[('0', '無し'), ('1', '小さい'), ('2', '大きい')],
        default='0', validators=[DataRequired()])
