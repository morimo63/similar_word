# similar_word
類似単語の提示するCLIアプリケーション

## モチベーション
企業に提出するESや、学会に提出する論文を書く時に、文字数や別の表現方法を調べていた。  
しかし、単語ごとに調べることが手間となったり、最初に思いついた単語から離れられずに表現の幅が狭くなってしまう。  
そこで、入力された単語の類似度が高い単語を提示するアプリケーションのプログラムの作成をした。

## 読み込みする分散表現
東北大学の日本語版Wikipediaをコーパスに用いて訓練した単語の分散表現[1]を使用する。
今回は300次元の分散表現を読み込む。

## 利用する技術
- Gensim[2]  
自然言語処理でよく用いられる様々なトピックモデルを実装したPythonライブラリ。
- MeCab[3]  
オープンソースの形態素解析エンジン。

## アプリの流れ
1. 事前処理として分散表現を読み込む。
2. 文章を入力しMeCabで形態素解析し、類似単語を提出する必要がない助詞を取り除く。
3. 助詞を除く単語の類似度が高い10単語をテキストファイル(output.txt)を出力する。

## デモ
- ESの「あなたの強みは？」に対しての答えを例として挙げる。入力する内容は、「私の強みは自ら定めた目標・課題に対して計画的かつ根気強く取り組める点です。」とする。
![demo1](https://user-images.githubusercontent.com/81407420/130355307-2bcb0034-ce5a-4df1-873e-903ce25913ed.png)

- そして、実行すると下図のようにテキストファイルで出力される。このファイルを参考に言い換えをしていく。
![demo2](https://user-images.githubusercontent.com/81407420/130355425-8f81046c-7ac2-4662-b97d-a80af79b0071.png)

## 参考サイト
[1] singletongue/WikiEntVec: Distributed representations of words and named entities trained on Wikipedia.(https://github.com/singletongue/WikiEntVec)  
[2] Gensim: Topic modelling for humans.(https://radimrehurek.com/gensim/)  
[3] MeCab: Yet Another Part-of-Speech and Morphological Analyzer(https://taku910.github.io/mecab/)  