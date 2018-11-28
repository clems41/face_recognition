# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 16:44:33 2018

@author: cniot
"""

import tensorflow as tf
from tensorflow import keras

import numpy as np

print(tf.__version__)

train_data = np.load('x_train.npy')
train_labels = np.load('y_train.npy')
test_data = np.load('x_test.npy')
test_labels = np.load('y_test.npy')

print(train_data[0])
