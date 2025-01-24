"""
白紙に柱の頭を追加
"""

import json

from src.trellis import trellis_in_src as tr


# 設定ファイル（JSON形式）
file_path_of_config_doc = './examples/data/trellis_config_of_example5.json'

print(f"""\
example 5: auto split pillar""")

# 設定ファイル（JSON形式）を読込
print(f"""\
    🔧　read {file_path_of_config_doc} file""")
with open(file_path_of_config_doc, encoding='utf-8') as f:
    config_doc = json.load(f)


# 設定ファイルを加工
config_doc['compiler']['objectFilePrefix'] = 'no5'


# ビルド
tr.build(
        config_doc=config_doc)
