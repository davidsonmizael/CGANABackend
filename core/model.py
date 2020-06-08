import tensorflow as tf
import numpy as np
import json

class Model(object):

	def __init__(self, model_dir):
		self.model_dir = model_dir


	def predict(self, input_value):
		input_value = np.array(input_value)
		with tf.Session() as sess:
			saver = tf.train.import_meta_graph(self.model_dir + "/export.meta")
			saver.restore(sess, self.model_dir + "/export")
			input_vars = json.loads(tf.get_collection("inputs")[0].decode())
			output_vars = json.loads(tf.get_collection("outputs")[0].decode())
			input = tf.get_default_graph().get_tensor_by_name(input_vars["input"])
			output = tf.get_default_graph().get_tensor_by_name(output_vars["output"])
			return sess.run(output, feed_dict={input: np.expand_dims(input_value, axis=0)})[0]
