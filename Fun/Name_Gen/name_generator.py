from __future__ import absolute_import, division, print_function, unicode_literals
try:
  get_ipython().run_line_magic('tensorflow_version', '2.x')
except Exception:
  pass
import random, math, csv, re, time, os
import tensorflow as tf
import numpy as np
EPOCHS=50
BATCH_SIZE = 64
BUFFER_SIZE = 10000

source = open("namesrc.txt").read()
source_set = sorted(set(source))
char2idx = {u:i for i, u in enumerate(source_set)}
idx2char = np.array(source_set)
text_as_int = np.array([char2idx[c] for c in source])


seq_length = 2
char_dataset = tf.data.Dataset.from_tensor_slices(text_as_int)
for i in char_dataset.take(5):
    print(idx2char[i.numpy()])

seq = char_dataset.batch(seq_length + 1, drop_remainder = True)
for item in seq.take(5):
    print(repr(''.join(idx2char[item.numpy()])))

def split_input_target(chunk):
    input_text = chunk[:-1]
    target_text = chunk[1:]
    return input_text, target_text

dataset = seq.map(split_input_target)

for input_example, target_example in  dataset.take(1):
  print ('Input data: ', repr(''.join(idx2char[input_example.numpy()])))
  print ('Target data:', repr(''.join(idx2char[target_example.numpy()])))

for i, (input_idx, target_idx) in enumerate(zip(input_example[:5], target_example[:5])):
    print("Step {:4d}".format(i))
    print("  input: {} ({:s})".format(input_idx, repr(idx2char[input_idx])))
    print("  expected output: {} ({:s})".format(target_idx, repr(idx2char[target_idx])))

dataset = dataset.shuffle(BUFFER_SIZE).batch(BATCH_SIZE, drop_remainder=True)
set_size = len(source_set)
embedding_dim = 256
rnn_units = 1024
def build_model(set_size, embedding_dim, rnn_units, batch_size):
  model = tf.keras.Sequential([
    tf.keras.layers.Embedding(set_size, embedding_dim,
                              batch_input_shape=[batch_size, None]),
    tf.keras.layers.GRU(rnn_units,
                        return_sequences=True,
                        stateful=True,
                        recurrent_initializer='glorot_uniform'),
    tf.keras.layers.Dense(set_size)
  ])
  return model
model = build_model(
  set_size = len(source_set),
  embedding_dim=embedding_dim,
  rnn_units=rnn_units,
  batch_size=BATCH_SIZE)
for input_example_batch, target_example_batch in dataset.take(1):
  example_batch_predictions = model(input_example_batch)
  print(example_batch_predictions.shape, "# (batch_size, sequence_length, set_size)")
model.summary()
sampled_indices = tf.random.categorical(example_batch_predictions[0], num_samples=1)
sampled_indices = tf.squeeze(sampled_indices,axis=-1).numpy()
def loss(labels, logits):
  return tf.keras.losses.sparse_categorical_crossentropy(labels, logits, from_logits=True)

example_batch_loss  = loss(target_example_batch, example_batch_predictions)
print("Prediction shape: ", example_batch_predictions.shape, " # (batch_size, sequence_length, vocab_size)")
print("scalar_loss:      ", example_batch_loss.numpy().mean())

model.compile(optimizer='adam', loss=loss)
checkpoint_dir = './training_checkpoints'
checkpoint_prefix = os.path.join(checkpoint_dir, "ckpt_{epoch}")

checkpoint_callback=tf.keras.callbacks.ModelCheckpoint(
    filepath=checkpoint_prefix,
    save_weights_only=True)

history = model.fit(dataset, epochs=EPOCHS, callbacks=[checkpoint_callback])

tf.train.latest_checkpoint(checkpoint_dir)

model = build_model(set_size, embedding_dim, rnn_units, batch_size=1)

model.load_weights(tf.train.latest_checkpoint(checkpoint_dir))

model.build(tf.TensorShape([1, None]))

model.summary()

def generate_text(model, start_string):
  num_generate = 1000
  input_eval = [char2idx[s] for s in start_string]
  input_eval = tf.expand_dims(input_eval, 0)

  text_generated = []

  temperature = 3.0

  model.reset_states()
  for i in range(num_generate):
      predictions = model(input_eval)

      predictions = tf.squeeze(predictions, 0)
      predictions = predictions / temperature
      predicted_id = tf.random.categorical(predictions, num_samples=1)[-1,0].numpy()

      input_eval = tf.expand_dims([predicted_id], 0)
      text_generated.append(idx2char[predicted_id])

  return (start_string + ''.join(text_generated))

name_arr = generate_text(model, start_string=u"卓")
name_arr = name_arr.replace(" ","")
interval = re.compile('.{2}')
lastname = ' '.join(interval.findall(name_arr))
lastname = lastname.split()

surname = open("surnamesrc.txt").read()
surname = surname.split()
p = [math.exp(- x * (4 / 97)) for x in range(1, len(surname))]
row = random.random()
surname_set = []
for j in range(len(name_arr)):
    for i in range(len(surname) - 1):
        if p[i] <= row:
            surname_set.append(surname[i])
            row = random.random()
            break

n = min(len(surname), len(lastname))
print("result: " + str(n) + " names generated")

name = []
for i in range(n):
    name.append(surname[i] + lastname[i])
print(name)
