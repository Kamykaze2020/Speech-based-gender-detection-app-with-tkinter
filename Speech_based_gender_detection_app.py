import os
import numpy as np
import tkinter as tk

from scipy.io import wavfile
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import speech_recognition as sr
from gtts import gTTS

path = ''
global start_a
global stop_a
global F0
global list
list = []
F0 = 0


# FUNCTION TO OPEN THE WAV FILE AND STORE THE DATA
def open_file():
    global data
    global path
    # t1.delete('1.0',tk.END)
    filepath = tk.filedialog.askopenfilename(title='select',
                                             filetypes=[("all wav format", ".wav")])
    path = filepath
    # os.system(path)
    # t1.insert(tk.END,filepath.split('/')[-1])
    t1.replace(1.0, 100.0, filepath.split('/')[-1])
    fs, data = wavfile.read(filepath)
    # btn3.grid(row =4, column = 2)
    print("data : ", data)


# FUNCTION TO SHOW ON INTERFACE THE DEFAULT SIGNAL
def show_default_signal():
    global canvas
    # CREATING THE FIGURE THAT WILL CONTAIN THE SIGNAL GRAPH
    fig = Figure(figsize=(5, 5), dpi=100)

    # ADDING THE SUBGRAPH
    plot1 = fig.add_subplot(111)

    # SIGNAL DISPLAY
    plot1.plot(data)

    # SET TITLE
    plot1.set_title("Default Signal")

    # CREATING THE CANVAS THAT WILL CONTAIN THE FIGURE
    canvas = FigureCanvasTkAgg(fig, master=window1)
    canvas.draw()

    # POSITIONING OF THE CANVAS
    canvas.get_tk_widget().grid(row=4, column=0, columnspan=10)


# FUNCTION TO SHOW SEGMENT OF THE SIGNAL
def show_default_signal_segment():
    global canvas
    global start_a
    global stop_a

    # CALCULATING THE
    tf = 20 / (10 ** 3)
    ts = 1 / fs
    N = tf / ts
    stop_a = int(start_a + N)

    # CREATING THE FIGURE THAT WILL CONTAIN THE SIGNAL GRAPH
    fig = Figure(figsize=(5, 5), dpi=100)

    # ADDING THE SUBGRAPH
    plot1 = fig.add_subplot(111)

    # SIGNAL DISPLAY
    plot1.plot(data[start_a:stop_a])

    # SET THE CORRESPONDING TICK LABELS
    # plot1.set_xticklabels(range(start_a, stop_a))

    # ADD TITILE
    plot1.set_title("Signal Segment")

    # CREATING THE CANVAS THAT WILL CONTAIN THE FIGURE
    canvas = FigureCanvasTkAgg(fig, master=window1)
    canvas.draw()

    # CANVAS POSITIONING
    canvas.get_tk_widget().grid(row=4, column=20, columnspan=10)


def smooth():
    global start_a
    global stop_a
    global F0
    global list

    # GET DATA FROM SEGMENT
    a = data[start_a:stop_a]

    # GET THE MAX FROM SEMGMENT
    max_a = max(abs(a))
    print(max_a)

    # VALUE FOR HIGH PASS FILTER
    cl = 0.7 * max_a

    n = [0]

    # SMOOTHING THE SIGNAL SO THAT WE CAN TAKE ONLY THE VALUES OVER THRESHOLD
    a = np.where(abs(a) > cl, 0.7 * a, 0)

    # RETURNS THE NON-ZERO ELEMENT INDICES
    idx = np.nonzero(a)[0]
    # print(idx)
    # print("idx[1]:", idx[1], "idx[0]:", idx[0])

    # CALCULATES THE DIFFERENCE BETWEEN THE VALUES AT INDICES 0 AND 1 IN THE IDX ARRAY.
    dif = idx[1] - idx[0]

    # CALCULATING THE FUNDAMENTAL TONE
    F0 = fs / dif

    print(f'The fundamental tone = {F0} Hz')

    t3.replace(1.0, 100.0, F0)

    # OPEN TEXT FILE
    text_file = open("DATA/data.txt", "w")

    # COMPARING THE FUNDAMENTAL TONE TO DETERMINE GENDER
    if (F0 > 70 and F0 < 160):
        t4.replace(1.0, 100.0, 'Man')
        # WRITE ANSWER STRING TO FILE
        text_file.write('Man')

        list.append("Man")

        with open('DATA/data.txt', 'w') as f:
            f.write('\n'.join(list))

        print(list)

        # CLOSE FILE
        text_file.close()

    elif (F0 > 160 and F0 < 280):
        t4.replace(1.0, 100.0, 'Woman')

        # WRITE ANSWER STRING TO FILE
        list.append("Woman")

        with open('DATA/data.txt', 'w') as f:
            f.write('\n'.join(list))

        print(list)
        # CLOSE FILE
        text_file.close()
    else:
        t4.replace(1.0, 100.0, 'Not a human frequency')

    global canvas
    # CREATING THE FIGURE THAT WILL CONTAIN THE SIGNAL GRAPH
    fig = Figure(figsize=(5, 5), dpi=100)

    # ADDING THE SUBGRAPH
    plot1 = fig.add_subplot(111)

    # SIGNAL DISPLAY
    plot1.plot(a)

    # SET TITLE
    plot1.set_title("Smoothed Signal")

    # CREATING THE CANVAS THAT WILL CONTAIN THE FIGURE
    canvas = FigureCanvasTkAgg(fig, master=window1)
    canvas.draw()

    # THE POSITIONING OF THE CANVAS
    canvas.get_tk_widget().grid(row=4, column=40, columnspan=10)


# FUNCTION TO PLAY WAV FILE WITH OS
def play_sound():
    os.system(path)


# FUNCTION TO GET INPUT FROM USER
def get_a():
    global t2
    global start_a
    start_a = int(t2.get())
    print(start_a)


# CREATE EMPTY WINDOW FOR TKINTER
window1 = tk.Tk()
window1.geometry("1500x700+300+100")

r = tk.IntVar()

# DEFAULT VALUES IN CASE YOU DON'T SAVE NEW TIME VALUE
tf = 20 / (10 ** 3)
fs = 8000
ts = 1 / fs
N = tf / ts
start_a = 9700  # 6050

stop_a = int(start_a + N)

# ADDING BUTTONS FOR INTERFACE
btn1 = tk.Button(window1, text='Search for file', command=open_file)

btn3 = tk.Button(master=window1, command=lambda: [show_default_signal(), show_default_signal_segment(), smooth()],
                 height=2, width=10, text="Show Signal")
btn4 = tk.Button(window1, height=2, width=10, text="Play Sound", command=play_sound)
btn5 = tk.Button(window1, height=1, width=8, text="Remember", command=get_a)

# ADDING LABELS FOR INTERFACE
w1 = tk.Label(window1, text='File name: ')
w2 = tk.Label(window1, text='Start_a: ')
w3 = tk.Label(window1, text='The fundamental frequency(Hz): ')
w4 = tk.Label(window1, text='Gender: ')

# ADDING TEXT BOXES
t1 = tk.Text(window1, height=1, width=20)
t2 = tk.Entry(window1, width=20)
t3 = tk.Text(window1, height=1, width=20)
t4 = tk.Text(window1, height=1, width=20)

# POSITIONING ELEMENTS
w1.grid(row=3, column=0)
w2.grid(row=0, column=0)
w3.grid(row=5, column=0)
w4.grid(row=7, column=0)

t1.grid(row=3, column=1)
t2.grid(row=0, column=1)
t3.grid(row=5, column=1)
t4.grid(row=7, column=1)

btn1.grid(row=2, column=1)
btn3.grid(row=2, column=4, columnspan=2)
btn4.grid(row=2, column=6, columnspan=3)
btn5.grid(row=0, column=2, columnspan=3)

window1.mainloop()
