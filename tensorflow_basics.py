# -*- coding: utf-8 -*-
"""Tensorflow.ipnyb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/gist/ashaycclub/66c6fe76e23509522d849999a38cf78a/tensorflow.ipynb
"""

# constant in tensorflow

import tensorflow as tf

a=tf.constant(2)
b=tf.constant(3)
c=tf.add (a,b)
print(c)   # does not print as it defines the graph

with tf.Session() as sess:
    res=sess.run(c)
    print(res)

# variables in tensorflow

a=tf.constant(3)
b=tf.Variable(0)
c=tf.add(a,b)
d=tf.assign(b,c)

# intialize all variable
var=tf.initialize_all_variables()
with tf.Session() as sess:
    sess.run(var)                                   # initialize variable
    for i in range (3):
            sess.run(d)                             # run operation
            print(sess.run(b))                      # run for the variable

# Placeholders

x=tf.placeholder('float32',shape=[None,None])
y=x+3

with tf.Session() as sess:
    print(sess.run(y,feed_dict={x:[[2,3,4],[4,5,56]]}))

# Tensorflow version    
import tensorflow as tf
tf.VERSION

# Tensorboard Visualization

import tensorflow as tf
import math

with tf.name_scope("main"):
    a=tf.add(1,3,name="addition_1")
    b=tf.math.divide(2,4,name="division_1")
    with tf.name_scope("part1"):
        c=tf.multiply(2,4,name="multiply_1")
        d=tf.add(3,6,name="addition2")

with tf.Session() as sess:
    writer=tf.summary.FileWriter("./logs",sess.graph)
    print(sess.run(d))
    writer.close()

"""download the event file from log directory

got to saved event directory using cmd

run tensorboard --logdir = logs

file is hosted on a server link

copy paste the link to get the graph visualization
"""
