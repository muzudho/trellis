"""
白紙の作成
"""

import json
import openpyxl as xl
from openpyxl.styles import PatternFill, Font
from openpyxl.styles.alignment import Alignment
from src.trellis import trellis_in_src as tr


print('step 1: render empty')

# ソースファイル（JSON形式）を読込
json_file_name = './examples/data/battle_sequence_of_unfair_cointoss.step1_full_manual.json'
print(f"json_file_name = {json_file_name}")
with open(json_file_name, encoding='utf-8') as f:
    document = json.load(f)

# ワークブックを新規生成
wb = xl.Workbook()

# ワークシート
ws = wb['Sheet']

# 定規の描画
tr.render_ruler(document, ws)

# ワークブックの保存            
wb.save('./temp/examples/step1_new_paper.xlsx')
