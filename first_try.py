# import tensorflow as tf
#
# # Create a Constant op that produces a 1x2 matrix.  The op is
# # added as a node to the default graph.
# #
# # The value returned by the constructor represents the output
# # of the Constant op.
# matrix1 = tf.constant([[3., 3.]])
#
# # Create another Constant that produces a 2x1 matrix.
# matrix2 = tf.constant([[2.],[2.]])
#
# # Create a Matmul op that takes 'matrix1' and 'matrix2' as inputs.
# # The returned value, 'product', represents the result of the matrix
# # multiplication.
# product = tf.matmul(matrix1, matrix2)
#
# # or use sess.close() here to explicitly release resources.
# with tf.Session() as sess:
#   result = sess.run(product)
#   print(result)
###########################################################################
# import tensorflow as tf
#
# with tf.Session() as sess:
#   with tf.device("/cpu:0"):
#     matrix1 = tf.constant([[3., 3.]])
#     matrix2 = tf.constant([[2.],[2.]])
#     product = tf.matmul(matrix1, matrix2)
#     result = sess.run(product)
#     print(result)
###########################################################################
# import tensorflow as tf
# # Create a Variable, that will be initialized to the scalar value 0.
# state = tf.Variable(0, name="counter")
#
# # Create an Op to add one to `state`.
#
# one = tf.constant(1)
# new_value = tf.add(state, one)
# update = tf.assign(state, new_value)
#
# # Variables must be initialized by running an `init` Op after having
# # launched the graph.  We first have to add the `init` Op to the graph.
# init_op = tf.global_variables_initializer()
#
# # Launch the graph and run the ops.
# with tf.Session() as sess:
#   # Run the 'init' op
#   sess.run(init_op)
#   # Print the initial value of 'state'
#   print(sess.run(state))
#   # Run the op that updates 'state' and print 'state'.
#   for _ in range(3):
#     sess.run(update)
#     print(sess.run(state))
###########################################################################
# import tensorflow as tf
# input1 = tf.constant([3.0])
# input2 = tf.constant([2.0])
# input3 = tf.constant([5.0])
# intermed = tf.add(input2, input3)
# mul = tf.mul(input1, intermed)
#
# with tf.Session() as sess:
#   result = sess.run([mul, intermed])
#   print(result)
###########################################################################
import tensorflow as tf

input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)
output = tf.mul(input1, input2)

with tf.Session() as sess:
  print(sess.run([output], feed_dict={input1:[7.], input2:[2.]}))


