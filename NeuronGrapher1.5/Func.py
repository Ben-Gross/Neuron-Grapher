import numpy as np
import time
import math
import random
import matplotlib.pyplot as plt
import socket
import sys
from _thread import *


class neuron:
    def __init__(self,func,lay,pos,val):
        self.func = str(func)
        self.lay = int(lay)
        self.pos = int(pos)
        self.val = float(val)

class weight:
    def __init__(self,pos1,pos2,mag):
        self.pos1 = list(pos1)
        self.pos2 = list(pos2)
        self.mag = float(mag)

def tanh(x):
    return math.tanh(x)
def sigmoid(x):
    return (math.tanh(x)/2)+.5
def sech(x):
    return 1/np.cosh(x)
def sin(x):
    return math.sin(x)
def cos(x):
    return math.cos(x)
def linear(x):
    return x
def ReLU(x):
    if x > 0:
        return x
    else:
        return x/3
def custom(x):
    return 1.5/(((2.7/2)**x)+(100**-x))
def randto(x):
    return (random.random()-.5)*2*x #returns random float from -x to x

def update(N,W,lay):
    Li = []
    for h in range(len(N[lay+1])):
        for i in range(len(N[lay])):
            Li += [W[lay][i][h]]
        Lh = list(map(lambda x: N[lay][x.pos1[1]].val*x.mag,Li))
        #print(Lh)
        N[lay+1][h].val = eval(N[lay+1][h].func)(sum(Lh))
        Li = []
    return N

def Practice(x,f1,f2,f3,f4,c1,c2,c3,c4):
    f = eval(f1)(x*c1)
    g = (eval(f2)(x))*c2
    h = eval(f3)(x*c3)
    i = eval(f4)(x*c4)
    return ((f*g)+i)*h
    
def practiceprint(f1,f2,f3,f4,c1,c2,c3,c4):
    return "(("+f1+"(x * "+str(c1)+") * ("+f2+"(x) * "+str(c2)+")) + "+f4+"(x * "+str(c4)+")) * "+f3+"(x * "+str(c3)+")"

def ifzero(x):
    if x == 0:
        return .1
    else:
        return x
    
def Loss(lis1,lis2):
    lis3 = []
    for i in range(len(lis1)):
        lis3 += [abs(lis1[i]-lis2[i])]
    return lis3
        
def Learn(N,W,Wlist,practice,learn,loss1):
    Wc = random.choice(Wlist)
    save = float(W[Wc[0]][Wc[1]][Wc[2]].mag)
    graphy = []
    W[Wc[0]][Wc[1]][Wc[2]].mag += randto(learn)
    for h in range(-120,120,1):
        N[0][0].val = h/8
        iterate(N,W)
        graphy += [N[len(N)-1][0].val]
    loss2 = sum(Loss(graphy,practice))
    if loss2 > loss1:
        W[Wc[0]][Wc[1]][Wc[2]].mag = save
        return Learn(N,W,Wlist,practice,learn,loss1)
    if loss2 <= loss1:
        return W
    
    if loss2 > loss1:
        W[Wc[0]][Wc[1]][Wc[2]].mag = save
        return Learn(N,W,Wlist,practice,learn,loss1)
    if loss2 <= loss1:
        return W
        
def iterate(N,W):
    for i in range(len(N)-1):
        update(N,W,i)
    return N

def funccolor(x):
    if x[2] == "tanh":
        return "orange"
    if x[2] == "custom":
        return "purple"
    if x[2] == "sech":
        return "green"
    if x[2] == "sigmoid":
        return "blue"
    if x[2] == "ReLU":
        return "red"
    if x[2] == "sin" or x[2] == "cos":
        return "yellow"
    else:
        return "black"
    
def poscolor(x):
    if x > 0:
        return "blue"
    if x == 0:
        return "black"
    if x < 0:
        return "orange"

def roundto(x,digits):
    y = x*(10**digits)
    y = int(y)
    y = y/(10**digits)
    return y

Ntxt = ""
Wtxt = ""
if __name__ == "__main__":
    #while True:
    pass
