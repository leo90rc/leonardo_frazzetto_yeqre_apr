import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import os



def plot_cuadricula_perros_train(train_tf, batch_size):
    plt.figure(figsize=(12, 12))
    for images, labels in train_tf.take(1):
        a = (int(np.sqrt(batch_size)))**2
        for i in range(a):
            ax = plt.subplot(np.sqrt(a), np.sqrt(a), i + 1)
            plt.imshow(images[i].numpy().astype("uint8"))
            plt.title(train_tf.class_names[labels[i]])
            plt.axis("off");


def accuracy_loss_plot(model_name, history, lim_sup1=1.1, lim_sup2=2.3, step_x = 2, step_y1 = 0.1, step_y2 = 0.25):
    acc_model = history.history['accuracy']
    val_acc_model = history.history['val_accuracy']

    loss_model = history.history['loss']
    val_loss_model = history.history['val_loss']

    epochs_range = range(1, len(history.history['loss']) + 1)

    plt.figure(figsize=(12, 8))
    plt.subplot(1, 2, 1)
    plt.plot(epochs_range, acc_model, label='Precisión Entrenamiento')
    plt.plot(epochs_range, val_acc_model, label='Precisión Validación')
    plt.legend(loc='upper left')
    plt.title('Precisión de entrenamiento y validación - ' + model_name)
    plt.xlabel("Época", size = 14)
    plt.xticks(np.arange(0, len(history.history['loss']) + 1, step_x))
    plt.ylabel("Precisión", size = 14)
    plt.yticks(np.arange(0, lim_sup1, step_y1))
    plt.ylim(0,lim_sup1)

    plt.subplot(1, 2, 2)
    plt.plot(epochs_range, loss_model, label='Pérdida Entrenamiento')
    plt.plot(epochs_range, val_loss_model, label='Pérdida Validación')
    plt.legend(loc='upper right')
    plt.title('Pérdida de entrenamiento y validación - ' + model_name)
    plt.xlabel("Época", size = 14)
    plt.xticks(np.arange(0, len(history.history['loss']) + 1, step_x))
    plt.ylabel("Pérdida", size = 14)
    plt.yticks(np.arange(0, lim_sup2, step_y2))
    plt.ylim(0,lim_sup2)
    plt.savefig('..' + os.sep + 'reports' + os.sep + model_name + '_accuracy_loss.png')
    plt.show()


def plot_cuadricula_rgb(train_imagenes, raza_list, train_labels):
    plt.figure(figsize=(15,15))
    for i in range(25):
        plt.subplot(5,5,i+1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(True)
        plt.imshow(train_imagenes[i])
        plt.xlabel(raza_list[train_labels[i]])
    plt.savefig('..' + os.sep + 'reports' + os.sep + 'cuadricula_rgb.png')
    plt.show();

def plot_cuadricula_gray(train_imagenes_gray, raza_list, train_labels):
    plt.figure(figsize=(15,15))
    for i in range(25):
        plt.subplot(5,5,i+1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(True)
        plt.imshow(train_imagenes_gray[i], cmap=plt.cm.binary)
        plt.xlabel(raza_list[train_labels[i]])
    plt.savefig('..' + os.sep + 'reports' + os.sep + 'cuadricula_gray.png')
    plt.show();