# -*- coding: utf-8 -*-
"""EmoRecogModel.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1C5dze_gZisFiH0gJfWhHm5QsWOSU80bQ
"""

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D,MaxPooling2D,Flatten,Dense,Dropout

model=Sequential()
model.add(Conv2D(filters=32,kernel_size=(5,5),activation='relu',input_shape=(32,32,1)))
model.add(MaxPooling2D(2,2))
model.add(Conv2D(filters=64,kernel_size=(5,5),activation='relu'))
model.add(MaxPooling2D(2,2))
model.add(Flatten())
model.add(Dense(256,activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(7,activation='softmax'))
print(model.summary())

model.compile(optimizer='adam',loss='catagorical_crossentropy',metrics=['acc'])

class myCallback (tf.keras.callbacks.Callback):
    def steps_per_epoch(self, epoch, logs = {}):
        if logs['acc'] > 0.95 :
            print('\nAccuracy reached 95%')
            self.model.stop_training = True

callbacks = myCallback()
history = model.fit_generator(train_generator, epochs = 20,validation_data=validation_generator, callbacks = [callbacks] )

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
acc=history.history['acc']
val_acc=history.history['val_acc']
loss=history.history['loss']
val_loss=history.history['val_loss']
epochs=range(len(acc)) 
plt.plot(epochs, acc, 'r', "Training Accuracy")
plt.plot(epochs, val_acc, 'b', "Validation Accuracy")
plt.title('Training and Validation Accuracy')
plt.grid()
plt.legend()
plt.figure()
plt.plot(epochs, loss, 'r', "Training Loss")
plt.plot(epochs, val_loss, 'b', "Validation Loss")
plt.title('Training and Validation Loss')
plt.grid()
plt.legend()
