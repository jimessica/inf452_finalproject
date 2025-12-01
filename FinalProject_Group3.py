##############################################################
# University of Toronto
# Faculty of Information
# Bachelor of Information Program
# INF 452H - Design Studio V: Coding
#
# Group: 3
# Student Names: Jessica Im, 
# Supervisor: Dr. Maher Elshakankiri
#
#
# Final Project
# Purpose: Study timer
# Date Created: November 2nd, 2025
# Date Modified: 
###################################################################

from tkinter import * 

# Create window
root = Tk()  
root.geometry("800x600") 


# Stress level scale
stress_var = DoubleVar()

#_# Create scale
s1 = Scale( root, bg = '#ffffff', fg = '#000000', troughcolor = '#FFF4C2', 
            length = '400', sliderlength = '40', variable = stress_var, 
           from_ = 1, to = 5, 
           orient = HORIZONTAL)   

#_# Create label
l3 = Label(root, text = "Stress level (0 is no stress; 5 is high stress)", anchor = "w", justify = LEFT)

#_# Show scale and label
l3.pack(padx=20, pady=4, anchor = "w")
s1.pack(padx=20, pady=4, anchor = "w")


# Focus level scale
focus_var = DoubleVar()

#_# Create scale
Focus_scale = Scale( root, bg = '#ffffff', fg = '#000000', troughcolor = '#FFF4C2', 
            length = '400', sliderlength = '40', variable = focus_var, 
           from_ = 1, to = 5, 
           orient = HORIZONTAL)   

#_# Create label
Focus_label = Label(root, text = "Focus level (0 is no motivation; 5 is high Focus)", anchor = "w", justify = LEFT)

#_# Show scale and label
Focus_label.pack(padx=20, pady=4, anchor = "w")
Focus_scale.pack(padx=20, pady=4, anchor = "w")


# Get scores with button click
#_# Set colour suggestion

theme = 1 # 1 is default yellow, 2 is blueberry, and 4 is grape

def suggest_settings():
    stress_score = stress_var
    focus_score = focus_var
    
    # high stress and high focus
    if stress_score >= 3 and focus_score >= 3:
        time = 45 # long time because of high focus
        font = "mono" # 
        theme = 3 # purple to reduce stress
        
    elif stress_score < 3 and focus_score >= 3:
        time = 30
        font = "crimson"
        theme = 2

root.mainloop()
