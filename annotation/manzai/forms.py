from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField
from wtforms.validators import DataRequired

class ManzaiForm(FlaskForm):
    manzai_id = StringField('漫才ID', validators=[DataRequired()])
    player_id = StringField('出場者ID', validators=[DataRequired()])
    submit_meta = SubmitField('スタート')