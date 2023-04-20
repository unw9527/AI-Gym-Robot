# import tkinter as tk
# import subprocess

# def run_program_1():
#     subprocess.run(["python", "main.py", '-t', 'squat'])

# def run_program_2():
#     subprocess.run(["python", "main.py", '-t', 'push-up'])

# root = tk.Tk()

# button1 = tk.Button(root, text="Count Squat", command=run_program_1,width=60, height=12, font=("Helvetica", 24), 
#                    foreground="white", background="black", 
#                    borderwidth=2, relief="groove")
# button1.pack()

# button2 = tk.Button(root, text="Count Push-Up", command=run_program_2,width=60, height=12, font=("Helvetica", 24), 
#                    foreground="white", background="black", 
#                    borderwidth=2, relief="groove")
# button2.pack()

# root.mainloop()



# import tkinter as tk
# # print(tk.TkVersion)
# import subprocess

# class ExerciseCounterGUI(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.master = master
#         self.master.title("Exercise Counter")
#         self.pack()
#         self.create_widgets()

#     def create_widgets(self):
#         self.intro_label = tk.Label(self, text="Welcome to Exercise Counter!", font=("Helvetica", 24))
#         self.intro_label.pack(pady=(50, 20))

#         self.start_button = tk.Button(self, text="Start Exercise", command=self.show_buttons, width=60, height=6, font=("Helvetica", 24), 
#                    foreground="black", bg="#008CBA", 
#                    borderwidth=2, relief="groove")
#         self.start_button.pack(pady=10)

#         self.squat_button = tk.Button(self, text="Count Squat", command=self.run_program_1,width=60, height=12, font=("Helvetica", 24), 
#                    foreground="black", bg="#4CAF50", 
#                    borderwidth=2, relief="groove")
#         self.squat_button.pack_forget()

#         self.push_up_button = tk.Button(self, text="Count Push-Up", command=self.run_program_2,width=60, height=12, font=("Helvetica", 24), 
#                    foreground="black", bg="#F44336", 
#                    borderwidth=2, relief="groove")
#         self.push_up_button.pack_forget()

#         self.back_button = tk.Button(self, text="Back", command=self.hide_buttons, width=60, height=6, font=("Helvetica", 24), 
#                    foreground="red", bg="#F44336", 
#                    borderwidth=2, relief="groove")
#         self.back_button.pack_forget()

#     def show_buttons(self):
#         self.squat_button.pack(pady=10)
#         self.push_up_button.pack(pady=10)
#         self.start_button.pack_forget()
#         self.back_button.pack(pady=10)

#     # def hide_buttons(self):
#     #     self.squat_button.pack_forget()
#     #     self.push_up_button.pack_forget()
#     #     self.back_button.pack_forget()
#     #     self.start_button.pack(pady=10)
        
#     def hide_buttons(self):
#         self.squat_button.pack_forget()
#         self.push_up_button.pack_forget()
#         self.start_button.pack(pady=10)
#         self.back_button.pack_forget()


#     def run_program_1(self):
#         subprocess.run(["python", "main.py", '-t', 'squat'])

#     def run_program_2(self):
#         subprocess.run(["python", "main.py", '-t', 'push-up'])



# root = tk.Tk()
# app = ExerciseCounterGUI(master=root)
# app.mainloop()


import tkinter as tk
import subprocess

class ExerciseCounterGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Exercise Counter")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.intro_label = tk.Label(self, text="Welcome to Exercise Counter!", font=("Helvetica", 24))
        self.intro_label.pack(pady=(50, 20))

        self.start_button = tk.Button(self, text="Start Exercise", command=self.show_buttons, width=60, height=6, font=("Helvetica", 24), 
               foreground="black", bg="#008CBA", 
               borderwidth=2, relief="groove")
        self.start_button.pack(pady=10)

        self.object_tracking_button = tk.Button(self, text="Object Tracking", command=self.run_object_tracking, width=60, height=6, font=("Helvetica", 24), 
               foreground="black", bg="#FFC107", 
               borderwidth=2, relief="groove")
        self.object_tracking_button.pack(pady=10)

        self.squat_button = tk.Button(self, text="Count Squat", command=self.run_program_1,width=60, height=12, font=("Helvetica", 24), 
               foreground="black", bg="#4CAF50", 
               borderwidth=2, relief="groove")
        self.squat_button.pack_forget()

        self.push_up_button = tk.Button(self, text="Count Push-Up", command=self.run_program_2,width=60, height=12, font=("Helvetica", 24), 
               foreground="black", bg="#F44336", 
               borderwidth=2, relief="groove")
        self.push_up_button.pack_forget()

        self.back_button = tk.Button(self, text="Back", command=self.hide_buttons, width=60, height=6, font=("Helvetica", 24), 
               foreground="red", bg="#555555", 
               borderwidth=2, relief="groove")
        self.back_button.pack_forget()

    def show_buttons(self):
        self.squat_button.pack(pady=10)
        self.push_up_button.pack(pady=10)
        self.object_tracking_button.pack_forget()  # hide the object tracking button
        self.start_button.pack_forget()
        self.back_button.pack(pady=10)

    def hide_buttons(self):
        self.squat_button.pack_forget()
        self.push_up_button.pack_forget()
        self.object_tracking_button.pack_forget()  # hide the object tracking button
        self.back_button.pack_forget()
        self.start_button.pack(pady=10)
        self.object_tracking_button.pack(pady=10)  # show the object tracking button

    def run_program_1(self):
        subprocess.run(["python", "main.py", '-t', 'squat'])

    def run_program_2(self):
        subprocess.run(["python", "main.py", '-t', 'push-up'])

    def run_object_tracking(self):
        # Add code here to run your object tracking function
        pass

root = tk.Tk()
app = ExerciseCounterGUI(master=root)
app.mainloop()
