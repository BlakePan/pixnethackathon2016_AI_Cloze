# -*- coding: UTF-8 -*-
import sys
import os
import numpy as np
import time

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

def solve(Q, w2v_model, neighbor=1, logger=False):
	if logger:
		_logger = log_enable()

	ans = 'c' #default answer

	## word2vec
	question = Q['question']	
	choices = Q['choices']
	wordvec = []
	blank_index = question.index('')

	# convert word to vector nearby the blank
	for i in range(blank_index-neighbor, blank_index+neighbor+1):
		if i<0 or i>=len(question) or question[i]=='':
			continue

		wordvec.append(w2v_model[question[i]])

	# convert choices to vector
	for key, value in choices.iteritems():
		choices[key] = w2v_model[value]

	if logger:
		_logger.debug('wordvec')
		_logger.debug(wordvec)
		_logger.debug('choices')
		_logger.debug(choices)

	## calculate mean vector
	_mean = np.asarray(np.mean(wordvec, axis=0))
	if logger:
		_logger.debug('wordvec maen')		
		_logger.debug(_mean)

	## find who is the closest one to mean
	dis = []
	for key, value in choices.iteritems():
		choices[key] = np.linalg.norm(value-_mean)
		
	ans = min(choices, key=choices.get)

	if logger:
		_logger.debug('choices')
		_logger.debug(choices)

	return ans