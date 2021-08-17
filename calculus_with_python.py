import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# below line is for get full data frame
pd.set_option("display.max_rows", None, "display.max_columns", None)

# list of x and y 
def lmkr(f,start = -100,end = 100,step = 1):
    x = np.arange(start,end,step)
    y = []
    for i in x:
        y.append(f(i))

    return x,y

################################################################################################################################
# table of x and y
def panda_table(x,y,col = 1):
    a = {}
    col = col + (col)
    row = (len(x)/col) + 1
    row = int(row) * 2 

    for i in range(col):
        a[f"{i+1}"] = [f"({row}x{col})"]

    data = pd.DataFrame(a)

    for r in range(row):
        df = {}
        for c,i in zip(np.arange(0,col,2),range(int(col/2))):
            try:
                df[f"{c+1}"] = f"{x[r+(row*i)]} = {y[r+(row*i)]}"
            except:
                pass
            df[f"{c+2}"] = "|"
    
        data = data.append(df, ignore_index = True)
    
    return data

################################################################################################################################
# display the graph
def displot(x,y,*args,x_lim = None,y_lim = None,grd = True,sct = True):
    if sct:
        plt.scatter(x,y)
    plt.plot(x,y)
    if grd:
        plt.grid()
    plt.axhline(linewidth=1, color='black')
    plt.axvline(linewidth=1, color='black')
    for i in np.arange(0,len(args),2):
        if sct:
            plt.scatter(args[i],args[i+1])
        plt.plot(args[i],args[i+1])
    
    if x_lim != None:
        plt.xlim(x_lim[0],x_lim[1])
        
    if y_lim != None:
        plt.ylim(y_lim[0],y_lim[1])
            
    plt.xlabel("\n<--------------------- X -------------------->")
    plt.ylabel("<--------------------- Y -------------------->\n")
    plt.show()
    
################################################################################################################################
# user input for find m and b (y = mx + b)
def linear_eq(x1,y1,x2,y2,inc_x = None,inc_y = None):
    
    m = (y2 - y1)/(x2 - x1)
    
    if inc_x != None:
        b = (-m)*(inc_x)    
    elif inc_y!= None:
        b = inc_y      
    
    return m,b

################################################################################################################################

def indf(f,*x,srt = False):
    if srt:
        x = sorted(x)
    
    ins = set()
    dins = set()
    nins = set()
    
    for i in range(1,len(x)):
          
        if x[i-1]<x[i]:
            
            if f(x[i-1]) < f(x[i]):
                ins.add(x[i-1])   
            elif f(x[i-1])>f(x[i]):
                dins.add(x[i-1])
            else:
                nins.add(x[i-1])
    
    return ins,dins,nins

################################################################################################################################

# Even or Odd Functions

# f(x) = f(-x):  (even)
# f(x) = -f(-x):  (odd)
def eo(f,x):
    
    x = list(set(abs(x)))
    a = set()
    for i in x:
        if i == 0:
            continue
        if f(i) == f(-i):
            a.add('Even')
        elif f(i) == -f(-i):
            a.add("Odd")
        else:
            a.add("Nether Even nor Odd")
        
    return list(a)[0] 