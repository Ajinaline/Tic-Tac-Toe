import tkinter as tk

identify = ["...", "...", "...", "...", "...", "...", "...", "...", "..."]
turn = 1

    
game = tk.Tk()

def move(box):
    global turn
    if (turn % 2) == 0 and identify[box] == "...":
        identify[box] = "X"
    elif (turn % 2) == 1 and identify[box] == "...":
        identify[box] = "O"
    turn += 1
    updateButton()
    
def updateButton():
    btn1.config(text=identify[0]) 
    btn2.config(text=identify[1])
    btn3.config(text=identify[2])
    btn4.config(text=identify[3]) 
    btn5.config(text=identify[4]) 
    btn6.config(text=identify[5])
    btn7.config(text=identify[6])
    btn8.config(text=identify[7])
    btn9.config(text=identify[8])
    


btn1 = tk.Button(game, text=identify[0], command=lambda: move(0))
btn2 = tk.Button(game, text=identify[1], command=lambda: move(1))
btn3 = tk.Button(game, text=identify[2], command=lambda: move(2))

btn4 = tk.Button(game, text=identify[3], command=lambda: move(3))
btn5 = tk.Button(game, text=identify[4], command=lambda: move(4))
btn6 = tk.Button(game, text=identify[5], command=lambda: move(5))

btn7 = tk.Button(game, text=identify[6], command=lambda: move(6))
btn8 = tk.Button(game, text=identify[7], command=lambda: move(7))
btn9 = tk.Button(game, text=identify[8], command=lambda: move(8))


btn1.grid(row = 0, column=0)
btn2.grid(row=0, column=1)
btn3.grid(row=0, column=2)

btn4.grid(row=1, column=0)
btn5.grid(row=1, column=1)
btn6.grid(row=1, column=2)

btn7.grid(row=2, column=0)
btn8.grid(row=2, column=1)
btn9.grid(row=2, column=2)

game.mainloop()

