# FakerRealText

## FakerPHPのRealTextっぽいことをpythonで実装する

### 銀河鉄道の夜を青空文庫からダウンロードする

- [こちら](https://www.aozora.gr.jp/cards/000081/card456.html)からテキストファイル(ルビあり)をダウンロード

### 特殊文字の削除と分かち書きを行う

```
$ python makeTxtData.py
```
- こちらのコードを実行するとルビの削除やMeCabによる分かち書きを行ったファイル(dataset.txt)が生成できます。