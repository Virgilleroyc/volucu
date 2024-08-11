import tensorflow as tf

def _int64_feature(value):
    return tf.cast(value, tf.float32)
