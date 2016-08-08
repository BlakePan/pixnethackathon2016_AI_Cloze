# -*- coding: UTF-8 -*-
#import bsddb3

#freq_db = bsddb3.btopen('resource/wordcnt.db', 'r')
#keywd_db = bsddb3.btopen('resource/keyword_test.db', 'r')

import numpy as np

def log_enable():
	#logging setting
	import logging
	if not os.path.exists('./log'):
		os.makedirs('./log')

	file_name =  os.path.basename(sys.argv[0])
	timestr = time.strftime("%Y%m%d_%H%M%S")

	log_file = "./log/"+file_name+"_"+timestr+".log"
	log_level = logging.DEBUG
	logger = logging.getLogger(file_name)
	handler = logging.FileHandler(log_file, mode='w')
	formatter = logging.Formatter("[%(levelname)s][%(funcName)s]\
	[%(asctime)s]%(message)s")
	handler.setFormatter(formatter)
	logger.addHandler(handler)
	logger.setLevel(log_level)

	return logger

def solve(Q, freq_db, keywd_db, logger=False):
	if logger:
		_logger = log_enable()

	question = Q['question']	
	choices = Q['choices']
	blank_index = question.index('')
	if len(question) is 0 or len(choices) is 0:
		return None

	score = {}
	for key, choice in choices.iteritems():
		score[key] = 0
		choice_utf8 = choice.decode('utf8')

		keyword_set = keywd_db[choice].split()
		for word in question:			
			if word in keyword_set and word is not '':
				#score[key] = score[key] + 1
				score[key] = score[key]+1-float(freq_db[word])

	# calculate softmax
	_max = score[max(score, key=score.get)]
	_sum = np.exp([x-_max for x in list(score.values())]).sum()
	for key, value in score.iteritems():
		score[key] = np.exp(value - _max)/_sum

	return score