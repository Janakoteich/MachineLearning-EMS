#!/usr/bin/env python
# coding: utf-8

# In[1]:


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'face_adding.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import sqlite3
import numpy as np
import io
import face_recognition
import speech_recognition as sr
from playsound import playsound


   


class Ui_MainWindow(object):
        
    image_name=""
    face_name=""
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        MainWindow.setStyleSheet("background: url(images/emmss.png)")
        list1=[]
        con = sqlite3.connect("database2-1.db")
        cur = con.cursor()
        result=cur.execute("""select * from code""")
        for j in result:
            list1.append(j[1])

        cur.close()
        con.close()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 240, 131, 121))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(170, 170, 91, 31))
        self.pushButton.setStyleSheet("background: rgb(255, 255, 255); selection-background-color: rgb(233, 99, 0);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/download.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(25, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 10, 121, 23))
        self.pushButton_2.setStyleSheet("background: rgb(255, 255, 255); selection-background-color: rgb(233, 99, 0);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/video512x512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(520, 340, 113, 20))
        self.lineEdit.setStyleSheet("background: rgb(255, 255, 255); selection-background-color: rgb(233, 99, 0);")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(460, 90, 41, 31))
        self.pushButton_3.setStyleSheet("")
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/15.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(460, 170, 41, 31))
        self.pushButton_4.setStyleSheet("")
        self.pushButton_4.setText("")
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(460, 250, 41, 31))
        self.pushButton_5.setStyleSheet("")
        self.pushButton_5.setText("")
        self.pushButton_5.setIcon(icon2)
        self.pushButton_5.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(460, 330, 41, 31))
        self.pushButton_6.setStyleSheet("")
        self.pushButton_6.setText("")
        self.pushButton_6.setIcon(icon2)
        self.pushButton_6.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_6.setObjectName("pushButton_6")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(520, 100, 113, 20))
        self.lineEdit_2.setStyleSheet("background: rgb(255, 255, 255); selection-background-color: rgb(233, 99, 0);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(520, 180, 113, 20))
        self.lineEdit_3.setStyleSheet("background: rgb(255, 255, 255); selection-background-color: rgb(233, 99, 0);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(520, 260, 113, 20))
        self.lineEdit_4.setStyleSheet("background: rgb(255, 255, 255); selection-background-color: rgb(233, 99, 0);")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(730, 190, 51, 51))
        self.pushButton_7.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/images.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon3)
        self.pushButton_7.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_7.setObjectName("pushButton_7")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(260, 460, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(360, 460, 101, 23))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/trash.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon4)
        self.pushButton_8.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_8.setObjectName("pushButton_8")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(520, 80, 47, 13))
        self.label.setObjectName("label")
        self.label.setText("name")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(520, 160, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_2.setText("age")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(520, 240, 47, 13))
        self.label_4.setObjectName("label_4")
        self.label_4.setText("crime")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(530, 320, 47, 13))
        self.label_5.setObjectName("label_5")
        self.label_5.setText("address")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.comboBox.clear()
        self.comboBox.addItems(list1)
        self.pushButton_2.clicked.connect(self.printt)
        self.pushButton.clicked.connect(self.setImage)
        self.pushButton_3.clicked.connect(self.speak11)
        self.pushButton_4.clicked.connect(self.speak2)
        self.pushButton_5.clicked.connect(self.speak3)
        self.pushButton_6.clicked.connect(self.speak4)
        self.pushButton_7.clicked.connect(self.okay)
        self.pushButton_8.clicked.connect(self.delete_criminal)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Add Image"))
        self.pushButton_2.setText(_translate("MainWindow", "go to video stream"))
        self.pushButton_8.setText(_translate("MainWindow", "delete criminal"))

        

    def setImage(self):
        
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "", "Images Files(*.png *.jpg *.jpeg *.bmp)")
        if filename:
            pixmap = QtGui.QPixmap(filename)
            pixmap=pixmap.scaled(self.label_3.width(), self.label_3.height(), QtCore.Qt.KeepAspectRatio)
            self.label_3.setPixmap(pixmap)
            self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        Ui_MainWindow.image_name=filename
        
    def speak11(self):
        
        r=sr.Recognizer()
        with sr.Microphone() as source:
            playsound('sounds/beep-3.wav')
            r.adjust_for_ambient_noise(source)
            audio=r.listen(source)
            try:
                text=r.recognize_google(audio)
                self.lineEdit_2.setText('{}'.format(text))
            except:
                self.lineEdit_2.setText('sorry')      
    def speak2(self):
        
        r=sr.Recognizer()
        with sr.Microphone() as source:
            playsound('sounds/beep-3.wav')
            r.adjust_for_ambient_noise(source)
            audio=r.listen(source)
            try:
                text=r.recognize_google(audio)
                self.lineEdit_3.setText('{}'.format(text))
            except:
                self.lineEdit_3.setText('sorry')
    def speak3(self):
        
        r=sr.Recognizer()
        with sr.Microphone() as source:
            playsound('sounds/beep-3.wav')
            r.adjust_for_ambient_noise(source)
            audio=r.listen(source)
            try:
                text=r.recognize_google(audio)
                self.lineEdit_4.setText('{}'.format(text))
            except:
                self.lineEdit_4.setText('sorry')
    def speak4(self):
        
        r=sr.Recognizer()
        with sr.Microphone() as source:
            playsound('sounds/beep-3.wav')
            r.adjust_for_ambient_noise(source)
            audio=r.listen(source)
            try:
                text=r.recognize_google(audio)
                self.lineEdit.setText('{}'.format(text))
            except:
                self.lineEdit.setText('sorry')
    def okay(self):
        playsound('sounds/beep-6.wav')
        # Converts np.array to TEXT when inserting
        sqlite3.register_adapter(np.ndarray, self.adapt_array)

        # Converts TEXT to np.array when selecting
        sqlite3.register_converter("array", self.convert_array)
   
        con = sqlite3.connect("database2-1.db", detect_types=sqlite3.PARSE_DECLTYPES)
        
        cur = con.cursor()
        #cur.execute("""create table code (name TEXT,image array)""")
        
        address=self.lineEdit.text()
        name=self.lineEdit_2.text()
        crime=self.lineEdit_4.text()
        age=self.lineEdit_3.text()
        if Ui_MainWindow.image_name!="" and name!="" and address!="" and crime!="" and age!="":
        
            biden_image = face_recognition.load_image_file(Ui_MainWindow.image_name)
            biden_face_encoding = face_recognition.face_encodings(biden_image)[0]
        
            cur.execute("insert into code (full_name,image,crime,address,age) values (?,?,?,?,?)", (name,biden_face_encoding,crime,address,age, ))
            con.commit()
        
        cur.close()
        con.close()
        
                
    def delete_criminal(self):
        criminal_name = str(self.comboBox.currentText())
        con = sqlite3.connect("database2-1.db")
        cur = con.cursor()
        cur.execute("""delete from code where full_name=?""",(criminal_name,))
        con.commit()

        cur.close()
        con.close()
    
    
    
    def adapt_array(self,arr):
        """
        http://stackoverflow.com/a/31312102/190597 (SoulNibbler)
        """
        out = io.BytesIO()
        np.save(out, arr)
        out.seek(0)
        return sqlite3.Binary(out.read())

    def convert_array(self,text):
        out = io.BytesIO(text)
        out.seek(0)
        return np.load(out)
    
    
    def printt(self):
        playsound('sounds/beep-3.wav')
        
        # Converts np.array to TEXT when inserting
        sqlite3.register_adapter(np.ndarray, self.adapt_array)

        # Converts TEXT to np.array when selecting
        sqlite3.register_converter("array", self.convert_array)
   
        con = sqlite3.connect("database2-1.db", detect_types=sqlite3.PARSE_DECLTYPES)
        
        cur = con.cursor()
  #      cur.execute("""create table code (name TEXT,image array)""")
        
        
        known_face_encodings=[]
        known_face_names=[]
        age=[]
        address=[]
        crime=[]
        
        result=cur.execute("""select * from code""")
        for j in result:
            print (j[1])
            print(j[0])
            print(j[2])
            print(j[3])
            print(j[4])
            known_face_encodings.append(j[0])
            known_face_names.append(j[1])
            age.append(j[2])
            crime.append(j[3])
            address.append(j[4])
            
        cur.close()
        con.close()
        
        
        
        video_capture = cv2.VideoCapture(0)

        # Initialize some variables
        face_locations = []
        face_encodings = []
        face_names = []
        process_this_frame = True

        while True:
            # Grab a single frame of video
            ret, frame = video_capture.read()

            # Resize frame of video to 1/4 size for faster face recognition processing
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

            # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
            rgb_small_frame = small_frame[:, :, ::-1]

            # Only process every other frame of video to save time
            if process_this_frame:
                # Find all the faces and face encodings in the current frame of video
                face_locations = face_recognition.face_locations(rgb_small_frame)
                face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

                face_names = []
                for face_encoding in face_encodings:
                    # See if the face is a match for the known face(s)
                    matches = face_recognition.compare_faces(known_face_encodings, face_encoding,0.5556)
                    name="Unknown"
                    y=True
                   # x=matches.index(True)
                    #print(x)
                 #   for i in range(matches):
                  #      print(i)
                   #     print(matches[i])
                    #    if matches[i] == True:
                     #       name=known_face_names[i]
                      #      criminal_age=age[i]
                       #     criminal_crime=crime[i]
                        #    criminal_address=address[i]
        
                    # If a match was found in known_face_encodings, just use the first one.
                    if y in matches:
                            first_match_index = matches.index(True)
                            name = known_face_names[first_match_index]
                            criminal_age=age[first_match_index]
                            criminal_crime=crime[first_match_index]
                            criminal_address=address[first_match_index]
                    # Or instead, use the known face with the smallest distance to the new face
                   
                #    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                 #   best_match_index = np.argmin(face_distances)
                  #  if matches[best_match_index]:
                   #     name = known_face_names[best_match_index]
                    #    criminal_age=age[best_match_index]
                     #   criminal_crime=crime[best_match_index]
                      #  criminal_address=address[best_match_index]
                        
              #      else:
                        
               #          name="Unknown"
                        
                    face_names.append(name)

            process_this_frame = not process_this_frame


            # Display the results
            for (top, right, bottom, left), name in zip(face_locations, face_names):
                # Scale back up face locations since the frame we detected in was scaled to 1q/4 size
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                font = cv2.FONT_HERSHEY_DUPLEX
                
                # Draw a box around the face
               
                if name=="Unknown":
                    cv2.rectangle(frame, (left, top), (right, bottom), (255, 0, 0), 2)
                else:
                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                # Draw a label with a name below the face
                if name=="Unknown":
                    cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (255, 0, 0), cv2.FILLED)
                    #playsound('beep-8.wav')
                else:
                    cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                    cv2.line(frame,(right, top),(right + 60 ,top - 60),(0,0,255),2)
                    cv2.line(frame,(right, bottom),(right + 60 ,bottom + 60),(0,0,255),2)
                    
                    
                    cv2.rectangle(frame, (right + 60, top - 60), (right + 300, bottom + 60), (0, 0, 255), 2)
                    cv2.putText(frame, "age: "+str(criminal_age), (right + 70, top + 20), font, 0.5, (0, 0, 0), 1)
                    cv2.putText(frame, "address: "+criminal_address, (right + 70, bottom - 60), font, 0.5, (0, 0, 0), 1)
                    cv2.putText(frame, "crime: "+criminal_crime, (right + 70, bottom + 10),font, 0.5, (0, 0, 0), 1)
                    
                cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)    
               # playsound('beep-8.wav')
            # Display the resulting image
            cv2.imshow('Video', frame)

            # Hit 'q' on the keyboard to quit!
            if cv2.waitKey(1) & 0xFF == ord('q'):
                
                self.lineEdit.setText("")
                self.lineEdit_2.setText("")
                self.lineEdit_3.setText("")
                self.lineEdit_4.setText("")
                break
                

        # Release handle to the webcam
        video_capture.release()
        cv2.destroyAllWindows()



if __name__ == "__main__":
    import sys
    
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


    



