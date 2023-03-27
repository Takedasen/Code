# Sketchbook program

# Define the canvas size
canvas_width = 800
canvas_height = 600

# Define the drawing color
color = 'black'

# Define a function to draw a line
def draw_line(event):
    x, y = event.x, event.y
    canvas.create_line(x, y, x+2, y+2, fill=color)

# Define a function to change the drawing color
def change_color(c):
    global color
    color = c

# Create the window and canvas
from tkinter import *
root = Tk()
root.title('Sketchbook')
canvas = Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

# Add buttons to change the drawing color
red_button = Button(root, text='Red', command=lambda: change_color('red'))
red_button.pack(side=LEFT)
blue_button = Button(root, text='Blue', command=lambda: change_color('blue'))
blue_button.pack(side=LEFT)
green_button = Button(root, text='Green', command=lambda: change_color('green'))
green_button.pack(side=LEFT)

# Bind the canvas to the mouse events
canvas.bind('<B1-Motion>', draw_line)

# Start the main loop
root.mainloop()
