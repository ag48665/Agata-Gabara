# Sonically Augmented Fountain 🎶💧

### Fast Fourier Transform (FFT) based interactive sound system using Arduino

## Overview

This project presents a prototype system that augments the natural sound of water fountains by analysing their acoustic signal and generating musical notes in real time.

The system captures fountain sounds using a microphone, performs frequency analysis with a Fast Fourier Transform (FFT), identifies dominant frequencies, maps them to musical notes (pentatonic scale), and triggers a MIDI synthesizer to produce harmonically matched sounds.

The goal is to create a relaxing and natural “wind-chime like” soundscape that enhances public environments such as parks or urban spaces.

---

## How It Works

1. A microphone records water sounds.
2. Arduino samples the audio signal.
3. FFT is applied to extract frequency components.
4. The dominant frequency (peak) is detected.
5. Frequency is mapped to a musical note.
6. A MIDI message is sent to a synthesizer.
7. The synthesizer produces the corresponding musical tone.

The generated sound follows the natural rhythm of water flow, creating an adaptive ambient music system.

---
## Project Demonstration

The system working in real conditions can be seen in the video below:

[![Arduino Neural Network Demo](https://img.youtube.com/vi/C2fHkNSJhOs/0.jpg)](https://www.youtube.com/watch?v=C2fHkNSJhOs)

The video presents the trained neural network running on Arduino UNO and classifying patterns based on real-time input signals from the digital pins.
After the training phase finishes, the microcontroller reads a 4x4 binary input grid and produces a prediction using the trained weights.

This demonstrates that the neural network is not only simulated but actually deployed on embedded hardware and performs inference in real time.


## Hardware Requirements

* Arduino UNO R3
* MAX9814 microphone (with automatic gain control)
* GY-MAX4466 microphone (optional alternative)
* Breadboard and jumper wires
* Resistors
* MIDI connection
* External speakers (Yamaha speakers used in prototype)
* Computer or smartphone for sound playback/testing

---

## Software Requirements

* Arduino IDE
* `arduinoFFT` library
* `SoftwareSerialTX` library
* SynthEdit (software synthesizer)
* Windows 10 (development environment)

---

## Signal Processing

The system uses a **Fast Fourier Transform (FFT)** to convert the recorded time-domain audio signal into the frequency domain.

FFT allows detection of dominant frequencies contained in the fountain sound. Each detected peak frequency corresponds to a musical pitch.

Example mapping (Pentatonic Scale):

| Frequency (Hz) | Musical Note |
| -------------- | ------------ |
| ~222 Hz        | A3           |
| ~266 Hz        | C4           |
| ~298 Hz        | D4           |
| ~334 Hz        | E4           |
| ~398 Hz        | G4           |
| ~447 Hz        | A4           |

After detection, the Arduino sends a MIDI Note On / Note Off message to the synthesizer.

---

## MIDI Communication

A MIDI message consists of:

* Command byte
* Note number
* Velocity (volume)

Example:

```
noteOn(0x90, 60, 0x45);
```

This triggers a musical note in the synthesizer.

---

## Audio Effects

To improve sound quality, audio effects were added:

* Reverb Zita
* Reverb DH

These effects make the synthesized tone more natural and similar to wind chimes.

---

## System Architecture

Microphone → Arduino ADC → FFT → Frequency Detection → MIDI → Synthesizer → Speakers

---

## Challenges

* Harmonics causing incorrect frequency detection
* Microphone quality affecting measurements
* Conflict between `SoftwareSerial` and `arduinoFFT` libraries
* Environmental noise (air conditioning, room acoustics)
* Limited memory of Arduino UNO

---

## Results

The system successfully:

* Detected dominant frequencies of water sounds
* Generated musical notes in real time
* Produced a relaxing ambient soundscape
* Demonstrated feasibility of interactive musical fountains

External speakers significantly improved sound quality and echo perception.

---

## Future Improvements

* Spectrum analyzer visualization
* Dynamic note scaling
* Outdoor fountain deployment
* LED/DMX lighting synchronization
* Advanced DSP filtering
* Higher-performance microcontroller (e.g., Teensy or ESP32)

---

## Applications

* Public parks
* Smart cities
* Interactive installations
* Relaxation environments
* Soundscape therapy
* Museum or art exhibitions

---

## Author

**Agata Gabara**
BSc Project — Middlesex University
2022

---

## License

This project is for educational and research purposes.


---

## How to Run / Upload Code to Arduino 🔧

Follow these steps to compile and upload the project to your Arduino UNO.

### 1. Install Arduino IDE

1. Download Arduino IDE: [https://www.arduino.cc/en/software](https://www.arduino.cc/en/software)
2. Install using default settings.
3. Connect your Arduino UNO via USB.
4. Open Arduino IDE.

---

### 2. Install Required Libraries

Open **Arduino IDE → Sketch → Include Library → Manage Libraries…**

Install:

* `arduinoFFT` (by kosme / Enrique Condes)
* `SoftwareSerialTX` (used instead of SoftwareSerial due to conflict with FFT)

After installation restart the Arduino IDE.

---

### 3. Connect Hardware

#### Microphone (MAX9814)

| MAX9814 Pin | Arduino UNO Pin |
| ----------- | --------------- |
| VDD         | 5V              |
| GND         | GND             |
| OUT         | A0              |

#### MIDI Connection

| Component              | Arduino Pin   |
| ---------------------- | ------------- |
| MIDI TX (via resistor) | Digital Pin 2 |

Use a **220Ω resistor** between the Arduino TX pin and the MIDI connector.

---

### 4. Configure Arduino IDE

In Arduino IDE:

1. Tools → Board → **Arduino Uno**
2. Tools → Port → Select your COM port
3. Tools → Processor → ATmega328P

---

### 5. Upload the Code

1. Open the `.ino` project file.
2. Click **Verify (✓)** to compile.
3. If compilation succeeds, click **Upload (→)**.
4. Wait for:
   `Done uploading.`

---

### 6. Test Serial Output

Open:

**Tools → Serial Monitor**

Set:

* Baud rate: **115200**

You should see detected frequency peaks:

```
peak = 298.2
peak = 334.0
peak = 266.1
```

This means FFT detection works correctly.

---

### 7. Connect MIDI Synthesizer

1. Start SynthEdit (or any MIDI synthesizer software).
2. Select Arduino as MIDI input device.
3. Connect:
   MIDI IN → Synth → Speakers

When water sound (or recorded fountain sound) is played into the microphone, musical notes should be generated automatically.

---

### 8. Test Audio

Play a fountain sound near the microphone
(example: water stream, tap water, or fountain recording).

Expected result:

* Arduino detects dominant frequency
* MIDI note is triggered
* Synthesizer produces musical tone

You should hear a soft ambient “wind-chime” style sound.

---

## Troubleshooting

**No sound**

* Check MIDI connection
* Verify synthesizer input device
* Confirm speakers output device

**Random notes**

* Reduce environmental noise
* Move microphone closer to sound source

**Compilation error**

* Make sure `arduinoFFT` is installed
* Ensure `SoftwareSerialTX` is installed (NOT SoftwareSerial)

**Unstable detection**

* Use external speakers instead of phone speaker
* Disable air conditioning / background noise
* Check microphone power (5V)

---

Now your interactive musical fountain system should be fully operational 🎶💧

---

## Project Skills Demonstrated 🧠

This project demonstrates practical, hands-on engineering and programming skills rather than only theoretical knowledge.

### Embedded Systems

* Programming microcontrollers (Arduino UNO / ATmega328P)
* Working with analog sensors and ADC sampling
* Real-time signal processing on constrained hardware
* Memory and performance optimisation for low-resource devices
* Hardware debugging and electrical wiring (breadboard prototyping)

### Signal Processing / DSP

* Audio signal acquisition
* Fast Fourier Transform (FFT) implementation
* Frequency-domain analysis
* Peak frequency detection
* Mapping frequencies to musical notes (pitch detection)
* Handling harmonics and signal noise

### Programming

* C/C++ for embedded systems
* Serial communication
* MIDI protocol message generation
* Library integration and debugging
* Working with hardware interrupts and timing

### Audio & Communication Protocols

* MIDI Note On / Note Off messages
* Serial communication (31250 baud MIDI rate)
* Analog audio capture
* Real-time audio triggering

### Software & Tools

* Arduino IDE
* SynthEdit audio synthesizer
* Serial Monitor debugging
* Library conflict troubleshooting
* Hardware/software integration testing

### Problem Solving & Engineering

* Diagnosing library conflicts (`SoftwareSerial` vs `arduinoFFT`)
* Noise reduction and measurement reliability
* Calibration of sensors
* Experimental testing and iterative prototyping
* Working with real-world physical signals instead of simulated data

### Concepts Covered

* Embedded programming
* Digital Signal Processing (DSP)
* Real-time systems
* Human-computer interaction (interactive sound environment)
* Hardware/software co-design

---

This project simulates a real engineering workflow: prototype → test → debug → improve → deploy.
