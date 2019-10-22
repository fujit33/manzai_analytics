import os
from datetime import datetime

from flask import url_for
import pandas as pd

class ManzaiMeta():
    def __init__(self, data):
        self.manzai_id = data.get("manzai_id")
        self.player_id = data.get("player_id")
    
    def add(self, file_path):
        new_record = pd.Series({"manzai_id": self.manzai_id, "player_id":self.player_id})
        
        # データ読み込み（ない場合は新規作成）
        if os.path.exists(file_path):
            manzai_df = pd.read_table(file_path, sep="\t")
        else:
            manzai_df = pd.DataFrame(columns=["manzai_id", "player_id"])
        
        # 追記
        manzai_df = manzai_df.append(new_record, ignore_index=True)
        manzai_df.to_csv(file_path, sep='\t', index=False)

        return None

class ManzaiLog():
    def __init__(self, data=None):
        self.log_data = data
    
    def add(self, file_path):
        """
        一つの漫才のログに追記
        """
        new_record = pd.Series({
            "logging_time": datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
            "manzai_id": self.log_data.get("manzai_id"), 
            "player_id":self.log_data.get("player_id"), 
            "talk_num": 0,
            "talker":self.log_data.get("talker"), 
            "talk_text":self.log_data.get("talk_text"), 
            "boke_flag":self.log_data.get("boke_flag"), 
            "tsukkomi_flag":self.log_data.get("tsukkomi_flag"), 
            "tsukkomi_for":self.log_data.get("tsukkomi_for"), 
            "act_flag":self.log_data.get("act_flag"), 
            "ma":self.log_data.get("ma"), 
            "move":self.log_data.get("move"), 
            "position":self.log_data.get("position"), 
            "voice_speed":self.log_data.get("voice_speed"), 
            "voice_loudness":self.log_data.get("voice_loudness"), 
            "voice_pitch":self.log_data.get("voice_pitch"), 
            "laugher":self.log_data.get("laugher"), 
            })

        # ファイル読み込み、ない場合は作成
        if os.path.exists(file_path):
            manzai_df = pd.read_table(file_path, sep="\t")
        else:
            manzai_df = pd.DataFrame(index=[], columns=new_record.index)

        new_record["talk_num"] = len(manzai_df) + 1
        manzai_df = manzai_df.append(new_record, ignore_index=True)
        manzai_df.to_csv(file_path, sep='\t', index=False)

        return None

    def union(self, tmp_file_path, full_file_path):
        """
        １つの漫才のログを全体のログに結合
        """
        manzai_df = pd.read_table(tmp_file_path, sep="\t")
        if os.path.exists(full_file_path):
            full_df = pd.read_table(full_file_path, sep="\t")
        else:
            full_df = pd.DataFrame(index=[], columns=manzai_df.columns)

        append_df = full_df.append(manzai_df)
        append_df.to_csv(full_file_path, sep='\t', index=False)

        return None

