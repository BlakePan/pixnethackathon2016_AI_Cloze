# -*- coding: UTF-8 -*-
from __future__ import division
import time
import os
import gensim
import bsddb3

#_w2v_model = gensim.models.Word2Vec.load('./mymodel/word2vec_model/w2v_model20160806_194219')

db = bsddb3.btopen('resource/wordcnt.db', 'c')
cnt = 0

for file in os.listdir("resource/result"):
	if file.endswith(".txt"):
		print(file)
	else:
		continue
	
	with open('./resource/result/'+file, 'r') as train_data:
		
		for line in train_data:

			words = line.split()
			#if cnt > 10:
			#	break
			
			for word in words:
				cnt = cnt + 1
				#print cnt
				#word = word.decode('utf8')

				if word in db:
					db[word] = str(int(db[word])+1)
				else:
					db[word] = '1'

for key in db:
	db[key] = str(float(db[key])/cnt)

print db
