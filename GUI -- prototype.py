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
root.geometry("600x750")

# Retro CRT colors
CRT_GREEN = "#33FF33"
CRT_BLACK = "#000000"

root.configure(bg=CRT_BLACK)

# ----- Fake Scanlines -----
def scanlines(event):
    w = event.width
    h = event.height
    canvas.delete("scan")
    for y in range(0, h, 4):
        canvas.create_line(0, y, w, y, fill="#003300", tags="scan")

canvas = tk.Canvas(root, bg=CRT_BLACK, highlightthickness=0)
canvas.pack(fill="both", expand=True)
canvas.bind("<Configure>", scanlines)

# ----- Retro Frame Maker -----
def retro_frame(parent):
    frame = tk.Frame(
        parent,
        bg=CRT_BLACK,
        highlightbackground=CRT_GREEN,
        highlightcolor=CRT_GREEN,
        highlightthickness=2,
        bd=0
    )
    frame.pack(pady=15, padx=15, fill="both", expand=False)
    return frame

# ----- TIME SECTION -----
time_frame = retro_frame(canvas)

time_label = tk.Label(
    time_frame,
    font=("Courier", 46, "bold"),
    fg=CRT_GREEN,
    bg=CRT_BLACK
)
time_label.pack(pady=10)

date_label = tk.Label(
    time_frame,
    font=("Courier", 20),
    fg=CRT_GREEN,
    bg=CRT_BLACK
)
date_label.pack()

# ----- CALENDAR SECTION -----
cal_frame = retro_frame(canvas)
cal_frame.pack(fill="both", expand=True)  # Allow frame to grow properly

cal_title = tk.Label(
    cal_frame,
    text="MONTHLY CALENDAR",
    font=("Courier", 22, "bold"),
    fg=CRT_GREEN,
    bg=CRT_BLACK
)
cal_title.pack(pady=10)

calendar_label = tk.Label(
    cal_frame,
    font=("Courier", 16),
    fg=CRT_GREEN,
    bg=CRT_BLACK,
    justify="left"
)
calendar_label.pack(padx=20, pady=20)

# Start updates
update_time()
update_calendar()

root.mainloop()
