# EMS — Embedded Manhunt System
<img src="images/ems.jpj" alt="EMS Logo" width="200" align="right"/>
> A multimodal AI identification system combining face recognition, voice recognition, and speech recognition, with a custom PyQt5 GUI and sound effects.

**Bachelor's Senior Project** — Heba Ibrahim · Jana Koteich · Rima Hasan

---

## Overview

EMS is a Python-based identification pipeline that authenticates users through three complementary modalities:

- **Face Recognition** — real-time identification via webcam using pretrained deep learning models
- **Voice Recognition** — speaker identification from audio input using VGGVox embeddings
- **Speech Recognition** — spoken command processing via Google Speech API
- **GUI** — a PyQt5 desktop interface with voice login, animated waveform display, and themed sound effects

User data (enrolled identities) is persisted in a local SQLite3 database.

---

## Architecture & Credits

This project builds on two open-source pretrained models:

| Component | Source |
|---|---|
| Voice / Speaker Recognition | [vggvox-speaker-identification](https://github.com/linhdvu14/vggvox-speaker-identification) |
| Face Recognition | [face_recognition (ageitgey)](https://github.com/ageitgey/face_recognition) |

---

## Requirements

- Python 3.7
- Windows with [Anaconda](https://www.anaconda.com/)

### Dependencies

**Face Recognition**
```
opencv-python
numpy
face_recognition
sqlite3  (standard library)
```

**Voice Recognition**
```
tensorflow
keras
gTTS
```

**Speech Recognition**
```
SpeechRecognition
PyAudio
```

**GUI & Utilities**
```
PyQt5
playsound
```

> **Note:** SQLite3 is included in Python's standard library but must be available in your environment.

---

## Installation

```bash
git clone https://github.com/Janakoteich/MachineLearning-EMS.git
cd MachineLearning-EMS
pip install opencv-python numpy face_recognition tensorflow keras gTTS SpeechRecognition PyAudio PyQt5 playsound
```

---

## Usage

### Run the application

```bash
python first.py
```

### Enroll new users (voice)

Edit the CSV config files to point to your local `.wav` files:

- `cfg/enroll_list.csv` — audio files for enrollment
- `cfg/test_list.csv` — audio files for evaluation/testing

### Customize GUI assets

Sound effects and images are in `sounds/` and `images/`. To replace them, swap the files and update the corresponding paths in the source code.

---

## Project Structure

```
MachineLearning-EMS/
├── cfg/                  # Enrollment and test configuration files
├── data/                 # Data directory
├── images/               # GUI image assets
├── sounds/               # GUI sound effects
├── first.py              # Entry point — launches the application
├── ems3.py               # Core EMS logic
├── model.py              # VGGVox model definition
├── face_adding.py        # Face enrollment utility
├── wav_reader.py         # Audio preprocessing
├── sigproc.py            # Signal processing utilities
├── constants.py          # Configuration constants
└── database2-1.db        # SQLite3 identity database
```

---

## Team

| Name | Role |
|---|---|
| Heba Ibrahim | Co-developer |
| Jana Koteich | Co-developer |
| Rima Hasan | Co-developer |

*Submitted as a Bachelor's senior project.*
