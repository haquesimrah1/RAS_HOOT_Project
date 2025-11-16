# ----- CALENDAR SECTION -----
cal_frame = tk.Frame(
    canvas,
    bg=CRT_BLACK,
    highlightbackground=CRT_GREEN,
    highlightcolor=CRT_GREEN,
    highlightthickness=2,
    bd=0
)
cal_frame.pack(pady=15, fill="both", expand=True)

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
calendar_label.pack(padx=10, pady=10, anchor="center")

