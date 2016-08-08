# -*- coding: UTF-8 -*-
import numpy as np
import theano as theano
import theano.tensor as T
import time
import operator
from utils import load_data, load_model_parameters_theano, generate_sentences
from gru_theano import *
import sys

# Load parameters of pre-trained model
model = load_model_parameters_theano('./data/GRU-2016-07-29dat.npz')