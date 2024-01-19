import tkinter as tk
from tkinter import messagebox
import subprocess


def run_file(file_name):
    try:
        subprocess.run(["python", file_name], check=True)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Error running {file_name}: {e}")


def menu_selection(choice):
    if choice == "simple graph":
        run_file("simple.py")
    elif choice == "complete graph":
        run_file("complete.py")
    elif choice == "bipartite graph":
        run_file("bipartite.py")
    elif choice == "tripartite graph":
        run_file("tripartite.py")
    elif choice == "havel hakimi":
        run_file("hh.py")
    elif choice == "Exit":
        root.destroy()


def main():
    global root

    root = tk.Tk()
    root.title("Select Graph")
    root.geometry("600x400")

    # Set background color
    root.configure(bg="#303030")

    menu = tk.Menu(root)
    root.config(menu=menu)

    script_menu = tk.Menu(menu, tearoff=0, font=("Helvetica", 14))
    menu.add_cascade(label="Graphs", menu=script_menu)

    # Set menu background and foreground color
    script_menu.configure(bg="#303030", fg="pink")

    script_menu.add_command(label="Simple Graph", command=lambda: menu_selection("simple graph"),
                            background="#404040", foreground="pink")
    script_menu.add_command(label="Complete Graph", command=lambda: menu_selection("complete graph"),
                            background="#404040", foreground="pink")
    script_menu.add_command(label="Bipartite Graph", command=lambda: menu_selection("bipartite graph"),
                            background="#404040", foreground="pink")
    script_menu.add_command(label="Tripartite Graph", command=lambda: menu_selection("tripartite graph"),
                            background="#404040", foreground="pink")
    script_menu.add_command(label="Havel Hakimi ", command=lambda: menu_selection("havel hakimi"),
                            background="#404040", foreground="pink")
    script_menu.add_separator()
    script_menu.add_command(label="Exit", command=lambda: menu_selection("Exit"),
                            background="#404040", foreground="pink")

    title = tk.Label(root, text=" MT3001 GRAPH THEORY PROJECT "
                                " \n Instructor: Engr. Usama Antuley "
                                " \n\n 21K-4523 Nabiha Rajani"
                                " \n 21K-4899 Asad Tariq"
                                " \n 21K-3455 Fatima Ashraf",
                                font=("Helvetica", 16), bg="#303030", fg="pink")
    title.pack(pady=20)

    root.mainloop()


if __name__ == "__main__":
    main()
