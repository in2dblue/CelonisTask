# Requirements
Python V3.10
Install requirements.txt (pip install -r requirements.txt)

Run main.py for execution

- Logistic Regression algorithm developed in logreg.py
- File preprocessing done in utils/data_prep.py

# Details
The task is to implement the complete machine learning pipeline that classifies gestures by training a model that consumes time series data.

# Data
We use an existing dataset that contains gesture movement data recorded by an external system. The gestures have been recorded from uWave: Accelerometer-based personalized gesture recognition and its applications

In gestures. the dot denotes the start, and the arrow the end of the gesture. You can download the dataset as a zip-file using the following URL:
http://zhen-wang.appspot.com/rice/files/uwave/uWaveGestureLibrary.zip

If you download and unpack the data, you will get a couple of .rar files. The dataset is structured as follows:

On the top level, each .rar file includes the gesture samples collected from one user on one day. The .rar files are named as U$userIndex ($dayIndex).rar, where $userIndex is the index of the participant from 1 to 8, and $dayIndex is the index of the day from 1 to 7.

Inside each .rar file, there are .txt files recording the time series of acceleration of each gesture. The .txt files are named as [somePrefix]$gestureIndex-$repeatIndex.txt, where $gestureIndex is the index of the gesture as in the 8-gesture vocabulary, and $repeatIndex is the index of the repetition of the same gesture pattern from 1 to 10.

In each .txt file, the first column is the x-axis acceleration, the second y-axis acceleration, and the third z-axis acceleration. The unit of the acceleration data is G, or acceleration of gravity.

# Task

I implemented a machine learning pipeline, including data preparation, preprocessing, feature extraction, modeling, training, and evaluation to perform gesture detection for the given dataset. That is, given a time-series, classify it in one of the 8 classes.

The way I build mine machine learning pipeline:
1. Used Python and numpy for all aspects of the "data science workflow" data preprocessing / feature extraction / training / inference. (a few exceptions below).
2. Implemented and train a logistic regression model by hand (plain numpy).
4. Used libraries for visualizing the evaluation results or any kind of interesting insights you found during my data exploration phase.
