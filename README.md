# Speech-based-gender-detection-app-with-tkinter
Speech based gender detection app with tkinter that show the user the gender of the person speaking in the .wav audio file.

The application takes a .wav file from the user's computer, stores the data inside a vector, selects a semgemnt of the signal and makes a high pass filter so that the noise from the file is avoided. The smoothed signal is then used to calculate the fundamental frequency so that we can say the gender.

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


