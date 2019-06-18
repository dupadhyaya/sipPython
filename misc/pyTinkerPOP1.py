# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 07:58:06 2017 by Dhiraj Upadhyaya
Chp-16 GUI Programming
"""

from tkinter import *
root = Tk()
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
buttons = [0] * 26

"""
for i in range(26):
    buttons[i] = Button(text=alphabet[i])
    buttons[i].grid(row=0, column=i)
ok_button = Button(text = 'Ok', font =('Verdana', 24))
#ok_button.grid(row=1, column=0)
ok_button.grid(row=1, column=0, columnspan=26) #better way

mainloop()
"""
"""
button_frame = Frame()
for i in range(26):
    buttons[i] = Button(button_frame, text=alphabet[i])
    buttons[i].grid(row=0, column=i)
ok_button = Button(text = 'Ok', font =('Verdana', 24))
button_frame.grid(row=0, column=0)
ok_button.grid(row=1, column=0)

#mainloop()

def color_convert(r, g, b):
    return ('#{:02x}{:02x}{:02x}'.format(int(r*2.55), int(g*2.55), int(b*2.55)))

label = Label(text= 'Hi', bg=color_convert(100, 85, 80))
# 100% of Red, 85% of Green, 80% of Blue
"""

#10.3 Images
cheetah_image = PhotoImage(file='cheetahs.gif')
#putting into widgets
label = Label(image=cheetah_image)
#button=Button(image=cheetah_image, command=cheetah_callback())
#configure to set or change
label.configure(image=cheetah_image)
#Tkinter can only use gif , for others use Python Imaging Library

# Canvas
#lines, circles, rectangles
canvas = Canvas(width= 200, height=200, bg='white')
canvas.create_rectangle(20,100, 30, 150, fill='red')
