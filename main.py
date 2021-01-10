import tkinter as tk
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    reps = 0
    start_timer()
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    checkmark_display.config(text=f"{'✓' * math.floor(reps / 2)}")
    if reps == 8:
        return
    elif reps == 7:
        count_down(LONG_BREAK_MIN * 60)
        heading.config(text="BREAK", fg=RED)
    elif reps % 2 == 0:
        count_down(WORK_MIN * 60)
        heading.config(text="WORK", fg=GREEN)
    else:
        count_down(SHORT_BREAK_MIN * 60)
        heading.config(text="BREAK", fg=PINK)
    window.lift()
    reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    canvas.itemconfig(timer_text, text=f"{minutes:02}:{seconds:02}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Heading
heading = tk.Label(text="Timer", font=(FONT_NAME, 50), bg=YELLOW, fg=GREEN)
heading.grid(column=1, row=0)

# Tomato Image
canvas = tk.Canvas(width=210, height=230, bg=YELLOW, highlightthickness=0)
tomato_image = tk.PhotoImage(file="tomato.png")
canvas.create_image(105, 115, image=tomato_image)
# Time Display
timer_text = canvas.create_text(105, 140, text="00:00", font=(FONT_NAME, 30, "bold"), fill="white")
canvas.grid(column=1, row=1)

# Start Button
start_button = tk.Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

# Reset Button
reset_button = tk.Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

# Checkmark Display
checkmark_display = tk.Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, "bold"))
checkmark_display.grid(column=1, row=3)

window.mainloop()
