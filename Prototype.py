##############################################################
# University of Toronto
# Faculty of Information
# Bachelor of Information Program
# INF 452H - Design Studio V: Coding
#
# Group: 3
# Student Names: Jessica Im, Gaven Ren, Divine Ogaram
# Supervisor: Dr. Maher Elshakankiri
#
# Final Project
# Purpose: Study timer with accessibility features
# Date Created: November 2nd, 2025
# Date Modified: December 3rd, 2025
###################################################################

from tkinter import *


# Create window
root = Tk()
root.title("NeuroFlow")
root.geometry("1400x850")
root.configure(bg='#E8F0FF')  # soft blueberry background


# Global variables
timer_running = False
timer_paused = False
remaining_time = 1800  # 30 minutes default
timer_id = None
current_theme = "Blueberry"
current_font = "IBM Plex Mono"
suggested_time = 30
suggested_font = "IBM Plex Mono"
suggested_theme = "Blueberry"


# Theme configurations
themes = {
    "Banana": {
        "bg": "#FFF4C2",
        "timer_bg": "#FFE066",
        "button_bg": "#FFE066",
        "button_active": "#FFD700",
        "text": "#000000",
        "id": 1
    },
    "Blueberry": {
        "bg": "#E8F0FF",
        "timer_bg": "#5B7FC7",
        "button_bg": "#E8F0FF",
        "button_active": "#5B7FC7",
        "text": "#000000",
        "id": 2
    },
    "Grape": {
        "bg": "#F0E6FF",
        "timer_bg": "#B19CD9",
        "button_bg": "#E6D9FF",
        "button_active": "#B19CD9",
        "text": "#000000",
        "id": 3
    }
}


# Font configurations
fonts = {
    "Fredoka": "Fredoka One",
    "Crimson Text": "Crimson Text",
    "IBM Plex Mono": "IBM Plex Mono"
}


# Reverse mapping for theme IDs
theme_id_to_name = {1: "Banana", 2: "Blueberry", 3: "Grape"}
font_name_mapping = {"fredoka": "Fredoka", "crimson": "Crimson Text", "mono": "IBM Plex Mono"}


# ==================== ASSESSMENT SCREEN ====================
assessment_frame = Frame(root, bg='#E8F0FF')
assessment_frame.pack(expand=True, fill=BOTH)


# Top section with title and subtitle
top_section = Frame(assessment_frame, bg='#E8F0FF')
top_section.pack(pady=(60, 80))


# Main title
assessment_title = Label(
    top_section,
    text="Welcome to NeuroFlow",
    font=("Fredoka One", 48, "bold"),
    bg='#E8F0FF',
    fg='#000000'
)
assessment_title.pack()


# Subtitle
subtitle = Label(
    top_section,
    text="Based on your mood, get a suggested study timer!",
    font=("Fredoka One", 18),
    bg='#E8F0FF',
    fg='#000000'
)
subtitle.pack(pady=(10, 0))


# Middle section - Current mood
mood_section = Frame(assessment_frame, bg='#E8F0FF')
mood_section.pack(fill=BOTH, padx=80, pady=(0, 40))


mood_title = Label(
    mood_section,
    text="Current Mood",
    font=("Fredoka One", 16, "bold"),
    bg='#E8F0FF',
    fg='#000000',
    anchor="w"
)
mood_title.pack(anchor="w", pady=(0, 30))


# Stress level scale
stress_var = DoubleVar()
stress_label = Label(
    mood_section,
    text="Stress level (0 is no stress; 5 is high stress)",
    anchor="w",
    justify=LEFT,
    font=("Fredoka One", 14),
    bg='#E8F0FF',
    fg='#000000'
)
stress_label.pack(anchor="w", pady=(0, 8))

stress_value_label = Label(
    mood_section,
    text="Selected stress level: 0",
    anchor="w",
    justify=LEFT,
    font=("Fredoka One", 12),
    bg='#E8F0FF',
    fg='#000000'
)

stress_value_label.pack(anchor="w", pady=(5,0))

def update_stress_label(value):
    stress_value_label.config(text=f"Selected stress level: {value}")

stress_scale = Scale(
    mood_section,
    bg='#F6D36F',          # slightly richer banana
    fg='#000000',
    troughcolor='#FFF3BF',
    length=1200,
    sliderlength=160,
    variable=stress_var,
    from_=0,
    to=5,
    orient=HORIZONTAL,
    font=("Fredoka One", 10),
    highlightthickness=0,
    bd=0,
    showvalue=0,
    width=50,
    relief=FLAT,
    command=update_stress_label
)
stress_scale.pack(anchor="w", fill=X, pady=(0, 40))


# Focus level scale
focus_var = DoubleVar()
focus_label = Label(
    mood_section,
    text="Focus level (0 is no focus; 5 is high focus)",
    anchor="w",
    justify=LEFT,
    font=("Fredoka One", 14),
    bg='#E8F0FF',
    fg='#000000'
)
focus_label.pack(anchor="w", pady=(0, 8))

focus_value_label = Label(
    mood_section,
    text="Selected focus level: 0",
    anchor="w",
    justify=LEFT,
    font=("Fredoka One", 12),
    bg='#E8F0FF',
    fg='#000000'
)
focus_value_label.pack(anchor="w", pady=(5,0))

def update_focus_label(value):
    focus_value_label.config(text=f"Selected focus level: {value}")

focus_scale = Scale(
    mood_section,
    bg='#F6D36F',
    fg='#000000',
    troughcolor='#FFF3BF',
    length=1200,
    sliderlength=160,
    variable=focus_var,
    from_=0,
    to=5,
    orient=HORIZONTAL,
    font=("Fredoka One", 10),
    highlightthickness=0,
    bd=0,
    showvalue=0,
    width=50,
    relief=FLAT,
    command=update_focus_label
)
focus_scale.pack(anchor="w", fill=X)


# ==================== SESSION SETUP SCREEN ====================
setup_frame = Frame(root, bg='#E8F0FF')

selected_time = IntVar(value=suggested_time)
selected_font = StringVar(value=suggested_font)
selected_theme = StringVar(value=suggested_theme)

def update_setup_selections():
    selected_time.set(suggested_time)
    selected_font.set(suggested_font)
    selected_theme.set(suggested_theme)

def go_to_setup_screen():
    update_setup_selections()
    assessment_frame.pack_forget()
    setup_frame.pack(expand=True, fill=BOTH)

bottom_section = Frame(assessment_frame, bg='#E8F0FF')
bottom_section.pack(side=BOTTOM, anchor=SE, padx=80, pady=60)

def suggest_settings():
    global suggested_time, suggested_font, suggested_theme
    stress_score = stress_var.get()
    focus_score = focus_var.get()

    time = 30
    font = "mono"
    theme = 2

    if stress_score >= 3 and focus_score >= 3:
        time = 45
        font = "mono"
        theme = 3
    elif stress_score < 3 and focus_score >= 3:
        time = 30
        font = "crimson"
        theme = 2
    elif stress_score >= 3 and focus_score < 3:
        time = 20
        font = "mono"
        theme = 1
    else:
        time = 15
        font = "fredoka"
        theme = 2

    suggested_time = time
    suggested_font = font_name_mapping[font]
    suggested_theme = theme_id_to_name[theme]

    go_to_setup_screen()

suggest_button = Button(
    bottom_section,
    text="Get Suggested Timer",
    font=("Arial", 14, "bold"),
    bg="#F4C14A",
    fg='#000000',
    activebackground="#E0AA32",
    activeforeground="#000000",
    width=25,
    height=2,
    relief=RAISED,
    bd=2,
    cursor="hand2",
    command=suggest_settings
)
suggest_button.pack()

# ----- Setup content -----
setup_title = Label(
    setup_frame,
    text="Session Setup",
    font=("Fredoka One", 36, "bold"),
    bg="#E8F0FF",
    fg='#000000'
)
setup_title.pack(pady=(40, 10))

# "Suggested Timer" heading above light grey rectangle
suggested_heading = Label(
    setup_frame,
    text="Suggested Timer",
    font=("Fredoka One", 20, "bold"),
    bg='#E8F0FF',
    fg='#000000',
    anchor="w"
)
suggested_heading.pack(fill=X, padx=80, pady=(0, 5))

# Subtitle below heading
setup_subtitle = Label(
    setup_frame,
    text="Review and adjust your focus time, font, and theme.",
    font=("Fredoka One", 20),
    bg='#E8F0FF',
    fg='#000000',
    anchor="center",
    justify="center"
)
setup_subtitle.pack(fill=X, padx=80, pady=(0, 15))

# Lighter grey background frame behind middle content
setup_middle_bg = Frame(setup_frame, bg="#F5F5F5", bd=0)
setup_middle_bg.pack(fill=BOTH, expand=True, padx=70, pady=(0, 20))

setup_main = Frame(setup_middle_bg, bg='#F5F5F5')
setup_main.pack(fill=BOTH, expand=True, padx=20, pady=20)

for c in range(3):
    setup_main.grid_columnconfigure(c, weight=1)

# Time section
time_section = Frame(setup_main, bg='#F5F5F5')
time_section.grid(row=0, column=0, columnspan=3, pady=10, sticky="n")

time_label = Label(
    time_section,
    text="Focus Time (min)",
    font=("Fredoka One", 20, "bold"),
    bg='#F5F5F5',
    fg='#000000'
)
time_label.pack(pady=(0, 30))

time_buttons_frame = Frame(time_section, bg='#F5F5F5')
time_buttons_frame.pack()

time_options = [15, 20, 30, 45]

def select_time(t):
    selected_time.set(t)

for i, t in enumerate(time_options):
    btn = Radiobutton(
        time_buttons_frame,
        text=f"{t} min",
        variable=selected_time,
        value=t,
        font=("Arial", 14),
        bg='#F5F5F5',
        fg='#000000',
        activebackground="#FFD700",      # yellow when pressed
        activeforeground="#000000",
        selectcolor="#FFD700",           # yellow when selected
        indicatoron=False,
        width=10,
        pady=8,
        command=lambda v=t: select_time(v)
    )
    btn.grid(row=0, column=i, padx=8)

# Font section
font_section = Frame(setup_main, bg='#F5F5F5')
font_section.grid(row=1, column=0, columnspan=3, pady=20, sticky="n")

font_label_setup = Label(
    font_section,
    text="Font",
    font=("Fredoka One", 20, "bold"),
    bg='#F5F5F5',
    fg='#000000'
)
font_label_setup.pack(pady=(0, 30))

font_buttons_frame = Frame(font_section, bg='#F5F5F5')
font_buttons_frame.pack()

def select_font_option(fname):
    selected_font.set(fname)

for i, (fname, ffont) in enumerate(fonts.items()):
    btn = Radiobutton(
        font_buttons_frame,
        text=fname,
        variable=selected_font,
        value=fname,
        font=(ffont, 14),
        bg='#F5F5F5',
        fg='#000000',
        activebackground="#FFD700",      # yellow when pressed
        activeforeground="#000000",
        selectcolor="#FFD700",           # yellow when selected
        indicatoron=False,
        width=15,
        pady=8,
        command=lambda v=fname: select_font_option(v)
    )
    btn.grid(row=0, column=i, padx=8)

# Theme section
theme_section = Frame(setup_main, bg='#F5F5F5')
theme_section.grid(row=2, column=0, columnspan=3, pady=20, sticky="n")

theme_label_setup = Label(
    theme_section,
    text="Theme",
    font=("Fredoka One", 20, "bold"),
    bg='#F5F5F5',
    fg='#000000'
)
theme_label_setup.pack(pady=(0, 30))

theme_buttons_frame = Frame(theme_section, bg='#F5F5F5')
theme_buttons_frame.pack()

theme_display_colors = {"Banana": "#FFE066", "Blueberry": "#5B7FC7", "Grape": "#B19CD9"}

def select_theme_option(tname):
    selected_theme.set(tname)

for i, tname in enumerate(themes.keys()):
    btn = Radiobutton(
        theme_buttons_frame,
        text=tname,
        variable=selected_theme,
        value=tname,
        font=("Arial", 14, "bold"),
        bg=theme_display_colors[tname],
        fg='#000000',
        activebackground="#FFFFFF",
        activeforeground="#000000",
        selectcolor="#FFFFFF",
        indicatoron=False,
        width=15,
        pady=10,
        command=lambda v=tname: select_theme_option(v)
    )
    btn.grid(row=0, column=i, padx=8)

# Start button area
setup_bottom = Frame(setup_frame, bg='#E8F0FF', height=80)
setup_bottom.pack(fill=X, pady=40)

def format_time(seconds):
    mins = seconds // 60
    secs = seconds % 60
    return f"{mins:02d}:{secs:02d}"


# ==================== TIMER SCREEN ====================
timer_screen = Frame(root, bg='#f5f5f5')

main_frame = Frame(timer_screen, bg='#f5f5f5')
main_frame.pack(expand=True, fill=BOTH, padx=40, pady=30)

title_label = Label(
    main_frame,
    text="NeuroFlow",
    font=("Arial", 32, "bold"),
    bg='#f5f5f5',
    fg='#000000'
)
title_label.pack(pady=(0, 20))

timer_frame = Frame(
    main_frame,
    bg=themes[current_theme]["timer_bg"],
    height=150,
    relief=FLAT,
    bd=0
)
timer_frame.pack(fill=X, pady=20)
timer_frame.pack_propagate(False)

timer_label = Label(
    timer_frame,
    text="30:00",
    font=(fonts[current_font], 72, "bold"),
    bg=themes[current_theme]["timer_bg"],
    fg='#FFFFFF'
)
timer_label.pack(expand=True)

control_frame = Frame(main_frame, bg='#f5f5f5')
control_frame.pack(pady=10)

def set_timer_bg_running():
    timer_frame.config(bg=themes[current_theme]["timer_bg"])
    timer_label.config(bg=themes[current_theme]["timer_bg"])

def set_timer_bg_paused_or_complete():
    timer_frame.config(bg="#B0B0B0")
    timer_label.config(bg="#B0B0B0")

def start_break():
    """Start a 5-minute break timer after work timer completes."""
    global on_break, remaining_time, timer_running, timer_paused
    on_break = True
    remaining_time = break_duration
    timer_label.config(text=format_time(remaining_time))
    timer_running = True
    timer_paused = False
    pause_button.config(text="Pause")
    set_timer_bg_running()
    countdown()

def countdown():
    """Main countdown logic for both work and break timers."""
    global remaining_time, timer_id, timer_running, on_break, suggested_time

    if timer_running and remaining_time > 0:
        timer_label.config(text=format_time(remaining_time))
        remaining_time -= 1
        timer_id = root.after(1000, countdown)
    elif remaining_time <= 0:
        timer_label.config(text="00:00")
        timer_running = False

        if on_break:
            # Break is done; reset to suggested work time and pause
            on_break = False
            remaining_time = suggested_time * 60
            timer_label.config(text=format_time(remaining_time))
            finish_button.config(text="Start")  # user can start again
            set_timer_bg_paused_or_complete()
        else:
            # Work session completed; start 5-minute break automatically
            set_timer_bg_paused_or_complete()
            start_break()

def start_timer():
    global timer_running, timer_paused, timer_id, on_break
    if not timer_running and remaining_time > 0:
        timer_running = True
        timer_paused = False
        pause_button.config(text="Pause")
        set_timer_bg_running()
        countdown()

def pause_timer():
    global timer_running, timer_paused, timer_id
    if timer_running:
        timer_running = False
        timer_paused = True
        pause_button.config(text="Resume")
        set_timer_bg_paused_or_complete()
        if timer_id:
            root.after_cancel(timer_id)
    elif timer_paused and remaining_time > 0:
        timer_running = True
        timer_paused = False
        pause_button.config(text="Pause")
        set_timer_bg_running()
        countdown()

def finish_or_start_timer():
    """Toggle between Finish and Start behavior for work timer."""
    global timer_running, timer_paused, remaining_time, timer_id, on_break

    # Only allow finish/start logic when not in break
    if on_break:
        return

    if finish_button.cget("text") == "Finish":
        # Finish: stop timer, show 0:00, grey background, change to Start
        if timer_id:
            root.after_cancel(timer_id)
        timer_running = False
        timer_paused = False
        remaining_time = 0
        timer_label.config(text="00:00")
        set_timer_bg_paused_or_complete()
        pause_button.config(text="Pause")
        finish_button.config(text="Start")
    else:
        # Start again from initial suggested_time
        remaining_time = suggested_time * 60
        timer_label.config(text=format_time(remaining_time))
        set_timer_bg_running()
        finish_button.config(text="Finish")
        timer_running = True
        timer_paused = False
        pause_button.config(text="Pause")
        countdown()

def reset_timer_only():
    """Reset timer to initial time and pause (no navigation)."""
    global timer_running, timer_paused, remaining_time, timer_id, on_break
    if timer_id:
        root.after_cancel(timer_id)
        timer_id = None
    on_break = False
    timer_running = False
    timer_paused = False
    remaining_time = suggested_time * 60
    timer_label.config(text=format_time(remaining_time))
    pause_button.config(text="Pause")
    finish_button.config(text="Finish")
    set_timer_bg_paused_or_complete()

def return_to_home():
    """Return to assessment page (start page)."""
    global timer_running, timer_paused, remaining_time, timer_id, on_break
    if timer_id:
        root.after_cancel(timer_id)
        timer_id = None
    on_break = False
    timer_running = False
    timer_paused = False
    pause_button.config(text="Pause")
    remaining_time = suggested_time * 60
    timer_label.config(text=format_time(remaining_time))
    set_timer_bg_paused_or_complete()
    timer_screen.pack_forget()
    assessment_frame.pack(expand=True, fill=BOTH)

# Control buttons: [Return to Home] [Reset] [Pause] [Finish/Start]
home_button = Button(
    control_frame,
    text="Return to Home",
    font=("Arial", 14),
    bg='#FFFFFF',
    fg='#000000',
    activebackground='#E0E0E0',
    activeforeground='#000000',
    width=16,
    height=2,
    relief=RAISED,
    bd=2,
    cursor="hand2",
    command=return_to_home
)
home_button.grid(row=0, column=0, padx=5)

reset_button = Button(
    control_frame,
    text="Reset",
    font=("Arial", 14),
    bg='#FFFFFF',
    fg='#000000',
    activebackground='#E0E0E0',
    activeforeground='#000000',
    width=12,
    height=2,
    relief=RAISED,
    bd=2,
    cursor="hand2",
    command=reset_timer_only
)
reset_button.grid(row=0, column=1, padx=5)

pause_button = Button(
    control_frame,
    text="Pause",
    font=("Arial", 14),
    bg=themes[current_theme]["button_bg"],
    fg=themes[current_theme]["text"],
    activebackground=themes[current_theme]["button_active"],
    activeforeground=themes[current_theme]["text"],
    width=12,
    height=2,
    relief=RAISED,
    bd=2,
    cursor="hand2",
    command=pause_timer
)
pause_button.grid(row=0, column=2, padx=5)

finish_button = Button(
    control_frame,
    text="Finish",
    font=("Arial", 14),
    bg=themes[current_theme]["button_bg"],
    fg=themes[current_theme]["text"],
    activebackground=themes[current_theme]["button_active"],
    activeforeground=themes[current_theme]["text"],
    width=12,
    height=2,
    relief=RAISED,
    bd=2,
    cursor="hand2",
    command=finish_or_start_timer
)
finish_button.grid(row=0, column=3, padx=5)


# ==================== INLINE CHANGE THEME / OPTIONS UNDER TIMER ====================
inline_panel = Frame(main_frame, bg='#f0f0f0', relief=FLAT, bd=0)
inline_panel.pack(fill=X, pady=20)

inline_header = Frame(inline_panel, bg='#f0f0f0')
inline_header.pack(fill=X, padx=20, pady=(10, 0))

inline_label = Label(
    inline_header,
    text="Adjust Session Options",
    font=("Fredoka One", 14, "bold"),
    bg='#E8F0FF',
    fg='#000000',
    anchor="center",
    justify="center"
)
inline_label.pack(side=LEFT)

def toggle_inline_panel():
    if inline_options.winfo_viewable():
        inline_options.pack_forget()
        change_theme_button.config(text="Change Theme")
    else:
        inline_options.pack(fill=X, padx=20, pady=10)
        change_theme_button.config(text="Hide Options")

change_theme_button = Button(
    inline_header,
    text="Change Theme",
    font=("Arial", 12, "bold"),
    bg='#FFFFFF',
    fg='#000000',
    activebackground='#E0E0E0',
    activeforeground='#000000',
    relief=RAISED,
    bd=2,
    anchor="center",
    justify="center",
    cursor="hand2",
    command=toggle_inline_panel
)

change_theme_button.pack(side=RIGHT)

inline_options = Frame(inline_panel, bg='#f0f0f0')

# Time selector under timer
inline_time_label = Label(
    inline_options,
    text="Focus Time (min)",
    font=("Fredoka One", 14, "bold"),
    bg='#f0f0f0',
    fg='#000000'
)
inline_time_label.grid(row=0, column=0, sticky="w", pady=(10, 5))

inline_time_frame = Frame(inline_options, bg='#f0f0f0')
inline_time_frame.grid(row=1, column=0, sticky="w", pady=(0, 10))

inline_time_var = IntVar(value=suggested_time)

def apply_inline_time(t):
    global suggested_time, remaining_time, on_break
    inline_time_var.set(t)
    suggested_time = t
    remaining_time = t * 60
    on_break = False
    timer_label.config(text=format_time(remaining_time))
    finish_button.config(text="Finish")
    set_timer_bg_paused_or_complete()

for i, t in enumerate(time_options):
    btn = Radiobutton(
        inline_time_frame,
        text=f"{t} min",
        variable=inline_time_var,
        value=t,
        font=("Arial", 11),
        bg='#f0f0f0',
        fg='#000000',
        activebackground="#FFD700",
        activeforeground="#000000",
        selectcolor="#FFD700",
        indicatoron=False,
        width=8,
        pady=4,
        command=lambda v=t: apply_inline_time(v)
    )
    btn.grid(row=0, column=i, padx=4)

# Font selector under timer
inline_font_label = Label(
    inline_options,
    text="Font",
    font=("Fredoka One", 14, "bold"),
    bg='#f0f0f0',
    fg='#000000'
)
inline_font_label.grid(row=2, column=0, sticky="w", pady=(10, 5))

inline_font_frame = Frame(inline_options, bg='#f0f0f0')
inline_font_frame.grid(row=3, column=0, sticky="w", pady=(0, 10))

inline_font_var = StringVar(value=current_font)

def apply_inline_font(fname):
    global current_font
    inline_font_var.set(fname)
    current_font = fname
    timer_label.config(font=(fonts[current_font], 72, "bold"))

for i, (fname, ffont) in enumerate(fonts.items()):
    btn = Radiobutton(
        inline_font_frame,
        text=fname,
        variable=inline_font_var,
        value=fname,
        font=(ffont, 11),
        bg='#f0f0f0',
        fg='#000000',
        activebackground="#FFD700",
        activeforeground="#000000",
        selectcolor="#FFD700",
        indicatoron=False,
        width=12,
        pady=4,
        command=lambda v=fname: apply_inline_font(v)
    )
    btn.grid(row=0, column=i, padx=4)

# Theme selector under timer
inline_theme_label = Label(
    inline_options,
    text="Theme",
    font=("Fredoka One", 14, "bold"),
    bg='#f0f0f0',
    fg='#000000'
)
inline_theme_label.grid(row=4, column=0, sticky="w", pady=(10, 5))

inline_theme_frame = Frame(inline_options, bg='#f0f0f0')
inline_theme_frame.grid(row=5, column=0, sticky="w", pady=(0, 10))

inline_theme_var = StringVar(value=current_theme)

def apply_inline_theme(tname):
    global current_theme
    inline_theme_var.set(tname)
    current_theme = tname
    timer_frame.config(bg=themes[current_theme]["timer_bg"])
    timer_label.config(bg=themes[current_theme]["timer_bg"])
    main_frame.config(bg=themes[current_theme]["bg"])
    timer_screen.config(bg=themes[current_theme]["bg"])
    theme = themes[current_theme]
    for btn in [finish_button, pause_button, reset_button, home_button]:
        btn.config(bg=theme["button_bg"], activebackground=theme["button_active"], fg=theme["text"])

for i, tname in enumerate(themes.keys()):
    btn = Radiobutton(
        inline_theme_frame,
        text=tname,
        variable=inline_theme_var,
        value=tname,
        font=("Arial", 11, "bold"),
        bg=theme_display_colors[tname],
        fg='#000000',
        activebackground="#FFFFFF",
        activeforeground="#000000",
        selectcolor="#FFFFFF",
        indicatoron=False,
        width=12,
        pady=4,
        command=lambda v=tname: apply_inline_theme(v)
    )
    btn.grid(row=0, column=i, padx=4)

def apply_inline_theme_from_values():
    inline_time_var.set(suggested_time)
    inline_font_var.set(current_font)
    inline_theme_var.set(current_theme)


def start_session_from_setup():
    """Apply selections, go to timer screen, and start timer immediately."""
    global suggested_time, suggested_font, suggested_theme
    global current_theme, current_font, remaining_time, on_break

    suggested_time = selected_time.get()
    suggested_font = selected_font.get()
    suggested_theme = selected_theme.get()

    current_theme = suggested_theme
    current_font = suggested_font
    remaining_time = suggested_time * 60
    on_break = False

    timer_label.config(
        text=format_time(remaining_time),
        font=(fonts[current_font], 72, "bold"),
        bg=themes[current_theme]["timer_bg"]
    )
    timer_frame.config(bg=themes[current_theme]["timer_bg"])
    main_frame.config(bg=themes[current_theme]["bg"])
    timer_screen.config(bg=themes[current_theme]["bg"])

    theme = themes[current_theme]
    for btn in [finish_button, pause_button, reset_button, home_button]:
        btn.config(bg=theme["button_bg"], activebackground=theme["button_active"], fg=theme["text"])

    apply_inline_theme_from_values()

    setup_frame.pack_forget()
    timer_screen.pack(expand=True, fill=BOTH)

    finish_button.config(text="Finish")
    start_timer()

start_button = Button(
    setup_bottom,
    text="Start Timer",
    font=("Fredoka One", 18, "bold"),
    bg="#F4C14A",
    fg="#000000",
    activebackground="#F4C14A",
    activeforeground="#000000",
    width=16,
    height=2,
    relief=RAISED,
    bd=2,
    cursor="hand2",
    command=start_session_from_setup
)
start_button.place(relx=0.75, rely=0.5, anchor=CENTER)

root.mainloop()
