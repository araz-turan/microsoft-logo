from tkinter import *
master = Tk()
canvas = Canvas(master, height=350, width=350)
canvas.pack()

rectangle_up_right = canvas.create_rectangle(100, 100, 170, 170, fill='#f35322', outline='#f35322')#color = red

rectangle_down_right = canvas.create_rectangle(100, 180, 170, 250, fill='#05a6f1', outline='#05a6f1')#color = blue

rectangle_up_left = canvas.create_rectangle(180, 100, 250, 170, fill='#81dc05', outline='#81dc05')#color = green

rectangle_down_left = canvas.create_rectangle(180, 180, 250, 250, fill='#ffba05', outline='#ffba05')#color = yellow

text_logo = canvas.create_text(175, 270, text='Microsoft', fill='#808080', font=('Arial', 26, 'bold'))#text = Microsoft
                               

master.mainloop()