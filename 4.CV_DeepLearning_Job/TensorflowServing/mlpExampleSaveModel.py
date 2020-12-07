import tensorflow as tf
import numpy as np
from tensorflow import keras
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import RMSprop
batch_size = 50
num_classes = 3
epochs = 200

import pandas as pd
import os
iris=pd.read_csv("iris.csv")
#help(irist.drop)
iris.drop(['no'],1,inplace=True)
iris
# Shuffling
iriss=iris.sample(frac=1).reset_index(drop=True)
iris_train=iriss.iloc[0:100,:]
iris_test=iriss.iloc[100:150,:]

x_train=iris_train.iloc[:,0:4].values
x_test=iris_test.iloc[:,0:4].values
y_train=iris_train.iloc[:,4:5]
y_test= iris_test.iloc[:,4:5]
# encoder={k:v for v,k in enumerate(y_train.drop_duplicates())}
# encoder
sets=iris.iloc[:,4:5].drop_duplicates()["Species"].tolist()
encoder={k:v for v,k in enumerate(sets)}
y_train=[ encoder[i] for i in y_train["Species"].tolist() ]
y_train = keras.utils.to_categorical(y_train, num_classes)

y_test=[ encoder[i] for i in y_test["Species"].tolist() ]
y_test = keras.utils.to_categorical(y_test, num_classes)

model = Sequential()
model.add(Dense(4, activation='relu', input_shape=(4,)))
#model.add(Dropout(0.2))
model.add(Dense(5, activation='relu'))
#model.add(Dropout(0.2))
model.add(Dense(5, activation='relu'))
#model.add(Dropout(0.2))

model.add(Dense(num_classes, activation='softmax'))

model.summary()

model.compile(loss='categorical_crossentropy',
              optimizer=RMSprop(),
              metrics=['accuracy'])


history = model.fit(x_train, y_train,
                    batch_size=batch_size,
                    epochs=epochs,
                    verbose=1,
                    validation_data=(x_test, y_test))
score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

# Predict
#model.predict(x_test)


# Model Save
def make_directory(target_path):
  if not os.path.exists(target_path):
    os.mkdir(target_path)
    print('Directory ', target_path, ' Created ')
  else:
    print('Directory ', target_path, ' already exists')

SAVED_MODEL_PATH = '/tmp/saved_model'
make_directory(SAVED_MODEL_PATH)
MODEL_DIR = SAVED_MODEL_PATH

version = 1
export_path = os.path.join(MODEL_DIR, str(version))
print('export_path = {}\n'.format(export_path))

tf.keras.models.save_model(
  model,
  export_path,
  overwrite=True,
  include_optimizer=True,
  save_format=None,
  signatures=None,
  options=None
)
print('\nSaved model:')
