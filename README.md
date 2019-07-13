# MachineLearning-EMS-
Face Recognition-Speech Recognition-Voice Recognition

This project is based on pretrained models for voice recognition and face recognition
 1)https://github.com/linhdvu14/vggvox-speaker-identification
 2)https://github.com/ageitgey/face_recognition
 
Introduction:
This project is a combination of face recognition, voice recognition and speech recognition. In addition
of GUI that support them and sound effects

Installation:
Requirements:
 Python 3.7
 Windows (anaconda)
Installing on windows:
Make sure that all the following libraries are installed:
1. Face recognition libraries:
opencv,sqlite3,numpy ,face_recognition
2. Voice recognition:
Tensorflow, keras ,gTTs,
3. Speech recognition:
speech_recognition ,PyAudio

This project saves data in sqlite3 so make sure you install sqlite3
Also to add the effect of sounds install playsound
and don’t forget to install PyQt5 for the GUI.

Instructions:
To run evaluation run python first.py
Modify `cfg/enroll_list.csv` and `cfg/test_list.csv` to point to your local enroll/test wav files
Sounds and images files related to the gui, if you want to change them modify these files and don’t
forget to modify them in the code also
