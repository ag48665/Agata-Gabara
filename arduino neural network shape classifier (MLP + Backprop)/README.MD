# Arduino Neural Network Shape Classifier (MLP + Backpropagation)

## Overview

This project implements a feed-forward neural network (Multi-Layer Perceptron) written from scratch in Embedded C++ and running on an Arduino UNO.

The network is trained to recognize simple 4x4 binary patterns representing basic shapes.
After training, the Arduino reads real-time input from its digital pins and classifies the detected pattern.

> This project was created to understand how machine learning algorithms work internally without using external libraries such as TensorFlow or PyTorch.

## Project Demo (Video)

Watch the project in action here:
https://www.youtube.com/watch?v=i8t6EIOz1OY


## How the Neural Network Works

**Network architecture:**

* Input layer: 16 neurons (4x4 binary grid)
* Hidden layer: 6 neurons
* Output layer: 4 neurons
* Activation function: Sigmoid

**Training parameters:**

* Learning rate: 0.3
* Momentum: 0.9
* Random weight initialization
* Supervised learning using backpropagation
* Training stops when total error < 0.0004

The Arduino trains the network on startup.
After the error becomes sufficiently small, the program switches to inference mode and begins classifying real input signals.

---

## Training Data

The network is trained using 4 predefined patterns.
Each pattern is encoded as a 16-bit binary vector representing a 4x4 grid.

The output neurons represent the predicted class of the pattern.

Example idea:

* Triangle
* Square
* Circle
* Empty / other pattern

---

## Hardware Setup (Arduino UNO)

The Arduino reads a 4x4 binary grid using its digital pins.

Pins used:
D2–D13 and A0–A3 (used as digital inputs)

Each pin represents one cell in the 4x4 grid:

HIGH = 1
LOW = 0

The switches or buttons connected to the pins create a binary image which the neural network classifies.

---

## How to Run

1. Open the `.ino` file in the Arduino IDE
2. Connect Arduino UNO via USB
3. Select the correct COM port
4. Upload the program
5. Open **Serial Monitor**
6. Set baud rate to **9600**

The Serial Monitor will show:

* Training progress
* Error reduction
* Final predictions after training

When the message **"Training Set Solved!"** appears, the network is ready and will classify live input from the pins.

---

## Skills Demonstrated

* Embedded C++ programming
* Implementation of neural networks from scratch
* Backpropagation algorithm
* Working with Arduino GPIO pins
* Real-time data processing
* Serial debugging and monitoring
* Understanding of machine learning fundamentals

---

## Limitations and Possible Improvements

* Training on microcontroller is slow for larger datasets
* Output classification could use argmax decision logic
* Trained weights could be stored in EEPROM to avoid retraining after reset
* Dataset can be expanded to recognize more patterns

---

## Author
Agata Gabara
