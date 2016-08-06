# -*- coding: UTF-8 -*-
from __future__ import division
import time
import os
import gensim
import pickle

def save_obj(obj, name):
	filename = 'resource/'+ name + '.pkl'
	dir = os.path.dirname(filename)
	if not os.path.exists(dir):
		os.makedirs(dir)
	
	with open(filename, 'wb') as f:
		pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name ):
	with open('resource/' + name + '.pkl', 'rb') as f:
		return pickle.load(f)

def save_wordcnt(wordcnt_dict, name):
	save_obj(wordcnt_dict, name)

def load_wordcnt(name):
	return load_obj(name)

#_w2v_model = gensim.models.Word2Vec.load('./mymodel/word2vec_model/w2v_model20160806_194219')

D = {}
with open('./resource/result.txt', 'r') as train_data:
	t1 = time.time()
	cnt = 0
	for line in train_data:		
		#print line
		#print type(line)
		
		words = line.split()
		#print words

		for word in words:
			cnt = cnt + 1
			print cnt
			word = word.decode('utf8')
			#print word
			#print type(word)
			#print _w2v_model[word.decode('utf8')]

			if word in D:
				D[word] = D[word]+1
			else:
				D[word] = 1

	for key, value in D.iteritems():
		D[key] = value/cnt
		save_wordcnt(D, 'wordcnt')
	
	t2 = time.time()
	print "time: %f milliseconds" % ((t2 - t1) * 1000.)

D_read = load_wordcnt('wordcnt')
print D_read