#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import requests
import pyunpack
import shutil


data_url = 'http://zhen-wang.appspot.com/rice/files/uwave/uWaveGestureLibrary.zip'
data_dir = './data'


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

        if os.path.isdir(root.split(' ')[0]):
            # print(root.split(' ')[0])
            shutil.move(root, root.split(' ')[0])
        else:
            os.mkdir(root.split(' ')[0])
            shutil.move(root, root.split(' ')[0])

    list_dir = os.listdir(data_dir)
    dest = os.path.join(data_dir,'uWaveGestureLibrary')
    for sub_dir in list_dir:
        dir_to_move = os.path.join(data_dir, sub_dir)
        shutil.move(dir_to_move, dest)

    dest = os.path.join(data_dir,'uWaveGestureLibrary/U6')
    for root, dirs, files in os.walk(os.path.join(data_dir,'uWaveGestureLibrary')):
        if root.startswith('./data/uWaveGestureLibrary/U6'):
            shutil.move(root, dest)

def get_data(data_url,data_dir):
    download_data(data_url,data_dir)
    unzip_data(data_dir)
    format_data(data_dir)

# get_data(data_url, data_dir)
