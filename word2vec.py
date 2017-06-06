from gensim.models import Word2Vec

sentences = []
with open("./contextcleaned_1", encoding="ISO-8859-1") as f:
    lines = f.readlines()

    for line in lines:

        sentence = line.split("\t")
        print(sentence)
        # print(sentence)
        words = sentence[2].split()
        sentences.append(words)

# print(sentences)
# # sentences = [["hello world"]]
# # train word2vec on the two sentences
model = Word2Vec(sentences, min_count=1)

model.wv.save_word2vec_format('./word2vec_1', binary=False)
