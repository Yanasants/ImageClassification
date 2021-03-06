# -*- coding: utf-8 -*-
"""MLP.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Waq6YbE_2uZ0Hs4bTG3ojVu55WTzli8J

#### Base: https://www.tensorflow.org/tutorials/keras/classification?hl=pt-br

### Importando bibliotecas
"""

# TensorFlow e tf.keras
import tensorflow as tf
from tensorflow import keras

# Bibliotecas Auxiliares
import numpy as np
import matplotlib.pyplot as plt

from sklearn.metrics import classification_report
import pandas as pd

print(tf.__version__)

"""### Importando base de dados"""

mnist = keras.datasets.mnist

"""#### Definindo dados para treinamento e teste"""

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

"""#### Definição das classes"""

class_names = ['0','1', '2', '3', '4', '5',
               '6', '7', '8', '9']

"""### Exploração dos dados"""

train_images.shape #60.000 imagens de tamanho 28x28

len(train_labels)

train_labels

test_images.shape #10.000 imagens de tamanho 28x28

len(test_labels)

"""### Pré-processamento de dados"""

#Exibindo a primeira imagem do conjunto de treinamento

plt.figure()
plt.imshow(train_images[0])
plt.colorbar()
plt.grid(False)
plt.show()

"""#### Escalaremos esses valores no intervalo de 0 e 1 antes de alimentar o modelo da rede neural. Para fazer isso, dividimos os valores por 255."""

train_images = train_images / 255.0
test_images = test_images / 255.0

plt.figure()
plt.imshow(train_images[0])
plt.colorbar()
plt.grid(False)
plt.show()

"""#### Para verificar que os dados estão no formato correto e que estamos prontos para construir e treinar a rede, vamos mostrar as primeiras 25 imagens do conjunto de treinamento e mostrar o nome das classes de cada imagem abaixo."""

plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[train_labels[i]])
plt.show()

"""### Construindo o modelo"""

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)), #array unidimensional (784)
    keras.layers.Dense(128, activation='relu'), #1a camada 128 neurônios
    keras.layers.Dense(10, activation='softmax') #array de 10 probabilidades
])

"""### Compilação do modelo

*   Função Loss —Essa mede quão precisa o modelo é durante o treinamento. Queremos minimizar a função para guiar o modelo para a direção certa.
*   Optimizer —Isso é como o modelo se atualiza com base no dado que ele vê e sua função loss.


*   Métricas —usadas para monitorar os passos de treinamento e teste. O exemplo abaixo usa a acurácia, a fração das imagens que foram classificadas corretamente.
"""

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics = 'accuracy')

"""#### Para que o modelo aprenda a associar as imagens às labels com dados de treinamento:"""

model.fit(train_images,train_labels, epochs=10)

"""### Verificação da acurácia"""

test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)

print('\nAcurácia:', test_acc)

"""### Predições de imagens"""

predictions_array = model.predict(test_images)
predictions_array[0]

np.argmax(predictions_array[0])

plt.figure()
plt.imshow(test_images[0])
plt.colorbar()
plt.grid(False)
plt.show()

predictions = np.argmax(predictions_array, axis=1)

print(classification_report(test_labels, predictions))

np.argmax(predictions[0])

"""#### Exibição gráfica das predições"""

def plot_image(i, predictions_array, true_label, img):
  predictions_array, true_label, img = predictions_array[i], true_label[i], img[i]
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])

  plt.imshow(img, cmap=plt.cm.binary)

  predicted_label = np.argmax(predictions_array)
  if predicted_label == true_label:
    color = 'blue'
  else:
    color = 'red'

  plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],
                                100*np.max(predictions_array),
                                class_names[true_label]),
                                color=color)

def plot_value_array(i, predictions_array, true_label):
  predictions_array, true_label = predictions_array[i], true_label[i]
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])
  thisplot = plt.bar(range(10), predictions_array, color="#777777")
  plt.ylim([0, 1])
  predicted_label = np.argmax(predictions_array)

  thisplot[predicted_label].set_color('red')
  thisplot[true_label].set_color('blue')

i = 0
plt.figure(figsize=(6,3))
plt.subplot(1,2,1)
plot_image(i, predictions, test_labels, test_images)
plt.subplot(1,2,2)
plot_value_array(i, predictions,  test_labels)
plt.show()

i = 12
plt.figure(figsize=(6,3))
plt.subplot(1,2,1)
plot_image(i, predictions, test_labels, test_images)
plt.subplot(1,2,2)
plot_value_array(i, predictions,  test_labels)
plt.show()

# Plota o primeiro X test images, e as labels preditas, e as labels verdadeiras.
# Colore as predições corretas de azul e as incorretas de vermelho.
num_rows = 5
num_cols = 3
num_images = num_rows*num_cols
plt.figure(figsize=(2*2*num_cols, 2*num_rows))
for i in range(num_images):
  plt.subplot(num_rows, 2*num_cols, 2*i+1)
  plot_image(i, predictions, test_labels, test_images)
  plt.subplot(num_rows, 2*num_cols, 2*i+2)
  plot_value_array(i, predictions, test_labels)
plt.show()

"""### Predição de uma única imagem"""

img = test_images[0]

print(img.shape)

"""#### Modelos tf.keras são otimizados para fazer predições em um batch, ou coleções, de exemplos de uma vez. De acordo, mesmo que usemos uma única imagem, precisamos adicionar em uma lista:"""

# Adiciona a imagem em um batch que possui um só membro.
img = (np.expand_dims(img,0))

print(img.shape)

predictions_single = model.predict(img)

print(predictions_single)

plot_value_array(0, predictions_single, test_labels)
_ = plt.xticks(range(10), class_names, rotation=45)

np.argmax(predictions_single[0])

