from Func import *
from tkinter import *
import ast

tk = Tk()
tk.title("Neural Overlay")
try:
    Ntxt = open("N.txt","r")
    N = ast.literal_eval(str(Ntxt.read()))
except:
    print("Ntxt error")
finally:
    Ntxt.close()
window = Canvas(tk,width=len(N)*100+30,height=max(list(map(len,N)))*100+30)
window.pack()
done = False
while done == False:
    try:
        Wtxt = open("W.txt","r")
        W = ast.literal_eval(str(Wtxt.read()))
        Wtxt.close()
    except:
        print("Wtxt error")
    finally:
        Wtxt.close()
    window.update()
    window.delete("all")
    for h in range(len(N)):
        for i in range(len(N[h])):
            Ni = N[h][i]
            window.create_oval(Ni[0]*100+60,Ni[1]*100+60,Ni[0]*100+80,Ni[1]*100+80,fill=funccolor(Ni))
    for h in range(len(N)-1):
        for i in range(len(N[h])):
            for j in range(len(N[h+1])):
                window.create_line(W[h][i][j][0][0]*100+70,W[h][i][j][0][1]*100+70,W[h][i][j][1][0]*100+70,W[h][i][j][1][1]*100+70,width=ifzero(abs(roundto(W[h][i][j][2]/2,4))),fill=poscolor(W[h][i][j][2]))
    try:
        donetxt = open("done.txt","r")
        sign = str(donetxt.read())
        if sign == "done":
            done = True
    except:
        print("donetxt error")
        donetxt.close()
    finally:
        donetxt.close()
