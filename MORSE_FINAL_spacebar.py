from playsound import playsound
import time
from tkinter import *
from pynput import keyboard

root = Tk()
root.title('MORSE TRANSLATOR')

f = open("alphabet.txt", "r")
elements = f.read()

StringOfAlphabet = ''.join(elements.split())
ListOfAlphabet = StringOfAlphabet.split(",")
alphabet = {}

for i in ListOfAlphabet:
    alphabet[i[1:2]] = i[5:-1]
print(alphabet)



def text_to_morse_code_creator(inputToTranslate):
    morse = ' '.join(alphabet[letter] for letter in inputToTranslate.upper())
    for i in morse:
        if i == '.':
            playsound('D:\PYTHON_NAUKA\project_morse_code\E_morse_code.wav')
        elif i == '-':
            playsound('D:\PYTHON_NAUKA\project_morse_code\T_morse_code.wav')
        else:
            time.sleep(0.3)
    return morse


def morse_code_to_text_creator(inputToTranslate):
    decrypt = {value: key for key, value in alphabet.items()}

    return ''.join(decrypt[code] for code in inputToTranslate.split())


code_list = []
t = time.time()  # reading time in sec


def release(key):  # what to do on key-release
    if key == keyboard.Key.space:
        global t
        ti1 = time.time() - t
        if ti1 > 4:
            code_list.append(' / ')
            t = time.time()
        elif ti1 < 4 and ti1 > 2:
            code_list.append('-')
            t = time.time()
        else:
            code_list.append('.')
            t = time.time()
    if key == keyboard.Key.esc:
        return False




def press(key):  # what to do on key-press
    return False  # stop detecting more key-presses


intruction = Label(root, text='PLEASE ENTER WHAT YOU WANT TO TRANSLATE:\n')
intruction.pack()

totranslate = Entry(root)

r = IntVar()
r.get()

Radiobutton(root, text="Morse to text", variable=r, value=1).pack()
Radiobutton(root, text="Text to morse", variable=r, value=2).pack()
Radiobutton(root, text="CLICK-input to text", variable=r, value=3).pack()


def setTranslator():
    if (r.get() == 1):
        inputToTranslate = totranslate.get()
        label = Label(root, text=morse_code_to_text_creator(inputToTranslate), bg="black", fg="white")
        label.pack()
        label.config(font=("ARIAL", 20))
    elif (r.get() == 2):
        inputToTranslate = totranslate.get()
        label = Label(root, text=text_to_morse_code_creator(inputToTranslate), bg="black", fg="white")
        label.pack()
        label.config(font=("ARIAL", 20))
    elif (r.get() == 3):
        with keyboard.Listener(on_press=press) as listener1:  # setting code for listening key-press
            listener1.join()
        with keyboard.Listener(on_release=release) as listener:  # setting code for listening key-release
            listener.join()
        listToStr = ''.join([str(elem) for elem in code_list])
        label = Label(root, text=morse_code_to_text_creator(listToStr[1:]), bg="black", fg="white")
        label.pack()
        label.config(font=("ARIAL", 20))

def setOption():
    if (r.get() == 1) or (r.get() == 2):
        # totranslate = Entry(root)
        totranslate.pack()
    elif (r.get() == 3):
        intruction = Label(root, text='INPUT CODE WITH SPACEBAR AFTER CLICKING "Run Translate":\n(After pressing click spacebar once as a first "blank"')
        intruction.pack()


button1 = Button(root, text="Open selected translate option", command=setOption)
button1.pack()


button = Button(root, text="Run Translate", command=setTranslator)
button.pack(side=BOTTOM)

mainloop()
