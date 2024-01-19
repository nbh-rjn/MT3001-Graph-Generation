
import tkinter as tk


def on_click(event):
    global v
    x, y = event.x, event.y
    v += 1  # Increment v at each click
    points.append((x, y))
    canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill="white")
    canvas.create_text(x, y - 10, text=chr(v), fill="white")


def complete():
    if len(points) < 10:
        return

    for i in range(len(points)):
        for j in range(len(points)):
            if i != j:
                canvas.create_line(points[i][:2], points[j][:2], fill="pink")


root = tk.Tk()
root.title("Complete Graph")

canvas = tk.Canvas(root, width=500, height=500, bg="gray19")
canvas.pack()
v = ord('A') - 1  # Set v to the ASCII code of 'A' minus 1
points = []
canvas.bind("<Button-1>", on_click)

# Add a button to call the func function
button = tk.Button(root, text="Draw Graph", command=complete)
button.pack()

root.mainloop()
