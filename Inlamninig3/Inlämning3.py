import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import Inlamninglib as ines

df =pd.read_csv("temps.csv")
b=np.array(df.loc[:,"medeltemp"])       #Detta är värde y
a=np.array([[df.loc[0,"month"], 1.0],
            [df.loc[1,"month"], 1.0],
            [df.loc[2,"month"], 1.0],
            [df.loc[3,"month"], 1.0],
            [df.loc[4,"month"], 1.0],
            [df.loc[5,"month"], 1.0],
            [df.loc[6,"month"], 1.0],
            [df.loc[7,"month"], 1.0],
            [df.loc[8,"month"], 1.0],
            [df.loc[9,"month"], 1.0],
            [df.loc[10,"month"], 1.0],
            [df.loc[11,"month"], 1.0]
            ])                          #detta är Matris A


at=a.transpose()                #detta minstakvadrerar (AtAX=Aty)
z2=np.matmul(at,a)
z3=np.matmul(at,b)
z4=ines.gaussElim(z2,z3)                #detta är det som sökes efter (k och m)
zed=np.matmul(a,z4)                     #detta ger en linje över grafen

plt.plot(b,".",zed,"-")                 #plottar för att se resultatet
plt.show()



