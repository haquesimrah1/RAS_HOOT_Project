import tkinter as tk
import time
import calendar
from datetime import datetime

# ---------------------------
# Update the clock every 1 sec
# ---------------------------
def update_time():
    current_time = time.strftime("%I:%M:%S %p")
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)

# ---------------------------
# Build calendar for the month
# ---------------------------
def show_calendar(year, month):
    cal_text = calendar.month(year, month)
    calendar_label.config(text=cal_text)

# ---------------------------
# Main GUI setup
# ---------------------------
root = tk.Tk()
root.title("Raspberry Pi Time + Calendar")
root.geometry("350x400")
root.configure(bg="black")

# Time label
clock_label = tk.Label(
    root,
    font=("Arial", 32, "bold"),
    fg="lime",
    bg="black"
)
clock_label.pack(pady=10)

# Calendar label
calendar_label = tk.Label(
    root,
    font=("Courier", 12),
    fg="white",
    bg="black",
    justify="left"
)
calendar_label.pack(pady=10)

# Initialize calendar with current month/year
now = datetime.now()
show_calendar(now.year, now.month)

# Start the time loop
update_time()

root.mainloop()
