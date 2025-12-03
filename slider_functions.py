##############################################################
# University of Toronto
# Faculty of Information
# Bachelor of Information Program
# INF 452H - Design Studio V: Coding
#
# Group: 3
# Student Names: Jessica Im
# Supervisor: Dr. Maher Elshakankiri
#
# Final Project
# Purpose: Study timer
# Date Created: November 2nd, 2025
# Date Modified:
##############################################################

from tkinter import * 

# Create window
root = Tk()  
root.geometry("800x600") 


# Stress level scale

stress_var = DoubleVar()

s1 = Scale(root, bg='#ffffff', fg='#000000', troughcolor='#FFF4C2', 
           length=400, sliderlength=40, variable=stress_var, 
           from_=1, to=5, orient=HORIZONTAL)

l3 = Label(root, text="Stress level (0 is no stress; 5 is high stress)", 
           anchor="w", justify=LEFT)

l3.pack(padx=20, pady=4, anchor="w")
s1.pack(padx=20, pady=4, anchor="w")


# Focus level scale
focus_var = DoubleVar()

Focus_scale = Scale(root, bg='#ffffff', fg='#000000', troughcolor='#FFF4C2', 
                    length=400, sliderlength=40, variable=focus_var, 
                    from_=1, to=5, orient=HORIZONTAL)

Focus_label = Label(root, text="Focus level (0 is no motivation; 5 is high Focus)", 
                    anchor="w", justify=LEFT)

Focus_label.pack(padx=20, pady=4, anchor="w")
Focus_scale.pack(padx=20, pady=4, anchor="w")


# Default settings
time = 15
font = "fredoka"
theme = 1  # 1 = yellow, 2 = blueberry, 3 = grape


# Suggest settings based on sliders
def suggest_settings():
    global time, font, theme

    stress_score = stress_var.get()
    focus_score = focus_var.get()
    
    # high stress and high focus
    if stress_score >= 3 and focus_score >= 3:
        time = 45
        font = "mono"
        theme = 3   # purple
    
    # low stress and high focus    
    elif stress_score < 3 and focus_score >= 3:
        time = 30
        font = "crimson"
        theme = 2
    
    # high stress and low focus
    elif stress_score >= 3 and focus_score < 3:
        time = 20
        font = "mono"
        theme = 1
        
    # low stress and low focus
    else:
        time = 15
        font = "fredoka"
        theme = 2


# Show entry box AND run suggestion
def on_button_click():
    suggest_settings()
    entry = Entry(root)
    entry.pack()


# Button
button = Button(
    root,
    text="Get suggested timer",
    command=on_button_click,
    activebackground='#F5C856', 
    activeforeground='#F5C856',
    anchor="center",
    bg='#F5C856',
    disabledforeground='#F5C856',
    fg="black",
    font=("Arial", 12),
    height=2,
    highlightbackground='#F5C856',
    justify="center",
    overrelief="raised",
    padx=12,
    pady=8,
    width=20,
    wraplength=200
)

button.pack(padx=0, pady=20)

root.mainloop()
