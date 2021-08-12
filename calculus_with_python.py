import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
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
def displot(x,y,*args,x_lim = False,y_lim = False,grd = True):
    plt.plot(x,y)
    if grd:
        plt.grid()
    plt.axhline(linewidth=1, color='black')
    plt.axvline(linewidth=1, color='black')
    for i in np.arange(0,len(args),2):
        plt.plot(args[i],args[i+1])
    
    if x_lim:
        try :
            l = int(input("x_left side limit = "))
            r = int(input("x_right side limit = "))
            plt.xlim(l,r)
        except:
            print("tata")
    if y_lim:
        try :
            l = int(input("y_down side limit = "))
            r = int(input("y_up side limit = "))
            plt.ylim(l,r)
        except:
            print("tata")
            
    plt.xlabel("\n<--------------------- X -------------------->")
    plt.ylabel("<--------------------- Y -------------------->\n")
    plt.show()

################################################################################################################################
# user input for find m and b (y = mx + b)
def linear_eq(x1,y1,x2,y2,inc_x = True,inc_y = False):
    
    # find m (Slop)
    m = (y2 - y1)/(x2 - x1)
    print("\ny = mx + b,\twhere\n\t\tm = ",m)
    
    # x and y intercept
    # find b
    if inc_x:
        x = int(input("value of x :"))
        b = (-m)*(x)
        print(f"\nFor given X - INTERCEPT({x},0) :")                
        print(f"\ny = {m}x + b,\twhere\n\t\tb = ",b)
        print(f"\n\n\t-------------------\n=>\t| y = {m}x + {b} |\n\t-------------------")        
    
    elif inc_y:
        y = int(input("value of y :"))
        b = y
        print(f"\nFor given Y - INTERCEPT(0,{y}) :")        
        print(f"\ny = {m}x + b,\twhere\n\t\tb = ",b)
        print(f"\n\n\t-------------------\n=>\t| y = {m}x + {b} |\n\t-------------------")        
    
    return m,b
