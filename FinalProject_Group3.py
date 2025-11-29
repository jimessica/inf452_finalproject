from tkinter import * 


root = Tk()  
root.geometry("800x600") 

# Stress level scale
v1 = DoubleVar()

s1 = Scale( root, bg = '#ffffff', fg = '#000000', troughcolor = '#FFF4C2', 
            length = '400', sliderlength = '40', variable = v1, 
           from_ = 1, to = 5, 
           orient = HORIZONTAL)   

l3 = Label(root, text = "Stress level (0 is no stress; 5 is high stress)", anchor = "w", justify = LEFT)

l3.pack(padx=20, pady=4, anchor = "w")
s1.pack(padx=20, pady=4, anchor = "w")

# Motivation level scale
v2 = DoubleVar()

motivation_scale = Scale( root, bg = '#ffffff', fg = '#000000', troughcolor = '#FFF4C2', 
            length = '400', sliderlength = '40', variable = v2, 
           from_ = 1, to = 5, 
           orient = HORIZONTAL)   

motivation_label = Label(root, text = "Motivation level (0 is no motivation; 5 is high motivation)", anchor = "w", justify = LEFT)


motivation_label.pack(padx=20, pady=4, anchor = "w")
motivation_scale.pack(padx=20, pady=4, anchor = "w")

# Focus level scale
v2 = DoubleVar()

Focus_scale = Scale( root, bg = '#ffffff', fg = '#000000', troughcolor = '#FFF4C2', 
            length = '400', sliderlength = '40', variable = v2, 
           from_ = 1, to = 5, 
           orient = HORIZONTAL)   

Focus_label = Label(root, text = "Focus level (0 is no motivation; 5 is high Focus)", anchor = "w", justify = LEFT)


Focus_label.pack(padx=20, pady=4, anchor = "w")
Focus_scale.pack(padx=20, pady=4, anchor = "w")


# Energy level scale
v2 = DoubleVar()

Energy_scale = Scale( root, bg = '#ffffff', fg = '#000000', troughcolor = '#FFF4C2', 
            length = '400', sliderlength = '40', variable = v2, 
           from_ = 1, to = 5, 
           orient = HORIZONTAL)   

Energy_label = Label(root, text = "Energy level (0 is no motivation; 5 is high Energy)", anchor = "w", justify = LEFT)


Energy_label.pack(padx=20, pady=4, anchor = "w")
Energy_scale.pack(padx=20, pady=4, anchor = "w")

root.mainloop()


