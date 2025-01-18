# プログラミング・レッスン４：　トレリスのテキスト表示

## 手順１

👇　以下の内容の 📄 `./temp/lesson/hello_world.json` ファイルを作ってください。  

```json
{
    "canvas": {
        "bounds": {
            "left": 0,
            "top": 0,
            "width": 10,
            "height": 10
        }
    },
    "ruler": {
        "visible": true,
        "fgColor": [
            "xl_pale.xl_red",
            "xl_deep.xl_red"
        ],
        "bgColor": [
            "xl_deep.xl_red",
            "xl_pale.xl_red"
        ]
    },
    "rectangles" : [
        {
            "bounds" : {
                "left": 3,
                "top": 4,
                "width": 2,
                "height": 1
            },
            "bgColor": "paper_color",
            "mergeCells": true
        }
    ],
    "xl_texts": [
        {
            "location": {
                "x": 3,
                "y": 4
            },
            "text": "Hello, world!",
            "xl_alignment" : {
                "xl_horizontal" : "center",
                "xl_vertical" : "center"
            },
            "xl_font": {
                "color": "xl_strong.xl_red"
            }
        }
    ]
}
```

👆　`["xl_texts"]` の辺りを説明していきます。  
色は趣味で設定してください。  

そして、以下のコマンドを打鍵してください。  

```shell
py trellis.py compile --file ./temp/lesson/hello_world.json --temp ./temp --output ./temp/lesson/hello_world.xlsx
```

![テキスト描画](../../img/[20250119-0012]print-text4.png)  

👆　テキストを描画できた。  

`xl_horizontal` には `fill`, `left`, `distributed`, `justify`, `center`, `general`, `centerContinuous`, `right` が入れられるはず。  
`xl_vertical` には `distributed`, `justify`, `center`, `bottom`, `top` が入れられるはず。  
