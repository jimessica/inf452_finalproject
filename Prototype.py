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

stress_scale = Scale(
    mood_section,
    bg='#F6D36F',          # slightly richer banana
    fg='#000000',
    troughcolor='#F6D36F',
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
    relief=FLAT
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

focus_scale = Scale(
    mood_section,
    bg='#F6D36F',
    fg='#000000',
    troughcolor='#F6D36F',
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
    relief=FLAT
)
focus_scale.pack(anchor="w", fill=X)


# Suggest settings based on sliders
def suggest_settings():
    """Calculate suggested time, font, and theme from sliders, then start session."""
    global suggested_time, suggested_font, suggested_theme
    stress_score = stress_var.get()
    focus_score = focus_var.get()

    # Default suggestions
    time = 30
    font = "mono"
    theme = 2

    # High stress and high focus
    if stress_score >= 3 and focus_score >= 3:
        time = 45
        font = "mono"
        theme = 3  # purple

    # Low stress and high focus
    elif stress_score < 3 and focus_score >= 3:
        time = 30
        font = "crimson"
        theme = 2

    # High stress and low focus
    elif stress_score >= 3 and focus_score < 3:
        time = 20
        font = "mono"
        theme = 1

    # Low stress and low focus
    else:
        time = 15
        font = "fredoka"
        theme = 2

    # Store suggestions globally
    suggested_time = time
    suggested_font = font_name_mapping[font]
    suggested_theme = theme_id_to_name[theme]

    # Automatically start session after getting suggestions
    start_session()


# Bottom section - Button
bottom_section = Frame(assessment_frame, bg='#E8F0FF')
bottom_section.pack(side=BOTTOM, anchor=SE, padx=80, pady=60)

suggest_button = Button(
    bottom_section,
    text="Get Suggested Timer",
    font=("Arial", 14, "bold"),
    bg="#F4C14A",
    fg='#000000',
    activebackground="#E0AA32",
    width=25,
    height=2,
    relief=FLAT,
    bd=0,
    cursor="hand2",
    command=suggest_settings
)
suggest_button.pack()


# ==================== TIMER SCREEN ====================
timer_screen = Frame(root, bg='#f5f5f5')


# Main container for timer
main_frame = Frame(timer_screen, bg='#f5f5f5')
main_frame.pack(expand=True, fill=BOTH, padx=40, pady=30)


# Title
title_label = Label(
    main_frame,
    text="NeuroFlow",
    font=("Arial", 32, "bold"),
    bg='#f5f5f5',
    fg='#000000'
)
title_label.pack(pady=(0, 20))


# Timer display frame
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


# Control buttons frame
control_frame = Frame(main_frame, bg='#f5f5f5')
control_frame.pack(pady=10)


def format_time(seconds):
    """Convert seconds to MM:SS format."""
    mins = seconds // 60
    secs = seconds % 60
    return f"{mins:02d}:{secs:02d}"


def start_timer():
    """Start or resume the timer."""
    global timer_running, timer_paused, timer_id

    if not timer_running:
        timer_running = True
        timer_paused = False
        pause_button.config(text="Pause")
        countdown()


def countdown():
    """Handle the countdown logic."""
    global remaining_time, timer_id, timer_running

    if timer_running and remaining_time > 0:
        timer_label.config(text=format_time(remaining_time))
        remaining_time -= 1
        timer_id = root.after(1000, countdown)
    elif remaining_time <= 0:
        timer_label.config(text="00:00")
        timer_running = False


def pause_timer():
    """Pause or resume the timer."""
    global timer_running, timer_paused, timer_id

    if timer_running:
        timer_running = False
        timer_paused = True
        pause_button.config(text="Resume")
        if timer_id:
            root.after_cancel(timer_id)
    elif timer_paused:
        timer_running = True
        timer_paused = False
        pause_button.config(text="Pause")
        countdown()


def finish_timer():
    """Stop and reset the timer."""
    global timer_running, timer_paused, remaining_time, timer_id

    if timer_id:
        root.after_cancel(timer_id)
    timer_running = False
    timer_paused = False
    remaining_time = suggested_time * 60
    timer_label.config(text=format_time(remaining_time))
    pause_button.config(text="Pause")


def toggle_theme_panel():
    """Show or hide the theme customization panel."""
    if theme_panel.winfo_viewable():
        theme_panel.pack_forget()
        theme_button.config(text="Change Theme")
    else:
        theme_panel.pack(fill=BOTH, pady=20)
        theme_button.config(text="Hide Theme Options")


def apply_theme():
    """Apply selected theme and font."""
    global current_theme, current_font

    # Update colors
    theme = themes[current_theme]
    timer_frame.config(bg=theme["timer_bg"])
    timer_label.config(bg=theme["timer_bg"], font=(fonts[current_font], 72, "bold"))

    # Update button colors
    for btn in [finish_button, pause_button]:
        btn.config(bg=theme["button_bg"], activebackground=theme["button_active"])


def select_font(font_name):
    """Select font and update UI."""
    global current_font
    current_font = font_name

    # Update font button states
    for fname, btn in font_buttons.items():
        if fname == font_name:
            btn.config(relief=SOLID, bd=2, bg="#FFE066")
        else:
            btn.config(relief=SOLID, bd=2, bg="#FFFFFF")


def select_theme(theme_name):
    """Select theme and update UI."""
    global current_theme
    current_theme = theme_name

    # Update theme button states
    for tname, btn in theme_buttons.items():
        if tname == theme_name:
            btn.config(relief=SOLID, bd=3)
        else:
            btn.config(relief=SOLID, bd=2)


def start_session():
    """Transition from assessment to timer with suggested settings."""
    global current_theme, current_font, remaining_time

    # Apply suggested settings
    current_theme = suggested_theme
    current_font = suggested_font
    remaining_time = suggested_time * 60

    # Update timer display
    timer_label.config(
        text=format_time(remaining_time),
        font=(fonts[current_font], 72, "bold"),
        bg=themes[current_theme]["timer_bg"]
    )
    timer_frame.config(bg=themes[current_theme]["timer_bg"])

    # Update button colors
    theme = themes[current_theme]
    for btn in [finish_button, pause_button]:
        btn.config(bg=theme["button_bg"], activebackground=theme["button_active"])

    # Update theme panel selections
    select_font(current_font)
    select_theme(current_theme)

    # Hide assessment, show timer
    assessment_frame.pack_forget()
    timer_screen.pack(expand=True, fill=BOTH)

    # Auto-start timer
    start_timer()


def return_to_start():
    """Go back to the mood assessment screen so the user can change parameters."""
    global timer_running, timer_paused, remaining_time, timer_id

    # Stop any scheduled countdown first
    if timer_id is not None:
        root.after_cancel(timer_id)
        timer_id = None

    # Reset timer state
    timer_running = False
    timer_paused = False
    pause_button.config(text="Pause")

    # Reset time right away so label is ready next time
    remaining_time = suggested_time * 60
    timer_label.config(text=format_time(remaining_time))

    # Immediately swap frames
    timer_screen.pack_forget()
    assessment_frame.pack(expand=True, fill=BOTH)


# Optional: button for manual session start (currently not used/shown)
start_session_button = Button(
    bottom_section,
    text="Start Session",
    font=("Arial", 14, "bold"),
    bg="#4CAF50",
    fg='#FFFFFF',
    activebackground="#45A049",
    width=25,
    height=2,
    relief=FLAT,
    bd=0,
    cursor="hand2",
    command=start_session
)
# Not packed; suggestions auto-start the session.


# Control buttons for timer screen
finish_button = Button(
    control_frame,
    text="Finish",
    font=("Arial", 14),
    bg=themes[current_theme]["button_bg"],
    fg=themes[current_theme]["text"],
    activebackground=themes[current_theme]["button_active"],
    width=12,
    height=2,
    relief=FLAT,
    bd=0,
    cursor="hand2",
    command=finish_timer
)
finish_button.grid(row=0, column=0, padx=5)

pause_button = Button(
    control_frame,
    text="Pause",
    font=("Arial", 14),
    bg=themes[current_theme]["button_bg"],
    fg=themes[current_theme]["text"],
    activebackground=themes[current_theme]["button_active"],
    width=12,
    height=2,
    relief=FLAT,
    bd=0,
    cursor="hand2",
    command=pause_timer
)
pause_button.grid(row=0, column=1, padx=5)

theme_button = Button(
    control_frame,
    text="Change Theme",
    font=("Arial", 14),
    bg='#FFFFFF',
    fg='#000000',
    activebackground='#E0E0E0',
    width=12,
    height=2,
    relief=SOLID,
    bd=2,
    cursor="hand2",
    command=toggle_theme_panel
)
theme_button.grid(row=0, column=2, padx=5)

return_button = Button(
    control_frame,
    text="Return to Start",
    font=("Arial", 14),
    bg='#FFFFFF',
    fg='#000000',
    activebackground='#E0E0E0',
    width=14,
    height=2,
    relief=SOLID,
    bd=2,
    cursor="hand2",
    command=return_to_start
)
return_button.grid(row=0, column=3, padx=5)


# Theme customization panel
theme_panel = Frame(main_frame, bg='#f0f0f0', relief=FLAT, bd=0)

# Suggested timer label
suggested_label = Label(
    theme_panel,
    text="Suggested Timer",
    font=("Arial", 12),
    bg='#f0f0f0',
    fg='#000000'
)
suggested_label.pack(anchor=W, padx=20, pady=(20, 10))


# Font selection
font_label = Label(
    theme_panel,
    text="Font",
    font=("Arial", 11, "bold"),
    bg='#f0f0f0',
    fg='#000000'
)
font_label.pack(anchor=W, padx=20, pady=(10, 5))

font_frame = Frame(theme_panel, bg='#f0f0f0')
font_frame.pack(padx=20, pady=5, fill=X)

font_buttons = {}
for i, (fname, ffont) in enumerate(fonts.items()):
    btn = Button(
        font_frame,
        text=fname,
        font=(ffont, 10),
        bg="#FFE066" if fname == current_font else "#FFFFFF",
        fg='#000000',
        relief=SOLID,
        bd=2,
        width=15,
        height=2,
        cursor="hand2",
        command=lambda f=fname: select_font(f)
    )
    btn.grid(row=0, column=i, padx=5)
    font_buttons[fname] = btn


# Theme selection
theme_label = Label(
    theme_panel,
    text="Theme",
    font=("Arial", 11, "bold"),
    bg='#f0f0f0',
    fg='#000000'
)
theme_label.pack(anchor=W, padx=20, pady=(20, 5))

theme_frame = Frame(theme_panel, bg='#f0f0f0')
theme_frame.pack(padx=20, pady=5, fill=X)

theme_buttons = {}
theme_colors = {"Banana": "#FFE066", "Blueberry": "#5B7FC7", "Grape": "#B19CD9"}
for i, tname in enumerate(themes.keys()):
    btn = Button(
        theme_frame,
        text=tname,
        font=("Arial", 10),
        bg=theme_colors[tname],
        fg='#000000',
        relief=SOLID,
        bd=2,
        width=15,
        height=2,
        cursor="hand2",
        command=lambda t=tname: select_theme(t)
    )
    btn.grid(row=0, column=i, padx=5)
    theme_buttons[tname] = btn


# Apply theme button
apply_button = Button(
    theme_panel,
    text="Set Theme",
    font=("Arial", 12, "bold"),
    bg="#FFD700",
    fg='#000000',
    activebackground="#FFC700",
    width=20,
    height=2,
    relief=FLAT,
    bd=0,
    cursor="hand2",
    command=apply_theme
)
apply_button.pack(pady=20, padx=20, anchor=E)


# Run the application
root.mainloop()
