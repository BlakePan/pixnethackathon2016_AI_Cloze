# -*- coding: UTF-8 -*-
from __future__ import division
import time
import os
import bsddb3

filename = 'resource/keyword3.db'
if os.path.exists(filename):
    os.remove(filename)

wordfreqdb = bsddb3.btopen('resource/wordcnt.db', 'r')
db = bsddb3.btopen(filename, 'c')
sentce_cnt = 0
word_cnt = 0
low_band = 1e-5
high_band = 2e-5
line_limit = 20

for file in os.listdir("resource/result"):
	if file.endswith(".txt"):
		print(file)
	else:
		continue
	
	#if cnt > 10:
	#	break

	t1 = time.time()
	sentce_cnt = 0
	word_cnt = 0
	with open('./resource/result/'+file, 'r') as train_data:
		
		for line in train_data:

			words = line.split()
			if len(words) < line_limit:
				continue

			
			# fine 1st and 2nd keyword in current line
			keywd_cand={}
			for word in words:
				word_freq = float(wordfreqdb[word])
				if word not in keywd_cand and word_freq > low_band and word_freq < high_band:
					keywd_cand[word] = word_freq
			
			if len(keywd_cand) < 2:
				continue

			sentce_cnt = sentce_cnt+1

			keyword_1st = min(keywd_cand, key=keywd_cand.get)
			del(keywd_cand[keyword_1st])
			keyword_2nd = min(keywd_cand, key=keywd_cand.get)

			# store into database
			for word in words:
				word_cnt = word_cnt+1
				if word not in db:
					db[word] = ''

				keyword_set = db[word]
				if keyword_1st not in keyword_set:
					keyword_set = keyword_set + keyword_1st + ' '
				if keyword_2nd not in keyword_set:
					keyword_set = keyword_set + keyword_2nd + ' '
				db[word] = keyword_set

	t2 = time.time()
	print "sentence: %d, word: %d" % (sentce_cnt, word_cnt)
	print "time: %f seconds" % (t2 - t1)

#print db	