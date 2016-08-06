import gensim
import time

#sentences = gensim.models.word2vec.Text8Corpus('./resource/text8')
sentences = gensim.models.word2vec.Text8Corpus('./resource/result.txt')
model = gensim.models.Word2Vec(sentences, size=128, window=5, min_count=5, workers=10)

timestr = time.strftime("%Y%m%d_%H%M%S")
model.save('./mymodel/word2vec_model/w2v_model' + timestr)