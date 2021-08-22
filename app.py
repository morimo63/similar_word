import re
import sys
import MeCab
import gensim

# 類語非表示 #
remove = ["EOS","。","、","，","．"]

# 事前処理 #
file = open('output.txt', 'w')
wv = gensim.models.KeyedVectors.load_word2vec_format("jawiki.all_vectors.300d.txt", binary=False)

# 文章入力 #
print("input: ", end="")
sentense = input()
file.write(sentense+"\n")
mecab = MeCab.Tagger('')
# mecab-ipadic-neologdを利用したら専門用語でエラー発生
# mecab = MeCab.Tagger("-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")
parse = mecab.parse(sentense)

# 文字数 #
print("word count:",len(sentense))
file.write("----\nword count:"+str(len(sentense))+"\n")

# 助詞を除く #
words = []
lines = parse.split('\n')
# print(lines)
for line in lines:
    # print(line)
    items = re.split('[\t,]',line)
    if len(items) >= 2 and "助詞" in items[4]: #2以下(eosなど) && 助詞を除く
        continue
    words.append(items[0])

# 類似度の高い単語を上位10個表示する #
for word in words:
    if len(word) != 0 and word not in remove:
        print("\n"+word)
        file.write("\n"+word+"\n")
        results = wv.most_similar(word,topn=10)
        for result in results:
            print("{:.03f}".format(round(result[1],3)),result[0])
            file.write("{:.03f}".format(round(result[1],3))+" "+result[0]+"\n")

file.close()