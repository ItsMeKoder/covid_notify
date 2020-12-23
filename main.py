import tkinter as tk

import notifier
import config
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
root.title("Covid Cases")

config.State=""
config.Language=""

state_entry = tk.Entry(root,textvariable = config.State) 

def submit(): 
   config.State=state_entry.get()
   config.Language=language_entry.get()
   print(config.State)
   print(config.Language)
   notifier.notify()

state_entry = tk.Entry(root, textvariable = config.State) 

language_entry = tk.Entry(root, textvariable = config.Language) 


sub_btn=tk.Button(root,text = 'Submit', 
                  command = submit)

sub_btn.pack(side=tk.RIGHT)
state_entry.pack(side=tk.TOP)
language_entry.pack(side=tk.BOTTOM)

root.mainloop()

