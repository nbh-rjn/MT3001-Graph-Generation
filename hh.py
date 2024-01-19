
import tkinter as tk
import random


def on_click(event):
    global v
    global degrees
    x, y = event.x, event.y
    v += 1  # Increment v at each click
    points.append((x, y))
    degrees.append(0)
    canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill="white")
    canvas.create_text(x, y - 10, text=chr(v), fill="white")


def havelhakimi():

    global degrees
    if len(points) < 10:
        return

    for i in range(len(points)):
        deg = random.randint(1, len(points))
        for j in range(i + 1, deg):
            if i != j:
                canvas.create_line(points[i][:2], points[j][:2], fill="pink")
                degrees[i] += 1
                degrees[j] += 1

    ty = 250
    while True:
        degrees = sorted(degrees, reverse=True)

        tx = 550
        for i in range(len(degrees)):
            canvas.create_text(tx, ty, text=degrees[i], fill="white")
            tx += 20
        ty += 20

        if degrees[0] == 0 and degrees[len(degrees) - 1] == 0:
            canvas.create_text(tx, ty + 40, text="simple", font=("Helvetica", 14), fill="pink")
            return True

        d = degrees[0]
        degrees = degrees[1:]
        if d > len(degrees):
            canvas.create_text(tx, ty+40, text="not simple", font=("Helvetica", 14), fill="pink")
            return False

        for i in range(d):
            degrees[i] -= 1
            if degrees[i] < 0:
                canvas.create_text(tx, ty + 40, text="not simple", font=("Helvetica", 14), fill="pink")
                return False


root = tk.Tk()
root.title("Havel Hakimi")

canvas = tk.Canvas(root, width=1000, height=500, bg="gray19")
canvas.pack()
v = ord('A') - 1  # Set v to the ASCII code of 'A' minus 1

degrees = []
points = []
canvas.bind("<Button-1>", on_click)

# Add a button to call the func function
button = tk.Button(root, text="Draw Graph", command=havelhakimi)
button.pack()

root.mainloop()
