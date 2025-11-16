import tkinter as tk
import time
import calendar
from datetime import datetime

# ----- Update Clock -----
def update_time():
    now = datetime.now()
    time_str = now.strftime("%I:%M:%S %p")
    date_str = now.strftime("%A, %B %d, %Y")

    time_label.config(text=time_str)
    date_label.config(text=date_str)

    root.after(1000, update_time)

# ----- Update Calendar -----
def update_calendar():
    now = datetime.now()
    cal_text = calendar.month(now.year, now.month)
    calendar_label.config(text=cal_text)

# ===== GUI SETUP =====
root = tk.Tk()
root.title("Retro Pi Dashboard")
root.geometry("520x700")

# Retro CRT green + black
CRT_GREEN = "#33FF33"
CRT_BLACK = "#000000"

root.configure(bg=CRT_BLACK)

# ----- Optional Fake Scanlines -----
def scanlines(event):
    w = event.width
    h = event.height
    canvas.delete("scan")
    for y in range(0, h, 4):
        canvas.create_line(0, y, w, y, fill="#002200", tags="scan")

canvas = tk.Canvas(root, bg=CRT_BLACK, highlightthickness=0)
canvas.pack(fill="both", expand=True)
canvas.bind("<Configure>", scanlines)

# ----- Styled Frame -----
def retro_frame(parent):
    return tk.Frame(parent, bg=CRT_BLACK, highlightbackground=CRT_GREEN,
                    highlightcolor=CRT_GREEN, highlightthickness=2, bd=0)

# ----- TIME CARD -----
time_frame = retro_frame(canvas)
time_frame.place(relx=0.5, y=80, anchor="n", width=450, height=180)

time_label = tk.Label(
    time_frame, text="",
    font=("Courier", 44, "bold"),
    fg=CRT_GREEN, bg=CRT_BLACK
)
time_label.pack(pady=10)

date_label = tk.Label(
    time_frame, text="",
    font=("Courier", 18),
    fg=CRT_GREEN, bg=CRT_BLACK
)
date_label.pack()

# ----- CALENDAR CARD -----
calendar_frame = retro_frame(canvas)
calendar_frame.place(relx=0.5, y=300, anchor="n", width=450, height=350)

calendar_title = tk.Label(
    calendar_frame, text="MONTHLY CALENDAR",
    font=("Courier", 18, "bold"),
    fg=CRT_GREEN, bg=CRT_BLACK
)
calendar_title.pack(pady=10)

calendar_label = tk.Label(
    calendar_frame,
    font=("Courier", 14),
    fg=CRT_GREEN,
    bg=CRT_BLACK,
    justify="left"
)
calendar_label.pack()

# Start updates
update_time()
update_calendar()

root.mainloop()
