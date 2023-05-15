import tkinter as tk
import subprocess
import webbrowser
from generate_report import *

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

        self.squat_button = tk.Button(self, text="Count Squat", command=self.run_program_1,width=60, height=5, font=("Helvetica", 24), 
               foreground="black", bg="#4CAF50", 
               borderwidth=2, relief="groove")
        self.squat_button.pack_forget()

        self.push_up_button = tk.Button(self, text="Count Push-Up", command=self.run_program_2,width=60, height=5, font=("Helvetica", 24), 
               foreground="black", bg="#F44336", 
               borderwidth=2, relief="groove")
        self.push_up_button.pack_forget()

        self.back_button = tk.Button(self, text="Back", command=self.hide_buttons, width=60, height=5, font=("Helvetica", 24), 
               foreground="red", bg="#555555", 
               borderwidth=2, relief="groove")
        self.back_button.pack_forget()
        
        self.html_button = tk.Button(self, text="Generate Report", command=lambda: self.open_local_html(0), width=60, height=5, font=("Helvetica", 24),
               foreground="black", bg="#9C27B0",
               borderwidth=2, relief="groove")
        self.html_button.pack_forget()
        
        self.html_his_button = tk.Button(self, text="History Report", command=lambda: self.open_local_html(1), width=60, height=5, font=("Helvetica", 24),
               foreground="black", bg="#9C27B0",
               borderwidth=2, relief="groove")
        self.html_his_button.pack_forget()
        

    def show_buttons(self):
        self.squat_button.pack(pady=10)
        self.push_up_button.pack(pady=10)
        self.html_button.pack(pady=10)  # show the new button
        self.html_his_button.pack(pady=10)
        self.object_tracking_button.pack_forget()  # hide the object tracking button
        self.start_button.pack_forget()
        self.back_button.pack(pady=10)

    def hide_buttons(self):
        self.squat_button.pack_forget()
        self.push_up_button.pack_forget()
        self.html_button.pack_forget()  # hide the new button
        self.html_his_button.pack_forget()
        self.object_tracking_button.pack_forget()  # hide the object tracking button
        self.back_button.pack_forget()
        self.start_button.pack(pady=10)
        self.object_tracking_button.pack(pady=10)  # show the object tracking button

    def open_local_html(self, version):
        print("wtfwtfwtf")
        generate_html_random(version)
        web_generate_random = "/Users/liuchang/Desktop/Spring2023/ECE445/git_repo/proj/website/generated_random.html"
        web_history = "/Users/liuchang/Desktop/Spring2023/ECE445/git_repo/proj/website/history_report.html"
        if(version==0):
            webbrowser.open_new_tab('file://' + web_generate_random)
        else:
            webbrowser.open_new_tab('file://' + web_history)
            
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

# import tkinter as tk
# import tkinter.ttk as ttk
# import subprocess

# class ExerciseCounterGUI(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.master = master
#         self.master.title("Exercise Counter")

#         # Change the theme of the application and set a custom style for the buttons
#         self.style = ttk.Style()
#         self.style.theme_use("clam")
#         self.style.configure("ExerciseCounter.TButton", font=("Helvetica", 24), foreground="black", borderwidth=2, relief="groove")

#         self.pack()
#         self.create_widgets()

#     def create_widgets(self):
#         self.intro_label = tk.Label(self, text="Welcome to Exercise Counter!", font=("Helvetica", 24))
#         self.intro_label.pack(pady=(50, 20))

#         self.start_button = ttk.Button(self, text="Start Exercise", command=self.show_buttons, width=60, style="ExerciseCounter.TButton", 
#                foreground="black", background="#008CBA")
#         self.start_button.pack(pady=10)

#         self.object_tracking_button = ttk.Button(self, text="Object Tracking", command=self.run_object_tracking, width=60, style="ExerciseCounter.TButton", 
#                foreground="black", background="#FFC107")
#         self.object_tracking_button.pack(pady=10)

#         self.squat_button = ttk.Button(self, text="Count Squat", command=self.run_program_1, width=60, style="ExerciseCounter.TButton", 
#                foreground="black", background="#4CAF50", compound="c", padding=50)
#         self.squat_button.pack_forget()

#         self.push_up_button = ttk.Button(self, text="Count Push-Up", command=self.run_program_2, width=60, style="ExerciseCounter.TButton", 
#                foreground="black", background="#F44336", compound="c", padding=50)
#         self.push_up_button.pack_forget()

#         self.back_button = ttk.Button(self, text="Back", command=self.hide_buttons, width=60, style="ExerciseCounter.TButton", 
#                foreground="red", background="#555555")
#         self.back_button.pack_forget()

#     def show_buttons(self):
#         self.squat_button.pack(pady=10)
#         self.push_up_button.pack(pady=10)
#         self.object_tracking_button.pack_forget()
#         self.start_button.pack_forget()
#         self.back_button.pack(pady=10)

#     def hide_buttons(self):
#         self.squat_button.pack_forget()
#         self.push_up_button.pack_forget()
#         self.object_tracking_button.pack(pady=10)
#         self.back_button.pack_forget()
#         self.start_button.pack(pady=10)

#     def run_program_1(self):
#         subprocess.run(["python", "main.py", "-t", "squat"])

#     def run_program_2(self):
#         subprocess.run(["python", "main.py", "-t", "push-up"])

#     def run_object_tracking(self):
#         # Add code here to run your object tracking function
#         pass

# root = tk.Tk()
# app = ExerciseCounterGUI(master=root)
# app.mainloop()
