#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

li = load_iris()

x_train, x_test, y_train, y_test = train_test_split(li.data, li.target, test_size=0.25)

print('Training set: ', x_train, y_train)
print('Test set: ', x_test, y_test)
