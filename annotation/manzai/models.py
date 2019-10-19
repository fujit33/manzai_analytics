import os

from flask import url_for
import pandas as pd

class ManzaiMeta():
    def __init__(self, manzai_id, player_id):
        self.manzai_id = manzai_id
        self.player_id = player_id
    
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