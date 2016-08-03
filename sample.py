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

import gensim
from mymodel import mymodel_mk1

_w2v_model = gensim.models.Word2Vec.load('./mymodel/word2vec_model/w2v_model20160803_120737')

#Q = {"choices": {"a": "工法", "b": "南灣", "c": "妝效", "d": "禪風", "e": "茄子"}, 
#"question": ["因為", "我們", "前一天", "去", "", "玩水", "一堆", "水上摩扥車", "在", "海上", "呼嘯而過", "很危險", "阿"]}

Q = {"choices": {"a": "milk", "b": "travel", "c": "england", "d": "hot", "e": "mac"}, 
"question": ["me", "like", "to", "drink", ""]}

A = mymodel_mk1.solve(Q, _w2v_model, logger=True)

print A