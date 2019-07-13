#!/usr/bin/env python
# coding: utf-8

# In[1]:


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'second.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from playsound import playsound
from PyQt5 import QtCore, QtGui, QtWidgets
import speech_recognition as sr
from face_adding import Ui_MainWindow


import os
import numpy as np
import pandas as pd
from scipy.spatial.distance import cdist, euclidean, cosine
from glob import glob

import pyaudio
from model import vggvox_model
from wav_reader import get_fft_spectrum
import constants as c

import wave, struct, math, random
import csv
import csv as cv


class Ui_NextWindow(object):
  
    def build_buckets(self,max_sec, step_sec, frame_step):
        buckets = {}
        frames_per_sec = int(1/frame_step)
        end_frame = int(max_sec*frames_per_sec)
        step_frame = int(step_sec*frames_per_sec)
        for i in range(0, end_frame+1, step_frame):
            s = i
            s = np.floor((s-7+2)/2) + 1  # conv1
            s = np.floor((s-3)/2) + 1  # mpool1
            s = np.floor((s-5+2)/2) + 1  # conv2
            s = np.floor((s-3)/2) + 1  # mpool2
            s = np.floor((s-3+2)/1) + 1  # conv3
            s = np.floor((s-3+2)/1) + 1  # conv4
            s = np.floor((s-3+2)/1) + 1  # conv5
            s = np.floor((s-3)/2) + 1  # mpool5
            s = np.floor((s-1)/1) + 1  # fc6
            if s > 0:
                buckets[i] = int(s)
        return buckets


    # def get_embedding(model, wav_file, max_sec):
    # 	buckets = build_buckets(max_sec, c.BUCKET_STEP, c.FRAME_STEP)
    # 	signal = get_fft_spectrum(wav_file, buckets)
    # 	embedding = np.squeeze(model.predict(signal.reshape(1,*signal.shape,1)))
    # 	return embedding


    # def get_embedding_batch(model, wav_files, max_sec):
    # 	return [ get_embedding(model, wav_file, max_sec) for wav_file in wav_files ]


    def get_embeddings_from_list_file(self,model, list_file, max_sec):
        buckets = self.build_buckets(max_sec, c.BUCKET_STEP, c.FRAME_STEP)
        result = pd.read_csv(list_file, delimiter=",")
        result['features'] = result['filename'].apply(lambda x: get_fft_spectrum(x, buckets))
        result['embedding'] = result['features'].apply(lambda x: np.squeeze(model.predict(x.reshape(1,*x.shape,1))))
        return result[['filename','speaker','embedding']]


    def get_id_result(self):
        print("Loading model weights from [{}]....".format(c.WEIGHTS_FILE))
        model = vggvox_model()
        model.load_weights(c.WEIGHTS_FILE)
        model.summary()

        print("Processing enroll samples....")
        enroll_result = self.get_embeddings_from_list_file(model, c.ENROLL_LIST_FILE, c.MAX_SEC)
        enroll_embs = np.array([emb.tolist() for emb in enroll_result['embedding']])
        speakers = enroll_result['speaker']

        print("Processing test samples....")
        test_result = self.get_embeddings_from_list_file(model, c.TEST_LIST_FILE, c.MAX_SEC)
        test_embs = np.array([emb.tolist() for emb in test_result['embedding']])

        print("Comparing test samples against enroll samples....")
        distances = pd.DataFrame(cdist(test_embs, enroll_embs, metric=c.COST_METRIC), columns=speakers)

        scores = pd.read_csv(c.TEST_LIST_FILE, delimiter=",",header=0,names=['test_file','test_speaker'])
        scores = pd.concat([scores, distances],axis=1)
        scores['result'] = scores[speakers].idxmin(axis=1)
        scores['correct'] = (scores['result'] == scores['test_speaker'])*1. # bool to int

        print("Writing outputs to [{}]....".format(c.RESULT_FILE))
        result_dir = os.path.dirname(c.RESULT_FILE)
        if not os.path.exists(result_dir):
            os.makedirs(result_dir)
        with open(c.RESULT_FILE, 'w') as f:
            scores.to_csv(f, index=False)

    def record_vioce(self):


        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 2
        RATE = 44100
        RECORD_SECONDS = 5
        WAVE_OUTPUT_FILENAME = "data/wav/test/output.wav"

        p = pyaudio.PyAudio()

        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

        print("* recording")

        frames = []

        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)

        print("* done recording")

        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
        password=self.lineEdit.text()
        ##saving path to csv file
        row = ['data/wav/test/output.wav', password]
        with open('cfg/test_List.csv', 'a') as csvFile:
            writer = csv.writer(csvFile)
            print("??????????????????????????????????????????????????????????????????????")
            print(row)
            writer.writerow(row)
        csvFile.close()

        print("done")


    def final_result(self):
        with open('res/results.csv','r',encoding='UTF-8') as F0:
            Reader=cv.reader(F0,delimiter=',')
            Rows=list(Reader)
            Tot_rows=len(Rows)
            counter=8

        with open('res/results.csv','r',encoding='UTF-8') as F1: 
            Read=cv.reader(F1,delimiter=',')
            for i in Read:
                ncol=len(next(Read))

            print(i[6])
            return (i[6])
            
    
    
    
    def speak(self):
        playsound('sounds/beep-3.wav')
        self.record_vioce()
       
        self.get_id_result()
    
        x=self.final_result()
        print("the end....................")
        print(x)
        print(self.lineEdit.text())
        y=self.lineEdit.text()
        if (y=="9968" or y=="10130" or y=="9723") and (x=="1.0"):
            self.label.setText("welcome")
            if(self.lineEdit.text()=="9968"):
                name="heba"
                playsound('sounds/hiba.mp3')
            if(self.lineEdit.text()=="9911"):
                name="jana"
                playsound('sounds/jana.mp3')
            if(self.lineEdit.text()=="10130"):
                name="rima"
                playsound('sounds/rima.mp3')
        
            self.window=QtWidgets.QMainWindow()
            self.ui=Ui_MainWindow()
            self.ui.setupUi(self.window)
            self.window.show()
   #         self.window2=QtWidgets.QMainWindow()
    #        self.ui2=Ui_NextWindow()
     #       self.ui2.setupUi(self.window2)

        else:
            self.label.setText("try again!")
            self.lineEdit.setText("")
        
        
    def setupUi(self, NextWindow):
        NextWindow.setObjectName("NextWindow")
        NextWindow.resize(1200, 600)
        NextWindow.setStyleSheet("background: url(images/ems3.png)")
        self.centralwidget = QtWidgets.QWidget(NextWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(860, 300, 41, 31))
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/mic.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(50, 50))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.speak)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(766, 430, 241, 26))
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Wide Latin")
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(177, 19, 4)")
        self.label.setText("")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(830, 360, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(830, 340, 47, 13))
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_2.setStyleSheet("color: rgb(212, 59, 28)")
        self.label_2.setText("your id:")
        self.label_2.setObjectName("label_2")
        NextWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(NextWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 21))
        self.menubar.setObjectName("menubar")
        NextWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(NextWindow)
        self.statusbar.setObjectName("statusbar")
        NextWindow.setStatusBar(self.statusbar)

        self.retranslateUi(NextWindow)
        QtCore.QMetaObject.connectSlotsByName(NextWindow)

    def retranslateUi(self, NextWindow):
        _translate = QtCore.QCoreApplication.translate
        NextWindow.setWindowTitle(_translate("NextWindow", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NextWindow = QtWidgets.QMainWindow()
    ui = Ui_NextWindow()
    ui.setupUi(NextWindow)
    NextWindow.show()
    sys.exit(app.exec_())


# In[ ]:





# In[ ]:




