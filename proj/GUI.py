import tkinter as tk
import subprocess

def run_program_1():
    subprocess.run(["python", "main.py", '-t', 'squat'])

def run_program_2():
    subprocess.run(["python", "main.py", '-t', 'push-up'])

root = tk.Tk()

button1 = tk.Button(root, text="Count Squat", command=run_program_1,width=60, height=12, font=("Helvetica", 24), 
                   foreground="white", background="black", 
                   borderwidth=2, relief="groove")
button1.pack()

button2 = tk.Button(root, text="Count Push-Up", command=run_program_2,width=60, height=12, font=("Helvetica", 24), 
                   foreground="white", background="black", 
                   borderwidth=2, relief="groove")
button2.pack()

root.mainloop()
