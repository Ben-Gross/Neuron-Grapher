from Func import *

def Npic(N):
    Ni = []
    Nt = []
    for h in range(len(N)):
        for i in range(len(N[h])):
            Ni += [[N[h][i].lay,N[h][i].pos,N[h][i].func]]
        Nt += [Ni]
        Ni = []
    return Nt
            

def Wpic(W,N):
    Wj = []
    Wi = []
    Wtxt = []
    for h in range(len(N)-1):
        for i in range(len(N[h])):
            for j in range(len(N[h+1])):
                Wj += [[W[h][i][j].pos1,W[h][i][j].pos2,W[h][i][j].mag]]
            Wi += [Wj]
            Wj = []
        Wtxt += [Wi]
        Wi = []
    return Wtxt

try:
    donetxt = open("done.txt","w")
    donetxt.write("[]")
except:
    print("donetxt blank error")
    donetxt.close()
finally:
    donetxt.close()

if __name__ == "__main__":

    functions = ["tanh","sigmoid","sech","sin","linear","ReLU"]
    Pf1 = random.choice(functions)
    Pf2 = random.choice(functions)
    Pf3 = random.choice(functions)
    Pf4 = random.choice(functions)
    Pc1 = random.randint(-10,10)
    Pc2 = random.randint(-10,10)
    Pc3 = random.randint(-10,10)
    Pc4 = random.randint(-10,10)

    Pgenx = []
    Pgeny = []
    for i in range(-120,120,1):
        Pgeny += [Practice(i/8,Pf1,Pf2,Pf3,Pf4,Pc1/2,Pc2/2,Pc3/2,Pc4/2)]
        Pgenx += [i/8]
    
    print("the practice function is:",practiceprint(Pf1,Pf2,Pf3,Pf4,Pc1/2,Pc2/2,Pc3/2,Pc4/2))
    NhidLay = int(input("how many hidden layers?          "))
    
    N = []
    N += [[neuron("linear",0,i,0) for i in range(1)]]
    N += [[neuron("linear",h+1,i,0) for i in range(len(functions))] for h in range(NhidLay)]
    N += [[neuron("linear",len(N),i,0) for i in range(1)]]

    for i in range(len(N)):
        if len(N[i]) > 1:
            N[i][0].func = "sigmoid"
        if len(N[i]) > 2:
            N[i][1].func = "tanh"
        if len(N[i]) > 3:
            N[i][2].func = "sech"
        if len(N[i]) > 4:
            N[i][3].func = "sin"
        #if len(N[i]) > 5:
        #    N[i][4].func = "cos"
        if len(N[i]) > 5:
            N[i][4].func = "ReLU"
try:
    Ntxt = open("N.txt","w+")
    Ntxt.write(str(Npic(N)))
except:
    print("Ntxt error")
    Ntxt.close()
finally:
    Ntxt.close()
    
W = []
Wlist = []
Wj = []
Wi = []
for h in range(len(N)-1):
    for i in range(len(N[h])):
        for j in range(len(N[h+1])):
            Wj += [weight([h,i],[h+1,j],randto(3))]
            Wlist += [[h,i,j]]
        Wi += [Wj]
        Wj = []
    W += [Wi]
    Wi = []
if __name__ == "__main__":
    iterations = int(input("how many training iterations?    "))
    learning = float(input("what is the learning rate?       "))
    while iterations > 0:
        lossy = []
        for i in range(iterations):
            x = 0
            graphx = []
            graphy = []
            for h in range(-120,120,1):
                x += 1
                N[0][0].val = h/8
                iterate(N,W)
                graphx += [h/8]
                graphy += [N[len(N)-1][0].val]
            plt.clf()
            x = plt.plot(graphx,graphy,"b-",linewidth=1)
            P = plt.plot(Pgenx,Pgeny,"r-")
            L = plt.plot(graphx,Loss(graphy,Pgeny),"g-",linewidth=.4)
            plt.title("figure: "+str(i)+"  loss: "+str(sum(Loss(graphy,Pgeny))))
            plt.show(block=False)
            plt.pause(.05)
            lossy += [sum(Loss(graphy,Pgeny))]
            Learn(N,W,Wlist,Pgeny,3,sum(Loss(graphy,Pgeny)))
            try:
                Wtxt = open("W.txt","w")
                Wtxt.write(str(Wpic(W,N)))
            except:
                print("Wtxt error")
                Wtxt.close()
            finally:
                Wtxt.close()
        print("Do you want to continue?")
        iterations = int(input("If so, how many more iterations?    "))
for i in range(2):
    try:
        donetxt = open("done.txt","w")
        donetxt.write("done")
    except:
        print("donetxt error")
        donetxt.close()
    finally:
        donetxt.close()
