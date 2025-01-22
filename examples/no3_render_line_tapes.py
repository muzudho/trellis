"""
白紙に柱の頭を追加
"""

import json
import openpyxl as xl
from openpyxl.styles import PatternFill, Font
from src.trellis import trellis_in_src as tr


# 設定ファイル（JSON形式）
file_path_of_config_doc = './examples/data/trellis-config-of-example3.json'

print(f"""\
example 3: line tapes
    {file_path_of_config_doc=}""")

# 設定ファイル（JSON形式）を読込
with open(file_path_of_config_doc, encoding='utf-8') as f:
    config_doc = json.load(f)


# ソースファイル（JSON形式）
file_path_of_contents_doc = config_doc['compiler']['--source']
# 出力ファイル（JSON形式）
file_path_of_output = config_doc['compiler']['--output']

print(f"""\
    {file_path_of_contents_doc=}
    {file_path_of_output=}""")

# ソースファイル（JSON形式）を読込
with open(file_path_of_contents_doc, encoding='utf-8') as f:
    contents_doc = json.load(f)


# ワークブックを新規生成
wb = xl.Workbook()

# ワークシート
ws = wb['Sheet']

# ワークシートへの描画
tr.render_to_worksheet(ws, contents_doc)

# ワークブックの保存            
wb.save(file_path_of_output)
