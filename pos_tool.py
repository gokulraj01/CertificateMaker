import tkinter as tk
from PIL.ImageTk import PhotoImage
from PIL import Image


def fix_handle():
    print("Button Pressed")
    main.destroy()

filename = "Cert.jpeg"
resize_factor = 512

main = tk.Tk()
main.title("Positioning Tool")
imgload = Image.open(filename)
orig_dim = (imgload.width, imgload.height)
new_dim = (int(orig_dim[0]/orig_dim[1]*resize_factor), resize_factor)
imgload = imgload.resize(new_dim)
img = PhotoImage(imgload)
can = tk.Canvas(main, width=new_dim[0], height=new_dim[1])
can.create_image(0, 0, image=img, anchor='nw')
can.grid(row=1, column=0, columnspan=3)

points_view = tk.Label(main, text="Click a point to save")
points_view.grid(row=0, column=0, columnspan=1, sticky='W')
tk.Button(main, text="Fix Point", command=fix_handle).grid(row=0, column=2, sticky="E")
tk.Label(main, text=f"{filename}").grid(row=2, column=0, sticky="W")
tk.Label(main, text=f"{orig_dim[0]}×{orig_dim[1]} ({new_dim[0]}×{new_dim[1]})").grid(row=2, column=1, sticky="EW")
pos = tk.Label(main, text=f"Move Cursor")
pos.grid(row=2, column=2, sticky="E")

def remap(val, max1, max2):
    return int(val/max1*max2)

def showImg():
    can.create_image(0, 0, image=img, anchor='nw')

def cursor_handler(e):
    pos.configure(text=f"Image Pos: ({e.x}, {e.y})")

def click_handler(e):
    x, y = e.x, e.y
    length = 10
    stroke = 5
    showImg()
    can.create_line(x-length, y-length, x+length, y+length, fill="red", width=stroke)
    can.create_line(x+length, y-length, x-length, y+length, fill="red", width=stroke)
    nx = remap(x, new_dim[0], orig_dim[0])
    ny = orig_dim[1] - remap(y, new_dim[1], orig_dim[1])
    can.create_text(x+length, y+length, text=f"({nx},{ny})", fill="red", anchor="nw", font="Arial 10")

    label = f"Selected Point: ({nx},{ny})"
    points_view.configure(text=label)

can.bind("<Motion>", cursor_handler)
can.bind("<Button>", click_handler)
orig_dim = (int(29.7*72/2.5), int(21*72/2.5))
main.mainloop()
print("END")