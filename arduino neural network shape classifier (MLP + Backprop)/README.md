# 🤖 Arduino Neural Network (Embedded Machine Learning Project)

![Arduino](https://img.shields.io/badge/Platform-Arduino-blue)
![C++](https://img.shields.io/badge/Language-C++-informational)
![Machine Learning](https://img.shields.io/badge/Field-Machine%20Learning-red)
![Neural Network](https://img.shields.io/badge/Type-Feedforward%20Neural%20Network-orange)
![Embedded Systems](https://img.shields.io/badge/Area-Embedded%20AI-green)

---

## Project Overview

This project implements a **feed-forward artificial neural network with backpropagation** directly on an Arduino microcontroller.

Unlike typical machine learning projects that use high-level frameworks (TensorFlow, PyTorch), this neural network is written from scratch in embedded C++ and trained directly on the device.

The network learns to recognize input patterns (binary sensor signals) and classify them into predefined categories.

This project demonstrates understanding of:

* neural network fundamentals
* training algorithms
* embedded systems programming
* edge AI concepts

---
---

## 🎥 Project Demonstration (Video)

Click the image below to watch the project working on real hardware:

[![Watch the demo](https://img.youtube.com/vi/i8t6EIOz1OY/0.jpg)](https://www.youtube.com/watch?v=i8t6EIOz1OY)

This video demonstrates:

* neural network training on Arduino
* live sensor input reading
* classification output in Serial Monitor
* real-time prediction after training

The neural network is trained directly on the microcontroller and then used to classify input signals from digital pins.


## Neural Network Architecture

The neural network has three layers:

* **Input layer:** 16 neurons
* **Hidden layer:** 6 neurons
* **Output layer:** 4 neurons

Training parameters:

* Learning rate: 0.3
* Momentum: 0.9
* Activation function: Sigmoid
* Training method: Backpropagation

The network trains until the error drops below a predefined threshold.

---

## How It Works

### 1. Training Phase

The Arduino initializes random weights and trains the neural network using predefined training patterns.

The training data consists of binary input patterns representing different shapes or signal combinations.

During training the algorithm:

1. Performs forward propagation
2. Calculates error
3. Backpropagates gradients
4. Updates weights

Training progress and error values are printed to the Serial Monitor.

---

### 2. Inference Phase (Prediction)

After training:

* The Arduino reads 16 digital inputs (pins)
* The neural network processes the inputs
* The output layer produces classification probabilities

The predicted output is displayed in the Serial Monitor.

---

## Hardware Requirements

* Arduino board (Uno / Nano / Mega)
* 16 digital input signals (e.g., switches, buttons, sensors)
* USB connection to PC
* Arduino IDE

Digital pins are used as binary input features for the neural network.

---

## Installation & Usage

### 1. Upload the Program

1. Open Arduino IDE
2. Connect Arduino board
3. Open file:

```
arduino-neural-network.ino
```

4. Select correct board and port
5. Click **Upload**

---

### 2. Run the Network

1. Open **Serial Monitor**
2. Set baud rate to:

```
9600
```

The Arduino will:

* train the neural network
* display training error
* then classify live input signals

---

## Skills Demonstrated

* Neural network implementation from scratch
* Backpropagation algorithm
* Gradient-based optimization
* Embedded C++ programming
* Serial communication
* Working with digital input signals
* Edge AI concepts (machine learning on microcontrollers)

---

## What I Learned

Through this project I learned:

* how neural networks actually work internally
* how backpropagation updates weights
* numerical stability considerations
* implementing ML without libraries
* integrating machine learning with hardware

---

## Why This Project Matters

Most machine learning projects rely on pre-built frameworks.
This project demonstrates a deeper understanding of machine learning fundamentals by implementing the algorithm manually on a microcontroller.

It shows the ability to combine:
**Artificial Intelligence + Embedded Systems + Programming**

---

## Author

**Agata Gabara**
IT Graduate | Data Analyst | Aspiring Bioinformatician | Machine Learning Enthusiast

GitHub: [https://github.com/ag48665](https://github.com/ag48665)
