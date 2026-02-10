# Sonically Augmented Fountain (Arduino + FFT + MIDI)

## 📌 Project Overview

This project analyzes real-world sound (water fountain noise) and converts it into musical notes using frequency analysis.

The system records sound through a microphone, performs a Fast Fourier Transform (FFT) to detect dominant frequencies, and triggers MIDI notes that are played through a synthesizer.

The goal was to create an interactive soundscape where natural environmental sound becomes music.

---

## 🎯 Motivation

Urban environments often contain relaxing natural sounds like water fountains.
I wanted to explore whether natural sound could be transformed into music automatically using embedded systems and signal processing.

This project demonstrates how real-time audio signal processing can be implemented on low-cost hardware.

---

## ⚙️ How It Works

1. Microphone captures sound from a water fountain
2. Arduino samples the analog audio signal
3. FFT algorithm extracts the dominant frequency
4. Frequency is mapped to musical notes (pentatonic scale)
5. MIDI message is sent to a synthesizer
6. Speakers play the generated musical tone

---
## 🎬 Live Demonstration

Watch the project working in real time:

[https://www.youtube.com/watch?v=C2fHkNSJhOs](https://www.youtube.com/watch?v=C2fHkNSJhOs)

In this demo:

* The microphone captures the fountain sound
* Arduino performs FFT frequency detection
* Detected frequencies are mapped to musical notes
* MIDI messages trigger the synthesizer
* Speakers output generated musical tones


## 🧠 Technologies Used

* Arduino UNO R3
* C++ (Arduino)
* Fast Fourier Transform (arduinoFFT library)
* MIDI protocol
* SynthEdit synthesizer
* Signal processing concepts
* Electronics prototyping (breadboard circuits)

---

## 🖥️ Hardware Components

* Arduino UNO
* MAX9814 microphone module
* Breadboard & resistors
* MIDI interface
* Speakers

---

## 🚀 Installation & Usage

### 1. Requirements

* Arduino IDE
* arduinoFFT library
* MIDI synthesizer (software or hardware)

### 2. Upload Code

1. Connect Arduino to PC
2. Open the `.ino` file in Arduino IDE
3. Select correct COM port
4. Upload the sketch

### 3. Run

* Play water sound (or any sound)
* The system will detect frequencies
* MIDI notes will be generated automatically

---

## 📊 Example Result

When water sound is detected, the Arduino identifies dominant frequencies and triggers musical notes such as A3, C4, D4, E4, G4, and A4.

---

## 📚 What I Learned

* Embedded programming
* Real-time signal processing
* FFT frequency analysis
* MIDI communication
* Debugging hardware/software interaction

---

## 🔮 Future Improvements

* Better noise filtering
* LED light synchronization
* Machine learning note classification
* Multiple instrument modes

---

## 👩‍💻 Author

Agata Gabara

