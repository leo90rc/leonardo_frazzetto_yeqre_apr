import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np



def plot_cuadricula_perros_train(train_tf, batch_size):
    plt.figure(figsize=(12, 12))
    for images, labels in train_tf.take(1):
        a = (int(np.sqrt(batch_size)))**2
        for i in range(a):
            ax = plt.subplot(np.sqrt(a), np.sqrt(a), i + 1)
            plt.imshow(images[i].numpy().astype("uint8"))
            plt.title(train_tf.class_names[labels[i]])
            plt.axis("off");

