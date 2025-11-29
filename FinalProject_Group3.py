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


# Motivation level scale
motivation_var = DoubleVar()

#_# Create scale
motivation_scale = Scale( root, bg = '#ffffff', fg = '#000000', troughcolor = '#FFF4C2', 
            length = '400', sliderlength = '40', variable = motivation_var, 
           from_ = 1, to = 5, 
           orient = HORIZONTAL)   

#_# Create label
motivation_label = Label(root, text = "Motivation level (0 is no motivation; 5 is high motivation)", anchor = "w", justify = LEFT)

#_# Show scale and label
motivation_label.pack(padx=20, pady=4, anchor = "w")
motivation_scale.pack(padx=20, pady=4, anchor = "w")


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


# Energy level scale
energy_var = DoubleVar()

#_# Create scale
Energy_scale = Scale( root, bg = '#ffffff', fg = '#000000', troughcolor = '#FFF4C2', 
            length = '400', sliderlength = '40', variable = energy_var, 
           from_ = 1, to = 5, 
           orient = HORIZONTAL)   

#_# Create label
Energy_label = Label(root, text = "Energy level (0 is no motivation; 5 is high Energy)", anchor = "w", justify = LEFT)

#_# Show scale and label
Energy_label.pack(padx=20, pady=4, anchor = "w")
Energy_scale.pack(padx=20, pady=4, anchor = "w")



# Get scores with button click
def suggest_settings():
    stress_score = stress_var
    motivation_score = motivation_var
    focus_score = focus_var
    energy_score = energy_var
    
    if stress_score == 1:
        colour = 2


root.mainloop()
