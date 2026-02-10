#include "arduinoFFT.h"
#include "SoftwareSerialTX.h"

SoftwareSerialTX midiSerial(2);

#define SAMPLES 128
#define SAMPLING_FREQUENCY 1000

arduinoFFT FFT = arduinoFFT();

unsigned int sampling_period_us;
unsigned long microseconds;

double vReal[SAMPLES];
double vImag[SAMPLES];

void noteOn(byte cmd, byte pitch, byte velocity) {
midiSerial.write(cmd);
midiSerial.write(pitch);
midiSerial.write(velocity);
}

bool inRange(double v, double lo, double hi) {
return (v > lo && v < hi);
}

void playNote(byte midiNote) {
noteOn(0x90, midiNote, 0x45);
delay(10);
noteOn(0x90, midiNote, 0x00);
}

void setup() {
Serial.begin(115200);
midiSerial.begin(31250);
sampling_period_us = round(1000000.0 * (1.0 / SAMPLING_FREQUENCY));
}

void loop() {

for (int i = 0; i < SAMPLES; i++) {
microseconds = micros();
vReal[i] = analogRead(A0);
vImag[i] = 0;

```
while (micros() < (microseconds + sampling_period_us)) {}
```

}

FFT.Windowing(vReal, SAMPLES, FFT_WIN_TYP_HAMMING, FFT_FORWARD);
FFT.Compute(vReal, vImag, SAMPLES, FFT_FORWARD);
FFT.ComplexToMagnitude(vReal, vImag, SAMPLES);

double peak = FFT.MajorPeak(vReal, SAMPLES, SAMPLING_FREQUENCY);

Serial.println(peak);

if (inRange(peak, 221, 225)) playNote(57);
else if (inRange(peak, 263, 267)) playNote(60);
else if (inRange(peak, 296, 300)) playNote(62);
else if (inRange(peak, 333, 337)) playNote(64);
else if (inRange(peak, 395, 401)) playNote(67);
else if (inRange(peak, 445, 449)) playNote(69);
}
