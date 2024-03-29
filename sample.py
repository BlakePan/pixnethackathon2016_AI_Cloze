# -*- coding: UTF-8 -*-
'''
question format from pixnet
https://github.com/pixnet/2016-pixnet-hackathon-crossword/blob/master/example/question.example

{"answer": "b", 
"choices": {"a": "工法", "b": "南灣", "c": "妝效", "d": "禪風", "e": "茄子"},
"index": 8, 
"question": "因為我們前一天去︽⊙＿⊙︽玩水..一堆水上摩扥車在海上呼嘯而過很危險阿...."}

data format for mymodel:
dictionary with choices and question,
replace "︽⊙＿⊙︽" with "",
and remove marks.

for example
{"choices": {"a": "工法", "b": "南灣", "c": "妝效", "d": "禪風", "e": "茄子"}, 
"question": ["因為", "我們", "前一天", "去", "", "玩水", "一堆", "水上摩扥車", "在", "海上", "呼嘯而過", "很危險", "阿"]}
'''
import bsddb3
import gensim
from mymodel import mymodel_mk1, mymodel_mk2
from mymodel.RNNmodel.utils import load_data, load_model_parameters_theano, generate_sentences
from mymodel.RNNmodel.gru_theano import *

# Load word2vec model
_w2v_model = gensim.models.Word2Vec.load('./mymodel/word2vec_model/w2v_model20160806_194219')

# Load word association database
freq_db = bsddb3.btopen('resource/wordcnt.db', 'r')
keywd_db = bsddb3.btopen('resource/keyword2.db', 'r')

Q1 = {"choices": {"a": "工法", "b": "南灣", "c": "妝效", "d": "禪風", "e": "茄子"}, 
"question": ["因為", "我們", "前一天", "去", "", "玩水", "一堆", "水上摩扥車", "在", "海上", "呼嘯而過", "很危險", "阿"]}

Q2 = {"choices": {"a1": "水潤", "a2": "面膜", "b": "明樺", "c": "淨膚儀", "d": "刷哥", "e": "眼影"}, 
"question": ["你", "也", "知道", "我", "把", "所有", "的", "精力", "都", "花", "在", "", "上", "了", "再來", "就", "迅速", "的", "隨便", "介紹", "一下", "保養新品"]}

A1 = mymodel_mk1.solve(Q1, _w2v_model)
A2 = mymodel_mk2.solve(Q1, freq_db, keywd_db)

print A1
print A2