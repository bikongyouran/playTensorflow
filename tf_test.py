'''For using tensorflow, pay attention to the file name, which should not be same as "tensorflow.py"!!!'''
'''In windows, install anaconda3 for python3.5, and use "pip install tensorflow" to install tensorflow.
   configure the python3.5 as the python interpreter since currently tensorflow only supports python3 in windows.'''
import tensorflow as tf

hello = tf.constant('hello, tensorflow.')
sess = tf.Session()
print(sess.run(hello))
