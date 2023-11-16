from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.5
SHORT_BREAK_MIN = 0.5
LONG_BREAK_MIN = 20
reps=0
timer_id=None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global reps
    window.after_cancel(timer_id)
    canvas.itemconfigure(timer,text="00:00")
    progres_label["text"]=""
    timer_label["text"]="Timer"
    timer_label["fg"]=GREEN
    reps=0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    
    if reps%8==0:
        count_down(LONG_BREAK_MIN*60)
        timer_label["text"]="BREAK"
        timer_label["fg"]=GREEN
        
    elif(reps%2==0):
        count_down(SHORT_BREAK_MIN*60)
        timer_label["text"]="BREAK"
        timer_label["fg"]=GREEN
        
    else:
        count_down(WORK_MIN*60)
        timer_label["text"]="WORK"
        timer_label["fg"]=PINK
        
        

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer_id
    minute=int(count//60)
    sec=int(count%60)
    if sec<10:
        sec=f"0{sec}"
    if minute<10:
        minute=f"0{minute}"
    canvas.itemconfigure(timer,text=f"{minute}:{sec}")
    if(count>0):
        timer_id=window.after(1000,count_down,count-1)
    else:
        start_timer()
        progres_label["text"]="✔"*(reps//2)

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro")
window.config(padx=70,pady=20,bg=YELLOW)

canvas=Canvas(width=200,height=223,bg=YELLOW)
tom_img=PhotoImage(file="./Pomodora/tomato.png")
canvas.create_image(103,112,image=tom_img)
timer=canvas.create_text(103,138,text="00:00",font=(FONT_NAME,30,"bold"),fill="white")
canvas.grid(row=1,column=1)

timer_label=Label(text="Timer",fg=GREEN,font=(FONT_NAME,45,"bold"),bg=YELLOW)
timer_label.grid(row=0,column=1)

progres_label=Label(text="",fg=GREEN,bg=YELLOW,font=(FONT_NAME,20,"normal"),pady=10)
progres_label.grid(row=3,column=1)

start=Button(text="Start",padx=10,command=start_timer)
start.grid(row=2,column=0)

reset=Button(text="Reset",padx=10,command=reset)
reset.grid(row=2,column=2)

window.mainloop()