#!/usr/bin/env python
# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path
from log_reg import LogisticRegression
from utils.data_prep import *
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

data_path = 'data/uWaveGestureLibrary/'
data_url = 'http://zhen-wang.appspot.com/rice/files/uwave/uWaveGestureLibrary.zip'
data_dir = './data'

def extract_gesture(directory):
    gesture = []
    pathlist = Path(directory).rglob('*.txt')
    
    for path in pathlist:
        file = open(path, "r")
        lines = file.readlines()[1:]
        file.close()
        x_array = []
        y_array = []
        z_array = []
        for line in lines:
            s = line.split()
            x_array.append(float(s[0]))
            y_array.append(float(s[1]))
            z_array.append(float(s[2]))
            
        gesture.append(np.concatenate(([x_array], [y_array], [z_array]), axis=0))
    return gesture


def create_dataset(gestures, shuffle=False):
    n_samples = 0
    n_features = 0
    for gesture in gestures:
        n_samples += len(gesture)
        for sample in gesture:
            if n_features < sample.shape[1]:
                n_features = sample.shape[1]
    X = np.zeros((n_samples, 3 * n_features))
    y = np.zeros(n_samples, dtype=int)
    i = 0
    for index, gesture in enumerate(gestures):
        for sample in gesture:
            X[i, :sample.shape[1]] = sample[0, :]
            X[i, n_features:n_features+sample.shape[1]] = sample[1, :]
            X[i, 2*n_features:2*n_features+sample.shape[1]] = sample[2, :]
            y[i] = int(index)
            i += 1
    if shuffle:
        p = np.random.permutation(n_samples)
        X = X[p, :]
        y = y[p]
    return X, y


def main():
    # Feature extraction from the uWaveGesture dataset 
    print("Feature extraction started....")
    print("============================================================================")
    gesture_1 = extract_gesture(data_path + '/U1/')
    gesture_2 = extract_gesture(data_path + '/U2/')
    gesture_3 = extract_gesture(data_path + '/U3/')
    gesture_4 = extract_gesture(data_path + '/U4/')
    gesture_5 = extract_gesture(data_path + '/U5/')
    gesture_6 = extract_gesture(data_path + '/U6/')
    gesture_7 = extract_gesture(data_path + '/U7/')
    gesture_8 = extract_gesture(data_path + '/U8/')

    X, y = create_dataset([gesture_1, gesture_2, gesture_3, gesture_4, gesture_5, gesture_6, gesture_7, gesture_8], shuffle=True)
    print("Number of samples: " +  str (X.shape[0]))
    print("Number of features: " +  str (X.shape[1]))
    print("Number of classes: 8")

    # Splitting train test data in 70:30
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Build our logistic regression model. 
    lr = LogisticRegression(n_iter = 3000)  

    print("\nBuilding logistic regression model .....")
    print("============================================================================")
    lr.fit(X_train, y_train, batch_size=64, lr=0.001, verbose=True)
    print("Training finished!")
    lr.score(X_train, y_train)

    # Ploting model's training loss convergence with every iterations. 
    print("Saving training loss plot across iterations at image/training_loss.png.....")
    fig = plt.figure(figsize=(8,6))
    plt.plot(np.arange(len(lr.loss)), lr.loss)
    plt.title("Convergence of training loss")
    plt.xlabel("#Iterations")
    plt.ylabel("Loss")
    fig.savefig('image/training_loss.png', dpi=fig.dpi)

    print("\nEvaluating the trained model on test set ....")
    print("============================================================================")
    y_pred = lr.predict_classes(X_test) 
    accuracy_score(y_test, y_pred)

    cm = confusion_matrix(y_test, y_pred)
    print("Confusion matrix on the test set")
    print(cm)

    print("\n Classsificatin report on the test set")
    print(classification_report(y_test, y_pred))


if __name__ == "__main__":
    get_data(data_url, data_dir)
    main()