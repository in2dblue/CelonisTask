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
data_dir = './data2'
letters = ['A', 'C', 'E', 'H', 'J', 'M', 'R', 'Z']

def download_data(data_url,data_dir):
    isExist = os.path.exists(data_dir)
    if not isExist:
        os.mkdir(data_dir)
    data_file = os.path.join(data_dir, 'uWaveGestureLibrary.zip')
    data = requests.get(data_url)
    with open(data_file, 'wb')as file:
        file.write(data.content)


def unzip_data(data_dir):
    arch = pyunpack.Archive(os.path.join(data_dir,'uWaveGestureLibrary.zip'))
    arch.extractall(directory=data_dir)
    os.remove(os.path.join(data_dir,'uWaveGestureLibrary.zip'))

    for root, dirs, files in os.walk(data_dir):
        for filename in files:
            if filename.endswith(".rar") :
                print('Extracting '+os.path.join(root,filename))
            else:
                print('Removing '+os.path.join(root,filename))
                os.remove(os.path.join(root,filename))
            if filename.endswith(".rar"):
                name = os.path.splitext(os.path.basename(filename))[0]
                try:
                    arch = pyunpack.Archive(os.path.join(root,filename))
                    item_dir = os.path.join(root,name)
                    os.mkdir(item_dir)
                    arch.extractall(directory=item_dir)
                    os.remove(os.path.join(root,filename))
                except Exception as e:
                    print("ERROR: BAD ARCHIVE "+os.path.join(root,filename))
                    print(e)   


def format_data(data_dir):
    for root, dirs, files in os.walk(data_dir):
        print(root)
        for filename in files:
            if filename.endswith('.txt') and 'Template_Acceleration' not in filename:
                print('Removing '+os.path.join(root,filename))
                os.remove(os.path.join(root,filename))


def load_data():
    print ("Loading dataset...")
    data, labels = [], []
    for us in range(1, 9):
        da, la = [], []
        for day in range(1, 8):
            for ges in range(1, 9):
                fx = data_dir + "/U" + str(us) + " (" + str(day) + ")/"
                fy = fx + letters[us-1] + "_Template_Acceleration" + str(ges) + "-"
                for ges_inst in range(1, 11):
                    fz = fy + str(ges_inst) + '.txt'
                    d = np.loadtxt(fz).reshape(-1, 3)
                    da.append(d)
                    la.append(ges)
        data.append(da)
        labels.append(la)
    data = np.array(data)
    labels = np.array(labels)
    
    return data, labels



def main():
    # download_data(data_url,data_dir)
    # unzip_data(data_dir)
    # format_data(data_dir)

            
    data_set, data_label = load_data()

    data_set = data_set.T
    data_labels = data_label.T

    print ("Dataset: ", data_set.shape)
    print ("Labels: ", data_labels.shape)

    Xtrain, Xtest, ytrain, ytest = train_test_split(data_set, data_labels, test_size=0.25, random_state=5125, stratify=data_labels)

    # data_sets = np.array(data_set[0]).reshape(1, -1)
    # data_sets = np.hstack((data_sets, data_set[1].reshape(1, -1)))
    # data_sets = np.hstack((data_sets, data_set[2][:224].reshape((1, -1))))
    # data_sets = np.hstack((data_sets, data_set[2][225:].reshape(1, -1)))
    # data_sets = np.hstack((data_sets, data_set[3:6].reshape(1, -1)))
    # data_sets = np.hstack((data_sets, data_set[6][:404].reshape(1, -1)))
    # data_sets = np.hstack((data_sets, data_set[6][405:].reshape(1, -1)))
    # data_sets = np.hstack((data_sets, data_set[7].reshape(1, -1)))
    # data_sets = data_sets.reshape(-1, 1)
    # print (data_sets.shape)

    # data_labels = np.array(data_label[0]).reshape(1, -1)
    # data_labels = np.hstack((data_labels, data_label[1].reshape(1, -1)))
    # data_labels = np.hstack((data_labels, data_label[2][:224].reshape((1, -1))))
    # data_labels = np.hstack((data_labels, data_label[2][225:].reshape(1, -1)))
    # data_labels = np.hstack((data_labels, data_label[3:6].reshape(1, -1)))
    # data_labels = np.hstack((data_labels, data_label[6][:404].reshape(1, -1)))
    # data_labels = np.hstack((data_labels, data_label[6][405:].reshape(1, -1)))
    # data_labels = np.hstack((data_labels, data_label[7].reshape(1, -1)))
    # data_labels = data_labels.reshape(-1, 1)
    # print (data_labels.shape)

if __name__ == "__main__":
    main()