# Speech-based-gender-detection-app-with-tkinter
Speech based gender detection app with tkinter that show the user the gender of the person speaking in the .wav audio file.

The application takes a .wav file from the user's computer, stores the data inside a vector, selects a semgemnt of the signal and makes a high pass filter so that the noise from the file is avoided. The smoothed signal is then used to calculate the fundamental frequency so that we can say the gender.

The application stores the answers in a .txt file inside the '**DATA**' folder. Keep the folder '**DATA**' inside the project repository, otherwise the program won't work correctly!

# Interface

![8](https://github.com/Kamykaze2020/Speech-based-gender-detection-app-with-tkinter/assets/62187923/6711d25b-eaf8-4422-8dae-5871e8c80c37)

# Example of running

https://github.com/Kamykaze2020/Speech-based-gender-detection-app-with-tkinter/assets/62187923/a912b6f7-6203-4478-b609-10274225464e

# Theory

When you hear a sound, your eardrum oscillates because the density and pressure of the air in close proximity to your ear also oscillates. Thus, sound recordings contain the relative signal of these oscillations. Digital signal is sound that has been recorded or converted into digital form. In digital signal, the sound wave of the audio signal is encoded as numerical samples in continuous sequence.

For example, for a CD (or WAV), samples are taken 44100 times per second, each with a sample depth of 16 bits, meaning there are 2^16 = 65536 possible signal values: from -32768 to 32767. For the example below, a sound wave, in red, digitally represented in blue (after 4-bit sampling and quantization).

![image](https://github.com/Kamykaze2020/Speech-based-gender-detection-app-with-tkinter/assets/62187923/6fc1700c-baf7-4473-8c41-24fc6ff44f15)

This means that sound pressure values are mapped to integer values that can range from -2^15 to (2^15)-1.

Any signal that can be heard by the human ear is called an audio signal and has a frequency between 20 Hz and 20 KHz.

Depending on the physiology of each speaker, the spectrum of the signal in the frequency domain has certain characteristics: the fundamental frequency (F0) and a series of harmonics. The location of the fundamental frequency depends on the speaker and is directly responsible for the pitch of the voice. The vocal signal produced by an adult male has a typical fundamental frequency between 85 and 180 Hz, while for an adult female it is between 165 and 255 Hz. The fundamental frequency of children is between 250 and 650 Hz, in some cases it can reach over 1000 Hz.

An adequate analysis of audio signals is done both in the time domain and in the frequency domain.

For example, if we have a signal over a period of time.

![image](https://github.com/Kamykaze2020/Speech-based-gender-detection-app-with-tkinter/assets/62187923/ec97c023-9171-4e47-a315-30e01b71dab6)

We will select and work with a frame from the signal.

![image](https://github.com/Kamykaze2020/Speech-based-gender-detection-app-with-tkinter/assets/62187923/d8b573d9-6fbd-4b88-aee3-0b0d0bd808bf)

# Tracing the signal in frequency with FT (Fourier Transform)

Another useful graphical representation is that of the frequency content or spectrum of the note. The standard way to do this is with a discrete Fourier transform. Basically, we take a sound signal and isolate the sine wave frequencies that make up that sound.

![image](https://github.com/Kamykaze2020/Speech-based-gender-detection-app-with-tkinter/assets/62187923/97e6a002-14f7-4071-b990-61a26e451ed4)

So we will use the np.fft.rfft() function. This is intended for data that does not contain complex numbers only real numbers. The function np.fft.rfftfreq() always goes together with np.fft.rfft() because it provides the way to get the appropriate frequency units:

**fft_spectrum = np.fft.rfft(signal)**

**freq = np.fft.rfftfreq(signal.size, d=1./sampFreq)**

![image](https://github.com/Kamykaze2020/Speech-based-gender-detection-app-with-tkinter/assets/62187923/61f84394-4c0a-4aae-ab62-f6d3f9413b0f)

![image](https://github.com/Kamykaze2020/Speech-based-gender-detection-app-with-tkinter/assets/62187923/15821143-db0d-4dc3-80fc-a3b11a4cd16f)

The graph shows a large peak at and around 60 Hz (black arrow). This is the frequency standard used for AC (Alternating Current) in North America, where the recording was probably made, and is very noticeable when playing a sound. In Europe, for example, the standard frequency is 50 Hz.

This effect is called electrical hum. In short, because of the ubiquitous AC electromagnetic fields from nearby appliances and cables, 60 Hz electrical noise can penetrate audio systems.

The second highest peak is called **the fundamental frequency** (green arrow) - and it is close to 233 Hz. The other peaks are called overtone harmonics and are multiples of the fundamental frequency. We see that, except for the 60 Hz noise, there are peaks around 233 Hz, 465 Hz, 698 Hz, 932 Hz, 1167 Hz, 1401 Hz, and 1638 Hz (all are multiples of ~233 Hz).

# Installation

Download the file as a .zip file and extract it. You will need to open the .py file and run it in PyCharm. This application need multiple packages to be installed.

Keep the folder '**DATA**' inside the project repository, otherwise the program won't work correctly!

You can install the necessary packages through terminal with the pip commands:

**pip install scipy**

**pip install matplotlib**
