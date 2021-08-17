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

# display the graph for any number of point/pairs of (x,y)
 
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

# Increasing and Decreasing Function
# f(x1) < f(x2)
# f(x1) > f(x2)

def indf(f,x,srt = False):
    
    if srt:
        x = sorted(x)
        
    ins = set()
    dins = set()
    nins = set()
    
    for i in range(1,len(x)):
        if x[i-1]<x[i]:
            try:                
                if f(x[i-1]) < f(x[i]):
                    ins.add(x[i-1]) 
                    ins.add(x[i])  
                elif f(x[i-1])>f(x[i]):
                    dins.add(x[i-1])
                    dins.add(x[i])  
                else:
                    nins.add(x[i])  
                    nins.add(x[i-1])
            except:
                pass
    ins = list(ins)
    dins = list(dins)
    nins = list(nins)
    
    try:
        rng_ins = rng(ins,True)
    except:
        rng_ins = (0,0)
    
    try:
        rng_dins = rng(dins,True)
    except:
        rng_dins = (0,0)
        
    try:
        rng_nins = rng(nins,True)
    except:
        rng_nins = (0,0)
        
    return rng_ins,rng_dins,rng_nins

################################################################################################################################

# Even or Odd Functions

# f(x) = f(-x):  (even)
# f(x) = -f(-x):  (odd)
def eo(f,x):
    
    # x = list(set(abs(x)))
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

################################################################################################################################

# range function

# warning : This function is not proper

def rng(l,srt = False):
    
    if srt:
        l = sorted(l)
    
    lis_1= []
    lis_1.append(l[0])
    indx = 0
    f_lst = []
    
    for j in range(len(l)):
        
        k = indx + 1
        lis_1.append(l[k])
        f_lst.append(l[k])
        
        for i in range(k,len(l)-1):
            
            a = l[i] + 1

                
            if a == l[i+1] :
                lis_1.append(a)
                
                if i == len(l)-2:
                    f_lst[0] = l[0]
                    
                    f_lst.append(l[len(l)-1])
                    final_intervals = list()
                    
                    for i in range(0,len(f_lst),2):
                        intervle = (f_lst[i],f_lst[i+1])
                        final_intervals.append(intervle)
                    
                    return final_intervals
            else:
                indx = i
                f_lst.append(l[indx])
                break 
