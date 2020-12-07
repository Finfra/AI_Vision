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


from tensorflow.keras.callbacks import ModelCheckpoint
filename = f'/tmp/checkpoint-epoch-{epochs}-batch-{batch_size}-trial-001.h5'
checkpoint = ModelCheckpoint(filename,
                             monitor='val_loss',
                             verbose=1,
                             save_best_only=True,
                             mode='auto'
                            )



history = model.fit(x_train, y_train,
                    batch_size=batch_size,
                    epochs=epochs,
                    verbose=1,
                    validation_data=(x_test, y_test),
                    callbacks=[checkpoint]
)
