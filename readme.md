# NeuroFlow – Accessible Study Timer

###################################################

University of Toronto  
Faculty of Information  
Bachelor of Information Program  
INF 452H – Design Studio V: Coding  

Student Names: Divine Ogaram, Jessica Im, Gaven Ren  
Supervisor: Dr. Maher Elshakankiri  

Final Project: NeuroFlow  
Purpose: NeuroFlow study timer with accessibility features  

Date Created: 2025‑11‑23  
Date Modified: 2025‑12‑04  

###################################################

## Overview

NeuroFlow is a Python Tkinter desktop application that helps users, especially neurodivergent individuals (e.g., ADHD, autism spectrum) and users with different sensory and cognitive needs, plan and manage focused study sessions.  
The app combines a simple mood assessment with a configurable timer, allowing users to adjust session length, fonts, and color themes to reduce decision fatigue, support focus, and provide a calmer study environment.

## Features

### Customizable Focus Sessions

1. **Mood‑based suggestions**  
   Users first select their current stress and focus levels (0–5) using sliders.  
   The program uses these values to suggest a study duration, font, and theme that match the user’s current state.

2. **Configurable session settings**  
   On the “Session Setup” screen, users can:
   - Choose a focus time of 15, 20, 30, or 45 minutes.  
   - Select a font (Fredoka, Crimson Text, IBM Plex Mono).  
   - Choose among three visual themes (Banana, Blueberry, Grape).

3. **Inline adjustments during the session**  
   On the timer screen, a “Change Theme” button reveals an inline panel where users can:
   - Adjust focus time (15/20/30/45 min).  
   - Change font and theme at any time.  
   - Save settings without restarting the application.

### User Interface

1. **Minimal and structured layout**  
   - Three clear stages: Mood Assessment → Session Setup → Timer.  
   - Large buttons, readable labels, and consistent spacing reduce visual clutter.

2. **Accessibility options**  
   - **Fonts**: Multiple font families support different readability preferences (rounded sans‑serif, serif, monospace).  
   - **Color contrast**: Themes are designed with strong contrast between text and background, and the timer bar turns grey when paused or completed to clearly indicate state changes.  
   - **Manual start**: The timer **does not start automatically** when entering the timer screen; the user explicitly presses “Start” on the middle button.

3. **Automatic breaks**  
   - When a work session reaches 0:00, NeuroFlow automatically starts a 5‑minute break timer.  
   - After the break, the timer resets to the chosen focus duration and begins immediately.

### Focus Session Flow

1. User selects stress and focus levels with sliders and clicks **“Get Suggested Timer”**.  
2. On the **Session Setup** screen, the app shows suggested time, font, and theme and lets the user adjust them.  
3. The user clicks **“Start timer”** to go to the timer screen (the countdown is still stopped).  
4. On the **Timer** screen:
   - The middle button initially shows **“Start”**; pressing it begins the countdown and changes the text to **“Pause”**.  
   - **“Pause” / “Resume”** toggles the running state; the timer bar turns grey when paused or finished.  
   - **“Finish Session”** starts an automatic 5‑minute break, then restarts the initial, longer timer when complete.  
   - **“Return to Home”** stops the timer, resets the sliders, hides the inline panel if it was open, and returns to the mood assessment screen.

## Installation

- **System Requirements**
  - Operating System: Windows, macOS, or Linux.  
  - Python 3.x installed.  
  - Tkinter available (included with most standard Python installations).

- **Download**
  - Save the Python source file as:  
    `Final_PY_Im_Ren_Ogaram.py'.

- **Run Instructions**
  1. Open a terminal/command prompt in the folder containing the file.  
  2. Run:
     - On Windows:  
       `python Final_PY_Im_Ren_Ogaram.py`  
     - On macOS / Linux:  
       `python3 Final_PY_Im_Ren_Ogaram.py`  
  3. The NeuroFlow window will open on the mood assessment screen.

## Usage

### Launching the Application

- Start the program from the terminal as described above.  
- The first screen shows the title, description, and two sliders for **Stress level** and **Focus level**.

### Setting Up a Session

1. **Adjust mood sliders**
   - Move the **Stress level** and **Focus level** sliders (0–5).  
   - Labels under each slider show the exact selected value.

2. **Get suggested timer**
   - Click **“Get Suggested Timer”**.  
   - NeuroFlow computes and displays suggested values for:
     - Focus time (15/20/30/45 minutes).  
     - Font (Fredoka, Crimson Text, IBM Plex Mono).  
     - Theme (Banana, Blueberry, Grape).

3. **Customize settings**
   - On the **Session Setup** screen:
     - Click one of the **“xx min”** buttons to change session length.  
     - Choose a font; each option is rendered in its actual font style.  
     - Select a theme; each theme button uses its representative color.

4. **Move to the timer**
   - Click **“Start timer”**.  
   - The timer screen appears with your selected time, font, and theme, but the countdown is not yet running.

### Running a Focus Session

1. **Start / pause / resume**
   - Press the middle button labeled **“Start”** to begin the countdown.  
   - The button text changes to **“Pause”** while the timer runs.  
   - Press **“Pause”** to pause; the timer bar turns grey and the button changes to **“Resume”**.  
   - Press **“Resume”** to continue from the same time.

2. **Finish and break**
   - Press **“Finish Session”** to transition into a 5‑minute break timer.  
   - When the break ends, the timer resets to the selected focus duration, and the user can press **“Start”** again.

3. **Inline adjustments**
   - Press **“Change Theme”** to reveal the inline settings panel under the timer.  
   - Adjust focus time, font, and theme as needed and click **“Save settings”**.  
   - The panel can be closed again; it starts hidden when you return from the home screen.

4. **Return to home**
   - Press **“Return to Home”** to stop the timer, reset the sliders to 0, hide the inline panel, and go back to the mood assessment screen to set up a new session.

## Socio‑Cultural and Accessibility Considerations

- **Support for users with disabilities**
  - Multiple fonts and high‑contrast themes support users with visual impairments or reading difficulties.  
  - Large buttons and clear labels assist users with motor or vision challenges.

- **Accessibility for neurodivergent users**
  - Linear, predictable flow (Assessment → Setup → Timer) reduces cognitive load.  
  - Manual start of the timer allows users to prepare before focus begins.  
  - Clear color changes between running, paused, and finished states give strong visual cues.

- **Age‑inclusive and culturally sensitive design**
  - Simple language avoids jargon and is approachable for a wide age range.  
  - Color choices aim to be calm and non‑threatening, without relying on culture‑specific symbolism.

## Collaboration and Teamwork

NeuroFlow was developed collaboratively by a group of three students.  
Work was distributed across:

- GUI layout and visual design (screens, frames, color themes).  
- Timer logic, state management, and break behavior.  
- Accessibility features, socio‑cultural design, and documentation (including this README).

Each member submitted individual biweekly progress reports and participated in peer and self‑evaluation as required by the course.

## Acknowledgments

Special thanks to neurodivergent communities and accessibility advocates whose experiences and design principles informed the features and interface of NeuroFlow.  
Thanks to the course instructor and peers for feedback during the development process.

## Contact

For questions, feedback, or support, please contact the development team through the course communication channels.
