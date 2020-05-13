from playsound import playsound
import time
from tkinter import *

root = Tk()
root.title('MORSE TRANSLATOR')

alphabet =  { 'A':'.-', 'B':'-...', 'C':'-.-.',
                  'D':'-..', 'E':'.', 'F':'..-.',
                  'G':'--.', 'H':'....', 'I':'..',
                  'J':'.---', 'K':'-.-', 'L':'.-..',
                  'M':'--', 'N':'-.', 'O':'---',
                  'P':'.--.', 'Q':'--.-', 'R':'.-.',
                  'S':'...', 'T':'-', 'U':'..-',
                  'V':'...-', 'W':'.--', 'X':'-..-',
                  'Y':'-.--', 'Z':'--..',
                  '1':'.----', '2':'..---', '3':'...--',
                  '4':'....-', '5':'.....', '6':'-....',
                  '7':'--...', '8':'---..', '9':'----.',
                  '0':'-----',
                  ' ':'/',
                  '.':'.-.-.-', ',':'---..--', ':':'---...',
                  ';':'-.-.-.', '?':'..--..', '!' :'-.-.--',
                  '-':'-....-', '+':'.-.-.', '/':'-..-.',
                  '(':'-.--.', ')':'-.--.-', '=':'-...-'
                  }



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
    decrypt = {value: key for key,value in alphabet.items()}

    return ''.join(decrypt[code] for code in inputToTranslate.split())


intruction = Label(root, text='PLEASE ENTER WHAT YOU WANT TO TRANSLATE:\n')
intruction.pack()

totranslate = Entry(root)
totranslate.pack()

r = IntVar()
r.get()

Radiobutton(root, text="Morse to text", variable=r, value=1).pack()
Radiobutton(root, text="Text to morse", variable=r, value=2).pack()

def setTranslator():
    inputToTranslate = totranslate.get()
    if(r.get() == 1):
        label = Label(root, text =morse_code_to_text_creator(inputToTranslate), bg="black", fg="white")
        label.pack()
        label.config(font=("ARIAL", 20))
    else:
        label = Label(root, text=text_to_morse_code_creator(inputToTranslate), bg="black", fg="white")
        label.pack()
        label.config(font=("ARIAL", 20))

button = Button(root, text="Translate", command=setTranslator)
button.pack()


mainloop()