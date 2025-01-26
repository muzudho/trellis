# プログラミング・レッスン５：　トレリスの影描画

## 手順１

👇　以下の内容の 📄 `./temp/lesson/hello_world.json` ファイルを作ってください。  

```json
{
    "imports": [
        "./examples/data_of_contents/alias_for_color.json"
    ],
    "canvas": {
        "varBounds": {
            "left": 0,
            "top": 0,
            "width": 10,
            "height": 10
        }
    },
    "ruler": {
        "visible": true,
        "foreground": {
            "varColors": [
                "xlPale.xlGreen",
                "xlDeep.xlGreen"
            ]
        },
        "background": {
            "varColors": [
                "xlDeep.xlGreen",
                "xlPale.xlGreen"
            ]
        }
    },
    "rectangles" : [
        {
            "varBounds" : {
                "left": 2,
                "right": 4,
                "top": 2,
                "bottom": 8
            },
            "background": {
                "varColor": "xlPale.xlRed"
            }
        },
        {
            "varBounds" : {
                "left": 4,
                "right": 6,
                "top": 2,
                "bottom": 8
            },
            "background": {
                "varColor": "xlPale.xlGreen"
            }
        },
        {
            "varBounds" : {
                "left": 6,
                "right": 8,
                "top": 2,
                "bottom": 8
            },
            "background": {
                "varColor": "xlPale.xlBlue"
            }
        }
    ]
}
```

そして、以下のコマンドを打鍵してください。  

```shell
py trellis.py build --config ./trellis_config.json --source ./temp/lesson/hello_world.json --temp ./temp --output ./temp/lesson/hello_world.xlsx
```

![地面](../../img/[20250121-1158]shadow-0.png)  

👆　ひとまず、これを地面とします。  


## 手順２

👇　以下の内容の 📄 `./temp/lesson/hello_world.json` ファイルを作ってください。  

```json
{
    "imports": [
        "./examples/data_of_contents/alias_for_color.json"
    ],
    "canvas": {
        "varBounds": {
            "left": 0,
            "top": 0,
            "width": 10,
            "height": 10
        }
    },
    "ruler": {
        "visible": true,
        "foreground": {
            "varColors": [
                "xlPale.xlGreen",
                "xlDeep.xlGreen"
            ]
        },
        "background": {
            "varColors": [
                "xlDeep.xlGreen",
                "xlPale.xlGreen"
            ]
        }
    },
    "rectangles" : [
        {
            "varBounds" : {
                "left": 2,
                "right": 4,
                "top": 2,
                "bottom": 8
            },
            "background": {
                "varColor": "xlPale.xlRed"
            }
        },
        {
            "varBounds" : {
                "left": 4,
                "right": 6,
                "top": 2,
                "bottom": 8
            },
            "background": {
                "varcolor": "xlPale.xlGreen"
            }
        },
        {
            "varBounds" : {
                "left": 6,
                "right": 8,
                "top": 2,
                "bottom": 8
            },
            "background": {
                "varColor": "xlPale.xlBlue"
            }
        },
        {
            "varBounds" : {
                "left": 1,
                "right": 8,
                "top": 4,
                "bottom": 5
            },
            "background": {
                "varColor": "xlPale.xlYellow"
            }
        },
        {
            "varBounds" : {
                "left": 2,
                "right": 9,
                "top": 5,
                "bottom": 6
            },
            "background": {
                "varColor": "xlLight.xlWhite"
            }
        }
    ]
}
```

👆　rectangles に要素を２つ追加しました。  

そして、以下のコマンドを打鍵してください。  

```shell
py trellis.py build --config ./trellis_config.json --source ./temp/lesson/hello_world.json --temp ./temp --output ./temp/lesson/hello_world.xlsx
```

![ドロップシャドウ１](../../img/[20250121-1207]shadow-1.png)  

👆　横長の長方形を黄色で塗りつぶし、その右下に横長の長方形をグレーで塗りつぶしました。  
トレリスではこれをドロップシャドウと呼びます。  


## 手順３

👇　以下の内容の 📄 `./temp/lesson/hello_world.json` ファイルを作ってください。  

```json
{
    "imports": [
        "./examples/data_of_contents/alias_for_color.json"
    ],
    "canvas": {
        "varBounds": {
            "left": 0,
            "top": 0,
            "width": 10,
            "height": 10
        }
    },
    "ruler": {
        "visible": true,
        "foreground": {
            "varColors": [
                "xlPale.xlGreen",
                "xlDeep.xlGreen"
            ]
        },
        "background": {
            "varColors": [
                "xlDeep.xlGreen",
                "xlPale.xlGreen"
            ]
        }
    },
    "colorSystem": {
        "shadowColorMappings": {
            "varColorDict": {
                "paperColor": "xlPale.xlWhite",
                "xlPale.xlRed": "xlLight.xlRed",
                "xlPale.xlGreen": "xlLight.xlGreen",
                "xlPale.xlBlue": "xlLight.xlBlue"
            }
        }
    },
    "rectangles" : [
        {
            "varBounds" : {
                "left": 2,
                "right": 4,
                "top": 2,
                "bottom": 8
            },
            "background": {
                "varColor": "xlPale.xlRed"
            }
        },
        {
            "varBounds" : {
                "left": 4,
                "right": 6,
                "top": 2,
                "bottom": 8
            },
            "background": {
                "varColor": "xlPale.xlGreen"
            }
        },
        {
            "varBounds" : {
                "left": 6,
                "right": 8,
                "top": 2,
                "bottom": 8
            },
            "background": {
                "varColor": "xlPale.xlBlue"
            }
        },
        {
            "varBounds" : {
                "left": 1,
                "right": 8,
                "top": 4,
                "bottom": 5
            },
            "background": {
                "varColor": "xlPale.xlYellow"
            }
        },
        {
            "varBounds" : {
                "left": 2,
                "right": 9,
                "top": 5,
                "bottom": 6
            },
            "background": {
                "varColor": {
                    "darkness": 1
                }
            }
        }
    ]
}
```

👆　rectangles に要素を２つ追加しました。  

そして、以下のコマンドを打鍵してください。  

```shell
py trellis.py build --config ./trellis_config.json --source ./temp/lesson/hello_world.json --temp ./temp --output ./temp/lesson/hello_world.xlsx
```
