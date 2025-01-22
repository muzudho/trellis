"""
白紙に柱の頭を追加
"""

import json
import openpyxl as xl
from openpyxl.styles import PatternFill, Font

from src.trellis import trellis_in_src as tr
from src.trellis.compiler import AutoShadowSolver, AutoSplitPillar


# 設定ファイル（JSON形式）
file_path_of_config_doc = './examples/data/trellis-config-of-example5.json'
# ソースファイル（JSON形式）
file_path_of_contents_doc = './examples/data/battle_sequence_of_unfair_cointoss.step5_auto_split_by_pillar.json'
file_path_of_contents_doc_3 = './temp/examples/data_step5_battle_sequence_of_unfair_cointoss.step5_auto_split_by_pillar_done.json'
file_path_of_contents_doc_2 = './temp/examples/data_step5_battle_sequence_of_unfair_cointoss.step4_auto_shadow_done.json'
# 出力ファイル（JSON形式）
file_path_of_output = './temp/examples/step5_auto_split_pillar.xlsx'

print(f"""example 5: auto split pillar\
    {file_path_of_config_doc=}
    {file_path_of_contents_doc=}
    {file_path_of_contents_doc_3=}
    {file_path_of_contents_doc_2=}
    {file_path_of_output=}
""")

# ソースファイル（JSON形式）を読込
with open(file_path_of_contents_doc, encoding='utf-8') as f:
    contents_doc = json.load(f)


# ドキュメントに対して、自動ピラー分割の編集を行います
AutoSplitPillar.edit_document(contents_doc)
with open(file_path_of_contents_doc_3, mode='w', encoding='utf-8') as f:
    f.write(json.dumps(contents_doc, indent=4, ensure_ascii=False))

with open(file_path_of_contents_doc_3, mode='r', encoding='utf-8') as f:
    contents_doc = json.load(f)


# ドキュメントに対して、影の自動設定の編集を行います
AutoShadowSolver.edit_document(contents_doc)
with open(file_path_of_contents_doc_2, mode='w', encoding='utf-8') as f:
    f.write(json.dumps(contents_doc, indent=4, ensure_ascii=False))

with open(file_path_of_contents_doc_2, mode='r', encoding='utf-8') as f:
    contents_doc = json.load(f)


# ワークブックを新規生成
wb = xl.Workbook()

# ワークシート
ws = wb['Sheet']

# ワークシートへの描画
tr.render_to_worksheet(ws, contents_doc)

# ワークブックの保存            
wb.save(file_path_of_output)
