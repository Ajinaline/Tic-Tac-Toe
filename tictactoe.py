import tkinter as tk

identify = ["...", "...", "...", "...", "...", "...", "...", "...", "..."]
turn = 1
order = []

    
game = tk.Tk()

def move(box):
    global turn
    if (turn % 2) == 0 and identify[box] == "...":
        identify[box] = "X"
        order.append(box)
    elif (turn % 2) == 1 and identify[box] == "...":
        identify[box] = "O"
        order.append(box)
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
    winnerCheckX()
    winnerCheckO()
    
def winnerCheckX():
    row1 = [0, 1, 2]
    row2 = [3, 4, 5]
    row3 = [6, 7, 8]
    #Below is to find the common X's in the first row
    for x in [identify[0:3], identify[3:6], identify[6:9]]:
        if x.count("X") == 3:
            game.destroy()
            return
        
    for y in range(len(identify[0:3])):
        if identify[y] == "X" and identify[y + 3] == "X" and identify[y + 6] == "X":
            game.destroy()
            return
    
    #Below is to find the common X's diagonally
    if identify[0] == "X" and identify[4] == "X" and identify[8] == "X":
        game.destroy()
        return
    elif identify[2] == "X" and identify[4] == "X" and identify[6] == "X":
        game.destroy()
        return
        
def winnerCheckO():
    row1 = [0, 1, 2]
    row2 = [3, 4, 5]
    row3 = [6, 7, 8]
    #Below is to find the common X's in a row
    for x in [identify[0:3], identify[3:6], identify[6:9]]:
        if x.count("O") == 3:
            game.destroy()
            return
    
    #Below is to find the common X's in a column
    for y in range(len(identify[0:3])):
        if identify[y] == "O" and identify[y + 3] == "O" and identify[y + 6] == "O":
            game.destroy()
            return
    
    #Below is to find the common X's diagonally
    if identify[0] == "O" and identify[4] == "O" and identify[8] == "O":
        game.destroy()
        return
    elif identify[2] == "O" and identify[4] == "O" and identify[6] == "O":
        game.destroy()
        return
    
    #Below is the removal of the first 3 moves when the game is tied
    for z in range(len(order)):
        if identify.count("X") == 4 and identify.count("O") == 5:
            identify[order[0]] = "..."
            identify[order[1]] = "..."
            identify[order[2]] = "..."
            order.pop(0)
            order.pop(1)
            order.pop(2)
            updateButton()
        elif identify.count("O") == 4 and identify.count("X") == 5:
            identify[order[0]] = "..."
            identify[order[1]] = "..."
            identify[order[2]] = "..."
            order.pop(0)
            order.pop(1)
            order.pop(2)
            updateButton()
        else:
            print(z)
            continue

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